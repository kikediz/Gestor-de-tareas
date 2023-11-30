import os
import json
import uuid
import traceback
from datetime import datetime

base_path = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_path + '/data/' 'task.json')

class Task(object):
    def __init__(self, title, description, due_date, completion_date, status):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completion_date = completion_date
        self.status = status

    @classmethod
    def from_dict(cls, id, title, description, due_date, completion_date, status):
        task = cls(title, description, due_date, completion_date, status)
        task.id = id
        return task

    
    def read_task(task_id):
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            for task in task_list:
                if task['id'] == task_id:
                    print("reda_task ",type(task))
                    return task
            return None

    @staticmethod
    def get_all_tasks():
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            return task_list

    @staticmethod
    def get_pending_tasks():
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            pending_tasks = []
            for task_data in task_list:
                if task_data['status'] == 'pending':
                    task = Task(
                        id=task_data['id'],
                        title=task_data['title'],
                        description=task_data['description'],
                        due_date=task_data['due_date'],
                        completion_date=task_data['completion_date'],
                        status=task_data['status']
                    )
                    pending_tasks.append(task)
            return pending_tasks

    
    def save(self):
        try:
            with open(data_file, "r") as f:
                data = json.load(f)
                task_list = data['task']
                task_list.append({
                    'id': self.id,
                    'title': self.title,
                    'description': self.description,
                    'due_date': self.due_date,
                    'completion_date': self.completion_date,
                    'status': self.status
                })
            with open(data_file, "w") as f:
                json.dump(data, f)
                
        except Exception as e:
            traceback_info = traceback.format_exc()
            print("Traceback:")
            print(traceback_info)

    def update(task):
        try:
            with open(data_file, "r") as f:
                data = json.load(f)
                task_list = data['task']
                for i, task_data in enumerate(task_list):
                    if task_data['id'] == task["id"]:
                        task_list[i] = {
                            'id': task["id"],
                            'title': task["title"],
                            'description': task["description"],
                            'due_date': task["due_date"],
                            'completion_date': task["completion_date"],
                            'status': task["status"]
                        }
                        break
                task_result = {"task": task_list}
            with open(data_file, "w") as f:
                json.dump(task_result, f)
            return True
        except Exception as e:
            traceback_info = traceback.format_exc()
            print("Traceback:")
            print(traceback_info)


    @staticmethod
    def delete(self):
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            for i, task_data in enumerate(task_list):
                if task_data['id'] == self.id:
                    del task_list[i]
                    break
        with open(data_file, "w") as f:
            json.dump(data, f)

    @staticmethod
    def filter_by_status(status):
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            filtered_tasks = []
            for task_data in task_list:
                if task_data['status'] == status:
                    filtered_tasks.append(task_data)
        return filtered_tasks


    def update_status(id, new_status):
        with open(data_file, "r") as f:
            data = json.load(f)
            task_list = data['task']
            for i, task_data in enumerate(task_list):
                if task_data['id'] == id:
                    task_list[i]['status'] = new_status
                    if new_status == "Completed":
                        now = datetime.now()
                        formatted_date = now.strftime("%Y-%m-%d")
                        task_list[i]['completion_date'] = formatted_date
                    break
        with open(data_file, "w") as f:
            json.dump(data, f)
        return True
