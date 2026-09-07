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



👥 Team Members & Responsibilities
👑 Member 1 — Team Leader (Mohaned Mohamed Hanfy Amin)
Responsibilities
Member 1 is responsible for coordinating the entire project and integrating the work of all team members.
Main responsibilities:
- Manage the GitHub repository.
- Coordinate the work between team members.
- Review Pull Requests.
- Integrate the different project components.
- Train Machine Learning models.
- Train Multinomial Naive Bayes.
- Train Logistic Regression.
- Train SVM.
- Generate predictions.
- Calculate evaluation metrics.
- Generate confusion matrices.
- Compare the Machine Learning models.
- Perform Hyperparameter Tuning.
- Use GridSearchCV.
- Analyze tuning results.
- Select the best-performing model.
- Save the final model.
- Perform final model validation.
- Make sure all project components work together

👤 Member 2 — Data Exploration & Preprocessing (asser abdallah ahmed mohammed)
Responsibilities
Member 2 is responsible for understanding and preparing the raw dataset before Machine Learning.
Main responsibilities:
- Load the raw dataset.
- Inspect the dataset.
- Check the number of rows and columns.
- Check column names.
- Check missing values.
- Check duplicate records.
- Analyze label distribution.
- Rename the dataset columns.
- Select the required columns.
- Remove missing records.
- Remove duplicate records.
- Validate Spam and Ham labels.
- Prepare the cleaned dataset.
- Save the cleaned dataset.


👤 Member 3 — Feature Extraction (mariam yahia ahmad)
Responsibilities
Member 3 is responsible for converting the cleaned text data into numerical features that can be used by Machine Learning algorithms.
Main responsibilities:
- Load the cleaned dataset.
- Create X and y.
- Perform Train/Test Split.
- Use train_test_split.
- Maintain Spam/Ham distribution using stratify.
- Apply CountVectorizer.
- Fit the vectorizer only on training data.
- Transform the testing data.
- Check feature dimensions.
- Perform feature sanity checks.
- Prevent data leakage.
- Save the CountVectorizer.
- Save training and testing features.
- Save training and testing labels.

👤 Member 4 — Streamlit Application & Documentation (Raghad mamdouh)
Responsibilities
Member 4 is responsible for building the user-facing application and helping finalize the project documentation.
Main responsibilities:
- Build the Streamlit application.
- Create the user interface.
- Create a text input for messages.
- Load the saved CountVectorizer.
- Load the saved best model.
- Transform new messages.
- Make predictions.
- Display Spam/Ham results.
- Display prediction probabilities when available.
- Test the application.
- Organize result files.
- Maintain and update the README.
- Help prepare the final project documentation.