import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Smart Home Energy Monitoring",
    page_icon="🏠",
    layout="centered"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

/* Main container */
.block-container{
    max-width:1100px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Title */
h1{
    text-align:center;
    margin-bottom:30px;
}

/* Metric cards */
.metric-card{
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

/* Chart containers */
[data-testid="stPlotlyChart"]{
    border-radius:15px;
    padding:10px;
    background-color:#111827;
}

/* Section spacing */
section.main > div{
    padding-top:1rem;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# TITLE
# ==================================

st.title("🏠 Smart Home Energy Monitoring System")

# ==================================
# LOAD DATA
# ==================================

try:

    df = pd.read_csv("data/energy_log.csv")

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # ==================================
    # KPI CALCULATIONS
    # ==================================

    total_energy = df["Energy_kWh"].sum()

    total_cost = df["Cost"].sum()

    alerts = len(
        df[df["Alert"] == "HIGH_USAGE"]
    )

    # ==================================
    # KPI CARDS
    # ==================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
        <div class="metric-card"
             style="background:#2563eb;">
             <h4>⚡ Total Energy</h4>
             <h2>{total_energy:.2f} kWh</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card"
             style="background:#16a34a;">
             <h4>💰 Total Cost</h4>
             <h2>₹ {total_cost:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        alert_color = "#dc2626" if alerts > 0 else "#15803d"

        st.markdown(f"""
        <div class="metric-card"
             style="background:{alert_color};">
             <h4>🚨 Alerts</h4>
             <h2>{alerts}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ==================================
    # ALERT MESSAGE
    # ==================================

    if alerts > 0:

        st.error(
            f"🚨 Warning: {alerts} High Usage Events Detected"
        )

    else:

        st.success(
            "✅ No High Usage Events Found"
        )

    # ==================================
    # HOURLY ENERGY CONSUMPTION
    # ==================================

    st.subheader("📊 Hourly Energy Consumption")

    hourly = (
        df.groupby(
            pd.Grouper(
                key="Timestamp",
                freq="h"
            )
        )["Energy_kWh"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        hourly,
        x="Timestamp",
        y="Energy_kWh",
        title="Energy Consumption Per Hour"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==================================
    # APPLIANCE DISTRIBUTION
    # ==================================

    st.subheader("🔌 Appliance Usage Distribution")

    appliance_usage = (
        df.groupby("Appliance")["Energy_kWh"]
        .sum()
        .reset_index()
    )

    pie = px.pie(
        appliance_usage,
        names="Appliance",
        values="Energy_kWh",
        hole=0.45
    )

    pie.update_layout(
        template="plotly_dark",
        height=500,
        title_x=0.5
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.divider()

    # ==================================
    # PREDICTIONS
    # ==================================

    st.subheader("🔮 Energy Prediction")

    predicted_energy = total_energy * 1.12

    predicted_cost = total_cost * 1.12

    p1, p2 = st.columns(2)

    with p1:

        st.warning(
            f"⚡ Predicted Next-Day Usage: "
            f"{predicted_energy:.2f} kWh"
        )

    with p2:

        st.info(
            f"💰 Predicted Next-Day Cost: "
            f"₹ {predicted_cost:.2f}"
        )

    st.divider()

    # ==================================
    # TOP APPLIANCE
    # ==================================

    top_appliance = (
        appliance_usage
        .sort_values(
            by="Energy_kWh",
            ascending=False
        )
        .iloc[0]
    )

    st.success(
        f"🏆 Highest Energy Consumer: "
        f"{top_appliance['Appliance']} "
        f"({top_appliance['Energy_kWh']:.2f} kWh)"
    )

except Exception as e:

    st.error(
        f"Error Loading Dashboard: {e}"
    )