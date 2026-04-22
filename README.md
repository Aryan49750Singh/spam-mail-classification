# Spam Mail Classification

## Live Demo

A deployed web application is available to test the model in real-time:

🔗 https://spam-mail-classification-2ae3juzvbnpsylchxd8qrj.streamlit.app/

---

## Overview

This project builds a machine learning model to classify emails as **spam** or **ham (not spam)** using Natural Language Processing techniques.
The model is deployed as an interactive web application for real-time predictions.

---

## Web Application

The project is deployed using Streamlit.
Users can enter a message and instantly receive a prediction indicating whether the message is spam or not.

---

## Dataset

The dataset contains labeled email messages categorized as:

* **Spam** – Unwanted or promotional messages
* **Ham** – Legitimate emails

---

## Approach

### Data Preprocessing

* Handled missing values
* Converted labels into numerical format
* Split data into training and testing sets

### Feature Extraction

* Applied **TF-IDF Vectorization** to convert text into numerical features

### Model

* Logistic Regression

---

## Results

| Metric    | Training | Testing |
| --------- | -------- | ------- |
| Accuracy  | 0.9677   | 0.9668  |
| Precision | 0.9912   | 1.0000  |
| Recall    | 0.7635   | 0.7613  |

---

## Key Insights

* High precision indicates very low false positives
* Moderate recall suggests some spam messages are missed
* Model performs well for practical spam detection tasks

---

## Tech Stack

* Python
* NumPy, Pandas
* Scikit-learn
* Streamlit

---

## How to Run Locally

1. Clone the repository
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app

   ```bash
   streamlit run app.py
   ```

---

## Future Improvements

* Improve recall using hyperparameter tuning
* Experiment with advanced models (Naive Bayes, SVM, XGBoost)
* Enhance UI/UX of the web application

---

## Conclusion

This project demonstrates an end-to-end machine learning pipeline, including data preprocessing, feature extraction, model training, evaluation, and deployment as a web application.

---
