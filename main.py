from flask import Flask, render_template ,jsonify
import pymysql

db = pymysql.connect(host="localhost", user="test123", password="test123", db="aiotdb")
cursor = db.cursor()

app = Flask(__name__, template_folder='template')


@app.route("/")
def index():
	sql = "SELECT * FROM `sensors`"

	cursor.execute(sql)
	data = cursor.fetchall()

	return render_template('index.html',data=data)

if __name__ == "__main__":
	app.run(debug=True)