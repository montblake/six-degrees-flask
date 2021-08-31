from app import db
from datetime import datetime


actor_film = db.Table('actor_film',
    db.Column('actor_id', db.String, db.ForeignKey('actor.id')),
    db.Column('film_id', db.String, db.ForeignKey('film.id'))
)

class Actor(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    image_url = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    films = db.relationship(
        'Film', secondary=actor_film,
        backref=db.backref('cast', lazy='joined'), lazy='joined')
    
    def __repr__(self):
        return '<Actor {}>'.format(self.name)


class Film(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    title = db.Column(db.String(120), index=True)
    year = db.Column(db.Integer)
    image_url = db.Column(db.Text)
    featured_cast = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Film {}>'.format(self.title)