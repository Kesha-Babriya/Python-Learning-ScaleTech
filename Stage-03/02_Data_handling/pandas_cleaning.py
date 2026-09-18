import pandas as pd

data = {
    "Name": ["Kesha", "Payal", "Tejasvi", "Neha", "Kesha", "Preksha"],
    "Age": [25, None, 22, 30, 25, None],
    "Department": ["IT", "HR", "IT", "sales", "IT", "HR"],
    "Salary": [50000, 45000, None, 60000, 50000, 48000]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())          #none become true in output
print(df.isnull().sum())

df['Age'] = df["Age"].fillna(df["Age"].mean())
df['Salary'] = df["Salary"].fillna(df["Salary"].mean())

print(df)

print(df.duplicated())
print("Sum: ",df.duplicated().sum())

df = df.drop_duplicates()

print(df)
print(df.dtypes)

df["Age"] = df["Age"].astype(int)
print(df.dtypes)

#add new column
df['bonus'] = df["Salary"] * 0.2

print(df)

df = df.drop('bonus' ,axis=1)       #axix =1 mean column
print(df)

print(df.groupby("Department")['Salary'].mean())

print(df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"]))