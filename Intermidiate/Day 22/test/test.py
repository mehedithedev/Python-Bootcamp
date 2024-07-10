import pandas as pd

try:
    df = pd.read_csv("/workspaces/Python-Bootcamp/Intermidiate/Day 22/data.csv")
    print(df)
except Exception as e:
    print(f"An error occurred: {e}")