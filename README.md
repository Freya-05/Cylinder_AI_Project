#  Cylinder AI Predictive Maintenance System

This project implements an **AI-powered predictive maintenance system** for hydraulic cylinders. It processes sensor data, detects anomalies, computes a health index, and visualizes results using an interactive dashboard.

The goal is to simulate an **industrial-grade condition monitoring system** similar to what is used in hydraulic testing and validation labs.


##  Key Features

* Data preprocessing and feature engineering
* AI-based anomaly detection
* Health index calculation
* Interactive Streamlit dashboard
* Modular project structure
* Ready for real sensor data integration


## Project Structure

```
Cylinder_AI_Project/
│
├── data/
│   ├── raw_data.csv
│   ├── processed_data.csv
│   ├── predictions.csv
│   ├── health_results.csv
│
├── models/
│   └── anomaly_model.pkl
│
├── ai/
│   ├── preprocessing.py
│   ├── anomaly_model.py
│   ├── health_index.py
│
├── dashboard.py
├── README.md
└── requirements.txt (optional)
```


## Workflow

1. **Preprocessing**
   Cleans and normalizes raw sensor data.
2. **Anomaly Detection**
   Uses machine learning to detect abnormal cylinder behavior.
3. **Health Index Calculation**
   Converts predictions into a health score.
4. **Dashboard Visualization**
   Displays trends, anomalies, and health metrics.

---

## How to Run Locally

### 1️ Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib streamlit joblib
```

### 2️ Run Preprocessing

```bash
python ai/preprocessing.py
```

### 3️ Train / Run Anomaly Model

```bash
python ai/anomaly_model.py
```

### 4️ Generate Health Index

```bash
python ai/health_index.py
```

### 5️ Launch Dashboard

```bash
python -m streamlit run dashboard.py
```

---

## Dashboard Output

The dashboard shows:

* Sensor trends (Pressure, Position, Time)
* Anomaly detection results
* Health index score
* Maintenance status

---

## AI Techniques Used

* Feature scaling
* Unsupervised anomaly detection (Isolation Forest / similar)
* Health index mapping
* Time-series visualization

---

## Future Improvements

* Add Remaining Useful Life (RUL) prediction
* Integrate live sensor/PLC data
* Add cloud logging (AWS/Firebase)
* Improve model accuracy with labeled data

---

## Author

**Freya Naomi Lobo**
Mechatronics Engineer 
GitHub: [https://github.com/Freya-05](https://github.com/Freya-05)

