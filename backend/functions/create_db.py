import sqlite3
import pandas as pd

dbname = 'sql_app.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# pandasでカレントディレクトリにあるcsvファイルを読み込む
# csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
df_0 = pd.read_csv("backend/data/2019_0.csv", encoding='cp932')
df_1 = pd.read_csv("backend/data/2019_1.csv", encoding='cp932')
df_2 = pd.read_csv("backend/data/2019_2.csv", encoding='cp932')
df_3 = pd.read_csv("backend/data/2019_3.csv", encoding='cp932')
df_4 = pd.read_csv("backend/data/2019_4.csv", encoding='cp932')
df_5 = pd.read_csv("backend/data/2019_5.csv", encoding='cp932')
df_6 = pd.read_csv("backend/data/2019_6.csv", encoding='cp932')

# カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
# pandasが自動で1行目をカラム名として認識してくれる。
df_0.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location', 
    'key', 
    'anti_theft', 
    'object', 
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_1.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location', 
    'gender', 
    'age', 
    'object', 
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]


df_2.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location',  
    'age', 
    'job',
    'key', 
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_3.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location',  
    'key', 
    'anti_theft',
    'object', 
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_4.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location',  
    'money',  
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_5.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location', 
    'key', 
    'money',  
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_6.columns = [
    'police_area', 
    'police_city', 
    'city_code', 
    'prefecture', 
    'city', 
    'street', 
    'date', 
    'hour', 
    'location', 
    'object', 
    'location_name', 
    'fx', 
    'fy', 
    'iconf', 
    'ilvl'
]

df_0['crime_type'] = 0
df_0['gender'] = ""
df_0['age'] = ""
df_0['job'] = ""
df_0['money'] = ""
df_1['crime_type'] = 1 
df_1['key'] = ""
df_1['job'] = ""
df_1['money'] = ""
df_1['anti_theft'] = ""
df_1['anti_theft'] = ""
df_2['crime_type'] = 2
df_2['gender'] = ""
df_2['object'] = ""
df_2['money'] = ""
df_2['anti_theft'] = ""
df_3['crime_type'] = 3
df_3['gender'] = ""
df_3['age'] = ""
df_3['job'] = ""
df_3['money'] = ""
df_4['crime_type'] = 4
df_4['key'] = ""
df_4['anti_theft'] = ""
df_4['object'] = ""
df_4['gender'] = ""
df_4['age'] = ""
df_4['job'] = ""
df_5['crime_type'] = 5
df_5['anti_theft'] = ""
df_5['object'] = ""
df_5['gender'] = ""
df_5['age'] = ""
df_5['job'] = ""
df_6['crime_type'] = 6
df_6['anti_theft'] = ""
df_6['key'] = ""
df_6['gender'] = ""
df_6['age'] = ""
df_6['job'] = ""
df_6['money'] = ""

df = pd.concat([
    df_0, 
    df_1, 
    df_2, 
    df_3,
    df_4,
    df_5,
    df_6,
], ignore_index=True)

# dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
df.to_sql('crimes', conn, if_exists='replace', index_label='id')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM crimes'
for row in cur.execute(select_sql):
    print(row)


# 空のデータを削除する
delete_sql = 'DELETE FROM crimes where fx IS NULL'
for row in cur.execute(delete_sql):
    print(row)
# 空のデータを削除する
delete_sql = 'DELETE FROM crimes where fx IS NULL'
for row in cur.execute(delete_sql):
    print(row)

cur.close()
conn.close()
