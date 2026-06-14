# 🏠 Smart Home Energy Monitoring System

An IoT-inspired Smart Home Energy Monitoring System that simulates real-time energy consumption, performs energy analytics, generates alerts, predicts future energy usage, and creates automated PDF reports. The project combines an ESP32-based hardware prototype (Wokwi Simulation) with a Python-powered analytics dashboard built using Streamlit.

---

## 📌 Project Overview

Energy consumption monitoring is an essential part of modern smart homes. This project provides a complete solution for tracking and analyzing household energy usage.

The system simulates sensor readings from home appliances, calculates power consumption, estimates electricity costs, identifies high-energy usage events, predicts future consumption, and visualizes all data through an interactive dashboard.

---

## 🎯 Objectives

* Monitor energy consumption of household appliances
* Calculate power usage and energy consumption
* Estimate electricity costs
* Detect high energy usage events
* Predict future energy consumption
* Generate automated PDF reports
* Visualize energy analytics through an interactive dashboard

---

## 🛠️ Technology Stack

### Hardware Simulation

* ESP32 DevKit V1
* Potentiometer (Current Sensor Simulation)
* OLED Display (SSD1306)
* LED Indicator
* Buzzer

### Software

* Python
* Streamlit
* Pandas
* Plotly
* FPDF2

### Simulation Platform

* Wokwi

---

## 📂 Project Structure

```text
Smart-Home-Energy-Monitoring-System/

│
├── arduino_code/
│   └── smart_energy_monitor.ino
│
├── python_simulation/
│   └── energy_simulator.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── energy_log.csv
│
├── outputs/
│   └── energy_report.pdf
│
├── images/
│   ├── dashboard.png
│   ├── pdf_report.png
│   ├── wokwi_circuit.png
│   └── serial_monitor.png
│
├── circuit_diagram/
│
├── docs/
│   └── architecture.txt
│
├── reports/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙️ System Architecture

```text
+----------------------+
| Potentiometer        |
| (Current Simulation) |
+----------+-----------+
           |
           v
+----------------------+
| ESP32 Controller     |
+----------+-----------+
           |
           v
+----------------------+
| Power Calculation    |
+----------+-----------+
           |
           v
+----------------------+
| CSV Data Logging     |
+----------+-----------+
           |
           v
+----------------------+
| Streamlit Dashboard  |
+----------+-----------+
           |
           v
+----------------------+
| Alerts & Reports     |
+----------------------+
```

---

## 🚀 Features

### Real-Time Energy Monitoring

* Simulates appliance energy consumption
* Calculates voltage, current, and power

### Interactive Dashboard

* Total Energy Consumption
* Estimated Cost Analysis
* High Usage Alert Counter
* Hourly Energy Consumption Chart
* Appliance Usage Distribution

### Alert System

* Detects high power consumption events
* Generates warning notifications

### Energy Prediction

* Predicts next-day energy usage
* Estimates future electricity costs

### Automated Reporting

* Generates PDF reports
* Includes energy statistics and usage summary

---

## 📊 Dashboard Preview

### Main Dashboard

![Dashboard](images/dashboard.png)

### Appliance Usage Distribution

Interactive Pie Chart showing appliance-wise energy usage.

### Hourly Energy Consumption

Bar Chart showing energy consumption trends.

---

## 🔌 Hardware Prototype (Wokwi)

Due to the absence of the ACS712 sensor in Wokwi, a potentiometer is used to simulate varying current values.

### Components

* ESP32 DevKit V1
* Potentiometer
* OLED Display
* LED
* Buzzer

### Circuit Preview

![Wokwi Circuit](images/wokwi_circuit.png)

---

## 📈 Energy Analytics

The system computes:

* Total Energy Consumption (kWh)
* Power Consumption (W)
* Estimated Cost (₹)
* High Usage Events
* Appliance-wise Distribution
* Future Energy Prediction

---

## 📄 PDF Report Generation

The system automatically generates:

```text
Energy Report
-------------
Total Energy Used
Estimated Cost
High Usage Alerts
Top Consuming Appliance
Recent Energy Records
Prediction Summary
```

### Report Preview

![PDF Report](images/pdf_report.png)

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Home-Energy-Monitoring-System.git
```

```bash
cd Smart-Home-Energy-Monitoring-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Generate Energy Data

```bash
python python_simulation/energy_simulator.py
```

### Launch Dashboard

```bash
streamlit run dashboard/dashboard.py
```

### Generate PDF Report

```bash
python main.py
```

---

## 📌 Future Enhancements

* Real ACS712 Current Sensor Integration
* MQTT Cloud Connectivity
* Firebase Integration
* Mobile Application
* Machine Learning-Based Forecasting
* Smart Appliance Control

---

## 🎓 Learning Outcomes

* IoT System Design
* Sensor Data Simulation
* Data Analytics
* Dashboard Development
* Python Programming
* Report Automation
* Energy Management Concepts

---

## 👨‍🏫 Acknowledgement

Special thanks to my mentor for continuous guidance and support throughout the development of this project.

---

## 📜 License

This project is developed for educational and academic purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
