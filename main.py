from fastapi import FastAPI, HTTPException
from zk_handler import fetch_attendance_records
from db import get_db

app = FastAPI()

@app.post("/fetch-attendance")
async def fetch_attendance():
    try:
        records = fetch_attendance_records()
        db = get_db()
        cursor = db.cursor()
        inserted = 0
        for rec in records:
            cursor.execute(
                "INSERT IGNORE INTO giriscikis (kullanici_id, giris_zamani) VALUES (%s, %s)",
                (rec["user_id"], rec["timestamp"])
            )
            inserted += cursor.rowcount
        db.commit()
        return {"status": "success", "inserted": inserted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
