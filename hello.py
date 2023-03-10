from flask import Flask, render_template, request	
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from scripts.emailing import mailing
from scripts.storing import store_form, get_data
import mysql.connector

app=Flask(__name__)
app.config['SECRET_KEY'] = "MY FIRST PROJECTS BY ME IN FLASK"

@app.route('/')
def index():
	#return '<h1> Hello</h1>'
	return render_template('index.html')

@app.route('/posting', methods=['GET','POST'])
def posting():
	if request.method=='POST':
		name=request.form.get('fname')
		email=request.form.get('email')
		msg=request.form.get('message')
		one=request.form.get('one')
		two=request.form.get('two')
		three=request.form.get('three')
		four=request.form.get('four')
		image=request.form.get('image')
		#mailing(name, email, msg,one,two,three,four)
		store_form(name,email,one,two,three,four)
		data=get_data()
		return render_template('posted.html', name=name, image=image) 
	return render_template('posting.html')

@app.route('/post')
def post():
	data=get_data()
	return render_template('post.html', data=data)