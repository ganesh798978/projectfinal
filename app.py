import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3

import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime

warnings.filterwarnings('ignore')



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
#     int_features= [float(x) for x in request.form.values()]
#     print(int_features,len(int_features))
#     final4=[np.array(int_features)]
#     model = joblib.load('clf.joblib')
#     predict = model.predict(final4)
#     print(predict)

#     if predict==0:
#         output='The Patient is not diagnosis with Heart Disease!'
   
#     elif predict == 1:
#         output = 'The Patient is diagnosis with Heart Disease!'


#     return render_template('prediction.html', output=output)

@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load('model.sav')
    predict = model.predict(final4)
    print(predict)

    if predict==0:
        output='The Patient is not diagnosis with Heart Disease!'
   
    elif predict == 1:
        output = 'The Patient is diagnosis with Heart Disease!'


    return render_template('prediction.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)