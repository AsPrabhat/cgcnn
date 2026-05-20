# CGCNN: Crystal Graph Convolutional Neural Network

A PyTorch implementation of Crystal Graph Convolutional Neural Networks for predicting material properties from crystal structures. This project uses graph-based deep learning to model atomic interactions in crystalline materials, utilizing the Materials Project API for data.

## 🚀 Quick Start

### 1. Environment Setup (First Time Only)

This project uses `uv` for fast, reliable dependency management. If you do not have `uv` installed, install it first via pip (`pip install uv`).

```powershell
# Sync all dependencies to create the virtual environment
uv sync

# Run the setup script to register Jupyter kernels and test the environment
powershell -ExecutionPolicy Bypass -File setup_environment.ps1
```

### 2. Materials Project API Setup

To download crystal structures, you need an API key from the Materials Project. The download notebook expects the `.env` file to be located in the `notebooks/` directory.

```powershell
# Create a .env file in the notebooks/ directory (persistent)
echo "MP_API=your_api_key_here" > notebooks/.env

# Alternatively, set it in your current terminal session:
$env:MP_API = "your_api_key_here"
```

### 3. Usage & Notebook Workflow

The repository is built around a reproducible Jupyter notebook pipeline. Start Jupyter Lab using `uv`:

```powershell
uv run jupyter lab
```

There are two ways to navigate the notebooks in `notebooks/`:

**Option A: Step-by-Step Tutorial (Recommended for learning)**
1. **`01_atom_embeddings.ipynb`**: Generate foundational atom feature embeddings from periodic table data.
2. **`02_data_download.ipynb`**: Download crystal structures (CIF files) from the Materials Project API.
3. **`03_graph_building.ipynb`**: Convert CIF structures into PyTorch Geometric graph representations.
4. **`04_graph_visualization.ipynb`**: Visualize crystal structures and their corresponding graphs.
5. **`05_cgcnn_data_loading.ipynb`**: Load and preprocess the datasets for the model.
6. **`06_cgcnn_model.ipynb`**: Define the CGCNN model architecture.
7. **`07_cgcnn_training.ipynb`**: Train the model and evaluate baseline performance.

**Option B: End-to-End Pipeline (For training & evaluation)**
1. **`01_atom_embeddings.ipynb`**: Generate embeddings.
2. **`02_data_download.ipynb`**: Download dataset.
3. **`08_cgcnn_complete.ipynb`**: The complete end-to-end data processing, training, evaluation, and visualization pipeline.

## 📁 Repository Structure

```text
cgcnn/
├── pyproject.toml              # Project dependencies and configuration
├── uv.lock                     # Locked dependency versions
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore patterns
│
├── notebooks/                  # Single source of truth for all workflows
│   ├── .env                    # (Create this) Environment variables for API keys
│   ├── 01_atom_embeddings.ipynb
│   ├── ...
│   ├── 08_cgcnn_complete.ipynb
│   ├── cif_structures/         # (Generated) Downloaded CIF files
│   ├── training_results/       # (Generated) Model checkpoints and logs
│   └── *.json / *.csv / *.pt   # (Generated) Intermediate datasets and configs
│
├── setup_environment.ps1       # Environment setup and kernel registration script
└── test_environment.py         # Utility script to verify package installations
```

*Note: The `notebooks/` directory internally manages all generated data. Raw structure data files (`cif_structures/` and `*.cif`) and the `.venv/` directory are excluded from version control, but the training results and model outputs are tracked for visibility.*

## 🛠️ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **Missing Packages** | Run `uv sync` to ensure your `.venv` is up to date. |
| **Complete Reset** | Run `Remove-Item -Recurse -Force .venv; uv sync` |
| **API Errors** | Ensure your `MP_API` key is correctly set in the `.env` file. |
| **Jupyter Kernel Missing**| Ensure you ran `.\setup_environment.ps1` to register the `cgcnn` kernel. |
