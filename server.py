from flask import Flask, jsonify, request

api = Flask(__name__)

users = [] # memoria ram

# Conectar con DB
class User:
    users_regitered = []
    def __init__(self, name):
        self.name = name
        self.id = len(self.users_regitered) + 1

@api.route("/", methods=['GET'])
def hello_world():
    return jsonify({ "hello": "world 🌍"}), 200 # Exito

@api.route("/users", methods=["GET","POST"]) # endpoint
def handle_users():
    
    if request.method == 'GET': # acceder methods
        return jsonify(users), 200

    body = request.json
    name = body.get("name", None)
    
    if not name: # Validaciones
        return "Error: name is missing in body", 400

    new_user = User(name=name)

    try:
        users.append(new_user)

        return "User created succesfully", 201
    
    except Exception as e:
        return f"Something wrong happened. error {e}", 500







api.run(host='localhost', port=5000, debug=True)