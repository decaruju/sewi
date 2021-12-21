from dataclasses import dataclass
from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/public/<path:path>')
# def public():
#     return send_from_directory('js', path)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@dataclass
class Image:
    src: str

@app.route('/')
def index():
    return render_template('index.html', images=[Image('https://via.placeholder.com/500'),Image('https://via.placeholder.com/500'),])

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
