from flask import Blueprint, jsonify, request

bp = Blueprint("products", __name__)

_products = {}

@bp.route("/products", methods=["GET"])
def list_products():
    return jsonify(list(_products.values())), 200

@bp.route("/products/<int:id>", methods=["GET"])
def read_product(id):
    return jsonify(_products.get(id, {})), 200

@bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    _products[id] = data
    return jsonify(_products[id]), 200

@bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    _products.pop(id, None)
    return "", 204
