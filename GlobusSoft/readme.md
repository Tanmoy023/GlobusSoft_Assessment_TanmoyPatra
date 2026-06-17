# 🚀 GlobusSoft Assignment Submission

Hi, I'm **Tanmoy Patra**.

This repository contains my solutions for the assignment provided by **GlobusSoft**. The assignment consists of two independent tasks:

* 🛒 **Task 1:** Amazon Laptop Data Scraping
* 🚁 **Task 2:** Drone Count Detection using FastAPI

Each task is organized inside its own folder and includes both the final solution and a development notebook (`test.ipynb`) that demonstrates my approach, experimentation, debugging process, and implementation logic.

---

## 📂 Project Structure

```text
.
├── Task_1/
│   ├── Web_Scraping.py
│   ├── test.ipynb
│   └── amazon-laptop-dataset.csv
│
├── Task_2/
│   ├── main.py
│   ├── Drone_Count_Detection.py
│   ├── test.ipynb
│   └── Image/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Common Setup

Before running any task, install the required dependencies.

## 1️⃣ Create a Virtual Environment

```bash
python -m venv myenv
```

Activate the environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux / Mac

```bash
source myenv/bin/activate
```

---

## 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🛒 Task 1 – Amazon Laptop Data Scraping

## 📌 Problem Statement

Develop a Python script to scrape laptop-related product information from Amazon India and store the extracted data in a CSV file.

The script collects:

* Product Image
* Product Title
* Product Rating
* Product Price
* Ad / Organic Result Information

---

## 🧠 Libraries Used

* requests
* BeautifulSoup (bs4)
* pandas
* os
* datetime

---

## ▶️ How to Run

Navigate to the Task 1 directory:

```bash
cd Task_1
```

Run the script:

```bash
python Web_Scraping.py
```

---

## 📊 Output

After execution:

* Laptop information is scraped from Amazon India.
* Data is stored inside the CSV dataset.
* New records are appended to the existing dataset.
* Output files contain timestamp information as required.

Output file:

```text
amazon-laptop-dataset.csv
```

---

## 📖 Development Notes

Inside the `Task_1` folder, I have included:

```text
test.ipynb
```

This notebook contains:

* Initial experimentation
* Data extraction testing
* Logic development
* Debugging steps
* Final implementation workflow

It can be referred to for a better understanding of the solution.

---

# 🚁 Task 2 – Drone Count Detection API

## 📌 Problem Statement

For Task 2, I selected:

### Option B – Drone Count Detection

The objective was to build a FastAPI service that:

* Accepts a drone/sky image
* Detects drones using a lightweight detection model
* Returns:

  * Bounding Boxes
  * Confidence Scores
  * Total Drone Count

Single-image inference only.

---

## 🧠 Libraries Used

* FastAPI
* inference_sdk
* tkinter
* os

---

## ✨ Features

* FastAPI-based REST API
* Interactive image selection
* Drone detection on uploaded image
* Confidence score reporting
* Bounding box extraction
* Total drone counting

---

## ▶️ How to Run

Navigate to the Task 2 directory:

```bash
cd Task_2
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## 🔗 API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Drone Detection API running"
}
```

---

### Detection Endpoint

```http
GET /detect
```

When this endpoint is called:

1. A file selection popup window will appear.
2. Select an image containing drones.
3. The model will run inference.
4. Results will be returned as JSON.

---

## ⚠️ Important Note

Sometimes the image selection popup may appear behind other windows.

If you do not immediately see the popup:

* Press `Alt + Tab`
* Locate the image selection window
* Bring it to the foreground

The popup title will be:

```text
Select image to detect drones
```

---

## 📊 Sample Response

```json
{
    "total_count": 2,
    "data": [
        {
            "name": "drone",
            "confidence": 0.95,
            "bbox": [100, 200, 150, 250]
        },
        {
            "name": "drone",
            "confidence": 0.88,
            "bbox": [300, 400, 350, 450]
        }
    ]
}
```

---

## ⏱️ Inference Time

Depending on:

* Image size
* System performance
* Model execution time

Prediction may take approximately:

```text
10 – 20 seconds
```

before the final response is returned.

---

## 📖 Development Notes

Inside the `Task_2` folder, I have included:

```text
test.ipynb
```

This notebook contains:

* Model testing
* API experimentation
* Debugging workflow
* Detection logic development
* Final implementation process

Reviewing the notebook can help understand the reasoning behind the implementation.

---

# 📦 Submission Contents

This repository contains:

* ✅ Task 1 Solution
* ✅ Task 2 Solution
* ✅ FastAPI Application
* ✅ Jupyter Notebooks (`test.ipynb`)
* ✅ requirements.txt
* ✅ README.md
* ✅ Sample Images

---

# 👨‍💻 Author

**Tanmoy Patra**

📧 Email: [tanmoypatra369@gmail.com](mailto:tanmoypatra369@gmail.com)

🌐 Portfolio: https://tanmoy023.github.io/Portfolio-website/

🔗 LinkedIn: https://www.linkedin.com/in/tanmoy-patra-00b756236

🐙 GitHub: https://github.com/Tanmoy023

Thank you for taking the time to review my submission. I appreciate the opportunity to work on this assignment and showcase my problem-solving approach and development skills.
