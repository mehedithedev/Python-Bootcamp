import streamlit as st
import psutil
import time

# Set Streamlit page configuration
st.set_page_config(page_title="System Monitor", layout="wide")

# Function to get real-time data
def get_system_info():
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    return cpu_percent, virtual_memory

# Main Streamlit app
st.title("Real-Time System Monitor")

# Create an empty container for updating
info_container = st.empty()

while True:
    cpu_percent, virtual_memory = get_system_info()

    # Update the existing lines
    info_container.write(f"CPU Usage: {cpu_percent:.2f}%")
    info_container.write(f"Total RAM: {virtual_memory.total / (1024**3):.2f} GB")
    info_container.write(f"Used RAM: {virtual_memory.used / (1024**3):.2f} GB")
    info_container.write(f"Available RAM: {virtual_memory.available / (1024**3):.2f} GB")

    # Wait for 1 second before updating again
    time.sleep(1)
