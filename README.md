#### run unicron for local development 

uvicorn backend.main:app --reload

#### run gunicorn for local development

gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.main:app --bind localhost:8000