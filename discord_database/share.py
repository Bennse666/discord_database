import json
from pip._internal import main as pip
try:
    from flask import Flask,jsonify,request
except:
    pip.main(['install', 'flask'])
try:
    from flask_httpauth import HTTPTokenAuth
except:
    pip.main(['install', ' Flask-HTTPAuth'])

class local:
    user={}
    filename=None
    app = Flask('app')
    auth = HTTPTokenAuth(scheme='Bearer')
    def add_user(username,password,access):
        local.user[username]={'password':password,'access':access}
    @auth.verify_token
    def verify_token(token):
        username,password=token.split(':')
        if username and password:
            if username in local.user:
                if password==local.user[username]['password']:
                    return local.user[username]['access']
        return 0

    @app.route("/load", methods=['POST'])
    @auth.login_required
    def load():
        if local.auth.current_user()<1:
            return {'error':'can not access'}
        with open(local.filename+'.discord_db')as f:
            try:
                return jsonify(json.load(f)['local'][request.json['server']][request.json['user']][request.json['key']])
            except Exception as error:
                return jsonify({"errror":str(error)})



    @app.route('/save', methods=['POST'])
    @auth.login_required
    def save():
        if local.auth.current_user()<2:
            return {'error':'can not access'}
        with open(local.filename+'.discord_db')as f:
            db=json.load(f)
        db['local'][request.json['server']][request.json['user']][request.json['key']]=request.json['item']
        with open(local.filename+'.discord_db','w')as f:
            json.dump(db,f)
        return db['local'][request.json['server']][request.json['user']][request.json['key']]
    @app.route('/new', methods=['POST'])
    @auth.login_required
    def new():
        if local.auth.current_user()<3:
            return {'error':'can not access'}
        with open(local.filename+'.discord_db')as f:
            db=json.load(f)
        try:
            db['local'][str(request.json['server'])][str(request.json['user'])]={}
        except KeyError:
            db['local'][str(request.json['server'])]={}
            db['local'][str(request.json['server'])][str(request.json['user'])]={}
        with open(local.filename+'.discord_db', 'w')as f:
            json.dump(db,f)

        return db['local'][str(request.json['server'])][str(request.json['user'])]

    def run():
        local.app.run(host='0.0.0.0', port=8888)



class globals:
    app = Flask('app')
    user={}
    filename=None
    auth = HTTPTokenAuth(scheme='Bearer')
    def add_user(username,password,access):
        globals.user[username]={'password':password,'access':access}
    @auth.verify_token
    def verify_token(token):
        username,password=token.split(':')
        if username and password:
            if username in globals.user:
                if password==globals.user[username]['password']:
                    return globals.user[username]['access']
        return 0


    @app.route("/load", methods=['POST'])
    @auth.login_required
    def load():
        if globals.auth.current_user()<1:
            return {'error':'can not access'}
        with open(globals.filename+'.discord_db')as f:
            try:
                return jsonify(json.load(f)['global'][request.json['user']][request.json['key']])
            except Exception as error:
                return jsonify({"errror":str(error)})

    @app.route('/new', methods=['POST'])
    @auth.login_required
    def new():
        if local.auth.current_user()<3:
            return {'error':'can not access'}
        with open(globals.filename+'.discord_db')as f:
            db=json.load(f)
        db['global'][str(request.json['user'])]={}
        with open(globals.filename+'.discord_db', 'w')as f:
            json.dump(db,f)
        return db['global'][str(request.json['user'])]


    @app.route('/save', methods=['POST'])
    @auth.login_required
    def save():
        if globals.auth.current_user()<2:
            return {'error':'can not access'}
        with open(globals.filename+'.discord_db')as f:
            db=json.load(f)
        db['global'][request.json['user']][request.json['key']]=request.json['item']
        with open(globals.filename+'.discord_db','w')as f:
            json.dump(db,f)
        return db['global'][request.json['user']][request.json['key']]
    def run():
        globals.app.run(host='0.0.0.0', port=8888)