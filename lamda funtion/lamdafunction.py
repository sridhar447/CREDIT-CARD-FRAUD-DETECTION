import json
import joblib # type: ignore
import uuid
from datetime import datetime

model = joblib.load("fraud_model.pkl")

def lambda_handler(event, context):

    transaction = event["features"]

    prediction = model.predict([transaction])[0]

    result = "Fraud" if prediction == 1 else "Legitimate"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "prediction": result
        })
    }