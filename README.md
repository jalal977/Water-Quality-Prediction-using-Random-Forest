# 💧 Machine Learning-Based Water Quality Prediction

A Machine Learning-based web application that predicts whether water is **safe for consumption or not** based on various water-quality parameters.

The project aims to support **sustainable water management** by using machine learning to analyze water characteristics and provide a quick prediction of water quality.

---

## 📌 Project Overview

Water quality is an important factor for human health and environmental sustainability. Traditional water-quality testing can require laboratory analysis and specialized equipment.

This project uses **Machine Learning** to predict water potability based on chemical and physical properties of a water sample.

Users can enter the water-quality parameters through a **Streamlit web application**, and the trained ML model predicts whether the given water sample is:

* ✅ **Safe / Potable**
* ❌ **Not Safe / Not Potable**

---

## 🎯 Objectives

* Predict water potability using Machine Learning.
* Analyze important water-quality parameters.
* Provide a simple and user-friendly prediction interface.
* Reduce the complexity of manual water-quality analysis.
* Support data-driven and sustainable water management.

---

## 🧠 Machine Learning Parameters

The model uses the following parameters as input:

| Parameter           | Description                                 |
| ------------------- | ------------------------------------------- |
| **pH**              | Measures the acidity or alkalinity of water |
| **Hardness**        | Amount of dissolved calcium and magnesium   |
| **Solids**          | Total dissolved solids in water             |
| **Chloramines**     | Amount of chloramine present in water       |
| **Sulfate**         | Concentration of sulfate in water           |
| **Conductivity**    | Ability of water to conduct electricity     |
| **Organic Carbon**  | Amount of organic carbon present            |
| **Trihalomethanes** | Concentration of trihalomethanes            |
| **Turbidity**       | Measures the clarity/cloudiness of water    |

---

## 🔄 Project Workflow

```text
                Water Quality Dataset
                         │
                         ▼
                 Data Preprocessing
                         │
                         ▼
                  Feature Selection
                         │
                         ▼
                  Model Training
                         │
                         ▼
                 Model Evaluation
                         │
                         ▼
                  Save Trained Model
                  (water_model.pkl)
                         │
                         ▼
                Streamlit Web Application
                         │
                         ▼
              User Enters Water Parameters
                         │
                         ▼
                  ML Model Prediction
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        ✅ Safe Water         ❌ Not Safe
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Development Environment

* Google Colab
* VS Code / Local Python Environment

### Model Serialization

* Pickle

---

## 📂 Project Structure

```text
Water-Quality-Prediction/
│
├── app.py
├── water_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── water_potability.csv
│
└── notebooks/
    └── water_quality_prediction.ipynb
```

> `scaler.pkl` is required if feature scaling was used while training the model.

---

## 📊 Dataset

The dataset contains different physical and chemical characteristics of water samples.

The main features are:

```text
pH
Hardness
Solids
Chloramines
Sulfate
Conductivity
Organic Carbon
Trihalomethanes
Turbidity
```

The target variable represents whether the water is potable.

```text
0 → Not Potable
1 → Potable
```

---

## ⚙️ Machine Learning Process

### 1. Data Collection

The water-quality dataset is collected containing different chemical and physical properties of water.

### 2. Data Preprocessing

The dataset is analyzed and processed before training.

Preprocessing may include:

* Handling missing values
* Feature selection
* Data cleaning
* Feature scaling
* Train-test splitting

### 3. Model Training

The processed dataset is used to train the Machine Learning model.

### 4. Model Evaluation

The trained model is evaluated using appropriate classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### 5. Model Deployment

The trained model is saved using Pickle and integrated with a Streamlit application.

---

## 🖥️ Streamlit Application

The application provides a simple interface where users can enter the values of the nine water-quality parameters.

Example:

```text
pH                → 7.2
Hardness          → 200
Solids            → 15000
Chloramines       → 7
Sulfate           → 300
Conductivity      → 400
Organic Carbon    → 10
Trihalomethanes   → 60
Turbidity         → 3
```

After entering the values, the application sends them to the trained ML model and displays the prediction.

### Example Output

```text
💧 Water Quality Prediction

Prediction: ✅ Water is Safe / Potable
```

or

```text
💧 Water Quality Prediction

Prediction: ❌ Water is Not Safe / Not Potable
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Navigate to the Project

```bash
cd Water-Quality-Prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

### Step 5: Open the Application

After running the command, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```text
numpy
pandas
scikit-learn
streamlit
matplotlib
seaborn
```

---

## 🌟 Key Features

* 💧 Water potability prediction
* 🤖 Machine Learning-based analysis
* 📊 Multiple water-quality parameters
* 🖥️ Interactive Streamlit interface
* ⚡ Fast prediction
* 📈 Data preprocessing and model evaluation
* 🌱 Supports sustainable water management

---

## 🔮 Future Enhancements

The project can be further improved by adding:

* 📱 Mobile application
* ☁️ Cloud deployment
* 📊 Interactive water-quality dashboards
* 📍 Location-based water-quality analysis
* 📈 Historical water-quality tracking
* 🔔 Water-quality alerts
* 🧠 Comparison of multiple ML algorithms
* 🌐 Real-time IoT sensor integration
* 🗺️ Water-quality monitoring using geographical maps

---

## ⚠️ Disclaimer

This application is an **ML-based prediction system for educational and research purposes**. The prediction should not be considered a replacement for certified laboratory water-quality testing or regulatory assessment.

---

## 👨‍💻 Project Author

**Jalal**

B.Tech – ECE

### Technologies

`Python` `Machine Learning` `Scikit-learn` `Pandas` `NumPy` `Streamlit`

---

## ⭐ Project Highlights

> **Machine Learning-Based Water Quality Prediction for Sustainable Water Management**

This project demonstrates how Machine Learning can be applied to real-world environmental problems by analyzing water-quality parameters and predicting water potability through an easy-to-use web application.
