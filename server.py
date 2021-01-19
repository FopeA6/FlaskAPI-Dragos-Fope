from flask import Flask

server = Flask(__name__)

server.config["DEBUG"] = True


@server.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == "__main__":
    server.run(debug=True)