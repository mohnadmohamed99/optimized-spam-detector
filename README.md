<h1>🚀 Optimized Spam Detection System</h1>
<h2>📌 Project Overview</h2>
<p>
  The <strong>Optimized Spam Detection System</strong> is a Machine Learning
  project developed to automatically classify SMS messages into two categories:
</p>
<ul>
  <li>🚨 <strong>Spam</strong></li>
  <li>✅ <strong>Ham</strong></li>
</ul>
<p>
  The project uses Natural Language Processing and traditional Machine Learning
  algorithms to clean the dataset, convert text messages into numerical features,
  train and compare different classification models, optimize model performance,
  and select the best-performing model.
</p>
<h2>🎯 Project Objectives</h2>
<ul>
  <li>🔍 Inspect and understand the SMS Spam dataset.</li>
  <li>🧹 Clean and prepare the dataset.</li>
  <li>❓ Handle missing values and duplicated records.</li>
  <li>✅ Validate the Spam and Ham labels.</li>
  <li>✂️ Split the dataset into training and testing sets.</li>
  <li>⚖️ Maintain the class distribution using stratified splitting.</li>
  <li>🔢 Convert text messages into numerical features.</li>
  <li>🔒 Prevent Data Leakage during feature extraction.</li>
  <li>🤖 Train multiple Machine Learning classification models.</li>
  <li>📊 Evaluate models using different classification metrics.</li>
  <li>🧩 Create and analyze Confusion Matrices.</li>
  <li>⚙️ Improve model performance using Hyperparameter Tuning.</li>
  <li>🔄 Use GridSearchCV and Cross-Validation.</li>
  <li>🏆 Select the best-performing model.</li>
  <li>💾 Save the trained models and CountVectorizer.</li>
  <li>🐙 Collaborate using Git and GitHub.</li>
</ul>
<h2>🛠️ Tools &amp; Technologies</h2>
<ul>
  <li>🐍 Python</li>
  <li>🐼 Pandas</li>
  <li>🔢 NumPy</li>
  <li>🤖 Scikit-learn</li>
  <li>📊 Matplotlib</li>
  <li>🎨 Seaborn</li>
  <li>💾 Joblib</li>
  <li>☁️ Google Colab</li>
  <li>🐙 Git</li>
  <li>🌐 GitHub</li>
</ul>
<h2>📊 Dataset</h2>
<p>
  The project uses the <strong>SMS Spam Collection Dataset</strong>,
  which contains SMS messages labeled as either Spam or Ham.
</p>
<ul>
  <li>✅ <code>ham</code> — A legitimate message.</li>
  <li>🚨 <code>spam</code> — An unwanted, promotional, or suspicious message.</li>
</ul>
<h3>Original Dataset Columns</h3>
<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>v1</code></td>
      <td>Message label</td>
    </tr>
    <tr>
      <td><code>v2</code></td>
      <td>Message text</td>
    </tr>
    <tr>
      <td><code>v3</code></td>
      <td>Unused column</td>
    </tr>
    <tr>
      <td><code>v4</code></td>
      <td>Unused column</td>
    </tr>
    <tr>
      <td><code>v5</code></td>
      <td>Unused column</td>
    </tr>
  </tbody>
</table>
<p>
  During data preprocessing, the unnecessary columns were removed,
  and the required columns were renamed.
</p>
<h3>Final Dataset Columns</h3>
<table>
  <thead>
    <tr>
      <th>Final Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>label</code></td>
      <td>Target variable containing Spam or Ham</td>
    </tr>
    <tr>
      <td><code>message</code></td>
      <td>Original SMS message text</td>
    </tr>
  </tbody>
</table>
<h2>🔄 Project Workflow</h2>
<pre>
Raw Dataset
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Prepare X and y
     ↓
Train/Test Split
     ↓
Feature Extraction
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Confusion Matrix Analysis
     ↓
Hyperparameter Tuning
     ↓
Model Comparison
     ↓
Best Model Selection
     ↓
