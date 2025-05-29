# Project-Work Setup for ACAM 2025 Training School

This guide provides instructions for setting up JupyterLab on your local machine for the ACAM 2025 Training School. The environment will be pre-configured at the venue, but these instructions are provided for reference.

## Table of Contents
- [1. Install Python](#1-install-python)
- [2. Install Git](#2-install-git)
- [3. Clone the Training Repository](#3-clone-the-training-repository)
- [4. Install JupyterLab and Required Libraries](#4-install-jupyterlab-and-required-libraries)
- [5. Launch JupyterLab](#5-launch-jupyterlab)
- [6. Troubleshooting](#6-troubleshooting)

---

## 1. Install Python

### Windows:
1. Download and install Python 3.10+ from [python.org](https://www.python.org/downloads/)
   - Check "Add Python to PATH" during installation

### macOS:
1. Open Terminal and install Homebrew if you don't have it:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python:
   ```bash
   brew install python
   ```

### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Linux (Fedora):
```bash
sudo dnf install python3 python3-pip
```

### Verify Installation:
```bash
python --version  # Should be 3.10 or higher
```

---

## 2. Install Git

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

## 4. Install JupyterLab and Required Libraries

1. Install JupyterLab and essential data science libraries:
   ```bash
   pip install jupyterlab jupyterlab-git xarray numpy pandas matplotlib cartopy netCDF4 scipy seaborn plotly
   ```

2. Install JupyterLab extensions:
   ```bash
   jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/git @jupyterlab/toc jupyterlab-plotly
   jupyter lab build
   ```

---

## 5. Launch JupyterLab

1. From the terminal, navigate to your project directory:
   ```bash
   cd ~/Documents/ACAM_2025_Training_School_Material
   ```
2. Start JupyterLab:
   ```bash
   jupyter lab
   ```
3. JupyterLab will open automatically in your default web browser at `http://localhost:8888/lab`
   > **Note:** No account or sign-up is required to use JupyterLab locally. It runs entirely in your browser but doesn't require any online authentication.

---

## 6. Troubleshooting

### Common Issues:

1. **Command not found**
   - Ensure Python is in your system PATH
   - Close and reopen your terminal after installation
   - On Windows, try using PowerShell instead of Command Prompt

2. **JupyterLab not opening in browser**
   - Try accessing it manually at `http://localhost:8888/lab`
   - Check for error messages in the terminal

3. **Port already in use**
   ```bash
   jupyter lab --port 8889
   ```

### Getting Help:
- Visit [JupyterLab documentation](https://jupyterlab.readthedocs.io/)
- Contact the training organizers for assistance

---

## Note for Training Participants

A pre-configured environment will be provided at the training venue. These instructions are for reference only. Please contact the training organizers if you need assistance setting up your local environment.
