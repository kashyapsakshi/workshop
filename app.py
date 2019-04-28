from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:////site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20))
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
