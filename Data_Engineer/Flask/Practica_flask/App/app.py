from flask import Flask, request
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('model.pkl', 'rb'))

print(model)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>APP FLASK IRIS</h1>'

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return '<h1>APP FLASK IRIS</h1> \n <h2>Hola {}</h2>'.format(name)

@app.route('/predict', methods=['POST'])
def predict():
    a = float(request.args.get('petalo', None))
    b = float(request.args.get('sepalo', None))
    c = float(request.args.get('perro', None))
    d = float(request.args.get('gato', None))
    prediction = model.predict([[a,b,c,d]])
    return 'la predicción es {}'.format(prediction)










if __name__ == '__main__':
    app.run(debug=True)