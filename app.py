from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/')
def base():
    return render_template('base.html', title='Base')


@app.route('/index')
def index():
    user = {'username': 'clyde'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
