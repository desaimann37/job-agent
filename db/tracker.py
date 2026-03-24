import sqlite_utils, datetime

DB_PATH = "jobs.db"

def init_db(path=DB_PATH):
    db = sqlite_utils.Database(path)
    if "applications" not in db.table_names():
        db["applications"].create({
            "id":               int,
            "url":              str,
            "company":          str,
            "role":             str,
            "location":         str,
            "tech_stack":       str,   # stored as comma-separated
            "fit_score":        float,
            "status":           str,   # draft / applied / interview / offer / rejected
            "tailored_resume":  str,
            "cover_letter":     str,
            "applied_at":       str,
            "follow_up_at":     str,
        }, pk="id")
    return db

def save_job(fields: dict, url: str, path=DB_PATH):
    db = init_db(path)
    db["applications"].insert({
        "url":         url,
        "company":     fields.get("company", ""),
        "role":        fields.get("role", ""),
        "location":    fields.get("location", ""),
        "tech_stack":  ", ".join(fields.get("tech_stack", [])),
        "status":      "draft",
        "applied_at":  datetime.date.today().isoformat(),
        "follow_up_at": (datetime.date.today() +
                         datetime.timedelta(days=7)).isoformat(),
    })
    print(f"Saved: {fields.get('role')} at {fields.get('company')}")