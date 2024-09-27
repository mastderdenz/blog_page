from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from .email_password_validator import is_valid_email, is_valid_password
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash,check_password_hash

authentication = Blueprint("authentication", __name__)

@authentication.route("/login",  methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Successfully logged in!", category='success')
                login_user(user, remember = True)
                return redirect(url_for('ui.home'))
            else:
                flash("Password is incorrect.", category = 'error')
        else:
            flash("Email does not exist.", category = 'error')

    return render_template("login.html", user=current_user)

@authentication.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = str(request.form.get("password1"))
        password2 = str(request.form.get("password2"))

        existing_email = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        if existing_email:
            flash("Email is already in use.", category = 'error')
        elif existing_username:
            flash("Username is already in use.", category = 'error')
        elif password1 != password2:
            flash("Passwords do not match", category = 'error')
        elif is_valid_email(email) == False:
            flash("The email '{user_email}' is not valid.", category = 'error')
        elif len(username) < 2:
            flash("Username is too short", category = 'error')
        elif is_valid_password(password1) == False:
            flash("Password is invalid\n"
                   "At least one uppercase letter\n, One lowercase letter\n, One digit,\n One special character and Minimum length of 8 characters\n"
                  , category = 'error')
        else:
            new_user = User(email = email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            flash("User created!")
            return redirect(url_for('ui.home'))
        
    return render_template("sign_up.html", user=current_user)

@authentication.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("ui.home"))


