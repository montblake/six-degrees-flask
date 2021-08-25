from app import db


actor_film = db.Table('actor_film',
    db.Column('actor_id', db.String, db.ForeignKey('actor.id')),
    db.Column('film_id', db.String, db.ForeignKey('film.id'))
)

class Actor(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    films = db.relationship(
        'Film', secondary=actor_film,
        backref=db.backref('cast', lazy='joined'), lazy='joined')
    
    def __repr__(self):
        return '<Actor {}>'.format(self.name)


class Film(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    title = db.Column(db.String(120), index=True)
    
    def __repr__(self):
        return '<Film {}>'.format(self.title)