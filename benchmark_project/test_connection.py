import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1", port=5433,
        database="benchmark_db", user="postgres", password="benchmark"
    )
    cur = conn.cursor()
    cur.execute("SELECT version()")
    print("PostgreSQL connected:", cur.fetchone()[0])
    conn.close()
except Exception as e:
    print("PostgreSQL FAILED:", e)

try:
    import mysql.connector
    conn = mysql.connector.connect(
        host="127.0.0.1", port=3306,
        database="benchmark_db", user="root", password="benchmark"
    )
    cur = conn.cursor()
    cur.execute("SELECT version()")
    print("MySQL connected:", cur.fetchone()[0])
    conn.close()
except Exception as e:
    print("MySQL FAILED:", e)
