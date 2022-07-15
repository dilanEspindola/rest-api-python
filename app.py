from flask import Flask, jsonify, request
from tasks import tasks

app = Flask(__name__)

# routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "hola"})


# get aLl tasks
@app.route("/tasks", methods=["GET"])
def getTasks():
    return jsonify({"tasks": tasks})


# get single task
@app.route("/tasks/<int:id>", methods=["GET"])
def getTask(id):
    task_found = [task for task in tasks if task["id"] == id]
    if len(task_found) == 0:
        return jsonify({"message": "task not found"})
    else:
        return jsonify(task_found)


# create new task
@app.route("/tasks", methods=["POST"])
def createTask():
    get_data = request.json
    new_task = {
        "id": get_data["id"],
        "name": get_data["name"],
        "description": get_data["description"],
    }
    tasks.append(new_task)
    return jsonify(new_task)


# update task
@app.route("/tasks/<int:id>", methods=["PUT"])
def updateProduct(id):
    get_task = [task for task in tasks if task["id"] == id]
    if len(get_task) > 0:
        get_task[0]["name"] = request.json["name"]
        get_task[0]["description"] = request.json["description"]
        return jsonify({"message": "task updated"})
    else:
        return jsonify({"message": "task not found"})


# delete task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def deleteTask(id):
    get_task = [task for task in tasks if task["id"] == id]
    if len(get_task) > 0:
        tasks.remove(get_task[0])
        return jsonify({"message": "task deleted"})
    else:
        return jsonify({"message": "task not found"})


# starting server
if __name__ == "__main__":
    app.run(debug=True, port=4000)
