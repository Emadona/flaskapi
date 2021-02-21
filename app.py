from flask import Flask , jsonify , request
import json


app = Flask(__name__)

response = ''

@app.route('/name' , methods = ['GET' , 'POST'])
def nameroute():
    global response

    if (request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data['name']
        response = f'Hi {name} this is Python API'
        return ''
    else:
        return jsonify({'name' : response})


if (__name__) == ('__main__'):
    app.run()