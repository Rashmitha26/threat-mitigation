# Network Packet Classification Using Machine Learning

## Introduction
With the rise of the Internet, it has become a central part of our daily lives, facilitating many of our routine activities. However, this increase in online activity has also led to a rise in cybercrimes. Securing network traffic is now more important than ever for both individuals and organizations. This project aims to develop a machine learning (ML) model to classify network packets as legitimate or malicious.
To achieve this, **NSL_KDD dataset** is used and machine learning models using popular algorithms, including **Random Forest**, **AdaBoost**, and **XGBoost** are built. An ensemble model is developed by combining these individual models using **VotingClassifier**.
Among these models, the **Random Forest model** achieves the highest accuracy and is ultimately used for real-time packet classification.

## Features
- Classify network packets as legitimate or malicious
- Built using machine learning models: **Random Forest**, **AdaBoost**, **XGBoost**
- Ensemble model with **VotingClassifier**
- Deployable on network devices for packet filtering and security

## Project Structure
The project consists of the following files:
- **`NSL_KDD_SET.csv`**: The dataset used to train the models
- **`project.py`**: Contains the code for training and testing the machine learning models. It also handles the saving of the trained model.
- **`model_file.sav`**: The serialized Random Forest model used for packet classification. This file will be used in predicting the authenticity of the network packet.
- **`ui.py`**: The script for handling user input and processing predictions.
- **`index.html`**: The HTML code for the user interface where users can input packet details.
- **`result.html`**: The HTML code to display the classification result.

## Usage
To run the project on Google Colab, follow these steps:
1. **Clone the repository**:
   Clone the project repository to your local machine or Google Colab environment.
2. **Upload necessary files**:
   - Upload `model_file.sav` (the trained Random Forest model).
   - Upload `index.html` and `result.html` into the `sample_data/static/templates` folder in your Colab environment.
3. **Run the application**:
   - Open `ui.py` in a new notebook and run the script.
   - Once executed, an URL will be displayed in the notebook.
   - Click the URL to open the user interface in your browser.
4. **Enter packet details**:
   - On the web interface, input the packet information you want to classify.
   - Click on the **"Predict"** button to receive the result (either **Legitimate** or **Malicious**).


## Requirements
- Python 3.x
- Google Colaboratory (for running the notebook)
- Required Python packages (can be installed via `requirements.txt`):
  - `pandas`
  - `numpy`
  - `matplotlib.pyplot`
  - `seaborn`
  - `sklearn`
  - `math`
  - `xgboost`
  - `flask`
  - `pickle`


## Model Performance
The **Random Forest model** is the most accurate among the other tested models, achieving the highest accuracy on the NSL_KDD dataset. This model is used in the final implementation for packet classification.


Project.py - [Colab link](https://colab.research.google.com/drive/1rY3o2-DwoluKb4ssYR6epqUtPs0Zv00V?usp=sharing#scrollTo=SbCXsAkPuQAM)

Ui.py – [Colab link](https://colab.research.google.com/drive/1JsGcYwDZN0nuI5UKrINOPEZlZeHWqKoD?usp=sharing#scrollTo=pX-kaIFNt5SJ)
