from flask import Flask

app = Flask(__name__)
#HOST='0.0.0.0'
#PORT=3200

from Connect import view

if __name__ == "__main__":
    app.run()