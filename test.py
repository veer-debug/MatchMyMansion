from flask import Flask ,render_template
from flask_socketio import SocketIO,send


app=Flask(__name__)
app.config['SECRET']='secret!123'
socketio=SocketIO(app,cors_allowed_origin="*")

@socketio.on('message')
def handel_massege(message):
    print('Receiver message : ' +message)
    if message=='user_connected!':
        send(message,broadcast=True)



@app.rout('/')
def index():
    return render_template('test.html')