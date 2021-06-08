import pandas as pd
from pathlib import Path
from datetime import date
from sqlalchemy import create_engine


file_path = 'C:/Users/sriram.uppala/Downloads/Privia_ACO_Member_Roster_20210331/Privia_ACO_Member_Roster_20210331.txt'
load_date = date.today()
p = Path(file_path)
file_name = p.stem
group = file_name.split('_')
source_file_name = '_'.join(group[:3])
print(source_file_name)


def main(path_of_file, file_name_of_source, loaded_date):
    df = pd.read_csv(path_of_file, sep="|")
    df['source_file_name'] = file_name_of_source
    df["load_date"] = loaded_date
    print(df.shape)
    connection = create_engine('mssql://GGKU2SER6/sriramU?driver=SQL Server Native Client 11.0?Trusted_connection=yes')
    df.to_sql('PriviaHealthDetailsTable', connection, if_exists='append', index=False)


if __name__ == '__main__':
    main(file_path, source_file_name, load_date)
