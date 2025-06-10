# =============================================================================
#               Two-Box Methane (CH₄) Box Model - ACAM2025 Tutorial Version
# =============================================================================
# Description:
#   This script demonstrates a 2-box hemispheric CH₄ model.
#   It reads CH₄ emissions from CSV, interpolates them,
#   runs an ODE model (NH and SH), and compares results with observations.
#
# Author : Naveen Chandra
# Date   : 6 June 2025
#
# Contact for details at naveennegi@jamstec.go.jp and nav.phy09@gmail.com

# =============================================================================

# -----------------------------------------------------------------------------
# 1. IMPORTS
# -----------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from datetime import datetime


# -----------------------------------------------------------------------------
# 2. CH₄ MODEL CLASS DEFINITION
# -----------------------------------------------------------------------------
class CH4BoxModel:

    """
    Two‐box CH₄ model for Northern Hemisphere (NH) and Southern Hemisphere (SH).

    Equations (in ppb/day):
      dC_nh/dt = E_nh_ppb/day 
                 + (C_sh – C_nh) / tau_exch_days 
                 – C_nh * k_ch4_nh

      dC_sh/dt = E_sh_ppb/day 
                 + (C_nh – C_sh) / tau_exch_days 
                 – C_sh * k_ch4_sh

    where:
       E_nh, E_sh  = CH₄ emissions (NH, SH) converted to ppb/day
       tau_exch    = interhemispheric exchange time (converted from years → days)
       C_nh, C_sh  = concentrations (ppb) in NH & SH
    """
    
    def __init__(self, year_ordinals, flux_matrix):
        
        self.St     = np.array(year_ordinals)
        self.fluxes = np.array(flux_matrix)
        
        self.sink_nh = []
        self.sink_sh = []

        # --------------------------------------------------------------
        # (a)      UNIT CONVERSION CONSTANTS
        # --------------------------------------------------------------
        M_atm = 5.1e21       # [g]
        M_air = 28.97        # [g/mol]
        M_ch4 = 16.04        # [g/mol]

        # Conversion: TgCH4/ppb
        # 1 ppb = 1e‐9 mole fraction of CH₄
        #   → mass_CH4(ppb) = M_atm * 1e‐9 * (M_ch4 / M_air) [g]
        #   → convert [g] → [Tg = 1e12 g]
        self.alpha = (M_atm * 1e-9 * M_ch4) / M_air / 1e12
        print(f"Conversion α (Tg/ppb): {self.alpha:.4f}")

        # --------------------------------------------------------------
        # (b)      TIME CONVERSION
        # --------------------------------------------------------------
        self.YrToDay  = 365.25
        self.DaysToS  = 86400
        self.tau_exch = 1.0 * self.YrToDay

        # ----------------------
        # Loss parameters
        # ---------------------
        OH         = 1.0e6;            # Average OH concentration in molec/cm3
        k_ch4      = 3.395e-15;        # reaction rate of OH with CH4 (cm3/molec/s)
        self.k_ch4 = OH * self.DaysToS * k_ch4

        # Initial conditions (ppb)
        self.IC    = [1700.0, 1600.0] # NH, SH

        # ODE solver config
        self.Tspan = (self.St[0], self.St[-1])
        
        # Limit max step size to one month (~30 days) to ensure stability
        self.odeOpts = {"max_step": self.YrToDay / 12.0}

    def rhs(self, t, y, S):
        """
        Right‐hand side of the ODE system at time t.

        Parameters
        ----------
        t : float
            Current “time” in ordinal days.
        y : array‐like, shape (2,)
            Current concentrations [C_nh, C_sh] in ppb.
        S : ndarray, shape (N, 4)
            Original flux matrix (unchanged). We will interpolate row‐wise.

        Returns
        -------
        [dC_nh, dC_sh] : list of floats
            Time‐derivatives dC_nh/dt and dC_sh/dt (units: ppb/day).
        """
        # Interpolate emissions and loss factors at time t
        E_nh, E_sh, L_nh, L_sh = [np.interp(t, self.St, S[:, i]) for i in range(4)]

        # Calculate loss rates (per day)
        k_nh = L_nh * self.k_ch4
        k_sh = L_sh * self.k_ch4

        # Compute chemical sink terms
        sink_nh = (k_nh - k_nh * 0.04) * y[0]
        sink_sh = (k_sh - k_sh * 0.04) * y[1]

        # Interhemispheric exchange terms
        exch_nh = (y[1] - y[0]) / self.tau_exch
        exch_sh = (y[0] - y[1]) / self.tau_exch

        # Time derivatives
        dC_nh = E_nh + exch_nh - sink_nh
        dC_sh = E_sh + exch_sh - sink_sh

        return [dC_nh, dC_sh]


    def run(self):
        """
        Solve the 2‐box ODE system on the time grid self.St.

        Returns
        -------
        years : ndarray, shape (N,)
            Array of integer years corresponding to self.St.
        C_nh : ndarray, shape (N,)
            Modeled NH concentration (ppb) at each time.
        C_sh : ndarray, shape (N,)
            Modeled SH concentration (ppb) at each time.
        """
        S = self.fluxes.copy()
  
        # Convert emissions: Tg/yr → Tg/day → ppb/day
        S[:, 0:2] /= self.YrToDay
        S[:, 0] = (2.0 / self.alpha) * S[:, 0]
        S[:, 1] = (2.0 / self.alpha) * S[:, 1]

        # Solve the system
        sol = solve_ivp(
            fun=lambda t, y: self.rhs(t, y, S),
            t_span=self.Tspan,
            y0=self.IC,
            method="RK45",
            t_eval=self.St,
            max_step=self.odeOpts['max_step']
        )
        
        # Extract concentration time series
        C_nh, C_sh = sol.y[0], sol.y[1]
        self.nh, self.sh = C_nh, C_sh

        # Interpolate loss factors over solution times
        L_nh_all = np.interp(sol.t, self.St, S[:, 2])
        L_sh_all = np.interp(sol.t, self.St, S[:, 3])
        k_nh_all = L_nh_all * self.k_ch4
        k_sh_all = L_sh_all * self.k_ch4

        # Compute sink terms (ppb/day → Tg/yr)
        sink_nh_ppb = k_nh_all * 0.96 * C_nh
        sink_sh_ppb = k_sh_all * 0.96 * C_sh
        self.sink_nh = sink_nh_ppb * self.YrToDay * self.alpha / 2.0
        self.sink_sh = sink_sh_ppb * self.YrToDay * self.alpha / 2.0
        
        # =======================================
        # Compute burden (Tg) and lifetime (yr)
        # =======================================
        burden     = (C_nh + C_sh) / 2.0 * self.alpha
        loss_total = self.sink_nh + self.sink_sh
        lifetime   = np.nanmean(burden / loss_total)

        print(f"Mean CH$_4$ Burden (Tg):       {np.nanmean(burden):.2f}")
        print(f"Mean Total Loss (Tg/yr):       {np.nanmean(loss_total):.2f}")
        print(f"Mean Chemical Lifetime (yr):   {lifetime:.2f}")

        # Convert time to calendar years
        self.T_mod = pd.Series(sol.t).apply(lambda x: datetime.fromordinal(int(x))).dt.year.values

        # Save to CSV
        df_out = pd.DataFrame({
            "year": self.T_mod,
            "C_nh_ppb": self.nh,
            "C_sh_ppb": self.sh,
            "sink_nh_TgYr": self.sink_nh,
            "sink_sh_TgYr": self.sink_sh,
            "emis_nh_TgYr": self.fluxes[:, 0],
            "emis_sh_TgYr": self.fluxes[:, 1],
        })
        df_out.to_csv("./data/ch4_model_output_with_sinks.csv", float_format="%.2f", index=False)
        print("Output saved to: ./data/ch4_model_output_with_sinks.csv")
        
        return self.T_mod, self.nh, self.sh
    
    
    def plot(self):
        
        """
        Plot two-panel figure:
        (1) Emission and sink (Tg/yr)
        (2) CH₄ concentrations (ppb) vs observations
        """
        years            = np.array(self.T_mod)
        C_nh, C_sh       = np.array(self.nh), np.array(self.sh)
        sink_nh, sink_sh = np.array(self.sink_nh), np.array(self.sink_sh)
        emis_nh, emis_sh = np.array(self.fluxes[:, 0]), np.array(self.fluxes[:, 1])

        # Load observational data
        obs       = pd.read_csv("./data/ch4_obs_hmean.csv", sep=",").set_index("time")
        obs.index = pd.to_datetime(obs.index)
        t_obs     = obs.index.year.values

        # Set up 2-panel figure
        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True, constrained_layout=True)
        colors = ["c", "maroon"]
        labels = ["NH", "SH"]

        # =============================
        # Panel 1: Emissions & Loss
        # =============================
        ax1.plot(years, emis_nh, label="NH Emission", color="c", lw=2)
        ax1.plot(years, emis_sh, label="SH Emission", color="maroon", lw=2)
        ax1.plot(years, sink_nh, "--", label="NH Sink", color="c", lw=1.5)
        ax1.plot(years, sink_sh, "--", label="SH Sink", color="maroon", lw=1.5)
        ax1.set_ylabel("CH$_4$ Flux (Tg yr$^{-1}$)")
        ax1.set_title("CH$_4$ Emissions and Chemical Sink")
        ax1.grid(True)
        ax1.legend()

        # =============================
        # Panel 2: CH₄ Concentration
        # =============================
        symbols = ["o", "^"]
        for hemi, col, sym in zip(labels, colors, symbols):
        
            ax2.errorbar(x=np.array(t_obs), y=np.array(obs[f"{hemi}_mean"]), yerr=np.array(obs[f"{hemi}_error"]),
                    fmt=sym, mfc="none", ms=6, capsize=3,
                    elinewidth=0.5, color=col, label=f"{hemi} obs")
        
        for C, hemi, col in zip([C_nh, C_sh], labels, colors):
            ax2.plot(years, C, label=f"{hemi} model", color=col, lw=2)

        ax2.set_xlabel("Year")
        ax2.set_ylabel("CH$_4$ Concentration (ppb)")
        ax2.set_title("Two-Box CH$_4$ Model vs Observations")
        ax2.grid(True)
        ax2.legend()

        # =============================
        # Finalize and Save
        # =============================
        #fig.tight_layout()
        fig.savefig("ch4_2dbox_results_base.pdf", dpi=300, bbox_inches="tight")
        plt.close(fig)
        print("Plot saved to: ch4_2dbox_results_v2.pdf")
    
    def plot_conc(self):
    
        """
        Single-panel figure:
        (1) CH4 concentrations (ppb) vs observations
        """
        years = self.T_mod
        C_nh, C_sh = self.nh, self.sh

        obs = pd.read_csv("./data/ch4_obs_hmean.csv", sep=",").set_index("time")
        obs.index = pd.to_datetime(obs.index)
        t_obs = obs.index.year.values

        fig, ax = plt.subplots(figsize=(8, 6))
        colors = ["c", "maroon"]
        symbols = ["o", "^"]
        hemi_labels = ["NH", "SH"]

        for hemi, col, sym in zip(hemi_labels, colors, symbols):
            ax.errorbar(x=np.array(t_obs), y=np.array(obs[f"{hemi}_mean"]), yerr=np.array(obs[f"{hemi}_error"]),
                        fmt=sym, mfc="none", ms=6, capsize=3,
                        elinewidth=0.5, color=col, label=f"{hemi} obs")

        for C, hemi, col in zip([C_nh, C_sh], hemi_labels, colors):
            ax.plot(years, C, label=f"{hemi} model", color=col, lw=2)

        ax.set_xlabel("Year")
        ax.set_ylabel("CH$_4$ Concentration (ppb)")
        ax.set_title("Two-Box CH$_4$ Model vs Observations")
        ax.legend()
        ax.grid(True)
        fig.tight_layout()
        fig.savefig("ch4_2dbox_results_base.pdf", dpi=300, bbox_inches="tight")
        plt.close(fig)


# -----------------------------------------------------------------------------
# 3. MAIN EXECUTION BLOCK
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    sYear, eYear = 1970, 2020
    St = [datetime(y, 1, 1).toordinal() for y in range(sYear, eYear + 1)]

    #df_ems = pd.read_csv("./data/ch4_ems_hmean.csv", sep=",").set_index("year")
    df_ems = pd.read_csv("./data/ch4ems_hmean_base.csv", sep=",").set_index("year")
    tDat = pd.to_datetime(df_ems.index.astype(str), format="%Y").map(datetime.toordinal).to_numpy()

    interp_data = {}
    for col in ["nh", "sh"]:
        f = interp1d(tDat, df_ems[col].values, kind="cubic",
                     bounds_error=False, fill_value="extrapolate")
        interp_data[col] = f(St)

    #print(interp_data); quit()
    fluxes = np.column_stack([
        interp_data["nh"]*0.98,
        interp_data["sh"]*1.01,
        np.zeros(len(St)),
        np.zeros(len(St))
    ])
    
    

    model = CH4BoxModel(St, fluxes)
    model.run()
    model.plot()
    print("Model run complete")#. Plot saved to: ch4_2dbox_results_v2.pdf")
