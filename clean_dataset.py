import pandas as pd

# Load dataset + remove rows without a description
df = pd.read_csv(r"v0.csv")
df = df[df['Description'].notna()]
df = df[df['Description'] != "Herk:   ?"]
df = df[df['Description'] != "Herk:      ?"]
df = df[df['Description'] != "Herk:     ?"]
df = df[df['Description'] != "Herk:    ?"]
df = df[df['Description'] != "Herk:       ?"]
df = df[df['Description'] != "Herk:  ?"]

# Save cleaned dataset
df.to_csv("sabio_dataset.csv", index=False)
