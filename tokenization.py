import pandas as pd
import hashlib

df = pd.read_csv("diabetes_dataset.csv")

def create_token(value):
    return hashlib.sha256(value.encode()).hexdigest()[:10]

df["PatientID_Token"] = df["PatientID"].apply(create_token)
df["Name_Token"] = df["Name"].apply(create_token)

df_tokenized = df.drop(columns=["Name", "PatientID"])

df_tokenized.to_csv("tokenized_dataset.csv", index=False)

print(df_tokenized)
print("\n Tokenized dataset saved as tokenized_dataset.csv")
