import os
import uuid
import base64
import sqlite3
from dataclasses import dataclass
from flask import Flask, request, render_template

app = Flask(__name__)

def init():
    os.system('rm -rf static/pictures/*')
    db = sqlite3.connect('sewi.db')
    db.execute('DROP TABLE pictures;')
    db.execute('CREATE TABLE pictures (path text);')

# @app.route('/public/<path:path>')
# def public():
#     return send_from_directory('js', path)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@dataclass
class Image:
    src: str

@app.route('/picture/upload', methods=['POST'])
def upload():
    path = str(uuid.uuid4())
    _, data = request.json['image'].split(',')
    with open(f'static/pictures/{path}.png', 'wb') as f:
        f.write(base64.b64decode(data))
    db = sqlite3.connect('sewi.db')
    db.execute(f"INSERT INTO pictures VALUES ('/static/pictures/{path}.png');")
    db.commit()
    db.close()
    return ''

@app.route('/')
def index():
    db = sqlite3.connect('sewi.db')
    images = db.execute('SELECT * FROM pictures;').fetchall()
    db.close()
    return render_template('index.html', images=[Image(*image) for image in images])

if __name__ == '__main__':
    # init()
    app.run(threaded=True, port=5000)
