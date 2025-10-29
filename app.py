# # app.py - Streamlit Dashboard (Sensor + Image only)
# import streamlit as st
# import requests
# from PIL import Image
# import os

# # CONFIGURATION
# API_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
# st.set_page_config(page_title="Strawberry Disease Predictor", layout="wide", initial_sidebar_state="expanded")

# def check_api_status():
#     try:
#         response = requests.get(f"{API_URL}/", timeout=2)
#         return response.status_code == 200
#     except:
#         return False

# # Styling
# st.markdown("""
#     <style>
#         .main-header { text-align: center; color: #228B22; }
#         .stButton>button { width: 100%; }
#         .stMetric { text-align: center; }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<h1 class="main-header">Strawberry Disease Prediction Dashboard</h1>', unsafe_allow_html=True)
# st.markdown("---")

# # API Status
# if check_api_status():
#     st.success(" **FastAPI Server: CONNECTED**")
# else:
#     st.error(" **FastAPI Server: NOT RUNNING**")
#     st.info("Fix: Run `uvicorn main:app --reload` in another terminal")
#     st.stop()

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Choose Action", [
#     "Sensor Prediction", 
#     "Image Detection"
# ], label_visibility="collapsed")

# # === SENSOR PREDICTION ===
# if page == "Sensor Prediction":
#     st.header("**Sensor-Based Health Prediction**")
#     st.markdown("Enter sensor readings to predict plant health.")

#     with st.expander("**Environmental Parameters**", expanded=True):
#         col1, col2 = st.columns(2)
#         with col1:
#             soil_moisture = st.slider("Soil Moisture (%)", 10.0, 40.0, 25.0)
#             temp = st.slider("Ambient Temp (°C)", 18.0, 30.0, 24.0)
#             humidity = st.slider("Humidity (%)", 40.0, 70.0, 55.0)
#         with col2:
#             light = st.slider("Light Intensity", 200.0, 1000.0, 600.0)
#             ph = st.slider("Soil pH", 5.5, 7.5, 6.5)
#             soil_temp = st.slider("Soil Temp (°C)", 15.0, 25.0, 20.0)
    
#     with st.expander("**Nutrient Levels**", expanded=True):
#         col3, col4, col5 = st.columns(3)
#         with col3: nitrogen = st.slider("Nitrogen", 10.0, 50.0, 30.0)
#         with col4: phosphorus = st.slider("Phosphorus", 10.0, 50.0, 30.0)
#         with col5: potassium = st.slider("Potassium", 10.0, 50.0, 30.0)
    
#     with st.expander("**Health Indicators**", expanded=True):
#         col6, col7 = st.columns(2)
#         with col6: chlorophyll = st.slider("Chlorophyll", 20.0, 50.0, 35.0)
#         with col7: signal = st.slider("Electro Signal", 0.0, 2.0, 1.0)
    
#     if st.button("**PREDICT PLANT HEALTH**", type="primary"):
#         with st.spinner("Analyzing..."):
#             payload = {
#                 "Plant_ID": 1,
#                 "Soil_Moisture": soil_moisture,
#                 "Ambient_Temperature": temp,
#                 "Soil_Temperature": soil_temp,
#                 "Humidity": humidity,
#                 "Light_Intensity": light,
#                 "Soil_pH": ph,
#                 "Nitrogen_Level": nitrogen,
#                 "Phosphorus_Level": phosphorus,
#                 "Potassium_Level": potassium,
#                 "Chlorophyll_Content": chlorophyll,
#                 "Electrochemical_Signal": signal
#             }
#             try:
#                 response = requests.post(f"{API_URL}/predict/health", json=payload, timeout=10)
#                 result = response.json()
                
#                 st.markdown("### Prediction Results")
#                 col_a, col_b = st.columns([3, 1])
#                 with col_a:
#                     status = result['plant_health_status']
#                     if "Healthy" in status:
#                         st.success(f"**{status}**")
#                     elif "Moderate" in status:
#                         st.warning(f"**{status}**")
#                     else:
#                         st.error(f"**{status}**")
#                 with col_b:
#                     st.metric("Confidence", result['confidence'])
                
#                 with st.expander("Detailed Response"):
#                     st.json(result)
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

# # === IMAGE DETECTION ===
# elif page == "Image Detection":
#     st.header("**Image-Based Plant Detection**")
#     st.markdown("Upload an image to detect plants and stress levels.")

#     uploaded_file = st.file_uploader("Upload Plant Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", width=400)
        
#         if st.button("**DETECT PLANTS**", type="primary"):
#             with st.spinner("Detecting..."):
#                 files = {"file": uploaded_file.getvalue()}
#                 try:
#                     response = requests.post(f"{API_URL}/detect/image", files=files, timeout=30)
#                     result = response.json()
                    
