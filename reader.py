import pandas as pd

def reader(file):
    df = pd.read_csv(file)
    df.columns = [column.replace(" ","_") for column in df.columns]
    return df
