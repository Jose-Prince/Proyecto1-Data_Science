import pandas as pd
import os

directory = "Instituciones/"

dfs = []

for file in os.listdir(directory):
    if file.endswith(".xls"):
        route = os.path.join(directory, file)
        print("Processing files...")
        
        try:
            tables = pd.read_html(route)
            if tables:
                df = tables[len(tables)-1]
                dfs.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")
        
df_final = pd.concat(dfs, ignore_index=True)

df_final.to_excel("institutions_data.xlsx", index=False)
print("All data merged!")