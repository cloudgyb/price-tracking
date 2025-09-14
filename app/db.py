import pymysql

class MySQLDatabase:
    def __init__(self, host, user, password, db, port=3306):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def create(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, tuple(data.values()))
            self.conn.commit()
            return cursor.lastrowid

    def read(self, table, where=None, order_by=None, limit=None):
        sql = f"SELECT * FROM {table}"
        params = ()
        if where:
            keys = ' AND '.join([f"{k}=%s" for k in where])
            sql += f" WHERE {keys}"
            params = tuple(where.values())
        if order_by:
            sql += f" ORDER BY {order_by}"
        if limit:
            sql += f" LIMIT {limit}"
        with self.conn.cursor() as cursor:
            cursor.execute('SET time_zone="+08:00"')  # 设置时区为北京时间
            cursor.execute(sql, params)
            return cursor.fetchall()

    def update(self, table, data, where):
        set_clause = ', '.join([f"{k}=%s" for k in data])
        where_clause = ' AND '.join([f"{k}=%s" for k in where])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        params = tuple(data.values()) + tuple(where.values())
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            self.conn.commit()
            return cursor.rowcount

    def delete(self, table, where):
        where_clause = ' AND '.join([f"{k}=%s" for k in where])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, tuple(where.values()))
            self.conn.commit()
            return cursor.rowcount

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()