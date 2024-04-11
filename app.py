from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#MODELS

# Define User model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)

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

# Define Playlist model
class Playlist(db.Model):
    __tablename__ = 'playlist'

    playlistid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    playlistname = db.Column(db.Text)
    song_name = db.Column(db.Text, nullable=False)
    creator_name = db.Column(db.Text, nullable=False)

# Define Album model
class Album(db.Model):
    __tablename__ = 'album'

    albumid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creatorid = db.Column(db.Integer)
    albumname = db.Column(db.Text)
    song_name = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(
        role=data.get('role'),
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User signed up successfully'}), 201


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


@app.route('/api/playlists', methods=['GET'])
def get_playlists():
    playlists = Playlist.query.all()
    playlist_list = []
    for playlist in playlists:
        playlist_data = {
            'playlistid': playlist.playlistid,
            'userid': playlist.userid,
            'playlistname': playlist.playlistname,
            'song_name': playlist.song_name,
            'creator_name': playlist.creator_name
        }
        playlist_list.append(playlist_data)
    
    return jsonify(playlists=playlist_list)


# @app.route('/api/creator')
# def get_creator():
#     creator = Creator.query.all()
#     creator_data = []
#     for create in creator:
#         creator_data.append({
#             'creatorid':creator.creatorid,
#             'creatorname':creator.creatorname,
#             'password':creator.password,
#         })
#     return jsonify(creator_data)


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


@app.route('/api/flag_song/<int:song_id>', methods=['PUT'])
def flag_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404

    song.flagged = True
    db.session.commit()
    return jsonify({'message': f'Song {song_id} flagged successfully'})

# API endpoint to delete a song
@app.route('/api/delete_song/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404

    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': f'Song {song_id} deleted successfully'})
# API endpoint to fetch lyrics for a specific song
@app.route('/api/songs/<int:song_id>/lyrics', methods=['GET'])
def get_song_lyrics(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404
    return jsonify({'lyrics': song.lyrics})


if __name__ == "__main__":
    app.run(debug=True)