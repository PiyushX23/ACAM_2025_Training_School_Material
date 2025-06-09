# Project-Work Setup for ACAM 2025 Training School

This guide provides instructions for setting up a scientific Python environment using Miniforge, which includes conda and mamba for package management. The environment will be pre-configured at the venue, but these instructions are provided for reference.

## Table of Contents
- [1. Install Miniforge](#1-install-miniforge)
- [2. Install Git](#2-install-git)
- [3. Clone the Training Repository](#3-clone-the-training-repository)
- [4. Create and Activate Conda Environment](#4-create-and-activate-conda-environment)
- [5. Install Required Packages](#5-install-required-packages)
- [6. Launch JupyterLab](#6-launch-jupyterlab)
- [7. Troubleshooting](#7-troubleshooting)

---

## 1. Install Miniforge

Miniforge is a minimal installer for conda that uses the community-led conda-forge repository.

### Windows:
1. Download the latest Miniforge3 Windows installer from [conda-forge.org](https://conda-forge.org/download/)
2. Run the installer and follow the on-screen instructions
   - Check "Add Miniforge3 to my PATH"
   - Choose "Just Me" installation
3. Open a new terminal and verify installation:
   ```bash
   conda --version
   mamba --version
   ```

### macOS (Intel or Apple Silicon):
1. Open Terminal
2. Download the latest Miniforge3 installer from [conda-forge.org](https://conda-forge.org/download/)
   - Or use the command line:
   ```bash
   curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-$(uname -m).sh
   bash Miniforge3-MacOSX-$(uname -m).sh -b
   ```
3. Close and reopen your terminal
4. Verify installation:
   ```bash
   conda --version
   mamba --version
   ```

### Linux:
1. Download the latest Miniforge3 installer from [conda-forge.org](https://conda-forge.org/download/)
   - Or use the command line:
   ```bash
   curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-$(uname -m).sh
   bash Miniforge3-Linux-$(uname -m).sh -b
   ```

# Close and reopen your terminal, then verify:
conda --version
mamba --version
```

---

## 2. Install UV (Alternative Package Manager)

UV is a fast Python package installer and resolver written in Rust. It's significantly faster than pip and can be used as an alternative to conda.

### Windows:
1. Open PowerShell and run:
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. Restart your terminal

### macOS/Linux:
```bash
curl -sSf https://astral.sh/uv/install.sh | sh
```

### Verify Installation:
```bash
uv --version
```

## 3. Install Git

### Windows:
1. Download Git from: [git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer with these settings:
   - Use Git from Git Bash and from Windows Command Prompt
   - Use OpenSSL library
   - Checkout Windows-style, commit Unix-style line endings
   - Use Windows' default console window
   - Enable file system caching

### macOS:
1. Install Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```
2. Or install via Homebrew:
   ```bash
   brew install git
   ```

### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install git
```

### Linux (Fedora):
```bash
sudo dnf install git
```

### Verify Git Installation:
```bash
git --version
```

---

## 3. Clone the Training Repository

1. Open terminal/command prompt
2. Navigate to your preferred directory:
   ```bash
   cd ~/Documents  # or any directory of your choice
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/PiyushX23/ACAM_2025_Training_School_Material.git
   ```
   > **Note:** You don't need a GitHub account to clone public repositories. The command above will work without authentication.
4. Navigate into the repository:
   ```bash
   cd ACAM_2025_Training_School_Material
   ```

---

## 4. Create and Activate Virtual Environment

You can choose either Conda (Section 4.1) or UV (Section 4.2) for environment management.

### 4.1 Using Conda (Original Method)

1. Create a new conda environment with Python 3.10:
   ```bash
   mamba create -n acam2025
   ```

2. Activate the environment:
   - Windows:
     ```bash
     conda activate acam2025
     ```
   - macOS/Linux:
     ```bash
     conda activate acam2025
     ```

### 4.2 Using UV (Faster Alternative)

1. Navigate to your project directory:
   ```bash
   cd ~/Documents/ACAM_2025_Training_School_Material
   ```

2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   uv venv .venv
   
   # Activate the environment
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   ```
# Install ipykernel in your UV environment:
   uv add ipykernel

# Register the kernel with Jupyter:
python -m ipykernel install --user --name=acam2025 --display-name="Python (ACAM2025)"

# Note: If you don't see your kernel in the list:
# Make sure JupyterLab is installed in the same environment:
uv add jupyterlab

3. Install required packages:
   ```bash
   uv add h5py numpy pandas scipy xarray netCDF4 matplotlib cartopy seaborn jupyterlab
   ```

## 5. Install Required Packages

### If using Conda (Section 4.1):
1. Install core scientific packages using mamba (faster than conda):
   ```bash
   mamba install -c conda-forge jupyterlab jupyterlab-git xarray numpy pandas matplotlib cartopy netcdf4 scipy seaborn plotly
   ```

2. Install JupyterLab extensions:
   ```bash
   jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
   jupyter lab build
   ```

3. (Optional) Install additional useful packages:
   ```bash
   mamba install -c conda-forge dask h5py scikit-learn
   ```

### If using UV (Section 4.2):
1. The required packages were already installed during environment setup.
   
2. To install JupyterLab extensions:
   ```bash
   jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
   jupyter lab build
   ```
   
3. (Optional) Install additional packages:
   ```bash
   uv add dask scikit-learn
   ```

---

## 6. Launch JupyterLab

1. Activate your conda environment if not already active:
   ```bash
   conda activate acam2025
   ```

2. Navigate to your project directory:
   ```bash
   cd ~/Documents/ACAM_2025_Training_School_Material
   ```

3. Start JupyterLab:
   ```bash
   jupyter lab
   ```

4. JupyterLab will open automatically in your default web browser at `http://localhost:8888/lab`
   > **Note:** No account or sign-up is required to use JupyterLab locally. It runs entirely in your browser but doesn't require any online authentication.

---

## 7. Troubleshooting

### Common Issues:

1. **Command not found**
   - Ensure Miniforge is properly installed and in your system PATH
   - Close and reopen your terminal after installation
   - On Windows, try using PowerShell instead of Command Prompt
   - Verify conda initialization by running: `conda init`

2. **Environment activation issues**
   - If you get "command not found: conda", run: `source ~/miniforge3/etc/profile.d/conda.sh` (adjust path if installed elsewhere)
   - Then try activating the environment again

3. **JupyterLab not opening in browser**
   - Try accessing it manually at `http://localhost:8888/lab`
   - Check for error messages in the terminal
   - Ensure no other application is using port 8888

4. **Port already in use**
   ```bash
   jupyter lab --port 8889
   ```

### Getting Help:
- Visit [JupyterLab documentation](https://jupyterlab.readthedocs.io/)
- Check [conda-forge documentation](https://conda-forge.org/)
- Contact the training organizers for assistance

---

## Note for Training Participants

A pre-configured environment will be provided at the training venue. These instructions are for reference if you want to set up your own environment. The conda environment file (`environment.yml`) is included in the repository for easy environment recreation:

```bash
# After cloning the repository
cd ACAM_2025_Training_School_Material
conda env create -f environment.yml
conda activate acam2025
```
