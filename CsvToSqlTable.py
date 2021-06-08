import pandas as pd
from sqlalchemy import create_engine

file_path = 'C:/Users/sriram.uppala/Downloads/Privia_ACO_Member_Roster_20210331/Privia_ACO_Member_Roster_20210331.txt'


def main(path_of_file):
    df = pd.read_csv(path_of_file, sep="|")
    connection = create_engine('mssql://GGKU2SER6/sriramU?driver=SQL Server Native Client 11.0?Trusted_connection=yes')
    df.to_sql('PriviaHealthDetailsTable', connection, if_exists='append', index=False)


if __name__ == '__main__':
    main(file_path)
