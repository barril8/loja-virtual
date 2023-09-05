from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    directory = request.form['directory']
    os.chdir(directory)
    files = os.listdir(directory)
    return render_template('results.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
