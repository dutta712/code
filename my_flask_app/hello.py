from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db =SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable= False)
    email = db.Column(db.String(120), nullable= False, unique = True)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact')
def conntact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
