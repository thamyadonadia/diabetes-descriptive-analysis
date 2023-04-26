import pandas as pd

import src.analysis as analysis

person = pd.read_csv("d.csv").to_dict()
df = pd.DataFrame(person)

age_stats = analysis.age_stats(df)
glucose_index_stats = analysis.glucose_index_stats(df)
blood_pressure_limits = analysis.blood_pressure_limits(df)
insulin_limits = analysis.insulin_limits(df)
age_limits = analysis.age_limits(df)
bmi_limits = analysis.bmi_limits(df)
age_variance = analysis.age_variance(df)
bmi_variance = analysis.bmi_variance(df)
insulin_std = analysis.insulin_std(df)
glucose_index_std = analysis.glucose_index_std(df)


# print(age_stats) 
#print(glucose_index_stats) 
#print(blood_pressure_limits) 
#print(insulin_limits) 
# print(age_limits)
print(bmi_limits)
# print(age_variance)
# print(bmi_variance)
# print(insulin_std)
# print(glucose_index_std)