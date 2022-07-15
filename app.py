from flask import Flask, jsonify
from tasks import tasks

app = Flask(__name__)

# routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "hola"})


@app.route("/tasks", methods=["GET"])
def getTasks():
    return jsonify(tasks)


@app.route("/tasks/<int:id>", methods=["GET"])
def getTask(id):
    task_found = [task for task in tasks if task["id"] == id]
    if len(task_found) == 0:
        return jsonify({"message": "task not found"})
    else:
        return jsonify(task_found)


# starting server
if __name__ == "__main__":
    app.run(debug=True, port=4000)
