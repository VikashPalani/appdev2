'''from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "this_is_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Song model
class Song(db.Model):
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50))
    song_name = db.Column(db.String(100))
    duration = db.Column(db.String(20))
    lyrics = db.Column(db.Text)
    creator_name = db.Column(db.String(100))
    song_path = db.Column(db.String(200))
    image_path = db.Column(db.Text(200))
    avg_rating = db.Column(db.Float)

# Define the Creator model
class Creator(db.Model):
    __tablename__ = 'creator'
    creatorid = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    creatorname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Define the User model
class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Define the Playlist model
class Playlist(db.Model):
    __tablename__ = 'playlist'
    playlistid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    playlistname = db.Column(db.Text)
    song_name = db.Column(db.Text, nullable=False)
    creator_name = db.Column(db.Text, nullable=False)

# Define the Album model
class Album(db.Model):
    __tablename__ = 'albums'
    album_id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(100))
    artist_name = db.Column(db.String(100))
    release_date = db.Column(db.String(20))
    genre = db.Column(db.String(50))

# Create all tables
with app.app_context():
    db.create_all()

# Route to fetch song and image paths
@app.route('/get_songs_and_images', methods=['GET'])
def get_songs_and_images():
    # Query the database to get song and image paths
    songs = Song.query.all()
    data = []

    for song in songs:
        song_data = {
            'song_name': song.song_name,
            'image_path': song.image_path,
            'song_path': song.song_path
            # Add more fields if needed
        }
        data.append(song_data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db = SQLAlchemy(app)

# Define Song model
class Song(db.Model):
    __tablename__ = 'songs'  # Specify the table name explicitly
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100))
    lyrics = db.Column(db.Text)
    audio_url = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

# API endpoint to fetch song data
@app.route('/api/songs')
def get_songs():
    songs = Song.query.all()
    song_data = []
    for song in songs:
        song_data.append({
            'song_id': song.song_id,  # Include song_id in the response
            'title': song.title,
            'artist': song.artist,
            'album': song.album,
            'lyrics': song.lyrics,
            'audio_url': song.audio_url,
            'release_date': str(song.release_date),  # Convert release_date to string
            'creator_id': song.creator_id
        })
    return jsonify(song_data)

# API endpoint to add a new song
@app.route('/api/add_song', methods=['POST'])
def add_song():
    data = request.get_json()
    new_song = Song(
        title=data.get('title'),
        artist=data.get('artist'),
        album=data.get('album'),
        lyrics=data.get('lyrics'),
        audio_url=data.get('audio_url'),
        release_date=data.get('release_date'),
        creator_id=data.get('creator_id')
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Song added successfully'})

if __name__ == "__main__":
    app.run(debug=True)
'''
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
