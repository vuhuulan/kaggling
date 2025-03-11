import os
import shutil
import kagglehub
import pandas
from pandas.core.frame import DataFrame as DF

TARGET = "anandshaw2001/video-game-sales"
SAVE_PATH = "./data/"
FNAME = "vgsales.csv"


def load_df() -> DF:
    if os.listdir(SAVE_PATH):
        return pandas.read_csv(os.path.join(SAVE_PATH, FNAME))
    fp = kagglehub.dataset_download(TARGET)
    shutil.copy(fp + "/" + FNAME, SAVE_PATH)
    return pandas.read_csv(os.path.join(SAVE_PATH, FNAME))


def explore(df: DF) -> None:
    action_games = df[df["Genre"] == "Action"]
    # print(df[df["Genre"] == "Action"].count())
    print(action_games[action_games["Year"].isna()])
    # print(df.groupby(["Genre"]).count())


def main() -> None:
    os.makedirs(SAVE_PATH, exist_ok=True)
    df = load_df()
    explore(df=df)


if __name__ == "__main__":
    main()
