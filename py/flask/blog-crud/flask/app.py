from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/a')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)



# posts = [
#     {
#         'title' : 'Post 1',
#         'content' : 'This is the content for post 1',
#         'author' : 'Akil'
#     },
#     {
#         'title' : 'Post 2',
#         'content' : 'This is the content for post 2'
#     },
#     {
#         'title' : 'Post 3',
#         'content' : 'This is the content for post 3',
#         'author' : 'Jane'
#     },
# ]

@app.route('/')
def index_page():
    return render_template('index.html')
#
@app.route('/posts', methods=['GET', 'POST']) 
def posts():
    if request.method == 'POST': 
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=posts)

@app.route('/posts/delete/<int:id>') 
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

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