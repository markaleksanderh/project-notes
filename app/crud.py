from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Setup db
project_directory = os.path.abspath(os.path.dirname(__file__))
database_file = 'sqlite:///' + os.path.join(project_directory, 'projectnotes.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

class Project(db.Model):
    project_name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    def __init__(self, project_name):
        self.project_name = project_name

@app.route("/", methods=["GET"])
def home():
    # if request.form:
    #     print(request.form)
    return "Projects list"



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
#
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
#

if __name__ == '__main__':
    app.run(debug=True)