Save Trained Models
</pre>
<h2>🔍 Data Exploration</h2>
<p>
  The dataset was inspected before training to understand its structure
  and identify possible data quality problems.
</p>
<ul>
  <li>Display the first and last records.</li>
  <li>Check the number of rows and columns.</li>
  <li>Check the column names.</li>
  <li>Check the data types.</li>
  <li>Check missing values.</li>
  <li>Check duplicated records.</li>
  <li>Count Spam messages.</li>
  <li>Count Ham messages.</li>
  <li>Analyze the class distribution.</li>
  <li>Validate the target labels.</li>
</ul>
<h2>🧹 Data Preprocessing</h2>
<p>
  The dataset was cleaned and prepared before feature extraction.
</p>
<ul>
  <li>Rename <code>v1</code> to <code>label</code>.</li>
  <li>Rename <code>v2</code> to <code>message</code>.</li>
  <li>Select only the required columns.</li>
  <li>Remove unnecessary columns.</li>
  <li>Remove missing values.</li>
  <li>Remove duplicated records.</li>
  <li>Remove empty messages.</li>
  <li>Verify that the labels contain only Spam and Ham.</li>
  <li>Reset the DataFrame index.</li>
  <li>Save the cleaned dataset.</li>
</ul>
<h2>🎯 Preparing X and y</h2>
<p>
  The dataset was separated into features and labels:
</p>
<pre><code>X = df["message"]
y = df["label"]</code></pre>
<ul>
  <li><code>X</code> contains the SMS messages.</li>
  <li><code>y</code> contains the correct Spam or Ham labels.</li>
</ul>
<p>
  The dataset was divided into:
</p>
<ul>
  <li>📘 <strong>Training Set:</strong> 80%</li>
  <li>📙 <strong>Testing Set:</strong> 20%</li>
</ul>
<p>
  A stratified split was used to preserve the original proportion
  of Spam and Ham messages in both sets.
</p>
<pre><code>X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)</code></pre>
<h2>🔢 Feature Extraction</h2>
<p>
  Machine Learning models cannot process raw text directly.
  Therefore, <strong>CountVectorizer</strong> was used to convert
  the SMS messages into numerical word-count features.
</p>
<pre><code>vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)</code></pre>
<p>
  The vectorizer was fitted using the training data only.
  The testing data was transformed using the same fitted vectorizer
  to prevent <strong>Data Leakage</strong>.
</p>
<h3>Feature Extraction Results</h3>
<ul>
  <li>📘 Training feature matrix: <code>(4135, 7591)</code></li>
  <li>📙 Testing feature matrix: <code>(1034, 7591)</code></li>
  <li>📚 Vocabulary size: <code>7591</code></li>
</ul>
<p>
  Each row represents one SMS message, while each column represents
  a word from the training vocabulary.
</p>
<h2>🤖 Machine Learning Models</h2>
<p>
  Three Machine Learning classification models were trained and evaluated:
</p>
<ul>
  <li>📨 Multinomial Naive Bayes</li>
  <li>📈 Logistic Regression</li>
  <li>📐 Linear Support Vector Machine</li>
</ul>
<h3>Multinomial Naive Bayes</h3>
<p>
  Multinomial Naive Bayes is a fast and effective classification algorithm
  commonly used for text classification and word-count features.
</p>
<h3>Logistic Regression</h3>
<p>
  Logistic Regression learns a weight for each feature and predicts
  the class of each SMS message.
</p>
<h3>Linear Support Vector Machine</h3>
<p>
  Linear SVM finds the best decision boundary that separates Spam
  messages from Ham messages.
</p>
<h2>📊 Evaluation Metrics</h2>
<p>
  The models were evaluated using multiple classification metrics because
  Accuracy alone may be misleading when the dataset is imbalanced.
  Spam was treated as the positive class.
