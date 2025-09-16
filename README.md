# Wavelet-Based Denoising and Emotion Detection from Physiological Signals

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Results](#results)
- [Hardware Components](#hardware-components)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Overview

This project presents a complete pipeline for detecting human emotional states (calm vs. stress) using multimodal physiological signals—specifically Galvanic Skin Response (GSR) and Heart Rate Variability (HRV). The core of this work is an advanced wavelet-based denoising technique designed to clean noisy signals from low-cost, non-clinical sensors, making reliable emotion detection more accessible. The processed signals are then used to train and evaluate multiple machine learning models.

## Key Features

- **Multimodal Signal Processing**: Leverages both GSR (skin conductance) and HRV (derived from PPG signals) for a more robust prediction.
- **Wavelet Denoising**: Implements a Discrete Wavelet Transform (DWT) based denoising pipeline to effectively remove noise from raw sensor data while preserving key physiological features.
- **Automated Feature Engineering**: Extracts a comprehensive set of features from the GSR and HRV signals, including SCR count, peak amplitude, SDNN, RMSSD, and pNN50.
- **Machine Learning Classification**: Trains, evaluates, and tunes three different machine learning models (SVM, KNN, and Decision Tree) for binary classification of emotional states.

## Prerequisites

- **Python Version:** Python 3.8 or newer is recommended to ensure compatibility with the libraries used.
- **System Requirements:** The project is OS-agnostic (Windows, macOS, Linux). A system with at least 4GB of RAM is recommended for processing the datasets.

## Project Structure

```
EMOTION-DETECTION-WAVELET/
├── data/
│   ├── processed/
│   │   ├── features_master_dataset.csv
│   │   └── features_s10.csv
│   └── raw/                    # Place WESAD dataset files here
├── notebooks/
│   ├── 01_data_exploration_and_denoising.ipynb
│   ├── 02_build_feature_dataset.ipynb
│   └── 03_machine_learning_classification.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── feature_extraction.py
│   └── processing.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Setup Instructions

To get this project running on your local machine, follow these steps.

### 1. Clone the repository:

```bash
git clone https://github.com/Yovan-J/Emotion-Detection-Wavelet.git
cd Emotion-Detection-Wavelet
```

### 2. Create and activate a virtual environment:

```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies:

The project requires Python with libraries such as NumPy, SciPy, scikit-learn, and PyWavelets.

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset:

This project uses the WESAD (Wearable Stress and Affect Detection) dataset for development and benchmarking. 

**Dataset Access**: [WESAD Dataset](https://uni-siegen.sciebo.de/s/HGdUkoNlW1Ub0Gx)

Download the preprocessed subject files (S2.pkl, S3.pkl, etc.) and place them inside the `data/raw/` directory.

**Note**: You may need to request access or register to download the dataset. Please follow the instructions provided on the dataset page.

## Usage

The project is organized into three Jupyter notebooks that should be run in order:

### 1. Data Exploration and Denoising
```bash
jupyter notebook notebooks/01_data_exploration_and_denoising.ipynb
```
This notebook is for initial exploration and visualizes the effect of the wavelet denoising on a sample signal segment.

### 2. Feature Dataset Creation
```bash
jupyter notebook notebooks/02_build_feature_dataset.ipynb
```
This script processes all the raw subject data from the `data/raw/` folder. It applies the denoising and feature extraction pipeline in a sliding window to create a master dataset, which is saved as `data/processed/features_master_dataset.csv`.

### 3. Machine Learning Classification
```bash
jupyter notebook notebooks/03_machine_learning_classification.ipynb
```
This notebook loads the final feature dataset, trains the three machine learning models, performs hyperparameter tuning using GridSearchCV, and evaluates their final performance.

## Results

After training and tuning on the WESAD dataset, the models achieved the following accuracies on the test set:

| Model | Tuned Accuracy |
|-------|----------------|
| Decision Tree | 95.37% |
| Support Vector Machine | 94.21% |
| K-Nearest Neighbors | 92.82% |

The project follows a standard signal processing and machine learning workflow, demonstrating effective emotion detection from physiological signals using wavelet-based preprocessing techniques.

## Hardware Components

The system is designed to work with the following low-cost hardware:

- **Microcontroller**: ESP32 Dev Board
- **PPG Sensor (for HRV)**: MAX30102
- **GSR Sensor**: Grove GSR Sensor

## Contributing

We welcome contributions to improve this project! Please feel free to:

- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

When contributing, please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- **Yovan Kovil Nayagam J**
- **Adithey P Suraj**
- **Khushi Kapil**
- **Kalaparan C A M**

---

*For questions or support, please open an issue on this repository.*