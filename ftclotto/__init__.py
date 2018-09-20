from flask import Flask
from flask import request, session, redirect, render_template
import requests
from requests_oauthlib import OAuth2Session
from ftclotto import discord_api_handler
import database_api


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	username = session['username']

	if not database_api.user_exists(username):
		database_api.add_user(username, 0)

	# adding username to template context
	@app.context_processor
	def user_adder():
		return database_api.get_user_dict(username)

	return render_template('home.html')


@app.route('/hi')
def hi():
    return '<img src="https://web.whatsapp.com/5c140479-7ae4-4c27-b907-bac61dca4f63">'

import ftclotto.discord_auth_views
import ftclotto.betting
import ftclotto.userdata_post
