from flask import Flask,jsonify, request,  render_template
import pickle
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model/Model.pkl", "rb"))
sc = pickle.load(open('model/scaler.pkl','rb'))


def encode_input(input):
    target_input =[]
    for i in range(0,7):
        target_input.append(np.zeros(19))
        # target_input[i][0] =  ## Year input
        if i==0 :
            target_input[i][1] = 1
            target_input[i][5] = 1
        if i==1 :
            target_input[i][1] = 1
            target_input[i][4] = 1
        if i==2 :
            target_input[i][2] = 1
            target_input[i][5] = 1
        if i==3 :
            target_input[i][2] = 1
            target_input[i][4] = 1
        if i==4 :
            target_input[i][3] = 1
            target_input[i][5] = 1
        if i==5 :
            target_input[i][3] = 1
            target_input[i][6] = 1
        if i==6 :
            target_input[i][3] = 1
            target_input[i][4] = 1
        target_input[i][7 + pd.to_numeric(input[0])] = 1
        target_input[i][0] = input[1]
    print(np.array(target_input))
    target_input = sc.transform(np.array(target_input).reshape(7,19))
    return target_input


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])

def predict():
    input = [x for x in request.form.values()]
    print(input)
    inputs = encode_input(input)
    # final = np.array(input)
    # input = input.reshape(1,-1)
    value =0
    for input in inputs:
        prediction = model.predict(input.reshape(1,-1))
        print(prediction)
        value = value + prediction
    print(value)
#     prediction = int(prediction.Label[0])
    return render_template('home.html', prediction=value)


@app.route('/json', methods=['POST'])
def json():
    request_data = request.get_json()
    input=[request_data['month'], request_data['year']]
    # input[1] = request_data['year']
    # input[0] = request_data['month']
    inputs = encode_input(input)

    value =0
    print(input)
    for input in inputs:
        print(input)
        prediction = model.predict(input.reshape(1,-1))
        value = value + prediction
    print(value)
    return jsonify(
        prediction=value[0]
    )

if __name__ == '__main__':
    app.run(debug=True)