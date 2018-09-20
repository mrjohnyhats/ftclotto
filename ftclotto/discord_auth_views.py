from flask import Flask
from flask import request, session, redirect, url_for, render_template
import requests
from requests_oauthlib import OAuth2Session
from ftclotto import app
from ftclotto.discord_api_handler import *


app.config['SECRET_KEY'] = CLIENT_SECRET


@app.route('/authorize')
def authorize():
	scope = request.args.get('scope', 'identify')
	discord = make_session(scope=scope)
	authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)
	session['oauth2_state'] = state

	return redirect(authorization_url)

@app.route('/callback')
def callback():
	discord = make_session(state=session.get('oauth2_state'))
	token = discord.fetch_token(
		TOKEN_URL,
		client_secret=CLIENT_SECRET,
		authorization_response=request.url
	)
	session['oauth2_token'] = token
	session['username'] = get_user_data()['username']

	return redirect(url_for('home'))
