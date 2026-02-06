from .preprocess import preprocess_input

def predict_churn(model, encoders, scalers, input_data):
    X = preprocess_input(input_data, encoders, scalers)
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]
    return pred, proba
