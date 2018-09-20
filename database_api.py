from tinydb import TinyDB, Query
from tinydb.operations import add, set

db = TinyDB('db.json')

def add_user(username, points):
	db.insert({
		'username': username,
		'points': points
	})

def user_exists(username):
	q = Query()
	if db.search(q.username == username) == []:
		return False

	return True

def change_points(username, points):
	q = Query()
	db.update(add('points', points), q.username == username)
	db.update(set('points', 0), q.points < 0)


def get_user_dict(username):
	q = Query()
	return db.search(q.username == username)[0]