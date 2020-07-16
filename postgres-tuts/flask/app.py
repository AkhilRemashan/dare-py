from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')
#
@app.route('/multi-line')
def hello_world():
    return '''
        <h3>multiline index</h3>
        <p>ML lorem ipsum</p>
    '''
#
@app.route('/login/<string:username>')
def w_username(username):
    return 'welcome, ' + username
#
@app.route('/only-get', methods=['GET'])
def only_get():
    return 'only get'
#
@app.route('/only-post', methods=['POST'])
def only_post():
    return 'only post'


if __name__ == '__main__':
    app.run(debug=True)