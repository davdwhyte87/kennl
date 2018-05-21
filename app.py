from flask import Flask
from extensions import login_manager
from extensions import db,migrate
from extensions import ma,cors
#blueprints

from blueprints.user import user
from blueprints.post import post

#app setup
app=Flask(__name__)

@app.route('/')
def hello():
	return "hello manns"

#app run
if __name__=='__main__':
    app.run()
