from flask import Flask ,render_template,request,redirect
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import pickle
import numpy as np


from login import User_othintaction

t=User_othintaction()

print(t.login('sbs123','1234'))