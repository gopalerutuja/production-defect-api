Predictive Analysis for Manufacturing Operations
# Production Defect Prediction API

This is a RESTful API for predicting production defects using a supervised machine learning model. It includes endpoints to upload a dataset, train the model, and make predictions based on provided input features.

---

## **Setup Instructions**

### **1. Prerequisites**
Ensure you have the following installed on your system:
- Python (version 3.8 or above)
- Flask
- Required Python libraries (see `requirements.txt`)
- Postman (optional, for testing the API)

### **2. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-folder>
```

### **3. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
Start the Flask application:
```bash
python app.py
```
The application will start running on `http://127.0.0.1:5000`.

---

## **API Endpoints**

### **1. Upload Dataset**
**Endpoint:** `POST /upload`

Uploads a CSV file containing the dataset for training and prediction.

**Request:**
- **Headers:**
  ```
  Content-Type: multipart/form-data
  ```
- **Body:**
  - Form-data with key `file` containing the CSV file.

**Example Request (Postman):**
1. Go to the Body tab and select "form-data."
2. Add a key named `file` and set its type to "File."
3. Upload your dataset file.

**Response:**
```json
{
    "columns": [
        "ProductionVolume",
        "ProductionCost",
        "SupplierQuality",
        "DeliveryDelay",
        "DefectRate",
        "QualityScore",
        "MaintenanceHours",
        "DowntimePercentage",
        "InventoryTurnover",
        "StockoutRate",
        "WorkerProductivity",
        "SafetyIncidents",
        "EnergyConsumption",
        "EnergyEfficiency",
        "AdditiveProcessTime",
        "AdditiveMaterialCost",
        "DefectStatus"
    ],
    "message": "File uploaded successfully"
}
```

---

### **2. Train Model**
**Endpoint:** `POST /train`

Trains the machine learning model on the uploaded dataset.

**Request:**
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body:**
  ```json
  {
  "features": ["ProductionVolume",
        "ProductionCost",
        "SupplierQuality",
        "DeliveryDelay",
        "DefectRate",
        "QualityScore",
        "MaintenanceHours",
        "DowntimePercentage",
        "InventoryTurnover",
        "StockoutRate",
        "WorkerProductivity",
        "SafetyIncidents",
        "EnergyConsumption",
        "EnergyEfficiency",
        "AdditiveProcessTime",
        "AdditiveMaterialCost"],
  "target": "DefectStatus",
  "model": "logistic_regression"
}

  ```

**Response:**
```json
{
    "accuracy": 0.5,
    "f1_score": 0.494949494949495,
    "message": "Model trained successfully"
}
```

---

### **3. Make Predictions**
**Endpoint:** `POST /predict`

Predicts outcomes based on input data using the trained model.

**Request:**
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body:**
  ```json
  {
  "data": [
    {
      "ProductionVolume": 202,
      "ProductionCost": 13175.40378,
      "SupplierQuality": 86.64853384,
      "DeliveryDelay": 1,
      "DefectRate": 3.121492267,
      "QualityScore": 63.46349433,
      "MaintenanceHours": 9,
      "DowntimePercentage": 0.052342867,
      "InventoryTurnover": 8.63051535,
      "StockoutRate": 0.081321681,
      "WorkerProductivity": 85.04237928,
      "SafetyIncidents": 0,
      "EnergyConsumption": 2419.616785,
      "EnergyEfficiency": 0.468946624,
      "AdditiveProcessTime": 5.55163899,
      "AdditiveMaterialCost": 236.439301
    }
  ]
}

  ```

**Response:**
```json
{
    "predictions (1 = defective/0 = not defective)": [
        1
    ]
}
```

---

## **Example Workflow**

1. **Upload a Dataset:**
   - Use the `/upload` endpoint to upload a CSV file containing the dataset.

2. **Train the Model:**
   - Send a `POST` request to `/train` with the feature names and target column.
   - Example response includes model performance metrics like accuracy and F1 score.

3. **Make Predictions:**
   - Use the `/predict` endpoint with a JSON object containing the input features.
   - The response contains predictions based on the trained model.

---

## **Testing the API**

### Using Postman:
- Install Postman and create a new collection for the API.
- Add the endpoints (`/upload`, `/train`, `/predict`) to the collection.
- Test the API by sending requests to each endpoint with appropriate payloads.




  





