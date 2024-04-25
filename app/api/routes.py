from flask import Flask, request, Blueprint, jsonify, session
from models import db, User
from helpers import token_required

from flask import current_app as app


graf = Blueprint('graf', __name__,)

                                                                # set graph routes by color
                                                                # red

@graf.route("/red", methods = ["PUT"])
@token_required
def set_red_graph(current_user_token):

    token = current_user_token.token
    red = request.json["red"]
    
    user = User.query.filter_by(token = token).first()

    if red != "":
      user.red = red

    db.session.commit()

    return jsonify({
        "red": user.red,
    })

                                                                #blue

@graf.route("/blue", methods = ["PUT"])
@token_required
def set_blue_graph(current_user_token):

    token = current_user_token.token
    blue = request.json["blue"]
    
    user = User.query.filter_by(token = token).first()

    if blue != "":
        user.blue = blue

    db.session.commit()

    return jsonify({
        "blue": user.blue
    })

                                                                #green

@graf.route("/green", methods = ["PUT"])
@token_required
def set_green_graph(current_user_token):

    token = current_user_token.token
    blue = request.json["green"]
    
    user = User.query.filter_by(token = token).first()

    if green != "":
        user.green = green

    db.session.commit()

    return jsonify({
        "green": user.green
    })

                                                                #yellow

@graf.route("/yellow", methods = ["PUT"])
@token_required
def set_yellow_graph(current_user_token):

    token = current_user_token.token
    blue = request.json["yellow"]
    
    user = User.query.filter_by(token = token).first()

    if yellow != "":
        user.yellow = yellow

    db.session.commit()

    return jsonify({
        "yellow": user.yellow
    })


                                                                # set API key route

@graf.route('/APIkey', methods = ["PUT"])
@token_required
def set_APIkey(current_user_token):

    token = current_user_token.token
    APIkey = request.json['API_key']
    
    user = User.query.filter_by(token = token).first()

    user.APIkey = APIkey

    db.session.commit()

    return jsonify({
        "APIkey": user.APIkey
    })


                                                                # set time zone
