from flask import Flask, request, Blueprint, jsonify, session
from models import db, User
from helpers import token_required

from flask import current_app as app


graf = Blueprint('graf', __name__,)

                                                                # set graph route

@graf.route("/create", methods = ["PUT"])
@token_required
def set_graph(current_user_token):

    token = current_user_token.token
    red = request.json["red"]
    blue = request.json["blue"]
    green = request.json["green"]
    yellow = request.json["yellow"]
    
    user = User.query.filter_by(token = token).first()

    if red != "":
        user.red = red

    if blue != "":
        user.blue = blue

    if green != "":
        user.green = green

    if yellow != "":
        user.yellow = yellow

    db.session.commit()

    return jsonify({
        "red": user.red,
        "blue": user.blue,
        "green": user.green,
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


@graf.route('/Timezone', methods = ["PUT"])
@token_required
def set_Timezone(current_user_token):

    token = current_user_token.token
    time_zone = request.json['time_zone']
    
    user = User.query.filter_by(token = token).first()

    user.time_zone = time_zone

    db.session.commit()

    return jsonify({
        "time_zone": user.time_zone
    })