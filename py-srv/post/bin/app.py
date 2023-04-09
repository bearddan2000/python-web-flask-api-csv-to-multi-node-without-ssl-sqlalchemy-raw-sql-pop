from flask import Flask, request

from node import Cluster

app = Flask(__name__)

es_node = Cluster()

@app.route('/')
def hello():
	return {"hello": "world"}

@app.route('/pop')
def get_all():
    return es_node.get_all()

@app.route('/pop/<pop_id>', methods=['GET', 'DELETE'])
def crud(pop_id):
    if request.method == 'GET':
        return es_node.filter_by(pop_id)
    
    return es_node.delete_by(pop_id)

@app.route('/pop/<pop_name>/<pop_color>', methods=['PUT'])
def insert_entry(pop_name, pop_color):
    return es_node.insert_entry(pop_name, pop_color)

@app.route('/pop/<pop_id>/<pop_name>/<pop_color>', methods=['POST'])
def update_entry(pop_id, pop_name, pop_color):
    return es_node.update_entry(pop_id, pop_name, pop_color)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
