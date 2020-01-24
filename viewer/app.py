import os
from datetime import datetime
from flask import (
    Flask, render_template, jsonify, request, abort,
    send_from_directory)
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_migrate import Migrate
from htmlmin.main import minify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, jwt_refresh_token_required, get_jwt_identity,
    get_jti, get_raw_jwt
)
from models import *
from serializer import *
from config import BaseConfig
from logger import Logger


app = Flask(__name__)
app.config.from_object(BaseConfig)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
cors = CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    msg = '*********** SOCKET CONNECTED ***********'
    emit('connect-test', msg)
    print(msg)


@socketio.on('disconnect')
def handle_disconnect():
    print('*********** SOCKET DISCONNECTED **********')


@socketio.on('sema')
def handle_sema(sema):
    with app.app_context():
        user_id = int(sema['user'])
        wave_file_id = int(sema['waveFile']) \
                if sema['waveFile'] is not None else -1

        sema = SemaStore.query.filter_by(user_id=user_id).first()
        if sema is None:
            sema = SemaStore(user_id, wave_file_id)
            db.session.add(sema)
        else:
             sema.wave_file_id = wave_file_id

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            abort(500)

        sema_store = SemaStore.query.all()
        ret = [sema.wave_file_id for sema in sema_store]
        emit('sema-broadcast', ret, broadcast=True)
        print('semaStore Broadcasting >>> ', ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
