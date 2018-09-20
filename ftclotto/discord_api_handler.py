from flask import request, session, redirect, url_for, render_template
import requests
from requests_oauthlib import OAuth2Session

CLIENT_ID = '484555073708621834'
CLIENT_SECRET = '0A-h7pN3oBVDE9V3Kivg460cKymNhQEr'
REDIRECT_URI = 'https://ec2-54-183-239-57.us-west-1.compute.amazonaws.com/callback'

API_ENDPOINT = 'https://discordapp.com/api/v6'
AUTHORIZATION_BASE_URL = API_ENDPOINT + '/oauth2/authorize'
TOKEN_URL = API_ENDPOINT + '/oauth2/token'


def token_updater(token):
	session['oauth2_token'] = token

def make_session(token=None, state=None, scope='identify'):
	return OAuth2Session(
		client_id=CLIENT_ID,
		token=token,
		state=state,
		scope=scope,
		redirect_uri=REDIRECT_URI,
		auto_refresh_kwargs={
			'client_id': CLIENT_ID,
			'client_secret': CLIENT_SECRET
		},
		auto_refresh_url=TOKEN_URL,
		token_updater=token_updater
	)

def get_user_data():
	discord = make_session(token=session.get('oauth2_token'))
	return discord.get(API_ENDPOINT+'/users/@me').json()
