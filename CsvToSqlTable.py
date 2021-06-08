import pandas as pd
import sqlalchemy

file_path = 'C:/Users/sriram.uppala/Downloads/Privia_ACO_Member_Roster_20210331/Privia_ACO_Member_Roster_20210331.txt'


def main(path_of_file):
    df = pd.read_csv(path_of_file, sep="|")
    print(df.shape)


if __name__ == '__main__':
    main(file_path)
