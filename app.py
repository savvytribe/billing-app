# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route("/render_invoice", methods=["POST"])
def render_invoice():
    try:
        # Get JSON data from the POST request
        json_data = request.get_json()

        # Render HTML template and pass data to it
        return render_template("invoice_template.html", data=json_data)
    except Exception as e:
        # Error response
        return render_template("error.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
