from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from flask import jsonify
from .cook import *
from .crypto import encrypt, decrypt

SECRET_KEY = 'my_secret_key'

@app.before_request
def before_request():
    pass


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
  return render_template('index.html',
      title = 'Home')

@app.route('/givenext', methods = ['POST'])
def givenext():
    selected = request.form['selected']
    im1 = request.form['img1']
    im2 = request.form['img2']
    cooka = request.form['c']
    if (not cooka):
        cooka = generate_sequence()
        cooka = encrypt(SECRET_KEY, cooka)
    cooka = decrypt(SECRET_KEY, cooka)
    (im1, im2), cooka = get_next_images(cooka)
    cooka = encrypt(SECRET_KEY, cooka)
    return jsonify({ 
          'img1': im1,
          'img2': im2,
	  'c': cooka })

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
