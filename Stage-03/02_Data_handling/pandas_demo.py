import pandas as pd

#Series => 1D
s = pd.Series([1,3,4,52,6,7] , index = ['a','b','c','d','e','f'])
print("--------Series--------")
print(s)

# read csv like many function for different files

data = pd.read_csv("student2.csv")
print("--------Read csv file--------")
print(data)
print("Describe about data")
print(data.describe())

data2 = pd.read_json("Stage-02/03_Advance_File_operation/01_json_parsing/file_dump_load/emp.json")
print("--------Read json file--------")
print(data2)
print("Gives info of data")
print(data2.info())

# .head() give first 5 rows
# .tail() give last 5 rows


#------------new example------------------

data = {
    "name": ["Keshaa", "Piyu", "jer", "conni"],
    "age": [21, 22, 25, 26],
    "department": ["IT", "HR", "IT", "Finance"],
    "salary": [50000, 60000, 55000, 45000]
}

#dataframe 2D
df = pd.DataFrame(data)
print(df)
print(df['name'])
print(df[['name','salary']])
print("--------")
print(df.loc[2])
print("--------")
print(df.loc[0:2])          #print raw 0,1,2
print("--------")
print(df.iloc[0])
print("--------")
print(df.iloc[0:2])          #print raw 0,1
print("--------")
print(df.head(2))
print(df.tail())
print(df.info)
print("--------")
print(df.info())
print(df['salary'].mean())
print(df['salary'].max())
print(df['salary'].min())
print(df['salary'].sum())
print(df['name'].count())
print(df.shape)             #(raw,column)
print(df.columns)
print(df.dtypes)

print("----Filtering data----")
result = df[df["salary"] > 50000]
print(result)
print("Filter with condition")
print(df[
    (df["department"] == "IT") &
    (df["salary"] > 45000)
])

df["bonus"] = df["salary"] * 0.10

print(df.sort_values("salary"))
df.sort_values("salary", ascending=False)

print(df)