from flask import Flask, render_template

app = Flask(__name__)

properties = [
    {"id": 1, "title": "Apartamento céntrico", "price": 120000},
    {"id": 2, "title": "Casa con jardín", "price": 250000},
    {"id": 3, "title": "Loft moderno", "price": 175000},
]

@app.route("/")
def index():
    return render_template("index.html", properties=properties)

if __name__ == "__main__":
    app.run(debug=True)
