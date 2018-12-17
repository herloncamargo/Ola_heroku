from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Olá heroku, eu sou o Herlon."

if __name__ == "__main__":
    app.run(debug=True)