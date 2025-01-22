from flask import Flask, render_template, request
from controller.GetPredictions import GetPredictions
from controller.LoadModel import LoadModel

app = Flask(__name__)

model = LoadModel('deployment\models\heart_attack_detection_model_99.3%.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        inputs = request.form.to_dict()
        prediction = GetPredictions(model, inputs)
        print(f"Prediction-------------------- = {prediction}")

        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)