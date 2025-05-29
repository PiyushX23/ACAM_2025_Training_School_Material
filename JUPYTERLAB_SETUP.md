# Step-by-Step Tutorial: Setting Up JupyterLab and Git for ACAM 2025

This guide provides comprehensive instructions for setting up your local development environment for the ACAM 2025 Training School. It covers installation of Anaconda, JupyterLab, Git, and essential Python libraries across Windows, macOS, and Linux.

## Table of Contents
- [1. Install Anaconda](#1-install-anaconda-python-distribution)
- [2. Install Git](#2-install-git)
- [3. Clone the Training Repository](#3-clone-the-training-repository)
- [4. Create and Activate a Conda Environment](#4-create-and-activate-a-conda-environment)
- [5. Install JupyterLab and Required Libraries](#5-install-jupyterlab-and-required-libraries)
- [6. Launch JupyterLab](#6-launch-jupyterlab)
- [7. Optional: Install JupyterLab Git Extension](#7-optional-install-jupyterlab-git-extension)
- [8. Troubleshooting](#8-troubleshooting)

---

## 1. Install Anaconda (Python Distribution)

### Windows/macOS/Linux:

1. Go to: [Anaconda Distribution](https://www.anaconda.com/products/distribution)
2. Download the installer for your operating system:
   - Windows: 64-Bit Graphical Installer
   - macOS: Choose Intel or Apple Silicon (M1/M2) as per your Mac
   - Linux: 64-Bit (x86) Installer
3. Run the installer with default settings
   - **Important**: Select "Add Anaconda to PATH" when prompted (Windows)
   - Choose "Install for me only" (recommended)
4. Complete the installation

### Verify Installation:

Open a new terminal/command prompt and run:

```bash
conda --version
python --version
```

You should see version numbers for both commands.

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
4. Navigate into the repository:
   ```bash
   cd ACAM_2025_Training_School_Material
   ```

---

## 4. Create and Activate a Conda Environment

1. Create a new conda environment with Python 3.10:
   ```bash
   conda create -n acam_env python=3.10 -y
   ```
2. Activate the environment:
   - Windows:
     ```bash
     conda activate acam_env
     ```
   - macOS/Linux:
     ```bash
     source activate acam_env
     ```

---

## 5. Install JupyterLab and Required Libraries

1. Install JupyterLab and essential data science libraries:
   ```bash
   conda install -c conda-forge jupyterlab xarray numpy pandas matplotlib cartopy netCDF4 scipy -y
   ```
2. Install additional packages as needed:
   ```bash
   pip install seaborn plotly
   ```

---

## 6. Launch JupyterLab

1. From the terminal, navigate to your project directory:
   ```bash
   cd ~/Documents/ACAM_2025_Training_School_Material
   ```
2. Start JupyterLab:
   ```bash
   jupyter lab
   ```
3. JupyterLab will open automatically in your default web browser at `http://localhost:8888/lab`

---

## 7. Optional: Install JupyterLab Git Extension

For better Git integration in JupyterLab:

```bash
pip install jupyterlab-git
jupyter lab build
```

If you encounter any server extension errors, you can continue using Git from the command line.

---

## 8. Troubleshooting

### Common Issues:

1. **Command not found**
   - Ensure Anaconda is in your system PATH
   - Close and reopen your terminal after installation
   - On Windows, try using "Anaconda Prompt" instead of Command Prompt

2. **JupyterLab not opening in browser**
   - Try accessing it manually at `http://localhost:8888/lab`
   - Check for error messages in the terminal

3. **Port already in use**
   ```bash
   jupyter lab --port 8889
   ```

4. **Environment not activating**
   - On Windows, use `activate acam_env` (without 'conda')
   - On macOS/Linux, use `source activate acam_env`

5. **Missing packages**
   ```bash
   conda install package_name
   # or
   pip install package_name
   ```

### Getting Help:
- Check the [JupyterLab documentation](https://jupyterlab.readthedocs.io/)
- Visit [Anaconda documentation](https://docs.anaconda.com/)
- Contact the training organizers for assistance

---

## You're all set!

You now have a fully functional development environment for the ACAM 2025 Training School. If you encounter any issues during the setup, please don't hesitate to reach out to the training organizers for assistance.
