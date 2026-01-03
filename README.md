# E-Commerce Analytics Dashboard 🚀

An interactive data analytics dashboard built with **Streamlit** to transform raw e-commerce transaction data into **actionable business insights**.  
This project focuses on **sales performance**, **customer behavior**, and **RFM-based segmentation** for strategic decision-making.

---

## 🎯 Project Objectives

- Monitor overall e-commerce performance
- Analyze order and revenue trends over time
- Identify top-performing product categories
- Segment customers using **RFM Analysis**
- Provide a ready-to-use dashboard for business stakeholders

---

## 🧠 Key Insights Delivered

- Monthly trends of **total orders vs total revenue**
- Revenue contribution by product category
- Customer segmentation:
  - Champions
  - Loyal Customers
  - Potential Loyalists
  - At Risk
  - Hibernating
- Average monetary value per customer segment

---

## ⚙️ Environment Setup

### Option 1 — Conda (Recommended)

```bash
conda create --name ecommerce-ds python=3.9
conda activate ecommerce-ds
pip install -r requirements.txt
````

---

### Option 2 — Standard Python Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard Locally

```bash
streamlit run dashboard/dashboard.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## ☁️ Deployment (Streamlit Cloud)

This dashboard is fully compatible with **Streamlit Community Cloud**.

Deployment configuration:

* **Repository**: GitHub
* **Branch**: `main`
* **Main file path**:

  ```
  dashboard/dashboard.py
  ```

No additional configuration required.

---

## 🛠 Tech Stack

* **Python**
* **Pandas & NumPy** — data processing
* **Matplotlib & Seaborn** — visualization
* **Streamlit** — interactive dashboard

---

## 📌 Notes

* CSV files must remain in the `/data` directory
* File paths are relative to ensure cloud compatibility
* Designed for analytical clarity over visual noise

---