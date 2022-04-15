import json
import uuid

from flask import render_template, request, url_for, redirect, make_response, jsonify, flash

from app import app, db
from app.models import OTS

from datetime import datetime, date, timedelta

from sqlalchemy import delete


def create_id():
    uuidQuattro = uuid.uuid4()
    str_uuid = str(uuidQuattro)
    print("uuid de version 4:", uuidQuattro)
    print(type(str_uuid))
    return uuidQuattro  # handle the POST request


def is_valid(ots_id):
    currrent_time = datetime.utcnow()
    date_fin = OTS.query.get(ots_id).ots_date_fin
    if date_fin > currrent_time:
        return False
    else:
        return True


@app.route('/')
def home():
    ots_id = create_id()
    print(ots_id)
    return render_template("pages/home.html", ots_id=create_id())


@app.route("/create-secret", methods=['GET', 'POST'])
def create_secret():
    if request.method == 'POST':
        data = request.get_json()
        rep = make_response(jsonify(data), 200)
        lifetime = int(data['ots_lifetime'])
        print(datetime.utcnow())
        date_de_fin = datetime.utcnow() + timedelta(days=lifetime)
        new_ots = OTS(ots_id=data['ots_id'], ots_content=data['ots_content'], ots_key2=data['ots_key2'],
                      ots_date_fin=date_de_fin)
        db.session.add(new_ots)
        db.session.commit()
        return {"message": f"Your message is registrated!!"}


@app.route("/purge", methods=['GET'])
def purge():
    if request.method == 'GET':
        db.session.query(OTS).filter(OTS.ots_date_fin < date.today()).delete()
        db.session.commit()
        return {"message": f"Purging performed!"}


@app.route('/get_ots/<ots_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_ots(ots_id):
    if request.method == 'GET':
        return display_ots(ots_id=ots_id)


@app.route('/get_ots/display_ots', methods=['GET', 'POST'])
def display_ots(ots_id):
    ots_exists = bool(OTS.query.filter_by(ots_id=ots_id).first())
    if ots_exists:
        ots_to_display = OTS.query.get(ots_id)
        current_time = datetime.utcnow()
        date_fin = ots_to_display.ots_date_fin
        if date_fin >= current_time:
            return render_template("pages/display_ots.html", ots_id=str(ots_to_display.ots_id),
                                   ots_content=ots_to_display.ots_content, ots_key2=ots_to_display.ots_key2,
                                   ots_date_fin=ots_to_display.ots_date_fin)
        else:
            return render_template("pages/error.html")
    else:
        return render_template("pages/error.html")


@app.route('/delete_ots', methods=['POST'])
def delete_ots():
    if request.method == 'POST':
        data = request.get_json()
        ots_exists = bool(OTS.query.filter_by(ots_id=data['ots_id']).first())
        if ots_exists:
            db.session.query(OTS).filter(OTS.ots_id == data['ots_id']).delete()
            db.session.commit()
            return {"message": f"Your message is deleted!!"}
