# 🌧️ Rainfall Prediction Project

## 📄 Overview

This project focuses on predicting rainfall using a machine learning approach. By analyzing weather data, such as wind speed, cloud cover, sunlight, and humidity, we developed a logistic regression model to classify whether it will rain or not.

## 🛠️ Features

- **Binary Classification**: Predicts rainfall as either "Yes" (Rain) or "No" (No Rain).
- **Data Preprocessing**: Converts raw rainfall data into a binary target variable.
- **Logistic Regression**: Implements a classification model to predict outcomes.
- **Performance Evaluation**: Assesses model accuracy, precision, recall, and F1-score.

## 📊 Dataset

The dataset includes weather parameters such as:
- Mean Wind Speed (km/h)
- Mean Amount of Cloud (%)
- Sunlight Hours
- Humidity
- Total Rainfall (mm)

The target variable is binary, with 1 indicating rainfall and 0 indicating no rainfall.

## 🚀 Methodology

1. **Data Preprocessing**:
   - Cleaned and transformed the dataset.
   - Converted `Total Rainfall (mm)` into a binary target variable (`Rain`).
   - Handled missing values in the target variable by filling NaNs with 0.

2. **Model Training**:
   - Split the dataset into training (80%) and testing (20%) sets.
   - Trained a logistic regression model using features like wind speed, cloud cover, sunlight, and humidity.

3. **Model Evaluation**:
   - Achieved an accuracy of **81.2%** on the test set.
   - Evaluated model performance using confusion matrix, precision, recall, and F1-score.

## 📈 Results

- **Accuracy**: 81.2%
- **Confusion Matrix**:
  ```
  [[155  24]
   [ 31  83]]
  ```
- **Classification Report**:
  ```
                 precision    recall  f1-score   support

           0       0.83      0.87      0.85       179
           1       0.78      0.73      0.75       114

    accuracy                           0.81       293
   macro avg       0.80      0.80      0.80       293
weighted avg       0.81      0.81      0.81       293
  ```

## 📂 Project Structure

- `CloudAmount.csv`, `Humidity.csv`, etc.: Datasets containing weather parameters.
- `modelling.ipynb`: Jupyter notebook with model implementation and evaluation.
- `Visualize.py`: Python script for data visualization.
- `emily_features.ipynb`: Feature engineering notebook.

## 🔧 How to Use

1. Clone the repository.
2. Ensure you have Python installed along with the required libraries:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
3. Run the `modelling.ipynb` notebook to preprocess data, train the model, and evaluate performance.

## 🌟 Team Contributions

- **Cynthia**: Feature engineering and initial modeling.
- **Emily**: Dataset preprocessing and visualization scripts.
