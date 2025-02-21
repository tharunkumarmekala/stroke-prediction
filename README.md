Stroke Prediction Using Machine Learning

📌 Research Project Overview

This research project explores machine learning techniques to predict stroke occurrences based on clinical and demographic parameters. Our model is trained on a dataset containing essential risk factors, including hypertension, atrial fibrillation, cholesterol levels, and other key indicators. The study aims to develop a robust, high-accuracy model and deploy it online for public use.

🧪 Methodology

1️⃣ Dataset

The dataset includes clinical parameters such as Age, BMI, Blood Sugar, Cholesterol, Hypertension, and Atrial Fibrillation.

It has been preprocessed to balance stroke and non-stroke cases to improve model performance.

Feature engineering was applied to enhance predictive capabilities.

2️⃣ Machine Learning Model

The model utilizes XGBoost, a powerful gradient boosting algorithm.

Hyperparameter tuning was conducted using GridSearchCV to optimize performance.

Class imbalance was handled using SMOTE (Synthetic Minority Over-sampling Technique).

3️⃣ Evaluation Metrics

Accuracy

ROC-AUC Score

Precision-Recall Score

Confusion Matrix Analysis

🚀 Deployment Instructions

This project is deployed using GitHub and Cloudflare Workers to provide a fast, reliable, and serverless interface for stroke risk prediction.

1️⃣ Installation & Setup

Ensure you have the following installed:

Python (>=3.8)

pip

Required Python libraries (install using pip install -r requirements.txt)

Clone the Repository

git clone https://github.com/yourusername/stroke-prediction.git
cd stroke-prediction

Install Dependencies

pip install -r requirements.txt

2️⃣ Run the Model Locally

python main.py

This will prompt the user to enter patient details and return the stroke prediction result.

3️⃣ Deploying on Cloudflare Workers

Sign up for Cloudflare Workers: Cloudflare Workers

Install Wrangler CLI (Cloudflare’s command-line tool):

npm install -g wrangler

Authenticate with Cloudflare:

wrangler login

Initialize the Worker:

wrangler init stroke-prediction-api

Modify wrangler.toml to define the worker settings.

Deploy the model as a Cloudflare Worker API:

wrangler publish

Access the API Endpoint:
Cloudflare provides a URL where the model can be accessed publicly.

🔬 Research Contributions

Improved Stroke Prediction Accuracy using an optimized ML model.

Feature Engineering Enhancements that improve risk assessment.

Public Deployment via Cloudflare for real-time stroke prediction.

📜 Citation

If you use this work in your research, please cite it as:

Author(s), "Stroke Prediction Using Machine Learning," Research Project, 2025.

📩 Contact

For any questions or collaboration inquiries, please reach out via GitHub Issues or email: tharunkumarmekala@outlook.com
