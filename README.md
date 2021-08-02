FastAPI + Vue のサンプルアプリ

#### run unicron for local development 

uvicorn backend.main:app --reload

#### run gunicorn for local development

gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.main:app --bind localhost:8000

#### sqlite

With launch of api, your local database file will be created.
You need to put csv files in data directory.

```
- backend
    - data
        - 2019_0csv
        - 2019_1csv
        - etc.
    - population_data
        - ***.csv
        - ***.csv
        - etc.
```

You need to insert all data by using backend/functions/crate_db.py.

```
python backend/functions/create_db.py
```

You need to delete empty data from crimes table.

```
sqlite3 ./sql_app.db
```

```
delete from crimes where fy is null;
```