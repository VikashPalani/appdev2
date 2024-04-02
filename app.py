from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db = SQLAlchemy(app)

# Define Song model
class Song(db.Model):
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50))
    song_name = db.Column(db.String(100))
    duration = db.Column(db.String(20))
    lyrics = db.Column(db.Text)
    creator_name = db.Column(db.String(100))
    song_path = db.Column(db.String(200))
    image_path = db.Column(db.String(200))
    avg_rating = db.Column(db.Float)

# API endpoint to fetch song data
@app.route('/api/songs')
def get_songs():
    songs = Song.query.all()
    song_data = []
    for song in songs:
        song_data.append({
            'song_id': song.song_id,
            'genre': song.genre,
            'song_name': song.song_name,
            'duration': song.duration,
            'lyrics': song.lyrics,
            'creator_name': song.creator_name,
            'song_path': song.song_path,
            'image_path': song.image_path,
            'avg_rating': song.avg_rating
        })
    return jsonify(song_data)

# API endpoint to add a new song
@app.route('/api/add_song', methods=['POST'])
def add_song():
    data = request.get_json()
    new_song = Song(
        genre=data.get('genre'),
        song_name=data.get('song_name'),
        duration=data.get('duration'),
        lyrics=data.get('lyrics'),
        creator_name=data.get('creator_name'),
        song_path=data.get('song_path'),
        image_path=data.get('image_path'),
        avg_rating=data.get('avg_rating')
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Song added successfully'})

if __name__ == "__main__":
    app.run(debug=True)