</p>
<ul>
  <li>
    ✅ <strong>Accuracy:</strong>
    The percentage of all predictions that were correct.
  </li>
  <li>
    🎯 <strong>Precision:</strong>
    The percentage of messages predicted as Spam that were actually Spam.
  </li>
  <li>
    🔍 <strong>Recall:</strong>
    The percentage of actual Spam messages detected by the model.
  </li>
  <li>
    ⚖️ <strong>F1-Score:</strong>
    The balance between Precision and Recall.
  </li>
  <li>
    🧩 <strong>Confusion Matrix:</strong>
    A detailed summary of correct and incorrect predictions.
  </li>
</ul>
<h2>🧩 Confusion Matrix Explanation</h2>
<ul>
  <li>
    ✅ <strong>True Positive (TP):</strong>
    A Spam message correctly classified as Spam.
  </li>
  <li>
    ✅ <strong>True Negative (TN):</strong>
    A Ham message correctly classified as Ham.
  </li>
  <li>
    ⚠️ <strong>False Positive (FP):</strong>
    A Ham message incorrectly classified as Spam.
  </li>
  <li>
    ⚠️ <strong>False Negative (FN):</strong>
    A Spam message incorrectly classified as Ham.
  </li>
</ul>
<h2>📈 Model Performance Results</h2>
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Multinomial Naive Bayes</td>
      <td>0.9865</td>
      <td>0.9756</td>
      <td>0.9160</td>
      <td>0.9449</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>0.9797</td>
      <td>0.9911</td>
      <td>0.8473</td>
      <td>0.9136</td>
    </tr>
    <tr>
      <td>Linear SVM</td>
      <td>0.9845</td>
      <td>1.0000</td>
      <td>0.8779</td>
      <td>0.9350</td>
    </tr>
  </tbody>
</table>
<h2>🧩 Confusion Matrix Results</h2>
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>TN</th>
      <th>FP</th>
      <th>FN</th>
      <th>TP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Multinomial Naive Bayes</td>
      <td>900</td>
      <td>3</td>
      <td>11</td>
      <td>120</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>902</td>
      <td>1</td>
      <td>20</td>
      <td>111</td>
    </tr>
    <tr>
      <td>Linear SVM</td>
      <td>903</td>
      <td>0</td>
      <td>16</td>
      <td>115</td>
    </tr>
  </tbody>
</table>
<h3>Naive Bayes Analysis</h3>
<ul>
  <li>Correctly classified 900 Ham messages.</li>
  <li>Incorrectly classified 3 Ham messages as Spam.</li>
  <li>Missed 11 Spam messages.</li>
  <li>Correctly detected 120 Spam messages.</li>
</ul>
<h3>Logistic Regression Analysis</h3>
<ul>
  <li>Correctly classified 902 Ham messages.</li>
  <li>Incorrectly classified 1 Ham message as Spam.</li>
  <li>Missed 20 Spam messages.</li>
  <li>Correctly detected 111 Spam messages.</li>
</ul>
<h3>Linear SVM Analysis</h3>
<ul>
  <li>Correctly classified 903 Ham messages.</li>
  <li>Did not classify any Ham message as Spam.</li>
  <li>Missed 16 Spam messages.</li>
  <li>Correctly detected 115 Spam messages.</li>
</ul>
<p>
  Linear SVM achieved a Precision of <strong>1.0000</strong>,
  meaning that every message classified as Spam was actually Spam.
</p>
<h2>⚙️ Hyperparameter Tuning</h2>
<p>
  <strong>GridSearchCV</strong> was used to optimize the Linear SVM model
  by testing different values of the <code>C</code> hyperparameter.
</p>
<pre><code>svm_parameters = {
    "C": [0.01, 0.1, 1, 10]
}</code></pre>
<p>
  The optimization process used:
</p>
<ul>
  <li>🔄 5-fold Cross-Validation.</li>
  <li>📊 Spam F1-Score as the scoring metric.</li>
  <li>📘 Training Data only.</li>
  <li>⚙️ Multiple values of the C hyperparameter.</li>
</ul>
<p>
  The Test Set remained untouched during Hyperparameter Tuning.
</p>
<h3>GridSearchCV Results</h3>
<ul>
  <li>🏆 Best Parameter: <code>C = 1</code></li>
  <li>📈 Best Cross-Validation F1-Score: <code>0.9239</code></li>
