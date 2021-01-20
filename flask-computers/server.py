from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import computers
from werkzeug import exceptions

server = Flask(__name__)
CORS(server)

@server.route('/')
def home():
    return "<h1>Computer Archive</h1><br><p>This site is a prototype API for archiving of computers in your company.</p>", 200

@server.route('/api/computers', methods=['GET', 'POST'])
def computers_handler():
    fns = {
        'GET': computers.index,
        'POST': computers.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@server.route('/api/computers/<int:computer_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_handler(computer_id):
    fns = {
        'GET': computers.show,
        'PATCH': computers.update,
        'PUT': computers.update,
        'DELETE': computers.destroy
    }
    resp, code = fns[request.method](request, computer_id)
    return jsonify(resp), code

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

if __name__ == "__main__":
    server.run(debug=True)
