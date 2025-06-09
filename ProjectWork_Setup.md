Okay, here's the revised `README.md` file, structured for clarity and beginner-friendliness.

```markdown
# ACAM 2025 Training School: Project Work Setup

Welcome! This guide will walk you through setting up a scientific Python environment for the ACAM 2025 Training School project work.

**Important Note for Training Participants:** A pre-configured environment will be available at the training venue. These instructions are provided if you wish to set up your own environment on your personal machine or for future reference.

## Table of Contents
- [Step 1: Install Miniforge (Conda Package Manager)](#step-1-install-miniforge-conda-package-manager)
- [Step 2: Install Git (Version Control)](#step-2-install-git-version-control)
- [Step 3: Clone the Training Repository](#step-3-clone-the-training-repository)
- [Step 4: Create and Activate Your Python Environment](#step-4-create-and-activate-your-python-environment)
  - [Option A: Using Conda (Recommended)](#option-a-using-conda-recommended)
    - [Method 1: From `environment.yml` file (Easiest)](#method-1-from-environmentyml-file-easiest)
    - [Method 2: Manual Conda Environment Creation](#method-2-manual-conda-environment-creation)
  - [Option B: Using UV (Alternative Fast Package Manager)](#option-b-using-uv-alternative-fast-package-manager)
- [Step 5: Launch JupyterLab](#step-5-launch-jupyterlab)
- [Step 6: Troubleshooting](#step-6-troubleshooting)

---

## Step 1: Install Miniforge (Conda Package Manager)

Miniforge is a minimal installer for `conda` that uses the community-led `conda-forge` repository by default. It also includes `mamba`, a much faster alternative to `conda` for installing packages and creating environments.

### Windows:
1.  Download the latest Miniforge3 Windows installer from [conda-forge.org/download/](https://conda-forge.org/download/). Look for "Miniforge3-Windows-x86_64.exe".
2.  Run the installer and follow the on-screen instructions:
    *   **Recommended:** Check "Add Miniforge3 to my PATH environment variable" during installation if you want `conda` and `mamba` to be accessible from any terminal. If you don't check this, you'll need to use the "Miniforge Prompt" installed by the installer.
    *   Choose "Install for Just Me".
3.  After installation, open a new terminal (Command Prompt, PowerShell, or the Miniforge Prompt) and verify the installation:
    ```bash
    conda --version
    mamba --version
    ```

### macOS (Intel or Apple Silicon):
1.  Open your Terminal (found in `/Applications/Utilities/`).
2.  Download and run the Miniforge3 installer script. You can do this by pasting the following commands into your terminal:
    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-$(uname -m).sh"
    bash Miniforge3-MacOSX-$(uname -m).sh -b -p "${HOME}/miniforge3"
    rm Miniforge3-MacOSX-$(uname -m).sh 
    ```
    This will install Miniforge into a `miniforge3` directory in your home folder.
3.  Add Miniforge to your shell configuration so it's available in new terminal sessions. The installer might do this automatically, or you might need to run `~/miniforge3/bin/conda init <your_shell_name>` (e.g., `zsh`, `bash`).
4.  Close and reopen your terminal.
5.  Verify the installation:
    ```bash
    conda --version
    mamba --version
    ```

