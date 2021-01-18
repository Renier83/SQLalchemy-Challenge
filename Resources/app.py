from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
          )


          
if __name__ == '__main__':
    app.run(debug=True, port=9000)
