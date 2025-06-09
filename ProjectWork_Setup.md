# Project-Work Setup for ACAM 2025 Training School

This guide provides step-by-step instructions for setting up your development environment. The environment will be pre-configured at the venue, but these instructions are provided for reference.

## Table of Contents
1. [Install Required Software](#1-install-required-software)
   - [1.1 Install Git](#11-install-git)
   - [1.2 Install Miniforge](#12-install-miniforge)
   - [1.3 Install JupyterLab](#13-install-jupyterlab)
   - [1.4 Install UV (Optional)](#14-install-uv-optional)
2. [Get the Training Materials](#2-get-the-training-materials)
3. [Set Up Python Environment](#3-set-up-python-environment)
   - [3.1 Using Conda (Recommended)](#31-using-conda-recommended)
   - [3.2 Using UV (Alternative)](#32-using-uv-alternative)
4. [Install Required Packages](#4-install-required-packages)
5. [Launch JupyterLab](#5-launch-jupyterlab)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Install Required Software

### 1.1 Install Git

#### Windows:
1. Download from: [git-scm.com/download/win](https://git-scm.com/download/win)
2. Run installer with these settings:
   - Use Git from Git Bash and Windows Command Prompt
   - Use OpenSSL library
   - Checkout Windows-style, commit Unix-style line endings
   - Use Windows' default console window
   - Enable file system caching

#### macOS:
```bash
xcode-select --install
# Or using Homebrew:
# brew install git
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update && sudo apt install git
```

#### Verify Installation:
```bash
git --version
```

### 1.2 Install Miniforge

Miniforge provides conda and mamba package managers.

#### Windows:
1. Download from: [conda-forge.org](https://conda-forge.org/download/)
2. Run installer with:
   - "Add Miniforge3 to my PATH" checked
   - "Just Me" installation

#### macOS/Linux:
```bash
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh
bash Miniforge3-$(uname)-$(uname -m).sh -b
```

#### Verify Installation:
```bash
conda --version
mamba --version
```

### 1.3 Install JupyterLab

JupyterLab is an interactive development environment for working with notebooks, code, and data.

#### Windows:
1. Using Miniforge (recommended):
   ```bash
   conda install -c conda-forge jupyterlab
   ```
2. Using pip (alternative):
   ```bash
   pip install jupyterlab
   ```

#### macOS/Linux:
```bash
# Using conda (recommended)
conda install -c conda-forge jupyterlab

# Or using pip
# pip install jupyterlab

# Or using your system package manager
# Ubuntu/Debian:
# sudo apt install jupyter-notebook jupyter
# 
# Fedora:
# sudo dnf install python3-jupyter-core python3-jupyter-notebook
```

#### Verify Installation:
```bash
jupyter --version
```

### 1.4 Install UV (Optional)

UV is a fast Python package installer.

#### Windows:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS/Linux:
```bash
curl -sSf https://astral.sh/uv/install.sh | sh
```

#### Verify Installation:
```bash
uv --version
```

---

## 2. Get the Training Materials

1. Open terminal/command prompt
2. Navigate to your preferred directory:
   ```bash
   cd ~/Documents  # or any directory of your choice
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/PiyushX23/ACAM_2025_Training_School_Material.git
   cd ACAM_2025_Training_School_Material
   ```

---

## 3. Set Up Python Environment

### 3.1 Using Conda (Recommended)

1. Create and activate environment:
   ```bash
   mamba create -n acam2025 python=3.10
   conda activate acam2025
   ```

### 3.2 Using UV (Alternative)

1. Create and activate environment:
   ```bash
   # Create a new virtual environment
   uv venv .venv
   
   # Activate the environment
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   
   # Install required packages for Jupyter
   uv add ipykernel jupyterlab
   
   # Register the kernel with Jupyter
   python -m ipykernel install --user --name=acam2025 --display-name="Python (ACAM2025)"
   
   # Verify the kernel is installed
   jupyter kernelspec list
   ```
   
   > **Note:** If you don't see your kernel in JupyterLab:
   > 1. Make sure JupyterLab is installed in the same environment
   > 2. Try refreshing the JupyterLab page
   > 3. Restart JupyterLab if needed

---

## 4. Install Required Packages

### If using Conda:
```bash
mamba install -c conda-forge jupyterlab xarray numpy pandas matplotlib cartopy netcdf4 scipy seaborn plotly dask h5py scikit-learn
jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
jupyter lab build
```

### If using UV:
```bash
uv add jupyterlab xarray numpy pandas matplotlib cartopy netCDF4 scipy seaborn plotly dask h5py scikit-learn
jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
jupyter lab build
```

---

## 5. Launch JupyterLab

1. Navigate to project:
   ```bash
   cd ~/Documents/ACAM_2025_Training_School_Material
   ```

2. Start JupyterLab:
   ```bash
   jupyter lab
   ```
   > Access at: http://localhost:8888/lab

3. Select kernel:
   - Click on the kernel name in the top-right corner
   - Choose "Python (ACAM2025)"

---

## 6. Troubleshooting

### Common Issues:

1. **Command not found**
   - Verify PATH settings
   - Restart terminal
   - On Windows, use PowerShell

2. **Environment activation**
   ```bash
   source ~/miniforge3/etc/profile.d/conda.sh
   conda activate acam2025
   ```

3. **Port in use**
   ```bash
   jupyter lab --port 8889
   ```

4. **Kernel not found in JupyterLab**
   - Ensure ipykernel is installed in the environment
   - Refresh JupyterLab page
   - Restart JupyterLab

### Getting Help:
- [JupyterLab Docs](https://jupyterlab.readthedocs.io/)
- [Conda Forge](https://conda-forge.org/)
- Contact training organizers

> **Note:** A pre-configured environment will be available at the venue.
