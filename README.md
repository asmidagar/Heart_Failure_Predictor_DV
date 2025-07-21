# ❤️ Heart Failure Prediction Web App

This project is a **Flask-based web application** that predicts the risk of heart failure in patients based on clinical parameters using a machine learning model. It was built as part of the **5-Day Predictive Modeling Bootcamp by [Devtown](https://www.devtown.in/)**.

---

## 🧠 Project Objective

To build and deploy a machine learning model that predicts whether a patient is at risk of heart failure, using medical attributes like age, blood pressure, diabetes, creatinine levels, and more.

---

## 🚀 Features

- Real-time prediction of heart failure risk
- Trained using XGBoost with hyperparameter tuning and SMOTE for class balancing
- Modern responsive web UI with background image
- Built using Flask, HTML, CSS, and Python ML libraries

---

## 🗂️ Project Structure

```

heart-failure-prediction/
├── app.py                  # Flask application logic
├── model.pkl               # Trained ML model + scaler
├── requirements.txt        # List of dependencies
├── templates/
│   └── index.html          # Web interface with embedded CSS
└── static/
└── background.jpg      # Background image for the app

````

---

## ⚙️ How to Run Locally

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/heart-failure-prediction.git
cd heart-failure-prediction
````

2. **Create a virtual environment**:

```bash
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**:

```bash
python app.py
```

5. **Visit the app** in your browser at:

```
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* **Algorithm Used**: XGBoost Classifier
* **Accuracy Achieved**: \~80% after hyperparameter tuning
* **Preprocessing**:

  * Log transformation for skewed features
  * Scaling with StandardScaler
  * SMOTE for class balancing
* **Evaluation Metrics**: Accuracy, ROC AUC, Classification Report

---

## 📸 Screenshot

<img width="1920" height="1020" alt="Screenshot 2025-07-21 175201" src="https://github.com/user-attachments/assets/12f28d3b-f8a4-4714-9bd0-51e3ba3abf20" />

<img width="1920" height="1020" alt="Screenshot 2025-07-21 175126" src="https://github.com/user-attachments/assets/5f233a49-b25d-4e63-b70d-8f882e717d94" />

---

## 🙏 Acknowledgement

This project was developed as part of the **5-Day Predictive Modeling Bootcamp by [Devtown](https://www.devtown.in/)**.
Special thanks to the instructors and mentors who guided us throughout the bootcamp and helped bring this project to life.

---

## ✍️ Author

**Asmi Dagar**
GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

```

