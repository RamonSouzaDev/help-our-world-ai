import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
from datetime import datetime
import sys
import os

# Ensure src is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensors.biosensor import BioSensor
from ai.diagnostic import MedicalDiagnosticAI
from ai.coach import HealthCoachAI
from data.gov_integration import GovernmentHealthAPI

# Page Config
st.set_page_config(
    page_title="Health Sentinel | AI Command Center",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize System
if 'sensor' not in st.session_state:
    st.session_state['sensor'] = BioSensor(patient_id="PATIENT-X-99")
    st.session_state['ai'] = MedicalDiagnosticAI()
    st.session_state['coach'] = HealthCoachAI()
    st.session_state['gov_api'] = GovernmentHealthAPI(region="BR-SP")
    st.session_state['history'] = []

def main():
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🏥 Health Sentinel AI")
        st.caption("Real-Time Epidemiological Monitoring System (SUS Integrated)")
    with col2:
        st.image("https://img.icons8.com/color/96/000000/heart-monitor.png", width=60)

    # Sidebar: Control Panel
    st.sidebar.header("🕹️ Simulation Controls")
    simulation_speed = st.sidebar.slider("Simulation Speed (ms)", 100, 2000, 1000)
    
    # Accessibility Controls
    st.sidebar.markdown("---")
    st.sidebar.header("♿ Accessibility")
    high_contrast = st.sidebar.toggle("High Contrast Mode", help="Optimized for low vision and WCAG 2.1 compliance")
    
    inject_event = st.sidebar.button("⚠️ INJECT SEPSIS EVENT")
    
    # Regional Context
    gov_data = st.session_state['gov_api'].fetch_epidemiological_alerts()
    st.sidebar.markdown("---\n")
    
    if high_contrast:
        st.sidebar.subheader(f"REGION: {gov_data['region']}")
        st.sidebar.error(f"OUTBREAKS: {', '.join([o['disease'] for o in gov_data['active_outbreaks']])}")
    else:
        st.sidebar.subheader(f"🌍 Region: {gov_data['region']}")
        st.sidebar.error(f"Active Outbreaks: {', '.join([o['disease'] for o in gov_data['active_outbreaks']])}")

    # Main Dashboard
    placeholder = st.empty()
    
    # Simulation Loop (Pseudo-Loop for Streamlit)
    if inject_event:
        st.session_state['sensor'].inject_pathology("SEPSIS_SHOCK")
        st.toast("⚠️ SEPSIS EVENT INJECTED!", icon="💉")

    # Generate Data
    vitals = st.session_state['sensor'].read_vitals()
    diagnosis = st.session_state['ai'].analyze_vitals(vitals)
    advice = st.session_state['coach'].generate_advice(vitals)
    
    # Update History
    st.session_state['history'].append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "HR": vitals.heart_rate_bpm,
        "SpO2": vitals.spo2_percent,
        "Temp": vitals.temperature_c
    })
    
    # Keep only last 20 points
    if len(st.session_state['history']) > 20:
        st.session_state['history'].pop(0)
        
    df = pd.DataFrame(st.session_state['history'])

    # Accessibility: Dynamic Color Palettes
    color_hr = "#FFFFFF" if high_contrast else "#FF4B4B"
    color_bg = "#000000" if high_contrast else "#1E1E1E"
    
    with placeholder.container():
        # KPI Metrics
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Heart Rate", f"{vitals.heart_rate_bpm} BPM", delta_color="inverse")
        kpi2.metric("SpO2", f"{vitals.spo2_percent}%", delta_color="normal")
        kpi3.metric("Temperature", f"{vitals.temperature_c}°C", delta_color="inverse")
        
        status_color = "red" if diagnosis["status"] == "CRITICAL" else "green"
        kpi4.markdown(f"**Status**: :{status_color}[{diagnosis['status']}]")

        # Charts
        chart1, chart2 = st.columns(2)
        
        # Charts - ACCESSIBILITY FOR BLIND USERS
        # Screen readers cannot read Plotly charts. We must provide a text summary.
        chart1, chart2 = st.columns(2)
        
        with chart1:
            st.subheader("Cardiology (Real-Time)")
            if not df.empty:
                # Text Summary for Screen Readers (Hidden visually or just plain text)
                st.markdown(f"**Accessibility Summary**: The heart rate graph shows a trend from {df['HR'].iloc[0]} to {df['HR'].iloc[-1]} BPM over the last {len(df)} seconds.", help="Text description of the chart for screen readers.")
                
                fig_hr = go.Figure()
                fig_hr.add_trace(go.Scatter(
                    y=df["HR"], 
                    mode='lines+markers', 
                    name='HR', 
                    line=dict(color=color_hr, width=4 if high_contrast else 2) 
                ))
                fig_hr.update_layout(
                    height=300, 
                    margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor=color_bg,
                    plot_bgcolor=color_bg,
                    font=dict(color=color_hr)
                )
                st.plotly_chart(fig_hr, use_container_width=True)

    # Accessibility: Voice Command Simulation (Reduced Mobility)
    st.markdown("---")
    st.subheader("🎤 Voice Command Interface (Accessibility)")
    col_mic, col_status = st.columns([1, 4])
    with col_mic:
        voice_active = st.toggle("Enable Microphone", help="Activate hands-free voice control for users with reduced mobility.")
    with col_status:
        if voice_active:
            st.info("Listening... (Simulated: Say 'Report Status' or 'Call Nurse')")
            if diagnosis["status"] == "CRITICAL":
                st.warning("Voice System Detecting Agonal Breathing Patterns.")


        with chart2:
            st.subheader("🌬️ Oxygen Saturation")
            if not df.empty:
                fig_spo2 = go.Figure()
                fig_spo2.add_trace(go.Scatter(y=df["SpO2"], mode='lines', name='SpO2', fill='tozeroy', line=dict(color='cyan')))
                fig_spo2.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(range=[80, 100]))
                st.plotly_chart(fig_spo2, use_container_width=True)

        # AI Insights Section
        st.markdown("### 🧠 AI Analysis & Coach")
        
        if diagnosis["status"] == "CRITICAL":
            st.error(f"🚨 **CRITICAL ALERT**: {diagnosis['detected_anomalies']}")
            st.warning(f"💊 **ACTION**: {diagnosis['recommendation']}")
            if "FEVER" in diagnosis["detected_anomalies"]:
                 st.info(f"🏛️ **GOV DATA**: Symptoms match active *Dengue Serotype 3* in BR-SP")
        else:
            st.success(f"✅ Patient Stable")
            st.chat_message("assistant").write(f"**Dr. Sentinel**: {advice}")

    # Auto-rerun trigger
    time.sleep(simulation_speed / 1000)
    st.rerun()

if __name__ == "__main__":
    main()
