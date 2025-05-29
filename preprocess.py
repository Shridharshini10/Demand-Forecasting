import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.dropna(inplace=True)
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month
    df['Is_Holiday'] = df['Holiday'].apply(lambda x: 1 if x == "Yes" else 0)
    df['Is_Promotion'] = df['Promotion'].apply(lambda x: 1 if x == "Yes" else 0)
    return df
