from flask import Flask

# Tutorial from https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
