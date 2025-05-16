from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Painting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20000))
    artist = db.Column(db.String(10000))
    year = db.Column(db.String(10000))
    artistBio = db.Column(db.String(100000))
    artistGender = db.Column(db.String(10000))
    artistNationality = db.Column(db.String(10000))
    creditLine = db.Column(db.String(10000))
    city = db.Column(db.String(10000))
    state = db.Column(db.String(10000))
    county = db.Column(db.String(10000))
    country = db.Column(db.String(10000))
    region = db.Column(db.String(10000))
    subregion = db.Column(db.String(10000))
    extraDataURL = db.Column(db.String(10000))
    dimensions = db.Column(db.String(10000))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "artistBio": self.artistBio,
            "artistGender": self.artistGender,
            "artistNationality": self.artistNationality,
            "creditLine": self.creditLine,
            "city": self.city,
            "state": self.state,
            "county": self.county,
            "country": self.country,
            "region": self.region,
            "subregion": self.subregion,
            "extraDataURL": self.extraDataURL,
            "dimensions": self.dimensions
        }