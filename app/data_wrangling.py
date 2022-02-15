from databaseClass import DB
import utils
import sql_files
import pandas as pd
import numpy as np

userName = utils.userName
userPass = utils.userPass
dbName = utils.dbName

db = DB(userName=userName, userPass=userPass, dataBaseName=dbName)


def generate_sql(input_sql_file):
    with open(input_sql_file, 'r') as file:
        sql = file.read()
        return sql



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


def final_table():

    def get_data():
        df_games = db.DBtoDF(generate_sql('sql_files/output.sql'))
        df_games = df_games[df_games['team'].notnull()]
        df_games['player'] = df_games['player'].str[0]
        df_games['player_team'] = df_games['player'] + "_" + df_games['team']
        player_names = df_games['player_team'].unique()
        player_names = player_names[~pd.isnull(player_names)] #remove empty player names
        return df_games, player_names

    def pre_process_df(player_team):
        df_temp = df_games[df_games['player_team'] == player_team].drop(columns=['homescore', 'awayscore'])
        df_temp = df_temp.rolling(window=3)
        df_temp = df_temp.mean().round(decimals=2)
        df_temp['player_team'] = player_team
        return df_temp

    df_games, player_names = get_data()

    df_list = []
    for player in player_names:
        df_list.append(pre_process_df(player))

    df = pd.concat(df_list, axis=0)
    df_merged = df_games.merge(df, how='outer', left_index=True, right_index=True)
    df_merged = df_merged[~df_merged['two_point_shots_made_y'].isnull()]
    df_merged['spread_target'] = df_merged['homescore'] - df_merged['awayscore']

    db.DFtoDB(df_merged, "final")

if __name__ == '__main__':
    prep for generating and aggregating data to postgres
    build_table('sql_files/game_scores.sql', 'game_scores')
    build_table('sql_files/shot_performance.sql',
                'player_game_shot_performance')
    build_table('sql_files/game_rosters_1.sql', 'game_rosters_1')
    build_table('sql_files/game_rosters_2.sql', 'game_rosters_2')
    build_table('sql_files/game_rebounds.sql', 'game_rebounds')
    build_table('sql_files/output.sql', 'output')

    #build final dataset for training
    final_table()