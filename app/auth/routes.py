from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserSignupForm, LoginForm
from app.models import User, db
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST']) #signup
def signup():
    form = UserSignupForm()
    if request.method == "POST":
        if form.validate():

            username = form.username.data
            first = form.first.data
            last = form.last.data
            email = form.email.data
            password = form.password.data

            print(username, first, last, email, password)

            user = User(username, first, last, email, password)

            db.session.add(user)
            db.session.commit()
            # user.save_to_db()
            # return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])  #login
def login():
    print('text')
    form = LoginForm()
    if request.method =='POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            #Query user from db
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in', 'success')
                    login_user(user)
                else:
                    print('Invalid password')
            else:
                print('User does not exist')
            print(user)
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
