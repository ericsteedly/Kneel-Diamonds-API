import sqlite3
import json


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    db_cursor.execute(
    """
    SELECT
        o.id,
        o.size_id,
        s.carets,
        s.price size_price,
        o.style_id,
        st.style,
        st.price style_price,
        o.metal_id,
        m.metal,
        m.price metal_price
    FROM Orders o
    JOIN Metals m ON m.id = o.metal_id
    JOIN Sizes s ON s.id = o.size_id
    JOIN Styles st ON st.id = o.style_id
    """
    )
    orders = []
    query_results = db_cursor.fetchall()
    for row in query_results:
        order = {
            'metal_id': row['metal_id'],
            'size_id': row['size_id'],
            'style_id': row['style_id']
        }
        order['metal'] = {
            'id': row['metal_id'],
            'metal': row['metal'],
            'price': row['metal_price']
        }
        order['size'] = {
            'id': row['size_id'],
            'carets': row['carets'],
            'price': row['size_price']
        }
        order['style'] = {
            'id': row['style_id'],
            'style': row['style'],
            'price': row['style_price']
        }
        orders.append(order)
    serialized_orders = json.dumps(orders)
    return serialized_orders
    
def get_single_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
        """
        SELECT *
        FROM Orders o
        WHERE
        o.id = ?
        """, (pk,)
        )
        query_results = db_cursor.fetchone()
        return json.dumps(dict(query_results))
    
def create_order(x):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """ 
            INSERT INTO Orders
            (metal_id, size_id, style_id)
            VALUES (?, ?, ?)
            """, (x['metal_id'], x['size_id'], x['style_id'])
        )
    
    return True if db_cursor.rowcount > 0 else False

def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Orders
            WHERE id = ?
            """, (pk,)
        )
    return True if db_cursor.rowcount > 0 else False