</ul>
<p>
  The best value selected by GridSearchCV was the same as the default
  value used by the original Linear SVM model. Therefore, the test
  performance remained unchanged after optimization.
</p>
<p>
  This result confirms that the original SVM configuration was already
  the best configuration among the tested values.
</p>
<h2>📊 SVM Performance Before and After Optimization</h2>
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SVM Before Optimization</td>
      <td>0.9845</td>
      <td>1.0000</td>
      <td>0.8779</td>
      <td>0.9350</td>
    </tr>
    <tr>
      <td>SVM After Optimization</td>
      <td>0.9845</td>
      <td>1.0000</td>
      <td>0.8779</td>
      <td>0.9350</td>
    </tr>
  </tbody>
</table>
<p>
  No performance improvement was observed because GridSearchCV selected
  <code>C = 1</code>, which was already used by the original model.
</p>
<h2>🏆 Best Model Selection</h2>
<p>
  <strong>Multinomial Naive Bayes</strong> achieved the highest Accuracy,
  Recall, and F1-Score.
</p>
<p>
  Therefore, Multinomial Naive Bayes was selected as the best overall
  model because it provided the strongest balance between Precision
  and Recall.
</p>
<p>
  Linear SVM achieved the highest Precision of <strong>1.0000</strong>,
  meaning that it did not incorrectly classify any legitimate Ham
  message as Spam.
</p>
<p>
  However, Linear SVM missed more Spam messages than Naive Bayes,
  which resulted in a lower Recall and F1-Score.
</p>
<h2>💾 Saved Project Files</h2>
<ul>
  <li>📄 Cleaned Spam dataset.</li>
  <li>🔢 Training and testing features.</li>
  <li>🏷️ Training and testing labels.</li>
  <li>📚 Fitted CountVectorizer.</li>
  <li>🤖 Trained Naive Bayes model.</li>
  <li>🤖 Trained Logistic Regression model.</li>
  <li>🤖 Trained Linear SVM model.</li>
  <li>⚙️ Optimized Linear SVM model.</li>
  <li>📊 Model evaluation results.</li>
  <li>📓 Project notebooks.</li>
</ul>
<h2>📂 Project Structure</h2>
<pre>
optimized-spam-detector/
│
├── data/
│   ├── spam.csv
│   ├── cleaned_spam.csv
│   │
│   └── processed/
│       ├── X_train_vec.pkl
│       ├── X_test_vec.pkl
│       ├── y_train.pkl
│       ├── y_test.pkl
│       └── model_results.csv
│
├── models/
│   ├── count_vectorizer.pkl
│   ├── naive_bayes_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── linear_svm_model.pkl
│   └── tuned_linear_svm_model.pkl
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_extraction.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_svm_evaluation_optimization.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
</pre>
<h2>👥 Team Members &amp; Responsibilities</h2>
<h3>👑 Member 1 — Team Leader</h3>
<p>
  <strong>Mohaned Mohamed Hanfy Amin</strong>
</p>
<p>
  Member 1 is responsible for coordinating the project and integrating
  the work completed by all team members.
</p>
<h4>Main Responsibilities</h4>
<ul>
  <li>Manage the GitHub repository.</li>
  <li>Coordinate tasks between team members.</li>
  <li>Review Pull Requests.</li>
  <li>Merge the completed project components.</li>
  <li>Ensure that all notebooks and files work together.</li>
  <li>Review the final project workflow.</li>
  <li>Prepare the project for final submission.</li>
</ul>
<h3>👤 Member 2 — Data Exploration &amp; Preprocessing</h3>
<p>
  <strong>Asser Abdallah Ahmed Mohammed</strong>
</p>
<p>
  Member 2 is responsible for understanding, cleaning, and preparing
  the raw dataset before the Machine Learning stages.
