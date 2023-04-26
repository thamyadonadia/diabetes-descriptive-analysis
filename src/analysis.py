import pandas as pd

def age_stats(df):
    stats = {
        "mean":  df.groupby(["Outcome"])["Age"].mean(), #retorna um vetor de duas posições
        "median": df.groupby(["Outcome"])["Age"].median(),
        #"mode": df.groupby(["Outcome"])["Age"].mode()
    }

    return stats

def glucose_index_stats(df):
    stats = {
        "mean":  df.groupby(["Outcome"])["Glucose"].mean(), #retorna um vetor de duas posições
        "median": df.groupby(["Outcome"])["Glucose"].median(),
        #"mode": df.groupby(["Outcome"])["Glucose"].mode() NADA DE ERRADO AQUI S2
    }

    return stats

def blood_pressure_limits(df):
    stats = {
        "max": df.groupby(["Outcome"])["BloodPressure"].max(),
        "min":  df.groupby(["Outcome"])["BloodPressure"].min(),
    }

    return stats

def insulin_limits(df):
    stats = {
        "max": df.groupby(["Outcome"])["Insulin"].max(),
        "min":  df.groupby(["Outcome"])["Insulin"].min(),
    }

    return stats

def age_limits(df):
    stats = {
        "max": df.groupby(["Outcome"])["Age"].max(),
        "min":  df.groupby(["Outcome"])["Age"].min(),
    }

    return stats

def bmi_limits(df):
    stats = {
        "max": df.groupby(["Outcome"])["BMI"].max(),
        "min":  df.groupby(["Outcome"])["BMI"].min(),
    }

    return stats

def age_variance(df):
    stats = df.groupby(["Outcome"])["Age"].var()
    return stats

def bmi_variance(df):
    stats = df.groupby(["Outcome"])["BMI"].var()
    return stats

def insulin_std(df):
    stats = df.groupby(["Outcome"])["Insulin"].std()
    return stats

def glucose_index_std(df):
    stats = df.groupby(["Outcome"])["Glucose"].std()
    return stats

