# app.py
from flask import Flask, render_template, request, jsonify, make_response
import json
import pdfkit

app = Flask(__name__)


@app.route("/render_invoice", methods=["POST"])
def render_invoice():
    try:
        # Get JSON data from the POST request
        json_data = request.get_json()

        # Render HTML template and pass data to it
        html = render_template("invoice_template.html", data=json_data)

        # Create a PDF file from the HTML content
        pdfkit.from_string(html, "invoice_template.pdf")

        # Return the PDF as a response
        response = make_response(open("invoice_template.pdf", "rb").read())
        response.headers["Content-Type"] = "application/pdf"
        response.headers[
            "Content-Disposition"
        ] = "inline; filename=invoice_template.pdf"

        return response

    except Exception as e:
        # Error response
        return render_template("error.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
