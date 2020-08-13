from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET'])
def index():
    return "this is api-gush"



if __name__ == '__main__':
    app.run(debug=True)


