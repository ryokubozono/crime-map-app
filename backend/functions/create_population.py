import sqlite3
import pandas as pd
import sys
import os

dbname = 'sql_app.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

population_dir = 'backend/population_data'

population_files = os.listdir(population_dir)
population_files.sort(reverse=False)

df = pd.DataFrame()

for file_name in population_files:
    filename = os.path.join(population_dir, file_name)
    print(filename)
    df_tmp = pd.read_csv(
        filename,
        skiprows=2,
        header=None,
        encoding='cp932'
    )
    df_tmp.columns = [
        'KEY_CODE',
        'HYOSYO',
        'CITYNAME',
        'PLACENAME',
        'HTKSYORI',
        'HTKSAKI',
        'GASSAN',
        'population',
        'men',
        'women',
        'homes',
        'LocName',
        'fx',
        'fy',
        'iconf',
        'ilvl',
    ]

    df_tmp['KEY_CODE'] = df_tmp['KEY_CODE'].fillna(0).astype('int')
    df_tmp['HYOSYO'] = df_tmp['HYOSYO'].fillna(0).astype('int')
    df_tmp = df_tmp.replace('-', '0')
    df_tmp['HTKSYORI'] = df_tmp['HTKSYORI'].fillna(0).astype('int')
    df_tmp['population'] = df_tmp['population'].astype(int)
    df_tmp['men'] = df_tmp['men'].fillna(0).astype(int)
    df_tmp['women'] = df_tmp['women'].fillna(0).astype(int)
    df_tmp['homes'] = df_tmp['homes'].fillna(0).astype(int)

    df = pd.concat([
        df,
        df_tmp
    ], ignore_index=True)


for index, row in df.iterrows():
    for i in range(7):
        place = row[11]

        sql_text = 'SELECT * FROM crimes where location_name like ' + '"%' + place + '%"' + 'and crime_type is ' + str(i)

        crime_count = 0
        for crime in cur.execute(sql_text):
            crime_count += 1
            print(crime)
        
        print('crime_count is ', crime_count, ', place is ', place, ', crime_type is ', i)

        df.at[index, 15+i] = crime_count


df.columns = [
    'KEY_CODE',
    'HYOSYO',
    'CITYNAME',
    'PLACENAME',
    'HTKSYORI',
    'HTKSAKI',
    'GASSAN',
    'population',
    'men',
    'women',
    'homes',
    'LocName',
    'fx',
    'fy',
    'iconf',
    'ilvl',
    'crime_0',
    'crime_1',
    'crime_2',
    'crime_3',
    'crime_4',
    'crime_5',
    'crime_6',
]

df['crime_0'] = df['crime_0'].fillna(0).astype(int)
df['crime_1'] = df['crime_1'].fillna(0).astype(int)
df['crime_2'] = df['crime_2'].fillna(0).astype(int)
df['crime_3'] = df['crime_3'].fillna(0).astype(int)
df['crime_4'] = df['crime_4'].fillna(0).astype(int)
df['crime_5'] = df['crime_5'].fillna(0).astype(int)
df['crime_6'] = df['crime_6'].fillna(0).astype(int)


df.to_sql('places', conn, if_exists='replace', index_label='id')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM places'
for row in cur.execute(select_sql):
    print(row)