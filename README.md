Wavelet-Based Denoising and Emotion Detection from Physiological Signals

This project presents a complete pipeline for detecting human emotional states (calm vs. stress) using multimodal physiological signals—specifically Galvanic Skin Response (GSR) and Heart Rate Variability (HRV). The core of this work is an advanced wavelet-based denoising technique designed to clean noisy signals from low-cost, non-clinical sensors, making reliable emotion detection more accessible. The processed signals are then used to train and evaluate multiple machine learning models.
Block Diagram

The project follows a standard signal processing and machine learning workflow:
Key Features

    Multimodal Signal Processing: Leverages both GSR (skin conductance) and HRV (derived from PPG signals) for a more robust prediction.

    Wavelet Denoising: Implements a Discrete Wavelet Transform (DWT) based denoising pipeline to effectively remove noise from raw sensor data while preserving key physiological features.

    Automated Feature Engineering: Extracts a comprehensive set of features from the GSR and HRV signals, including SCR count, peak amplitude, SDNN, RMSSD, and pNN50.

    Machine Learning Classification: Trains, evaluates, and tunes three different machine learning models (SVM, KNN, and Decision Tree) for binary classification of emotional states.

Setup Instructions

To get this project running on your local machine, follow these steps.

1. Clone the repository:

git clone [https://github.com/YourUsername/Emotion-Detection-Wavelet.git](https://github.com/YourUsername/Emotion-Detection-Wavelet.git)
cd Emotion-Detection-Wavelet

2. Create and activate a virtual environment:

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies:
The project requires Python with libraries such as NumPy, SciPy, scikit-learn, and PyWavelets.

pip install -r requirements.txt

4. Download the Dataset:
This project uses the WESAD (Wearable Stress and Affect Detection) dataset for development and benchmarking. Download the preprocessed subject files (S2.pkl, S3.pkl, etc.) and place them inside the data/raw/ directory.
Usage

The project is organized into three Jupyter notebooks that should be run in order:

    notebooks/01_data_exploration_and_denoising.ipynb

        This notebook is for initial exploration and visualizes the effect of the wavelet denoising on a sample signal segment.

    notebooks/02_build_feature_dataset.ipynb

        This script processes all the raw subject data from the data/raw/ folder. It applies the denoising and feature extraction pipeline in a sliding window to create a master dataset, which is saved as data/processed/features_master_dataset.csv.

    notebooks/03_machine_learning_classification.ipynb

        This notebook loads the final feature dataset, trains the three machine learning models, performs hyperparameter tuning using GridSearchCV, and evaluates their final performance.

Results

After training and tuning on the WESAD dataset, the models achieved the following accuracies on the test set:

Model
	

Tuned Accuracy

Decision Tree
	

95.37%

Support Vector Machine
	

94.21%

K-Nearest Neighbors
	

92.82%
Hardware Components

The system is designed to work with the following low-cost hardware:

    Microcontroller: ESP32 Dev Board

    PPG Sensor (for HRV): MAX30102

    GSR Sensor: Grove GSR Sensor

License

This project is licensed under the MIT License. See the LICENSE file for details.
Authors

    Yovan Kovil Nayagam J

    Adithey P Suraj

    Kushi Kapil

    Kalaparan C A M