from flask import request, session, redirect, render_template, Response
import database_api
import random
from ftclotto import discord_api_handler, app

random.seed(1)

@app.route('/bet', methods=['POST'])
def bet():
	username = request.get_json()['username']
	bet_amount = int(request.get_json()['betAmount'])

	if username == discord_api_handler.get_user_data()['username']:

		if not database_api.user_exists(username):
			database_api.add_user(username, 0)

		decision = random.choice([0, 1])
		
		if decision == 0:
			database_api.change_points(username, -bet_amount)
		else:
			database_api.change_points(username, bet_amount)

		return Response(status=200)