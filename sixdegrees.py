from app import app, db
from app.models import Actor, Film

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Actor': Actor, 'Film': Film}