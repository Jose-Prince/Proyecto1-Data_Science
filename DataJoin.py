import pandas as pd
import os

directory = "Instituciones/"

dfs = []
first = True

for file in os.listdir(directory):
    if file.endswith(".xls"):
        route = os.path.join(directory, file)
        print(f"Processing file: {file}...")
        
        try:
            tables = pd.read_html(route)
            if tables:
                df = tables[-1]

                if first:
                    df = df.iloc[:-1].reset_index(drop=True)
                    dfs.append(df)
                    first = False
                else:
                    df = df.iloc[1:-1].reset_index(drop=True)
                    dfs.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")
        
df_final = pd.concat(dfs, ignore_index=True)

df_final.to_csv("institutions_data.csv", index=False)
print("All data merged!")
