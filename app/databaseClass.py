import psycopg2
import pandas as pd
import io
from sqlalchemy import create_engine
import json


class DB:

    def __init__(self, userName, userPass, dataBaseName):
        self.userName = userName
        self.userPass = userPass
        self.dataBaseName = dataBaseName
        self.dbEngineText = 'postgresql+psycopg2://'+self.userName + \
            ':'+self.userPass+'@localhost:5432/'+self.dataBaseName

        def lstTables(self):
            query_listTables = '''
            SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
            '''
            conn = psycopg2.connect(
                "dbname="+self.dataBaseName+" user="+self.userName+" password="+self.userPass)
            cur = conn.cursor()
            cur.execute(query_listTables)
            # conn.commit()
            tables = cur.fetchall()
            tables = [table[0] for table in tables]
            conn.close()
            return tables

        self.tables = lstTables(self)

    def buildTable(self, tableName, fieldList):
        '''builds a new table in database
           fieldList example below:

            fieldList = triplequotesgohere(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT
            )triplequotesgohere

        '''
        if fieldList is None:
            print('There is no schema')
        else:
            query_make_table = '''
            CREATE TABLE {}{};
            '''.format(tableName, fieldList)
            conn = psycopg2.connect(
                "dbname="+self.dataBaseName+" user="+self.userName+" password="+self.userPass)
            cur = conn.cursor()
            cur.execute(query_make_table)
            conn.commit()
            conn.close()

    def dropTable(self, tableName):
        '''remove database table'''
        query_drop = '''
        DROP TABLE {}
        '''.format(tableName)
        conn = psycopg2.connect(
            "dbname="+self.dataBaseName+" user="+self.userName+" password="+self.userPass)
        cur = conn.cursor()
        cur.execute(query_drop)
        conn.commit()
        conn.close()

    def DFtoDB(self, df, tableName):
        '''puts dataframe in db'''
        engine = create_engine(self.dbEngineText)
        df.head(0).to_sql(tableName, engine, if_exists='append', index=False)
        #df.head(0).to_sql(tableName, engine, if_exists='replace',index=False)
        conn = engine.raw_connection()
        cur = conn.cursor()
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        cur.copy_from(output, tableName, null="")  # null values become ''
        conn.commit()
        conn.close()

    def MessagetoDB(self, message, tableName):
        message = message.replace('[', '')
        message = message.replace(']', '')
        dic = json.loads(message)
        df = pd.DataFrame(dic, index=[0])
        self.DFtoDB(df, tableName)

    def DBtoDF(self, query):
        '''runs query and returns df'''
        engine = create_engine(self.dbEngineText)
        df = pd.read_sql_query(query, con=engine)
        return df


if __name__ == '__main__':
    pass
