from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(df):
    features = ['Price', 'Is_Promotion', 'Is_Holiday', 'DayOfWeek', 'Month']
    X = df[features]
    y = df['Units_Sold']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    joblib.dump(model, 'models/demand_forecast_model.pkl')
    return model, X_test, y_test
