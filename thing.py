from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model = LogisticRegression()
    model.fit(X_train, y_train)
    prediction = model.predict(data['X_test'])
    return jsonify({'prediction': prediction.tolist()})
if __name__ == '__main__':
    X_train = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y_train = [0, 1, 0]
    app.run(debug=True)
