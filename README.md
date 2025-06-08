# ACAM 2025 Training School Materials

This repository contains training materials for the 6th Atmospheric Composition And The Asian Monsoon (ACAM) Training School.

## Contents

This repository includes:

- Practical exercises
- Code examples
- Datasets
- Additional resources

## How to Use This Repository

Each folder in this repository corresponds to a specific session or topic covered during the training school. Within each folder, you will find relevant materials such as:

- Jupyter notebooks (.ipynb files)
- Python scripts (.py files)
- Data files
- Documentation

## Requirements

To use the materials in this repository, you will need:

- Python 3.8 or higher
- Jupyter Lab (see [JupyterLab Setup Guide](JUPYTERLAB_SETUP.md) for installation instructions)
- Required Python packages (listed in requirements.txt)

## Installation

```bash
# Clone the repository
git clone [repository URL]

# Navigate to the repository
cd ACAM_2025_Training_School_Material

# Install required packages
pip install -r requirements.txt
```

## 4. Create and Activate Virtual Environment (using UV)
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

3. Install required packages:
   ```bash
   uv add h5py numpy pandas scipy xarray netCDF4 matplotlib cartopy seaborn jupyterlab
   ```

   
## Contributing

If you would like to contribute to this repository, please:

1. Fork the repository
2. Create a new branch for your changes
3. Submit a pull request with a clear description of your changes

## License

[License information to be added]

## Contact

For questions about these materials, please contact:
- [Contact information to be added]

Region of interest :
SE : 7, 95
NW : 23, 110

Data downloaded for region:
SE: 12,98
NW: 17,103