### Linux:
1.  Open your terminal.
2.  Download and run the Miniforge3 installer script:
    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-$(uname -m).sh"
    bash Miniforge3-Linux-$(uname -m).sh -b -p "${HOME}/miniforge3"
    rm Miniforge3-Linux-$(uname -m).sh
    ```
    This will install Miniforge into a `miniforge3` directory in your home folder.
3.  Add Miniforge to your shell configuration. The installer might do this automatically, or you might need to run `~/miniforge3/bin/conda init <your_shell_name>` (e.g., `bash`, `zsh`).
4.  Close and reopen your terminal.
5.  Verify the installation:
    ```bash
    conda --version
    mamba --version
    ```

---

## Step 2: Install Git (Version Control)

Git is a version control system used to manage and track changes to code. You'll use it to download (clone) the training materials.

### Windows:
1.  Download Git from: [git-scm.com/download/win](https://git-scm.com/download/win).
2.  Run the installer. The default settings are usually fine. Key settings to consider:
    *   **Choosing the default editor:** Select VS Code or another editor you are comfortable with (Nano is a simple terminal editor).
    *   **Adjusting your PATH environment:** Select "Git from the command line and also from 3rd-party software".
    *   **Configuring line ending conversions:** Select "Checkout Windows-style, commit Unix-style line endings".

### macOS:
Git might already be installed. If not, or if you want the latest version:
1.  **Option 1: Xcode Command Line Tools (easiest)**
    Open Terminal and type:
    ```bash
    xcode-select --install
    ```
    If it's already installed, it will tell you.
2.  **Option 2: Install via Homebrew (if you have Homebrew installed)**
    ```bash
    brew install git
    ```

### Linux (Ubuntu/Debian):
Open Terminal and type:
```bash
sudo apt update
sudo apt install git
```

### Linux (Fedora):
Open Terminal and type:
```bash
sudo dnf install git
```

### Verify Git Installation:
Open a new terminal and type:
```bash
git --version
```
You should see the installed Git version.

---

## Step 3: Clone the Training Repository

This step downloads the necessary code and materials for the training school from GitHub.

1.  Open your terminal (or Git Bash on Windows if you chose that during Git installation).
2.  Navigate to a directory where you want to store the training materials. For example, your `Documents` folder:
    ```bash
    # For macOS/Linux:
    cd ~/Documents
    # For Windows (Command Prompt):
    # cd %USERPROFILE%\Documents
    # For Windows (PowerShell):
    # cd ~\Documents
    ```
    You can choose any directory you prefer.

3.  Clone the repository using the following command:
    ```bash
    git clone https://github.com/PiyushX23/ACAM_2025_Training_School_Material.git
    ```
    > **Note:** You do not need a GitHub account to clone a public repository. This command will work without any authentication.

4.  After the command finishes, a new directory named `ACAM_2025_Training_School_Material` will be created. Navigate into this directory:
    ```bash
    cd ACAM_2025_Training_School_Material
    ```
    You should now be inside the `ACAM_2025_Training_School_Material` directory for the next steps.

---

## Step 4: Create and Activate Your Python Environment

A Python environment isolates the packages needed for this project from other Python projects on your system. You have two main options:

*   **Option A: Using Conda (Recommended)** - This is the primary method, especially if you want to use the provided `environment.yml` file for easy setup.
*   **Option B: Using UV (Alternative)** - UV is a newer, very fast package manager.

Choose **one** option.

### Option A: Using Conda (Recommended)

#### Method 1: From `environment.yml` file (Easiest)

The repository includes an `environment.yml` file that specifies all required packages and the Python version. This is the most straightforward way to create the Conda environment.

1.  Ensure you are in the `ACAM_2025_Training_School_Material` directory (from Step 3).
2.  Create the environment using the `environment.yml` file. This command uses `mamba` (which came with Miniforge) for faster processing:
    ```bash
    mamba env create -f environment.yml
    ```
    If `mamba` command is not found, you can use `conda`:
    ```bash
    conda env create -f environment.yml
    ```
    This command will create an environment named `acam2025` (as specified in the file) and install all necessary packages. This might take a few minutes.

3.  Once the environment is created, activate it:
    ```bash
    conda activate acam2025
    ```
    Your terminal prompt should now change to show `(acam2025)` at the beginning, indicating the environment is active.

You have now successfully set up your environment! You can proceed to [Step 5: Launch JupyterLab](#step-5-launch-jupyterlab).

#### Method 2: Manual Conda Environment Creation

If you prefer to create the environment manually or if Method 1 encounters issues:

1.  Ensure you are in the `ACAM_2025_Training_School_Material` directory.
2.  Create a new conda environment (we'll name it `acam2025`) with Python 3.10 (a common, stable version for scientific computing):
    ```bash
    mamba create -n acam2025 python=3.10 -c conda-forge -y
    ```
    (If `mamba` is not found, use `conda create -n acam2025 python=3.10 -c conda-forge -y`)

3.  Activate the newly created environment:
    ```bash
    conda activate acam2025
    ```

4.  Install the core scientific packages. We use `mamba` for speed and specify `conda-forge` channel for package consistency:
    ```bash
    mamba install -c conda-forge jupyterlab jupyterlab-git xarray numpy pandas matplotlib cartopy netcdf4 scipy seaborn plotly
    ```

5.  (Optional but Recommended) Install JupyterLab extensions:
    ```bash
    # These extensions enhance the JupyterLab interface
    jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly

    # After installing extensions, you often need to rebuild JupyterLab
    jupyter lab build
    ```
    *Note: For very new JupyterLab versions, some extensions might be pre-bundled or installed as Python packages directly with `mamba install ...`. If `jupyter labextension install` gives errors or warnings about being deprecated for certain packages, check the specific extension's documentation.*

6.  (Optional) Install additional useful packages:
    ```bash
    mamba install -c conda-forge dask h5py scikit-learn
    ```

### Option B: Using UV (Alternative Fast Package Manager)

UV is an extremely fast Python package installer and resolver, written in Rust. It can be used as an alternative to Conda for creating virtual environments and managing packages.

1.  **Install UV (if you haven't already):**
    *   **Windows (Open PowerShell as Administrator and run):**
        ```powershell
        powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```
    *   **macOS/Linux (Open Terminal and run):**
        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
    *   After installation, close and reopen your terminal or source your shell profile file (e.g., `source ~/.bashrc`, `source ~/.zshrc`).
    *   **Verify Installation:**
        ```bash
        uv --version
        ```

2.  Ensure you are in the `ACAM_2025_Training_School_Material` directory (from Step 3).

3.  Create a new virtual environment (e.g., named `.venv` in your project directory) using Python 3.10:
    ```bash
    uv venv .venv --python 3.10
    ```
    *(If you don't have Python 3.10 readily available on your system PATH for UV to find, you might need to install it first, or point UV to an existing Python 3.10 installation using `uv venv .venv -p /path/to/python3.10`)*

4.  Activate the environment:
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
        (If script execution is disabled, you might need to run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first in PowerShell)
    *   **Windows (Command Prompt):**
        ```cmd
        .venv\Scripts\activate.bat
        ```
    Your terminal prompt should change to indicate the `.venv` environment is active.

5.  Install the required Python packages using `uv pip install`:
    ```bash
    uv pip install jupyterlab ipykernel h5py numpy pandas scipy xarray netCDF4 matplotlib cartopy seaborn plotly
    ```
    *(`ipykernel` is needed so JupyterLab can find and use this environment).*

6.  **Register this environment's kernel with Jupyter:** This allows JupyterLab (even if installed elsewhere) to find and use the Python interpreter from this UV environment.
    ```bash
    python -m ipykernel install --user --name=acam2025-uv --display-name="Python (ACAM2025 UV)"
    ```

7.  (Optional) Install additional useful packages:
    ```bash
    uv pip install dask scikit-learn
    ```

8.  (Optional) Install JupyterLab extensions:
    If JupyterLab extensions are needed (many are now included or are pip-installable Python packages), and if they are traditional prebuilt extensions:
    ```bash
    jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
    jupyter lab build
    ```
    Check the specific extension's documentation for installation with modern JupyterLab.

---

## Step 5: Launch JupyterLab

Once your chosen environment (e.g., `acam2025` for Conda, or the one with `.venv` for UV) is set up and **activated**, you can start JupyterLab.

1.  Ensure your environment is active (your terminal prompt should indicate this, e.g., `(acam2025)` or `(.venv)`).
2.  Make sure you are in the main project directory:
    ```bash
    # Example: cd ~/Documents/ACAM_2025_Training_School_Material
    # (If you are not already there)
    ```
3.  Start JupyterLab:
    ```bash
    jupyter lab
    ```

4.  JupyterLab should open automatically in your default web browser. The address will typically be `http://localhost:8888/lab`.
    *   If it doesn't open automatically, look for a URL in the terminal output (it will look like `http://localhost:8888/lab?token=...` or similar) and copy-paste it into your browser.
    *   > **Note:** JupyterLab runs locally on your computer. No internet account or sign-up is required to use it after installation.

    When you open a notebook in JupyterLab, ensure you select the correct kernel if prompted (e.g., "Python (acam2025)" or "Python (ACAM2025 UV)").

