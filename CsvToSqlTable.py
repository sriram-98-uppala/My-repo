import pandas as pd


def main():
    df = pd.read_csv(r'C:/Users/sriram.uppala/Downloads/Privia_ACO_Member_Roster_20210331/Privia_ACO_Member_Roster_20210331.txt', sep = "|")
    print(df)


if __name__ == '__main__':
    main()
