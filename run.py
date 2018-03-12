from app import app
from db import # DEBUG:


db.init_app(app)

@app.before_first_request # run this code before executing first request
def create_tables():
    db.create_all()
