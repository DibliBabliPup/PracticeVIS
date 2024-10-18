from flask import Flask, render_template, send_file
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_sound')
def play_sound():
    sounds = ['meow1.mp3', 'meow2.mp3', 'meow3.mp3', 'meow4.mp3']  
    sound = random.choice(sounds)
    return send_file(f'static/sounds/{sound}', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
