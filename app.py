from flask import Flask
app = Flask(__name__)

app.config("DEBUG") = TRUE

@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello SFU World!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/int_test/<int:value>")
def int_type(value):
	print (value+1)
	return "correct"

@app.route("/float_test/<float:value>")
def float_type(value):
	print (value+1)
	return "correct"

@app.route("/path_test/<path:value>")
def path_type(value):
	print (value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "Francis":
		return "Hello, {}".format(name)
	else: 
		return "Not Found", 404

if __name__ == "__main__":
	app.run()