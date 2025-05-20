from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Painting 
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres.sjeuazjxomeczkowxvzj:Enderbe%40st123@aws-0-eu-west-2.pooler.supabase.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/search', methods = ['GET'])
def search_paintings():
    query = Painting.query

    artist = request.args.get('artist')
    year = request.args.get('year')
    title_keyword = request.args.get('title')

    if artist:
        query = query.filter(Painting.artist.ilike(f'%{artist}%'))
    if year:
        query = query.filter(Painting.year == year)
    if title_keyword:
        query = query.filter(Painting.title.ilike(f'%{title_keyword}%'))

    results = query.limit(100).all()
    return jsonify([p.to_dict() for p in results])

@app.route('/')
def home():
    return jsonify({"message": "VR museum API running"})


@app.route('/paintings', methods=['GET'])
def get_paintings():
    page = int(request.args.get('page', 1))  
    limit = int(request.args.get('limit', 10))  
    q = request.args.get('q', '').lower()
    offset = (page - 1) * limit
    query = Painting.query

    paintings = Painting.query.offset(offset).limit(limit).all()
    total = Painting.query.count()

    return jsonify({
        'data': [p.to_dict() for p in paintings],
        'total': total,
        'page': page,
        'limit': limit
        })

@app.route('/paintings/<int:painting_id>', methods=['GET'])
def get_painting(painting_id):
    painting = Painting.query.get_or_404(painting_id)
    return jsonify(painting.to_dict())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

