from databaseClass import DB
import utils
import sql_files

userName = utils.userName
userPass = utils.userPass
dbName = utils.dbName

db = DB(userName=userName, userPass=userPass, dataBaseName=dbName)


def generate_sql(input_sql_file):
    with open(input_sql_file, 'r') as file:
        sql = file.read()
        return sql


# #db.BuildTableFromQuery(generate_sql('sql_files/game_scores.sql'), 'game_scores')
# db.BuildTableFromQuery(generate_sql('sql_files/format_columns.sql'), 'format_columns')


def build_table(sql_file, table_name):
    '''postgres does not have a create or replace table option.  so we do that here instead'''
    try:
        db.BuildTableFromQuery(generate_sql(sql_file), table_name)
        print(f"{table_name} didn't exist. completed loading")
    except:
        db.dropTable(table_name)
        db.BuildTableFromQuery(generate_sql(sql_file), table_name)
        print(
            f"{table_name} did exist. dropped old version and completed loading new one")


if __name__ == '__main__':
    build_table('sql_files/game_scores.sql', 'game_scores')
    build_table('sql_files/shot_performance.sql',
                'player_game_shot_performance')
    build_table('sql_files/game_rosters_1.sql', 'game_rosters_1')
    build_table('sql_files/game_rosters_2.sql', 'game_rosters_2')
    build_table('sql_files/game_rebounds.sql', 'game_rebounds')
    build_table('sql_files/output.sql', 'output')
