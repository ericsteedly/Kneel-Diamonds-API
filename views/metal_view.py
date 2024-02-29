import sqlite3
import json

def update_metal(id, data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET 
                    metal = ?,
                    price = ?
            WHERE id = ?
            """, (data['metal'], data['price'], id)
        )   
        return True if db_cursor.rowcount > 0 else False