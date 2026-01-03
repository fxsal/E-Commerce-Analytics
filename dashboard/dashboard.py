import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Config
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    layout="wide"
)
# Load Data
monthly_summary = pd.read_csv("dashboard/dashboard_monthly_summary.csv")
category_revenue = pd.read_csv("dashboard/dashboard_revenue_by_category.csv")
rfm_customer = pd.read_csv("dashboard/dashboard_rfm_customer.csv")
rfm_segment_summary = pd.read_csv("dashboard/dashboard_rfm_segment_summary.csv")

# Data handling
monthly_summary["order_month"] = pd.to_datetime(monthly_summary["order_month"])

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <div style='text-align:center'>
            <h2>🛒 E-Commerce Dashboard</h2>
            <p style='color:gray'>Sales & Customer Analytics</p>
        </div>
        <hr>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📅 Rentang Waktu Transaksi")

    min_date = monthly_summary["order_month"].min().date()
    max_date = monthly_summary["order_month"].max().date()

    date_range = st.date_input(
        "Pilih Periode",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("### 📊 Insight yang Ditampilkan")
    st.markdown(
        """
        • Tren Order & Revenue  
        • Kontribusi Kategori Produk  
        • Segmentasi Pelanggan (RFM)  
        """
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        <small>
        <b>Author</b><br>
        Moch. Faisal Syahwaludin<br>
        Data Analyst
        </small>
        """,
        unsafe_allow_html=True
    )

filtered_monthly = monthly_summary[
    (monthly_summary["order_month"].dt.date >= date_range[0]) &
    (monthly_summary["order_month"].dt.date <= date_range[1])
]

# Header Metrics
st.title("📊 E-Commerce Performance Overview")

col1, col2, col3 = st.columns(3)

total_orders = filtered_monthly["total_orders"].sum()
total_revenue = filtered_monthly["total_revenue"].sum()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Total Revenue", f"${total_revenue:,.0f}")
col3.metric("Average Order Value", f"${avg_order_value:,.2f}")

# Trend Analysis
st.subheader("📈 Order & Revenue Trend")

fig, ax1 = plt.subplots(figsize=(14, 5))

sns.lineplot(
    data=filtered_monthly,
    x="order_month",
    y="total_orders",
    marker="o",
    ax=ax1,
    label="Orders"
)

ax2 = ax1.twinx()

sns.lineplot(
    data=filtered_monthly,
    x="order_month",
    y="total_revenue",
    marker="s",
    color="orange",
    ax=ax2,
    label="Revenue"
)

ax1.set_xlabel("Month")
ax1.set_ylabel("Total Orders")
ax2.set_ylabel("Total Revenue")

ax1.tick_params(axis="x", rotation=45)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines_1 + lines_2,
    labels_1 + labels_2,
    loc="upper left",
    bbox_to_anchor=(0.01, 0.99)
)

st.pyplot(fig)

# Product Category Analysis
st.subheader("🏆 Revenue Contribution by Product Category")

top_categories = category_revenue.head(10)

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=top_categories,
    y="product_category_name",
    x="price",
    palette="Blues_r",
    ax=ax
)

ax.set_xlabel("Total Revenue")
ax.set_ylabel("Product Category")

st.pyplot(fig)

# RFM Customer Segmentation
st.subheader("👥 Customer Segmentation (RFM Analysis)")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=rfm_segment_summary,
        x="customer_count",
        y="Segment",
        palette="viridis",
        ax=ax
    )
    ax.set_title("Customer Distribution per Segment")
    ax.set_xlabel("Number of Customers")
    ax.set_ylabel("Segment")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=rfm_segment_summary,
        x="avg_monetary",
        y="Segment",
        palette="magma",
        ax=ax
    )
    ax.set_title("Average Monetary Value per Segment")
    ax.set_xlabel("Average Monetary")
    ax.set_ylabel("Segment")
    st.pyplot(fig)
    
# Footer
st.caption("Copyright © Moch. Faisal Syahwaludin 2026")