import database

def create_student(data: dict):
    data["id"] = database.current_id

    database.db[database.current_id] = data
    database.current_id += 1

    return data

def get_all_students():
    return list(database.db.values())

def get_student(student_id: int):
    return database.db.get(student_id)

def update_student(student_id: int, data: dict):
    if student_id not in database.db:
        return None

    data["id"] = student_id
    database.db[student_id] = data
    return data

def delete_student(student_id: int):
    return database.db.pop(student_id, None)