from flask import Flask
from utils import get_current_time
from faker import Faker

app = Flask(__name__)
f = Faker()


@app.route('/')
@app.route('/index.html')
def hello():
    return f'<h1>Hello World!</h1><br>{get_current_time()}'


@app.route('/get_name')
def get_name():
    first_name = f.first_name()
    last_name = f.last_name()
    return f'Person: {first_name} {last_name}'


if __name__ == "__main__":
    app.run(debug=True, port=5050)
