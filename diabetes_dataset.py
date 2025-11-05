import pandas as pd
import random

names = [
    "Asha Menon", "Rohit Kumar", "Priya Nair", "Suresh Patel", "Neha Sharma",
    "Amit Joshi", "Kavita Rao", "Manish Verma", "Sana Khan", "Vikram Singh",
    "Meera Iyer", "Arjun Rao", "Lata Devi", "Ramesh Babu", "Tina Paul"
]

zip_codes = ["560034", "560045", "560072", "560010"]
medications = ["Metformin", "Insulin", "Diet Control"]
diagnoses = ["Type 1", "Type 2", "Pre-Diabetic"]

data = []

for i in range(15):
    age = random.randint(22, 70)
    gender = random.choice(["M", "F"])
    zip_code = random.choice(zip_codes)
    blood_sugar = round(random.uniform(120, 220), 1)
    bmi = round(random.uniform(22.0, 33.5), 1)
    medication = random.choice(medications)
    diagnosis = (
        "Type 2" if blood_sugar >= 160 else
        "Pre-Diabetic" if blood_sugar < 150 else
        random.choice(["Type 1", "Type 2"])
    )
    
    data.append([
        f"P{i+1:03}", names[i], age, gender, zip_code,
        blood_sugar, bmi, medication, diagnosis
    ])

df = pd.DataFrame(data, columns=[
    "PatientID", "Name", "Age", "Gender", "ZIP",
    "BloodSugarLevel", "BMI", "Medication", "Diagnosis"
])

print(df)
df.to_csv("diabetes_dataset.csv", index=False)
print("\nDataset saved as diabetes_dataset.csv")
