import joblib

data = joblib.load("Telco_customer_churn_train_model.pkl")
print(type(data))
print(data.keys())
