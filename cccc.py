import pandas as pd

dp = pd.read_csv("data.csv")

data = {
    "Nama":["Spongebob","Patrick","Squidward"],
    "Age": [30,20,50]
}
df = pd.DataFrame(data,index = [f"Employee {x}" for x in range(1,len(data["Nama"]) +1 )])

# Add New Column
df["Job"] = ["Cook","N/A","Cashier"]

# Add new row
new_row = pd.DataFrame([{"Nama": "Sandy","Job": "Engineer","Age": "32"},
                        {"Nama": "Eugene","Job": "Engineer","Age":"50"}],
                       index=["Employee 4","Employee 5"])
df = pd.concat([df,new_row])


# selection by coloumn
print(dp["Name"].to_string)
print(dp[["Name","Height","Weight"]].to_string)

# selection by row 
print(dp.loc[1]) 
print(dp.iloc[1:20])
'''
print(dp.loc["Pikachu"]) select if index is changed by its name (index_col="Name")
print(dp.loc["Pikachu",["Height","Weight"]]) select if index is changed by its name and custom displayed
print(dp.loc["Pikachu": "Blastoise",["Height",Weight]]) select if index is changed by its name and custom displayed more than one
'''
# Filtering
tall_pokemon = dp[dp["Height"] >= 2 ]
water = dp[(dp["Type1"] == "Water") | (dp["Type2"] == "Water") ]

# Aggregate
# Whole data
print(dp.mean(numeric_only= True)) # mean -> (sum - mean - min - max)
print(dp.count())

# Single Column
print(dp["Height"].mean(numeric_only= True)) # mean -> (sum - mean - min - max)
print(dp["Weight"].count())

# Rename Coloumn name
dp.rename(columns={"Type2":"TypeDua"},inplace=True)
group = dp.groupby("Type1")
print(group["Height"].mean()) # mean -> (sum - mean - min - max - count)

# Drop irrelevant columns

dp = dp.drop(columns=["Legendary","No"])

# Handle missing data
ddp = dp.dropna(subset=["Type2"]) # return new value
dp.dropna(inplace=  True)# didnt change the original
dp = dp.fillna({"Type2": "Hilang"}) # replace missing value
dp.fillna(130, inplace = True)#Replace NULL values with the number 130
dp.fillna({"Type2": 130}, inplace=True)#Replace NULL values in the "Type2" columns with the number 130

# fix inconsistent values
dp["Type1"] = dp["Type1"].replace({"Grass":"GRASS","Fire":"FIRE"})

# Standardize text
dp["Name"] = dp["Name"].str.lower()

# fix data types
dp["Legendary"] = dp["Legendary"].astype(bool)

# Remove duplicate values
dp = dp.drop_duplicates()
