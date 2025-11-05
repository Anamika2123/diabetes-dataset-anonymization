import pandas as pd

df = pd.read_csv("k_anonymized_dataset.csv")

qis = ["Age", "Gender", "ZIP"]
sensitive_attr = "Diagnosis"

groups = df.groupby(qis)

for name, group in groups:
    if group[sensitive_attr].nunique() < 2:
        idx = group.index
        df.loc[idx, sensitive_attr] = "*"

df.to_csv("l_diverse_dataset.csv", index=False)

print(df)
print("\n l-Diverse dataset (l=2) saved as l_diverse_dataset.csv")
