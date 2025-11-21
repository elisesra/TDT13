import argparse
import os

import pandas as pd
import matplotlib.pyplot as plt


def plot_hist(df, column, title, out_dir):
    values = df[column].dropna()

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{column}_hist.png")

    plt.figure()
    plt.hist(values, bins=30)
    plt.title(title)
    plt.xlabel(title)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main():
    parser = argparse.ArgumentParser(
        description="Histograms"
    )
    parser.add_argument("csv", help="Input file.")
    parser.add_argument("out_dir", help="Folder out.")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)

    plot_hist(df, "token_f1", "Token F1", args.out_dir)
    plot_hist(df, "bert_similarity", "BERT similarity", args.out_dir)
    plot_hist(df, "bart_similarity", "BART similarity", args.out_dir)


if __name__ == "__main__":
    main()
