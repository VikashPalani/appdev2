from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    user = User.query.filter_by(name=name, password=password).first()
    if user:
        # session['id'] = user.id
        # session['name'] = user.name

        return jsonify({'message': 'Login successful', 'role': user.role}), 200
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

# @app.route('/api/playlists', methods=['GET'])
# def get_playlists():
#     playlists = Playlist.query.all()
#     grouped_playlists = defaultdict(list)
    
#     for playlist in playlists:
#         playlist_info = {
#             'song_name': playlist.song_name,
#             'creator_name': playlist.creator_name
#         }
#         grouped_playlists[playlist.playlistname].append(playlist_info)
    
#     # Convert defaultdict to list of dictionaries
#     playlist_data = [{'playlist_name': key, 'songs': value} for key, value in grouped_playlists.items()]
    
#     return jsonify(playlists=playlist_data)



# @app.route('/api/playlists', methods=['GET'])
# def get_playlists():
#     playlists = Playlist.query.all()
#     playlist_list = []
#     for playlist in playlists:
#         playlist_data = {
#             'playlistid': playlist.playlistid,
#             'userid': playlist.userid,
#             'playlistname': playlist.playlistname,
#             'song_name': playlist.song_name,
#             'creator_name': playlist.creator_name
#         }
#         playlist_list.append(playlist_data)
    
#     return jsonify(playlists=playlist_list)


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()

    if query:
        # Perform case-insensitive search without using func.lower()
        search_results = Song.query.filter(
            db.func.lower(Song.song_name).contains(query) |
            db.func.lower(Song.genre).contains(query) |
            db.func.lower(Song.creator_name).contains(query) |
            db.cast(Song.avg_rating, db.String).contains(query)
        ).all()

        # Serialize the search results into JSON format
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
        # If no query provided, return an empty list (or all songs)
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


if __name__ == "__main__":
    app.run(debug=True)