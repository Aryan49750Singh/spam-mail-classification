# Spam Mail Classification

## Overview

This project builds a machine learning model to classify emails as **spam** or **ham (not spam)** using Natural Language Processing techniques. The goal is to accurately detect unwanted messages and improve filtering systems.

---

## Dataset

The dataset contains labeled email messages with two categories:

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

* **Logistic Regression** used for classification

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
* Model performs well and is suitable for basic spam detection

---

## Tech Stack

* Python
* NumPy, Pandas
* Scikit-learn

---

## How to Run

1. Clone the repository
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook and run all cells

---

## Future Improvements

* Use advanced models (Naive Bayes, SVM, XGBoost)
* Improve recall using hyperparameter tuning
* Deploy as a web application

---

## Conclusion

This project demonstrates an end-to-end NLP pipeline including preprocessing, feature extraction, model training, and evaluation for spam classification.

---

