import pandas as pd

df = pd.read_csv("data.csv",index_col="Name")

#print(df[["Name","Type1","Legendary"]].to_string())

#print(df.loc["Bulbasaur":"Pikachu",["Legendary","Weight"]])





def pokeName():
     while True:
        inp = input("Enter pokemon name (or Q to quit): ").strip().capitalize()
        if inp == "Q":
            print("Bye")
            break
        try:
            print(df.loc[inp])
        except KeyError:
            print(f"{inp} not found")
            inp = input("Enter pokemon name: ").capitalize()

def pokeData():
    Runnin = True
    while Runnin:
        jumlah = input("Whole Pokemon or Single Pokemon (W/S): ").upper()
        if jumlah not in ('W','S'):
            print("Please enter only (W/S)")
            continue
        
        print(f"You are Choosing {'Whole' if jumlah == 'W' else 'Single'}")

        tipe = input("U want to know abt (sum - mean - min - max - count): ").upper()

        if tipe not in("MAX","MEAN","MIN","SUM","COUNT"):
            print("Please insert only (sum - mean - min - max - count)")
            continue
        
        if jumlah == 'W' and tipe == "MAX":
            print(df.max(numeric_only=True))
        elif jumlah == 'W' and tipe == "MEAN":
            print(df.mean(numeric_only=True))
        elif jumlah == 'W' and tipe == "SUM":
            print(df.sum(numeric_only=True))
        elif jumlah == 'W' and tipe == "MIN":
            print(df.min(numeric_only=True))
        elif jumlah == 'W' and tipe == "COUNT":
            print(df.count())

        if jumlah == 'S':
            col = input("Which coloumn would you like to know (Type1/2 - Height - Weight - legendary): ").upper()
            
            if col not in("TYPE1","TYPE2","HEIGHT","WEIGHT","LEGENDARY"):
                continue
            elif tipe == "MEAN":
                print(df[col.capitalize()].mean(numeric_only= True))
            elif tipe == "COUNT":
                print(df[col.capitalize()].count())
            elif tipe == "MAX":
                print(df[col.capitalize()].max(numeric_only= True))
            elif tipe == "MIN":
                print(df[col.capitalize()].min(numeric_only= True))
            elif tipe == "SUM":
                print(df[col.capitalize()].sum(numeric_only= True))

#print(f"{df.loc["Bulbasaur",["Height"]]}")
print(df.loc["Bulbasaur", "Height"])