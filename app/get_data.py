import zipfile
from databaseClass import DB
import utils
import glob
import pandas as pd

path_to_zip_file = 'data/archive.zip'
directory_to_extract_to = 'data'
postgres_table_name = 'pbp'


def unzip():
    # unzip csv files
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

    print("unzipped files okay")


def send_to_database():
    # send files to database
    files = glob.glob(f"{directory_to_extract_to}/NBA*")
    # info needed to connect to database
    userName = utils.userName
    userPass = utils.userPass
    dbName = utils.dbName
    db = DB(userName=userName, userPass=userPass, dataBaseName=dbName)

    for file in files:
        df = pd.read_csv(file)
        if "Unnamed: 40" in df.columns:
            df = df.drop(["Unnamed: 40"], axis=1)
        df.columns= df.columns.str.lower()
        db.DFtoDB(df, postgres_table_name)
        print(f"loaded {file}")


if __name__ == '__main__':
    unzip()
    send_to_database()
