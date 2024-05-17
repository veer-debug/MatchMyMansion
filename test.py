from flask import Flask ,render_template,request,redirect
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import pickle
import numpy as np


app=Flask(__name__)

status=False


@app.route('/')
def login():
    return render_template('login.html')



@app.route('/c_login', methods=['POST','GET'])
def c_login():
    u_name=request.form['u_name']
    

    return u_name
    

app.run(debug=True)