# 🚀 Optimized Spam Detection System

## 📌 Project Overview

The **Optimized Spam Detection System** is a Machine Learning project developed to automatically classify SMS messages into two categories:

- 🚨 **Spam**
- ✅ **Ham**

The project uses Natural Language Processing (NLP) and traditional Machine Learning algorithms to clean the dataset, convert text messages into numerical features, train and compare different classification models, optimize the selected model, and provide a user-friendly prediction application using Streamlit.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Inspect and understand the SMS Spam dataset.
- Clean and prepare the dataset.
- Handle missing values and duplicate records.
- Split the dataset into training and testing sets.
- Convert text messages into numerical features.
- Train multiple Machine Learning classification models.
- Evaluate models using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- Compare the performance of different models.
- Improve model performance using Hyperparameter Tuning.
- Use GridSearchCV and Cross Validation.
- Select the best-performing model.
- Save the trained model and CountVectorizer.
- Build a Streamlit application for Spam/Ham prediction.
- Collaborate using Git and GitHub.

---

# 📊 Dataset

The project uses an SMS Spam dataset containing labeled messages.

Each message belongs to one of two classes:

- `ham` → legitimate message
- `spam` → unwanted or suspicious message

### Original Dataset Columns

| Column | Description |
|--------|-------------|
| `v1` | Message label |
| `v2` | Message text |
| `v3` | Unused column |
| `v4` | Unused column |
| `v5` | Unused column |

During preprocessing, the required columns were renamed and selected:

| Final Column | Description |
|-------------|-------------|
| `label` | Target variable (`spam` or `ham`) |
| `message` | SMS message text |

---

# 🔄 Project Workflow

The complete Machine Learning workflow is:

```text
Raw Dataset
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Train/Test Split
     ↓
Feature Extraction
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
Best Model Selection
     ↓
Final Evaluation
     ↓
Save Model
     ↓
Streamlit Application

<h2>👥 Team Members &amp; Responsibilities</h2>
<h3>👑 Member 1 — Team Leader (Mohaned Mohamed Hanfy Amin)</h3>
<h4>Responsibilities</h4>
<p>
  Member 1 is responsible for coordinating the project and integrating
  the work completed by all team members.
</p>
<ul>
  <li>Manage the GitHub repository.</li>
  <li>Coordinate tasks between team members.</li>
  <li>Review Pull Requests.</li>
  <li>Merge the completed project components.</li>
  <li>Ensure that all notebooks and files work together.</li>
  <li>Review the final project workflow.</li>
  <li>Prepare the project for final submission.</li>
</ul>
<h3>👤 Member 2 — Data Exploration &amp; Preprocessing (Asser Abdallah Ahmed Mohammed)</h3>
<h4>Responsibilities</h4>
<p>
  Member 2 is responsible for understanding, cleaning, and preparing
  the raw dataset before the Machine Learning stages.
</p>
<ul>
  <li>Load the raw SMS Spam dataset.</li>
  <li>Inspect the dataset structure.</li>
  <li>Check the number of rows and columns.</li>
  <li>Check column names and data types.</li>
  <li>Check missing values.</li>
  <li>Check duplicated records.</li>
  <li>Analyze the distribution of Spam and Ham messages.</li>
  <li>Rename the required columns.</li>
  <li>Select the label and message columns.</li>
  <li>Remove missing and duplicated records.</li>
  <li>Validate the Spam and Ham labels.</li>
  <li>Save the cleaned dataset.</li>
</ul>
<h3>👤 Member 3 — Feature Extraction &amp; Model Training (Mariam Yahia Ahmad)</h3>
<h4>Responsibilities</h4>
<p>
  Member 3 is responsible for converting the cleaned text messages into
  numerical features and training the first two classification models.
</p>
<ul>
  <li>Load the cleaned dataset.</li>
  <li>Prepare X as the messages and y as the labels.</li>
  <li>Split the dataset into training and testing sets.</li>
  <li>Maintain the Spam and Ham distribution using stratified splitting.</li>
  <li>Apply CountVectorizer to the training messages.</li>
  <li>Transform the testing messages using the fitted vectorizer.</li>
  <li>Prevent data leakage by fitting the vectorizer on training data only.</li>
  <li>Train the Multinomial Naive Bayes model.</li>
  <li>Train the Logistic Regression model.</li>
  <li>Generate predictions for both models.</li>
  <li>Calculate Accuracy, Precision, Recall, and F1-Score.</li>
  <li>Save the CountVectorizer and processed features.</li>
  <li>Save the trained Naive Bayes and Logistic Regression models.</li>
</ul>
<h3>👤 Member 4 — SVM, Evaluation &amp; Optimization (Raghad Mamdouh)</h3>
<h4>Responsibilities</h4>
<p>
  Member 4 is responsible for training and evaluating the Linear SVM model,
  analyzing the Confusion Matrices, optimizing the SVM model, and comparing
  the performance of all classification models.
</p>
<ul>
  <li>Load the processed training and testing features.</li>
  <li>Train the Linear Support Vector Machine model.</li>
  <li>Generate predictions using Linear SVM.</li>
  <li>Calculate Accuracy, Precision, Recall, and F1-Score for Linear SVM.</li>
  <li>Treat Spam as the positive class during evaluation.</li>
  <li>Create and visualize the Confusion Matrices.</li>
  <li>Explain True Positive, True Negative, False Positive, and False Negative results.</li>
  <li>Compare the performance of Naive Bayes, Logistic Regression, and Linear SVM.</li>
  <li>Apply GridSearchCV to optimize the Linear SVM model.</li>
  <li>Test different values of the C hyperparameter.</li>
  <li>Use 5-fold Cross-Validation during optimization.</li>
  <li>Identify the best SVM hyperparameter and Cross-Validation score.</li>
  <li>Compare SVM performance before and after optimization.</li>
  <li>Analyze and explain the final model results.</li>
  <li>Select the best overall model based on the evaluation results.</li>
  <li>Save the original and optimized Linear SVM models.</li>
  <li>Contribute to the final README and project documentation.</li>
</ul>
