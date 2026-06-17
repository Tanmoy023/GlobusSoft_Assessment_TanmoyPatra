import os
from inference_sdk import InferenceHTTPClient
import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw() 

    img_path = filedialog.askopenfilename(
        title="<-- Select  image to detect drones -->",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")
        ]
    )
    
    return img_path

def detect_drone():
    CLIENT = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key="77p1eJUJrBPA0nZTIT1I"
    )
    
    img_path = select_image()
    
    if not os.path.exists(img_path):
        return {"error": "Image Not Found!"}

    result = CLIENT.infer(img_path, model_id="drone_mil-u8fqk/1")

    API_result = {}

    total_predictions = result['predictions']
    API_result["total_predictions"] = len(total_predictions)

    API_result["data"] = []

    for detection in result['predictions']:
        dict = {}
        
        name = detection["class"]
        dict["name"] = name
        
        confidence = detection["confidence"]
        Confidence_score = f"{confidence:.2f}"
        dict["Confidence_Score"] = Confidence_score
        
        x = detection["x"]
        y = detection["y"]
        w = detection["width"]
        h = detection["height"]
        
        x1 = x - (w / 2)
        y1 = y - (h / 2)
        x2 = x + (w / 2)
        y2 = y + (h / 2)
        
        bounding_box = (x1, y1, x2, y2)
        dict["Bounding_Box"] = bounding_box
        
        API_result["data"].append(dict)

    return API_result

# r = detect_drone()
# print(r)