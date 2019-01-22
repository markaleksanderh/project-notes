# https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525

from flask import Flask

app = Flask(__name__)
app.debug = True


# Configs
# Modules
# Models
# Schema Objects
# Routes

@app.route('/')
def index():
    return '<p>Hello GraphQL</p>'

if __name__ == '__main__':
    app.run()