#                     if "detections" in result and result["total_detections"] > 0:
#                         st.success(f"**Found {result['total_detections']} detection(s)**")
#                         for i, det in enumerate(result["detections"], 1):
#                             with st.expander(f"**Detection {i}: {det['class']}**"):
#                                 st.metric("Confidence", f"{det['confidence']:.1%}")
#                                 st.write(f"**Bounding Box:** {det['bbox']}")
#                     else:
#                         st.info("**No plants detected**")
#                 except Exception as e:
#                     st.error(f"Error: {str(e)}")


# app.py - Streamlit Dashboard (Sensor + Image only)
import streamlit as st
import requests
from PIL import Image
import os

# CONFIGURATION - Use env var for backend URL (set in Render)
API_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
st.set_page_config(page_title="Strawberry Disease Predictor", layout="wide", initial_sidebar_state="expanded")

def check_api_status():
    try:
        response = requests.get(f"{API_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

# Styling
st.markdown("""
    <style>
        .main-header { text-align: center; color: #228B22; }
        .stButton>button { width: 100%; }
        .stMetric { text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Strawberry Disease Prediction Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# API Status
if check_api_status():
    st.success(" **FastAPI Server: CONNECTED**")
else:
    st.error(" **FastAPI Server: NOT RUNNING**")
    st.info("Fix: Run `uvicorn main:app --reload` in another terminal")
    st.stop()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose Action", [
    "Sensor Prediction", 
    "Image Detection"
], label_visibility="collapsed")

# === SENSOR PREDICTION ===
if page == "Sensor Prediction":
    st.header("**Sensor-Based Health Prediction**")
    st.markdown("Enter sensor readings to predict plant health.")

    with st.expander("**Environmental Parameters**", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            soil_moisture = st.slider("Soil Moisture (%)", 10.0, 40.0, 25.0)
            temp = st.slider("Ambient Temp (°C)", 18.0, 30.0, 24.0)
            humidity = st.slider("Humidity (%)", 40.0, 70.0, 55.0)
        with col2:
            light = st.slider("Light Intensity", 200.0, 1000.0, 600.0)
            ph = st.slider("Soil pH", 5.5, 7.5, 6.5)
            soil_temp = st.slider("Soil Temp (°C)", 15.0, 25.0, 20.0)
    
    with st.expander("**Nutrient Levels**", expanded=True):
        col3, col4, col5 = st.columns(3)
        with col3: nitrogen = st.slider("Nitrogen", 10.0, 50.0, 30.0)
        with col4: phosphorus = st.slider("Phosphorus", 10.0, 50.0, 30.0)
        with col5: potassium = st.slider("Potassium", 10.0, 50.0, 30.0)
    
    with st.expander("**Health Indicators**", expanded=True):
        col6, col7 = st.columns(2)
        with col6: chlorophyll = st.slider("Chlorophyll", 20.0, 50.0, 35.0)
        with col7: signal = st.slider("Electro Signal", 0.0, 2.0, 1.0)
    
    if st.button("**PREDICT PLANT HEALTH**", type="primary"):
        with st.spinner("Analyzing..."):
            payload = {
                "Plant_ID": 1,
                "Soil_Moisture": soil_moisture,
                "Ambient_Temperature": temp,
                "Soil_Temperature": soil_temp,
                "Humidity": humidity,
                "Light_Intensity": light,
                "Soil_pH": ph,
                "Nitrogen_Level": nitrogen,
                "Phosphorus_Level": phosphorus,
                "Potassium_Level": potassium,
                "Chlorophyll_Content": chlorophyll,
                "Electrochemical_Signal": signal
            }
            try:
                response = requests.post(f"{API_URL}/predict/health", json=payload, timeout=10)
                result = response.json()
                
                st.markdown("### Prediction Results")
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    status = result['plant_health_status']
                    if "Healthy" in status:
                        st.success(f"**{status}**")
                    elif "Moderate" in status:
                        st.warning(f"**{status}**")
                    else:
                        st.error(f"**{status}**")
                with col_b:
                    st.metric("Confidence", result['confidence'])
                
                with st.expander("Detailed Response"):
                    st.json(result)
            except Exception as e:
                st.error(f"Error: {str(e)}")

# === IMAGE DETECTION ===
elif page == "Image Detection":
    st.header("**Image-Based Plant Detection**")
    st.markdown("Upload an image to detect plants and stress levels.")

    uploaded_file = st.file_uploader("Upload Plant Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=400)
        
        if st.button("**DETECT PLANTS**", type="primary"):
            with st.spinner("Detecting..."):
                files = {"file": uploaded_file.getvalue()}
                try:
                    response = requests.post(f"{API_URL}/detect/image", files=files, timeout=30)
                    result = response.json()
                    
                    if "detections" in result and result["total_detections"] > 0:
                        st.success(f"**Found {result['total_detections']} detection(s)**")
                        for i, det in enumerate(result["detections"], 1):
                            with st.expander(f"**Detection {i}: {det['class']}**"):
                                st.metric("Confidence", f"{det['confidence']:.1%}")
                                st.write(f"**Bounding Box:** {det['bbox']}")
                    else:
                        st.info("**No plants detected**")
                except Exception as e:
                    st.error(f"Error: {str(e)}")