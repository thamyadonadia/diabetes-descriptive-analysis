import pandas as pd

def age_stats(df):
    stats = {
        "mean":  df.groupby(["Outcome"])["Age"].mean(), #retorna um vetor de duas posições
        "median": df.groupby(["Outcome"])["Age"].median(),
        "mode": df.groupby(["Outcome"])["Age"].mode()
    }

    return stats

def glucose_index_stats(df):
    stats = {
        "mean":  df.groupby(["Outcome"])["Glucose"].mean(), #retorna um vetor de duas posições
        "median": df.groupby(["Outcome"])["Glucose"].median(),
        "mode": df.groupby(["Outcome"])["Glucose"].mode()
    }

    return stats
