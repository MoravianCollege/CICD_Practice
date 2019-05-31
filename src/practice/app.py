from flask import abort, Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
	return "Why hello there! I am a simple Flask server."

@app.route('/foo', methods = ['GET'])
def get_bar():
    bar = request.args.get('bar', None)
    if bar is None:
        abort(404)
    else:
        return "<html>" +  hello() + "<br/>bar is " + bar + "</html>"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
