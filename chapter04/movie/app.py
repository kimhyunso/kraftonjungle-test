from bson import ObjectId
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
from flask.json.provider import JSONProvider

import json
import sys

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.jungle


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class CustomJSONProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=CustomJSONEncoder)
    
    def loads(self, s, **kwrags):
        return json.loads(s, **kwrags)
    

app.json = CustomJSONProvider(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/trash/move', methods=['POST'])
def trach_move():
    mode = True
    id = request.form['id']
    trash_mode = request.form['trashMode']
    if trash_mode == 'true':
        mode = False

    db.movies.update_one({'_id' : ObjectId(id)},{'$set':{'trashed': mode}})
    return jsonify({'result' : 'success'})

@app.route('/api/trash/delete', methods=['POST'])
def trach_delete():
    id = request.form['id']
    db.movies.delete_one({'_id' : ObjectId(id)})
    return jsonify({'result' : 'success'})

@app.route('/api/list', methods=['GET'])
def show_movies():
    sortMode = request.args.get('sortMode', 'likes')
    status = request.args.get('status', 'list')

    if sortMode not in ['likes', 'date', 'viewers']:
            return jsonify({'result': 'failure', 'message': 'Invalid sortMode value.'})
    elif sortMode == 'date':
        sortMode = {
            'open_year' : -1,
            'open_month' : -1,
            'open_day' : -1
        }
    else:
        sortMode = {
            sortMode : -1
        }
    if status == 'list':
        movies = list(db.movies.find({'trashed': False}).sort(sortMode))
    elif status == 'trash':
        movies = list(db.movies.find({'trashed': True}).sort(sortMode))

    
    return jsonify({'result': 'success', 'movies_list': movies})



@app.route('/api/like', methods=['POST'])
def like_movie():
    id = request.form['id']
    movie = db.movies.find_one({'_id' : ObjectId(id)})

    new_likes = movie['likes'] + 1
    result = db.movies.update_one({'_id' : ObjectId(id)}, {'$set': {'likes': new_likes}})

    if result.modified_count == 1:
        return jsonify({'result' : 'success'})
    else:
        return jsonify({'result' : 'failure'})
    

if __name__ == '__main__':
    print(sys.executable)
    app.run('0.0.0.0', port=5000, debug=True)

