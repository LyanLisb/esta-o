from flask import Flask
from config import config_all

app = Flask(__name__)

config_all(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
app.run(debug=True)
