
import pandas as pd

HOLDOUT_YEAR = 2024

def split_training_validation(df):
    """
    Reserve 2024 exclusively for final validation.
    """

    dates = pd.to_datetime(df["acq_date"])
    years = dates.dt.year

    training = df.loc[years != HOLDOUT_YEAR].copy()
    validation = df.loc[years == HOLDOUT_YEAR].copy()

    return training, validation
