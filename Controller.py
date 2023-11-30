from flask import url_for
from flask import Flask, request, jsonify
from flask import render_template
from markupsafe import escape
from model import Task
import requests
import traceback
import json
from model import Task

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_view():
    return render_template('create.html')


@app.route('/api/create', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('dueDate')
    completion_date = data.get('completionDate')
    status = data.get('status')
    print(title, description, due_date, completion_date, status)

    try:
        task = Task(title=title, description=description, due_date=due_date, completion_date=completion_date, status=status)
        task.save()
    except Exception as e:
        traceback_info = traceback.format_exc()
        print("Traceback:")
        print(traceback_info)

    return jsonify({'mensaje': 'Datos recibidos correctamente'})

@app.route('/api/pending', methods=['GET'])
def get_pending_tasks():
    pending_tasks = Task.filter_by_status(status='Pending')
    return render_template('pending.html', tasks=pending_tasks)

@app.route('/api/complete', methods=['POST'])
def update_status():
    data = request.get_json()
    taskId = data.get('taskId')
    
    if Task.update_status(id=taskId, new_status="Completed"):
        return jsonify({'mensaje': 'Tarea completada correctamente'})
    else:
        return jsonify({'mensaje': 'No se encontró la tarea'})


@app.route('/api/edit', methods=['GET'])
def get_tasks():
    tasks = Task.get_all_tasks()
    return render_template('edit.html', tasks=tasks)

@app.route('/api/update', methods=['POST'])
def update_task():
    data = request.get_json()
    taskId = data.get('id')
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('dueDate')
    completion_date = data.get('completionDate')
    status = data.get('status')
    try:
        task = Task.read_task(taskId)
        if task:
            task["title"] = title
            task["description"] = description
            task["due_date"] = due_date
            task["completion_date"] = completion_date
            task["status"] = status
            if Task.update(task):
                return jsonify({'mensaje': 'Tarea completada correctamente'})
            else:
                return jsonify({'mensaje': 'No se encontró la tarea'})
        else:
            return jsonify({'mensaje': 'No se encontró la tarea'})
    except Exception as e:
        traceback_info = traceback.format_exc()
        print("Traceback:")
        print(traceback_info)

@app.route('/api/list', methods=['GET'])
def get_tasks_filter():
    tasks = Task.get_all_tasks()
    return render_template('list.html', tasks=tasks)