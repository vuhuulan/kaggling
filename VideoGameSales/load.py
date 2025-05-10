import os
import shutil
import kagglehub
import pandas as pd
from pandas.core.frame import DataFrame as DF

TARGET = "anandshaw2001/video-game-sales"
SAVE_PATH = "./data/"
FNAME = "vgsales.csv"


def load_df() -> DF:
    if os.listdir(SAVE_PATH):
        return pd.read_csv(os.path.join(SAVE_PATH, FNAME))
    fp = kagglehub.dataset_download(TARGET)
    shutil.copy(fp + "/" + FNAME, SAVE_PATH)
    return pd.read_csv(os.path.join(SAVE_PATH, FNAME))


def clean(df: DF) -> DF:
    df = df.dropna()

    return df


def explore(df: DF) -> None:
    # Number of rows/games
    print(len(df.index))

    # Get games with NaN year
    action_games = df[df["Genre"] == "Action"]
    print(action_games[pd.isna(action_games["Year"])])

    # Clean the df
    clean_df = clean(df)
    print(len(clean_df.index))


def main() -> None:
    os.makedirs(SAVE_PATH, exist_ok=True)
    df = load_df()
    explore(df=df)


if __name__ == "__main__":
    main()