---

## Step 6: Troubleshooting

### Common Issues:

1.  **`conda`, `mamba`, `git`, or `uv` command not found:**
    *   Ensure the software (Miniforge, Git, UV) was installed correctly.
    *   **PATH Issue:** The program might not be in your system's PATH.
        *   For Miniforge: Ensure you checked "Add Miniforge3 to my PATH" (Windows) or that `conda init` ran correctly (macOS/Linux).
        *   For Git/UV: The installer usually handles this.
    *   **New Terminal:** Always close and reopen your terminal after installing command-line tools or running `conda init` to ensure changes take effect.
    *   On Windows, try using the "Miniforge Prompt" (if you didn't add Miniforge to PATH) or Git Bash (for Git commands).

2.  **Environment activation issues (e.g., `conda activate acam2025` fails):**
    *   If you see `CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'`, you likely need to initialize your shell for conda. Run `conda init <your_shell_name>` (e.g., `conda init bash`, `conda init zsh`). Then close and reopen your terminal.
    *   Ensure the environment name is correct. You can list all conda environments with `conda env list`.

3.  **JupyterLab not opening in browser:**
    *   Look for error messages in the terminal where you launched `jupyter lab`.
    *   Try manually navigating to `http://localhost:8888/lab` in your browser.
    *   Ensure no other application is using port `8888`.

4.  **Port already in use (when starting JupyterLab):**
    If port `8888` is busy, JupyterLab might try another port, or you can specify one:
    ```bash
    jupyter lab --port 8889
    ```
    Then access it at `http://localhost:8889/lab`.

5.  **Kernel not found in JupyterLab:**
    *   If using UV, ensure you ran `python -m ipykernel install --user --name=...` after activating the UV environment and installing `ipykernel`.
    *   Ensure `ipykernel` is installed in your active environment (`mamba install ipykernel` or `uv pip install ipykernel`).
    *   Try restarting JupyterLab.

### Getting Help:
If you encounter issues you can't resolve:
-   Consult the documentation for the respective tools:
    -   [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
    -   [Conda Documentation](https://docs.conda.io/) / [Mamba Documentation](https://mamba.readthedocs.io/)
    -   [UV Documentation](https://astral.sh/uv)
-   Search for the error message online (e.g., on Stack Overflow).
-   Contact the training organizers for assistance.

```