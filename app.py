from flask import Flask,jsonify, request,  render_template
import pickle
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model/Model.pkl", "rb"))
sc = pickle.load(open('model/scaler.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
