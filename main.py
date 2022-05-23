from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def test():
	return "Hello World!"

if __name__ == "__main__":
	app.run(debug=True)