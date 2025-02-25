"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
{}

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# VER TODOS LOS INTEGRANTES DE LA FAMILIA
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    
    return jsonify(members), 200


# VER UN SOLO INTEGRANTE POR EL ID
@app.route("/member/<int:id>",methods=['GET'])
def get_member(id):

    # try:
        member_needed=jackson_family.get_member(id)

    # if member_needed: 
        return jsonify(member_needed) ,200
    # else:
    #     return jsonify({"msg":"the member doesn't exist"}),404

    # except:
    #     return jsonify({"msg":"there was an error in the server"}),500


# CREAR INTEGRANTES DE LA FAMILIA
@app.route("/member",methods=['POST'])
def post_new_member():
    try:
        body = request.json
        new_member = jackson_family.add_member(body)
        return jsonify(new_member),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ELIMINAR UN INTEGRANTE DE LA FAMILIA POR ID
@app.route("/member/<int:id>",methods=["DELETE"])
def delete_member(id):
    try:
        members_list_updated = jackson_family.delete_member(id)
    # if (members_list_updated):
        return jsonify({"done":True}),200

    # else:
        return jsonify("the member does not exist!"), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
