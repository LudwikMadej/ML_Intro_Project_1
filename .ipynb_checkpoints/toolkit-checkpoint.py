import pandas as pd
import numpy as np

def pipeline(df):
    df.drop("Name", axis=1, inplace=True)
    
    df["Marital Status"] = np.where(
        df["Marital Status"] == "Widowed", 0,
        np.where(
            df["Marital Status"] == "Divorced", 1, 
                np.where(
                    df["Marital Status"] == "Single", 2, 3
                        )
                )
    ).astype(np.int8)

    df["Education Level"] = np.where(
        df["Education Level"] == "High School", 0,
        np.where(df["Education Level"] == "Accociate Degree", 1, 
                 np.where(df["Education Level"] == "Bachelor's Degree", 2,
                          np.where(df["Education Level"] == "Master's Degree", 3,
                                   4
                                  )
                         )
                )
    ).astype(np.int8)

    df["Smoking Status"] = np.where(
        df["Smoking Status"] == "Non-smoker", 0,
            np.where(df["Smoking Status"] == "Former", 1,
                    2
            )
    ).astype(np.int8)

    df["Physical Activity Level"] = np.where(
        df["Physical Activity Level"] == "Sedentary", 0, 
        np.where(df["Physical Activity Level"] == "Moderate", 1,
                2
            )
        ).astype(np.int8)

    df["Employed"] = (df["Employment Status"] == "Employed").astype(np.int8)
    df.drop("Employment Status", axis=1, inplace=True)

    df["Alcohol Consumption"] = np.where(
        df["Alcohol Consumption"] == "Low", 0,
        np.where(df["Alcohol Consumption"] == "Moderate", 1,
                 2
                )
        ).astype(np.int8)

    df["Dietary Habits"] = np.where(
        df["Dietary Habits"] == "Unhealthy", 0,
        np.where(df["Dietary Habits"] == "Moderate", 1,
                 2
                )
        ).astype(np.int8)

    df["Sleep Patterns"] = np.where(
        df["Sleep Patterns"] == "Poor", 0,
        np.where(df["Sleep Patterns"] == "Fair", 1,
                2
                )
        ).astype(np.int8)

    for colname in ["History of Mental Illness", "History of Substance Abuse", "Family History of Depression", "Chronic Medical Conditions"]:
        df[colname] = (df[colname] == "Yes")

    return df