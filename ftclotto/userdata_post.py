from flask import request, session, redirect, render_template, Response
from ftclotto import app
import database_api
from flask import jsonify


@app.route('/userdata', methods=['POST'])
def serve_userdata():
	username = request.get_json()['username']
	
	if database_api.user_exists(username):
		return jsonify(database_api.get_user_dict(username))

	return Response(status=404)