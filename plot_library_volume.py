import argparse
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot the library utilization from a history file.")
    parser.add_argument("--file", help="Path to the history file.", type=str)
    args = parser.parse_args()

    volumes = pd.read_csv(
        args.file,
        index_col="datetime",
    )
    volumes.index = pd.to_datetime(volumes.index)

    volumes['volume'].plot()
    plt.show()