from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


@app.route('/sam')
def sam():
    name = "Sam"

    return f"hello {name} how are you?"


if __name__ == '__main__':
    app.run(debug = True)
