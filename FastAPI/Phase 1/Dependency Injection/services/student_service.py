def create_student(db, data: dict):
    data["id"] = db["current_id"]
    db["database"][db["current_id"]] = data
    db["current_id"] += 1
    return data

def get_all_students(db):
    return list(db["database"].values())

def get_by_id(student_id: int, db):
    return db["database"].get(student_id)

def update_student(student_id: int, data: dict, db):
    if student_id not in db["database"]:
        return None

    data["id"] = student_id
    db["database"][student_id] = data
    return data

def delete_student(student_id: int, db):
    return db["database"].pop(student_id, None)