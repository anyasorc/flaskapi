
from flask import Flask, request
app = Flask(__name__)
@app.route('/api/myapi', methods=['POST'])
def predict():
       # Get the JSON data from the request
       data = request.get_json(force=True)
       Amount = float(data['Amount'])
       AccountNumber = data['AccountNumber']
       # Assuming the machine learning model was named model
       # prediction = model.predict(np.array([[Amount]]))
       # output = prediction
       output = 1
       if output == 1:
            remark = "The transaction amount is suspicious"
       else:
           remark = "The transaction amount is not suspicious"
       rsp = {
            'Prediction': str(output),
            'AccountNumber': AccountNumber,
            'Amount': Amount,
            'remark': remark
       }
       return rsp
	
if __name__ == '__main__':
    # Run using Waitress for production
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)

