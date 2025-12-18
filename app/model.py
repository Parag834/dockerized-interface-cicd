def predict(data):
    return {
        "input": data,
        "prediction": "POSITIVE" if len(data) % 2 == 0 else "NEGATIVE"
    }
