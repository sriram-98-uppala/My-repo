import pandas as pd
from pathlib import Path
from datetime import date


file_path = 'C:/Users/sriram.uppala/Downloads/Privia_ACO_Member_Roster_20210331/Privia_ACO_Member_Roster_20210331.txt'
load_date = date.today()
p = Path(file_path)
file_name = p.stem
group = file_name.split('_')
source_file_name = '_'.join(group[:3])
print(source_file_name)

def main(path_fo_file, file_name_of_source, loaded_date):
    df = pd.read_csv(path_fo_file, sep="|")
    df['source_file_name'] = file_name_of_source
    df["load_date"] = loaded_date
    print(df.shape)


if __name__ == '__main__':
    main(file_path, source_file_name, load_date)
