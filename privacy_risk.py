import pandas as pd

original = pd.read_csv("tokenized_dataset.csv")
k_anon = pd.read_csv("k_anonymized_dataset.csv")
l_div = pd.read_csv("l_diverse_dataset.csv")

qis = ["Age", "Gender", "ZIP"]

def compute_reid_risk(df):
    group_sizes = df.groupby(qis).size()
    risks = 1 / group_sizes
    avg_risk = risks.mean()
    min_risk = risks.min()
    max_risk = risks.max()
    return avg_risk, min_risk, max_risk

print("\n Re-identification Risk:")
for label, dataset in [("Tokenized", original), ("k-Anonymized", k_anon), ("l-Diverse", l_div)]:
    avg_r, min_r, max_r = compute_reid_risk(dataset)
    print(f"{label} → Avg Risk: {avg_r:.3f}, Min: {min_r:.3f}, Max: {max_r:.3f}")

def info_loss(original, anonymized):
    loss = 0
    for col in qis:
        unique_orig = original[col].nunique()
        unique_anon = anonymized[col].nunique()
        col_loss = (1 - (unique_anon / unique_orig)) * 100
        print(f"Info Loss for {col}: {col_loss:.2f}%")
        loss += col_loss
    return loss / len(qis)

print("\n Information Loss:")
avg_loss = info_loss(original, k_anon)
print(f"Average Info Loss: {avg_loss:.2f}%")
