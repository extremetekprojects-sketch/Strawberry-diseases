# # # main.py - FastAPI Backend (Sensor + Image only)
# # from fastapi import FastAPI, UploadFile, File
# # from pydantic import BaseModel
# # import joblib
# # from ultralytics import YOLO
# # import numpy as np
# # from PIL import Image
# # import io
# # import warnings

# # warnings.filterwarnings("ignore")

# # # Sensor Data Model (12 features)
# # class SensorData(BaseModel):
# #     Plant_ID: int = 1
# #     Soil_Moisture: float
# #     Ambient_Temperature: float
# #     Soil_Temperature: float
# #     Humidity: float
# #     Light_Intensity: float
# #     Soil_pH: float
# #     Nitrogen_Level: float
# #     Phosphorus_Level: float
# #     Potassium_Level: float
# #     Chlorophyll_Content: float
# #     Electrochemical_Signal: float

# # app = FastAPI(title="Strawberry Disease Prediction API", version="1.0.0")

# # # Load models
# # print("Loading models...")
# # yolo_model = YOLO("best.pt")
# # dt_model = joblib.load("Decision_Tree.pkl")
# # scaler = joblib.load("scaler.pkl")
# # print("Models loaded successfully!")

# # label_map = {0: "Healthy", 1: "Moderate Stress", 2: "High Stress"}

# # @app.post("/predict/health")
# # async def predict_health(data: SensorData):
# #     try:
# #         input_data = np.array([[
# #             data.Plant_ID, data.Soil_Moisture, data.Ambient_Temperature, 
# #             data.Soil_Temperature, data.Humidity, data.Light_Intensity,
# #             data.Soil_pH, data.Nitrogen_Level, data.Phosphorus_Level,
# #             data.Potassium_Level, data.Chlorophyll_Content, data.Electrochemical_Signal
# #         ]])
        
# #         input_scaled = scaler.transform(input_data)
# #         pred = dt_model.predict(input_scaled)[0]
# #         confidence = dt_model.predict_proba(input_scaled)[0].max() * 100
        
# #         health_status = label_map.get(int(pred), "Unknown")
        
# #         return {
# #             "plant_health_status": health_status,
# #             "confidence": f"{confidence:.2f}%",
# #             "prediction_code": int(pred)
# #         }
# #     except Exception as e:
# #         return {"error": f"Prediction failed: {str(e)}"}

# # @app.post("/detect/image")
# # async def detect_image(file: UploadFile = File(...)):
# #     try:
# #         contents = await file.read()
# #         image = Image.open(io.BytesIO(contents))
# #         results = yolo_model(image)
        
# #         detections = []
# #         for r in results:
# #             boxes = r.boxes
# #             if boxes is not None:
# #                 for box in boxes:
# #                     detections.append({
# #                         "class": r.names[int(box.cls)],
# #                         "confidence": float(box.conf),
# #                         "bbox": box.xyxy.tolist()[0]
# #                     })
        
# #         return {"detections": detections, "total_detections": len(detections)}
# #     except Exception as e:
# #         return {"error": f"Image detection failed: {str(e)}"}

# # @app.get("/")
# # async def root():
# #     return {
# #         "message": "Plant Disease Prediction API",
# #         "endpoints": [
# #             "POST /predict/health - Sensor data prediction",
# #             "POST /detect/image - Image detection"
# #         ]
# #     }

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="127.0.0.1", port=8000)


# # main.py - FastAPI Backend (Sensor + Image only)
# from fastapi import FastAPI, UploadFile, File
# from pydantic import BaseModel
# import joblib
# from ultralytics import YOLO
# import numpy as np
# from PIL import Image
# import io
# import warnings
# import os
# import uvicorn

# warnings.filterwarnings("ignore")

# # Sensor Data Model (12 features)
# class SensorData(BaseModel):
#     Plant_ID: int = 1
#     Soil_Moisture: float
#     Ambient_Temperature: float
#     Soil_Temperature: float
#     Humidity: float
#     Light_Intensity: float
#     Soil_pH: float
#     Nitrogen_Level: float
#     Phosphorus_Level: float
#     Potassium_Level: float
#     Chlorophyll_Content: float
#     Electrochemical_Signal: float

# app = FastAPI(title="Strawberry Disease Prediction API", version="1.0.0")

# # Load models (use relative paths)
# print("Loading models...")
# yolo_model = YOLO("best.pt")
# dt_model = joblib.load("Decision_Tree.pkl")
# scaler = joblib.load("scaler.pkl")
# print("Models loaded successfully!")

# label_map = {0: "Healthy", 1: "Moderate Stress", 2: "High Stress"}

# @app.post("/predict/health")
# async def predict_health(data: SensorData):
#     try:
#         input_data = np.array([[
#             data.Plant_ID, data.Soil_Moisture, data.Ambient_Temperature, 
#             data.Soil_Temperature, data.Humidity, data.Light_Intensity,
#             data.Soil_pH, data.Nitrogen_Level, data.Phosphorus_Level,
#             data.Potassium_Level, data.Chlorophyll_Content, data.Electrochemical_Signal
#         ]])
        
