from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {"id": self.id, "url": self.url, "rating": self.rating}
