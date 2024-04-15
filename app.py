from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import sqlite3

from collections import defaultdict
from sqlalchemy import func, desc, distinct

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from flask_cors import CORS
CORS(app)

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
    id = db.Column(db.Integer)
    playlistname = db.Column(db.Text)
    song_name = db.Column(db.Text, nullable=False)
    creator_name = db.Column(db.Text, nullable=False)

# Define Album model
class Album(db.Model):
    __tablename__ = 'album'

    albumid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer)
    albumname = db.Column(db.Text)
    song_name = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    creator_name = db.Column(db.Text, nullable=False)


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


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    user = User.query.filter_by(name=name, password=password).first()
    
    if user:
        return jsonify({
            'message': 'Login successful',
            'id': user.id,
            'name': user.name,
            'role': user.role
        }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
 
    
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

# Route to add songs to playlist
@app.route('/api/add_to_playlist', methods=['POST'])
def add_to_playlist():
    data = request.get_json()

    playlist_name = data.get('playlist_name')
    songs = data.get('songs')

    for song in songs:
        new_playlist = Playlist(
            id = 3,
            playlistname=playlist_name,
            song_name=song['song_name'],
            creator_name=song['creator_name']
        )
        db.session.add(new_playlist)

    db.session.commit()
    return jsonify({'message': 'Songs added to playlist successfully'}), 201

# Route to add a song to an album
@app.route('/api/add_to_album', methods=['POST'])
def add_to_album():
    data = request.get_json()
    song_name = data.get('song_name')
    creator_name = data.get('creator_name')
    album_name = data.get('album_name')

    if not (song_name and creator_name and album_name):
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        album = Album.query.filter_by(albumname=album_name).first()
        if not album:
            album = Album(albumname=album_name)
            db.session.add(album)
            db.session.commit()

        new_album_song = Album(
            id=7,
            albumname=album_name,
            song_name=song_name,
            creator_name=creator_name,
            genre='Pop' 
        )
        db.session.add(new_album_song)
        db.session.commit()

        return jsonify({'message': 'Song added to album successfully'}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemy Error: {str(e)}")
        return jsonify({'message': 'Failed to add song to album. Please try again.'}), 500

    except Exception as e:
        print(f"Error adding song to album: {str(e)}")
        return jsonify({'message': 'Failed to add song to album. Please try again.'}), 500
    

# API endpoint to fetch all albums
@app.route('/api/albums', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    album_data = []
    for album in albums:
        album_data.append({
            'album_id': album.albumid,
            'album_name': album.albumname,
            'genre': album.genre,
            'creator_name': album.creator_name
        })
    return jsonify(album_data)

# API endpoint to fetch songs for a specific album
@app.route('/api/albums/<int:album_id>/songs', methods=['GET'])
def get_songs_in_album(album_id):
    songs_in_album = Song.query.filter_by(album_id=album_id).all()
    song_data = []
    for song in songs_in_album:
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

# API endpoint to fetch albums matching a specific album name
@app.route('/api/albums/<string:album_name>/matching_albums', methods=['GET'])
def get_matching_albums(album_name):
    try:
        user_name = request.args.get('userName')
        matching_albums = Album.query.filter_by(albumname=album_name, creator_name=user_name).all()
        album_data = []
        for album in matching_albums:
            album_data.append({
                'album_id': album.albumid,
                'album_name': album.albumname,
                'song_name': album.song_name,
                'creator_name': album.creator_name
            })
        return jsonify(album_data), 200
    except Exception as e:
        print(f"Error fetching matching albums: {str(e)}")
        return jsonify({'message': 'Failed to fetch matching albums'}), 500


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()

    if query:
        search_results = Song.query.filter(
            db.func.lower(Song.song_name).contains(query) |
            db.func.lower(Song.genre).contains(query) |
            db.func.lower(Song.creator_name).contains(query) |
            db.cast(Song.avg_rating, db.String).contains(query)
        ).all()

        serialized_results = [{
            'song_id': song.song_id,
            'genre': song.genre,
            'song_name': song.song_name,
            'duration': song.duration,
            'lyrics': song.lyrics,
            'creator_name': song.creator_name,
            'song_path': song.song_path,
            'image_path': song.image_path,
            'avg_rating': song.avg_rating
        } for song in search_results]

        return jsonify(serialized_results)
    else:
        songs = Song.query.all()
        serialized_songs = [{
            'song_id': song.song_id,
            'genre': song.genre,
            'song_name': song.song_name,
            'duration': song.duration,
            'lyrics': song.lyrics,
            'creator_name': song.creator_name,
            'song_path': song.song_path,
            'image_path': song.image_path,
            'avg_rating': song.avg_rating
        } for song in songs]

        return jsonify(serialized_songs)

# API endpoint to delete a song
@app.route('/api/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404

    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': f'Song {song_id} deleted successfully'})


# @app.route('/api/flag_song/<int:song_id>', methods=['PUT'])
# def flag_song(song_id):
#     song = Song.query.get(song_id)
#     if not song:
#         return jsonify({'message': 'Song not found'}), 404

#     song.flagged = True
#     db.session.commit()
#     return jsonify({'message': f'Song {song_id} flagged successfully'})

# API endpoint to update lyrics for a specific song
@app.route('/api/songs/<int:song_id>', methods=['PUT'])
def update_song_lyrics(song_id):
    data = request.get_json()
    new_lyrics = data.get('lyrics')

    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404

    song.lyrics = new_lyrics
    db.session.commit()

    return jsonify({'message': f'Lyrics for song {song_id} updated successfully'}), 200


# API endpoint to fetch lyrics for a specific song
@app.route('/api/songs/<int:song_id>/lyrics', methods=['GET'])
def get_song_lyrics(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404
    return jsonify({'lyrics': song.lyrics})

@app.route('/api/admin_data')
def admin_data():
    num_users = User.query.filter_by(role='user').count()
    num_creators = User.query.filter_by(role='creator').count()
    num_songs = Song.query.count()
    num_playlists = Playlist.query.with_entities(distinct(Playlist.playlistname)).count()
    num_genres = Song.query.with_entities(distinct(Song.genre)).count()

    top_creators = (
        db.session.query(Song.creator_name, func.avg(Song.avg_rating).label('average_rating'))
        .group_by(Song.creator_name)
        .order_by(desc(func.avg(Song.avg_rating)))
        .limit(5)
        .all()
    )

    top_songs = (
        db.session.query(Song.song_name, func.avg(Song.avg_rating).label('average_rating'))
        .group_by(Song.song_name)
        .order_by(desc(func.avg(Song.avg_rating)))
        .limit(5)
        .all()
    )

    top_creators_dict = [{'creatorname': row[0], 'average_rating': row[1]} for row in top_creators]
    top_songs_dict = [{'song_name': row[0], 'average_rating': row[1]} for row in top_songs]

    data = {
        'num_users': num_users,
        'num_creators': num_creators,
        'num_songs': num_songs,
        'num_playlists': num_playlists,
        'num_genres': num_genres,
        'top_creators': top_creators_dict,
        'top_songs': top_songs_dict
    }

    return jsonify(data)


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
    return jsonify({'message': 'Song added successfully'}), 201


    
# Endpoint to fetch unique playlist names
@app.route('/api/playlists', methods=['GET'])
def get_unique_playlists():
    try:
        playlists = Playlist.query.with_entities(distinct(Playlist.playlistname)).all()
        unique_playlists = [playlist[0] for playlist in playlists]
        return jsonify(unique_playlists), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/playlists/<playlist_name>/songs', methods=['GET'])
def get_songs_by_playlist(playlist_name):
    try:
        user_id = request.args.get('userId')
        playlist = Playlist.query.filter_by(playlistname=playlist_name).first()

        if not playlist:
            return jsonify({'message': 'Playlist not found for the current user'}), 404

        playlists = Playlist.query.filter_by(playlistname=playlist_name).all()

        song_data = []
        for playlist in playlists:
            song_data.append({
                'song_name': playlist.song_name,
                'creator_name': playlist.creator_name
            })

        return jsonify(song_data), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': f'Failed to fetch songs for playlist: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'message': f'Error fetching songs for playlist: {str(e)}'}), 500



if __name__ == "__main__":
    app.run(debug=True)