#         input_scaled = scaler.transform(input_data)
#         pred = dt_model.predict(input_scaled)[0]
#         confidence = dt_model.predict_proba(input_scaled)[0].max() * 100
        
#         health_status = label_map.get(int(pred), "Unknown")
        
#         return {
#             "plant_health_status": health_status,
#             "confidence": f"{confidence:.2f}%",
#             "prediction_code": int(pred)
#         }
#     except Exception as e:
#         return {"error": f"Prediction failed: {str(e)}"}

# @app.post("/detect/image")
# async def detect_image(file: UploadFile = File(...)):
#     try:
#         contents = await file.read()
#         image = Image.open(io.BytesIO(contents))
#         results = yolo_model(image)
        
#         detections = []
#         for r in results:
#             boxes = r.boxes
#             if boxes is not None:
#                 for box in boxes:
#                     detections.append({
#                         "class": r.names[int(box.cls)],
#                         "confidence": float(box.conf),
#                         "bbox": box.xyxy.tolist()[0]
#                     })
        
#         return {"detections": detections, "total_detections": len(detections)}
#     except Exception as e:
#         return {"error": f"Image detection failed: {str(e)}"}

# @app.get("/")
# async def root():
#     return {
#         "message": "Plant Disease Prediction API",
#         "endpoints": [
#             "POST /predict/health - Sensor data prediction",
#             "POST /detect/image - Image detection"
#         ]
#     }

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))  # Render uses $PORT

#     uvicorn.run(app, host="0.0.0.0", port=port)  # Bind to all interfaces


# main.py - FastAPI Backend (Sensor + Image only) - Render-Optimized
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from ultralytics import YOLO
import numpy as np
from PIL import Image
import io
import warnings
import os
import uvicorn
import asyncio
from contextlib import asynccontextmanager

warnings.filterwarnings("ignore")

# Global models (lazy-loaded)
yolo_model = None
dt_model = None
scaler = None
label_map = {0: "Healthy", 1: "Moderate Stress", 2: "High Stress"}

# Lazy load on first use
async def load_models():
    global yolo_model, dt_model, scaler
    if dt_model is None or scaler is None:
        print("Loading DT + Scaler...")
        dt_model = joblib.load("Decision_Tree.pkl")
        scaler = joblib.load("scaler.pkl")
        print("DT + Scaler loaded!")
    if yolo_model is None:
        print("Loading YOLO...")
        yolo_model = YOLO("best.pt")  # Use "yolov8n.pt" for lighter model if available
        print("YOLO loaded!")

# Sensor Data Model
class SensorData(BaseModel):
    Plant_ID: int = 1
    Soil_Moisture: float
    Ambient_Temperature: float
    Soil_Temperature: float
    Humidity: float
    Light_Intensity: float
    Soil_pH: float
    Nitrogen_Level: float
    Phosphorus_Level: float
    Potassium_Level: float
    Chlorophyll_Content: float
    Electrochemical_Signal: float

# Lifespan for startup (optional warm-up)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Optional - warm up models (but lazy is better for cold starts)
    await load_models()
    yield
    # Shutdown: Cleanup if needed

app = FastAPI(title="Strawberry Disease Prediction API", version="1.0.0", lifespan=lifespan)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or add your dashboard URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/health")
async def predict_health(data: SensorData):
    try:
        await load_models()  # Lazy load
        input_data = np.array([[
            data.Plant_ID, data.Soil_Moisture, data.Ambient_Temperature, 
            data.Soil_Temperature, data.Humidity, data.Light_Intensity,
            data.Soil_pH, data.Nitrogen_Level, data.Phosphorus_Level,
            data.Potassium_Level, data.Chlorophyll_Content, data.Electrochemical_Signal
        ]])
        
        input_scaled = scaler.transform(input_data)
        pred = dt_model.predict(input_scaled)[0]
        confidence = dt_model.predict_proba(input_scaled)[0].max() * 100
        
        health_status = label_map.get(int(pred), "Unknown")
        
        return {
            "plant_health_status": health_status,
            "confidence": f"{confidence:.2f}%",
            "prediction_code": int(pred)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/detect/image")
async def detect_image(file: UploadFile = File(...)):
    try:
        await load_models()  # Lazy load
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        results = yolo_model(image, verbose=False)  # verbose=False for less output
        
        detections = []
        for r in results:
            boxes = r.boxes
            if boxes is not None:
                for box in boxes:
                    detections.append({
                        "class": r.names[int(box.cls)],
                        "confidence": float(box.conf),
                        "bbox": box.xyxy.tolist()[0]
                    })
        
        return {"detections": detections, "total_detections": len(detections)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image detection failed: {str(e)}")

@app.get("/")
async def root():
    return {
        "message": "Plant Disease Prediction API",
        "endpoints": [
            "POST /predict/health - Sensor data prediction",
            "POST /detect/image - Image detection"
        ]
    }

if __name__ == "__main__":
    port = 4000
    uvicorn.run(app, host="0.0.0.0", port=port)
