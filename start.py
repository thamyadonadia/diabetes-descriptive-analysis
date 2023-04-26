import pandas as pd

import src.analysis as analysis

person = pd.read_csv("d.csv").to_dict()
df = pd.DataFrame(person)

age_stats = analysis.age_stats(df)
glucose_stats = analysis.glucose_index_stats(df)



#print(df)