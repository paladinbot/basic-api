from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """ initial rote
    return Home for initialization
    """
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    """ 
    method to get uer name email and id
    return json file with this data
    """
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    """ method post to create a user
    return a json file with the user description"""
    data = request.get_json()

    return jsonify(data), 201
if __name__ == "__main__":
    app.run(debug=True)
