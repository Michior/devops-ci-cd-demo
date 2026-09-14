from flask import Flask, jsonify, request

from app.pricing import calculate_total

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/price")
def price():
    unit_price = request.args.get("unit_price", type=float)
    quantity = request.args.get("quantity", type=int)

    if unit_price is None or quantity is None:
        return jsonify(error="unit_price and quantity are required"), 400

    try:
        total = calculate_total(unit_price, quantity)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400

    return jsonify(
        unit_price=unit_price,
        quantity=quantity,
        total=total,
    )
