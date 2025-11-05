import pandas as pd

df = pd.read_csv("tokenized_dataset.csv")

df_k = df.copy()

def generalize_age(age):
    if age < 30:
        return "20-29"
    elif age < 40:
        return "30-39"
    elif age < 50:
        return "40-49"
    elif age < 60:
        return "50-59"
    else:
        return "60-70"

def generalize_zip(zip_code):
    return str(zip_code)[:3] + "**"

df_k["Age"] = df_k["Age"].apply(generalize_age)
df_k["ZIP"] = df_k["ZIP"].apply(generalize_zip)

df_k.to_csv("k_anonymized_dataset.csv", index=False)

print(df_k)
print("\n k-Anonymized dataset saved as k_anonymized_dataset.csv")
