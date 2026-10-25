from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/download')
def download():
    path = 'static/normal_view.jpg'
    return send_file(path, as_attachment=True)

@app.route('/download/image')
def download_image():
    path = 'static/normal_view.jpg'
    return send_file(path, as_attachment=True)

@app.route('/download/image2')
def download_image2():
    path = 'static/far_away.jpg'
    return send_file(path, as_attachment=True)

@app.route('/download/image3')
def download_image3():
    path = 'static/very_close_up.jpg'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)