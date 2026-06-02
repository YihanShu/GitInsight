from .database import get_conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        commit_hash TEXT,
        module TEXT,
        summary TEXT,
        risk TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(commit_hash, module,summary, risk):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analyses (commit_hash, module,summary, risk)
    VALUES (?, ?, ?, ?)
    """, (commit_hash, module,summary, risk))

    conn.commit()
    conn.close()

def query_by_module(module):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT commit_hash, module, summary, risk
    FROM analyses
    WHERE module = ?
    ORDER BY id DESC
    """, (module,))

    rows = cursor.fetchall()
    conn.close()

    return rows