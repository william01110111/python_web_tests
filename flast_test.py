from flask import Flask, request
app = Flask(__name__)

@app.route("/pets", methods = ["GET", "POST"])
def hello():
	if (request.method=="GET"):
		return "get called"
	elif (request.method=="POST"):
		return "post called"
	else:
		return "unknown method called"

if __name__ == "__main__":
    app.run()
