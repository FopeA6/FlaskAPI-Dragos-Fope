''' Computers controller '''
from werkzeug.exceptions import BadRequest

computers = [
    {'id': 1, 'brand': 'Dell', 'processor': 'Intel Core i5', 'RAM memory': '8GB', 'storage': '254GB'},
    {'id': 2, 'brand': 'Lenovo', 'processor': 'Intel Core i5', 'RAM memory': '8GB', 'storage': '512GB'},
    {'id': 3, 'brand': 'MacBook Air', 'processor': 'Intel Core i7', 'RAM memory': '8GB', 'storage': '1024GB'}
]

def index(req):
    return [c for c in computers], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_computer = req.get_json()
    new_computer['id'] = sorted([c['id'] for c in computers])[-1] + 1
    computers.append(new_computer)
    return new_computer, 201

def update(req, uid):
    computer = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        computer[key] = val
    return computer, 200

def destroy(req, uid):
    computer = find_by_uid(uid)
    computers.remove(computer)
    return computer, 204

def find_by_uid(uid):
    try:
        return next(computer for computer in computers if computer['id'] == uid)
    except:
        raise BadRequest(f"We don't have that computer with id {uid}!")