from flask import Flask
from flask import request
# from flask import render_template
from flask import jsonify
from json import dumps
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Setup db
project_directory = os.path.abspath(os.path.dirname(__file__))
database_file = 'sqlite:///' + os.path.join(project_directory, 'projectnotes.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['JSONIFY_MIMETYPE'] = 'application/json'

db = SQLAlchemy(app)
# ma = Marshmallow(app)

class Project(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    # client = db.Column(db.String(30), unique=True, nullable=False)
    # description = db.Column(db.String(200), unique=False, nullable=True)
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title

# @app.route("/", methods=["GET"])
# def get_index():
#     return "Hello world"

# Get projects
@app.route("/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    # print(json.dumps(projects))
    # print(jsonify({'projects': projects}))
    # return str(projects)
    # return jsonify({'projects': projects})
    projects = [str(i) for i in projects]
    print(projects)
    return jsonify({'projects': projects})

# Add project
@app.route("/projects", methods=["POST"])
def add_projects():
    data = request.get_json()
    title = data['title']
    project = Project(title)
    db.session.add(project)
    db.session.commit()
    return jsonify({"result": "Success", "title": title})

# Get project
@app.route("/projects/<id>", methods=["GET"])
def get_project(id):
    project = Project.query.get(id)
    return "View project"



# ma = Marshmallow(app)

# Models
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
# class UserSchema(ma.ModelSchema):
#     class Meta:
#         fields = ('username', 'email')
#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
#
#
# # Create new user
# @app.route("/user", methods=["POST"])
# def add_user():
#     username = request.get_json['username']
#     email = request.get_json['email']
#     new_user = User(username, email)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user)
#
#
# # Get all users
# @app.route("/user", methods=["GET"])
# def get_user():
#     all_users = User.query.all()
#     result = users_schema.dump(all_users)
#     return jsonify(result.data)
#
# # Get user by ID
# @app.route("/user/<id>", methods=["GET"])
# def user_detail(id):
#     user = User.query.get(id)
#     if user == None:
#         return "There is no user with that ID"
#     else:
#         return user_schema.jsonify(user)
#
# # Update user
# @app.route("/user/<id>", methods=["PUT"])
# def user_update(id):
#     user = User.query.get(id)
#     username = request.json['username']
#     email = request.json['email']
#     user.email = email
#     user.username = username
#     db.session.commit()
#
# # Delete user
# @app.route("/user/<id>", methods=["DELETE"])
# def user_delete(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()
#     return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