</p>
<h4>Main Responsibilities</h4>
<ul>
  <li>Load the raw SMS Spam dataset.</li>
  <li>Inspect the dataset structure.</li>
  <li>Check the number of rows and columns.</li>
  <li>Check column names and data types.</li>
  <li>Check missing values.</li>
  <li>Check duplicated records.</li>
  <li>Analyze the distribution of Spam and Ham messages.</li>
  <li>Rename the required columns.</li>
  <li>Select the Label and Message columns.</li>
  <li>Remove missing and duplicated records.</li>
  <li>Validate the Spam and Ham labels.</li>
  <li>Save the cleaned dataset.</li>
</ul>
<h3>👤 Member 3 — Feature Extraction &amp; Model Training</h3>
<p>
  <strong>Mariam Yahia Ahmad</strong>
</p>
<p>
  Member 3 is responsible for converting the cleaned text messages
  into numerical features and training the first two classification models.
</p>
<h4>Main Responsibilities</h4>
<ul>
  <li>Load the cleaned dataset.</li>
  <li>Prepare X as the messages and y as the labels.</li>
  <li>Split the dataset into training and testing sets.</li>
  <li>Maintain the Spam and Ham distribution using stratified splitting.</li>
  <li>Apply CountVectorizer.</li>
  <li>Fit the vectorizer only on the training data.</li>
  <li>Transform the testing data.</li>
  <li>Prevent Data Leakage.</li>
  <li>Check the feature dimensions.</li>
  <li>Perform feature sanity checks.</li>
  <li>Train the Multinomial Naive Bayes model.</li>
  <li>Train the Logistic Regression model.</li>
  <li>Generate predictions for both models.</li>
  <li>Calculate Accuracy, Precision, Recall, and F1-Score.</li>
  <li>Save the CountVectorizer.</li>
  <li>Save the processed features and labels.</li>
  <li>Save the trained classification models.</li>
</ul>
<h3>👤 Member 4 — SVM, Evaluation &amp; Optimization</h3>
<p>
  <strong>Raghad Mamdouh</strong>
</p>
<p>
  Member 4 is responsible for training and evaluating the Linear SVM
  model, analyzing the Confusion Matrices, optimizing the SVM model,
  and comparing the performance of all classification models.
</p>
<h4>Main Responsibilities</h4>
<ul>
  <li>Load the processed training and testing features.</li>
  <li>Train the Linear SVM model.</li>
  <li>Generate predictions using Linear SVM.</li>
  <li>Calculate Accuracy, Precision, Recall, and F1-Score for Linear SVM.</li>
  <li>Treat Spam as the positive class during evaluation.</li>
  <li>Create and visualize the Confusion Matrices.</li>
  <li>Explain TP, TN, FP, and FN results.</li>
  <li>Compare Naive Bayes, Logistic Regression, and Linear SVM.</li>
  <li>Apply GridSearchCV to optimize Linear SVM.</li>
  <li>Test different values of the <code>C</code> hyperparameter.</li>
  <li>Use 5-fold Cross-Validation during optimization.</li>
  <li>Identify the best SVM parameter and Cross-Validation score.</li>
  <li>Compare SVM performance before and after optimization.</li>
  <li>Analyze the final model results.</li>
  <li>Select the best overall model based on the evaluation metrics.</li>
  <li>Save the original and optimized Linear SVM models.</li>
  <li>Contribute to the final README and project documentation.</li>
</ul>
<h2>📝 Conclusion</h2>
<p>
  This project demonstrates how Machine Learning and Natural Language
  Processing techniques can be used to classify SMS messages as Spam or Ham.
</p>
<p>
  The complete project workflow included data exploration, data cleaning,
  Train/Test splitting, text feature extraction, model training, model
  evaluation, Confusion Matrix analysis, Hyperparameter Tuning, model
  comparison, and final model selection.
</p>
<p>
  The final results showed that Multinomial Naive Bayes provided the best
  overall balance between Precision and Recall.
</p>
<p>
  Linear SVM achieved perfect Precision and avoided incorrectly classifying
  legitimate Ham messages as Spam.
</p>
<p>
  The project also demonstrates the importance of evaluating classification
  models using multiple metrics instead of relying only on Accuracy.
</p>