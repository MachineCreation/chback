from models import User, db, check_password_hash, generate_password_hash
from flask import Blueprint, request, jsonify
from helpers import token_required
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)

                                                                                # signup

@auth.route('/register', methods = ["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    user_name = request.json["user_name"]
    
    email_in_use = User.query.filter_by(email = email).first() is not None
    user_in_use = User.query.filter_by(user_name = user_name).first() is not None
    
    if (user_name or email or password) == '':
        return jsonify({"Error": "All fields must be filled"}), 411

    if email_in_use:
        return jsonify({"Error": "Email already in use"}), 409
    
    if user_in_use:
        return jsonify({"Error": "User Name already in use"}), 409
    
    hashed_password = generate_password_hash(password)
    new_user = User(email = email, user_name = user_name, password = hashed_password)
        
    db.session.add(new_user)
    db.session.commit()
        
    return jsonify({
        "id": new_user.id,
        "email": new_user.email,
        "user_name": new_user.user_name
    })

                                                                                #signin

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    
    try:
        if request.method == 'POST':
            user_name = request.json["user_name"]
            password = request.json["password"]

            logged_user = User.query.filter(User.user_name == user_name).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)

                return jsonify({
                    "token": logged_user.token
                })
            else:
                return jsonify({"Error": "Unauthorized, wrong user user_name or Password"}), 401
    except:
        raise Exception('Invalid Form Data: Please Check your Form')
    

                                                                #@me
    
@auth.route("/@me")
@token_required
def current_user(current_user_token):
    user_token = current_user_token.token
    

    user = User.query.filter_by(token = user_token).first()

    return jsonify({
          "token": user.token,
          "id": user.id,
          "email": user.email,
          "user_name": user.user_name,
          "APIkey": user.APIkey,
          "red": user.red,
          "blue": user.blue,
          "green": user.green,
          "yellow": user.yellow
    })

@auth.route('/delete', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token):
    user_token = current_user_token.token

    
    user = User.query.filter_by(token = user_token).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({ "user": "deleted"})

                                                                                #Logout

@auth.route('/logout')
def logout():
    logout_user()
    return jsonify({
        "message": "user logged out"
    })