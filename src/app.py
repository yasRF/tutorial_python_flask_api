from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False } 
]

@app.route('/todos', methods=['GET'])
def get_todo():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)
   




@app.route('/todos/<int:index>', methods=['DELETE'])
def delete(index):
    todos.pop(index)
    return jsonify(todos)





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)