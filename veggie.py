from flask import Flask, jsonify, request

app = Flask(__name__)

veggies = [
	{ 
	'Vegetable' :'carrot', 
	'Quantity':15
	},
{ 
	'Vegetable' : 'onion', 
	'Quantity': 17
	}
]


@app.route('/groceries', methods=['GET'])
def veg():
    return jsonify(veggies)

@app.route('/groceries/<name>', methods=['GET'])
def vegg(name):
    if request.method == 'GET':
        for veg in veggies:
            if name == veg['Vegetable']:
                return veg
        else:
            return "Vegetable not found"
   
@app.route('/groceries', methods=['POST'])
def veggie():
    if request.method == 'POST':
        dic = {}
        dic['Vegetable'] = request.json['Vegetable']
        dic['Quantity'] = request.json['Quantity']
        veggies.append(dic)
        return request.json


@app.route('/groceries/<name>', methods=['DELETE'])
def vegdel(name):
    if request.method == 'DELETE':
        count=1
        for veg in veggies:
            if name == veg['Vegetable']:
                count = count+1
                break
        veggies.pop(count)    
        return veg
    
