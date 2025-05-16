import pandas as pd
from app import app, db
from models import Painting

df = pd.read_csv('paintings.csv', low_memory=False)

with app.app_context():
    db.drop_all()
    db.create_all()
    for _, row in df.iterrows():
        painting = Painting(
            title=str(row.get('Title', '')),
            artist=str(row.get('Artist Display Name', '')),
            year=str(row.get('Object Date', '')),
            artistBio=str(row.get('Artist Display Bio', '')),
            artistGender=str(row.get('Artist Gender', '')),
            artistNationality=str(row.get('Artist Nationality', '')),
            creditLine=str(row.get('Credit Line', '')),
            city=str(row.get('City', '')),
            state=str(row.get('State', '')),
            county=str(row.get('County', '')),
            country=str(row.get('Country', '')),
            region=str(row.get('Region', '')),
            subregion=str(row.get('Subregion', '')),
            extraDataURL=str(row.get('Object Wikidata URL', '')),
            dimensions=str(row.get('Dimensions', '')),
        )
        db.session.add(painting)
    db.session.commit()

print("Database loaded.")
