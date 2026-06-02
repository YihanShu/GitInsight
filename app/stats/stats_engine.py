from db.models import get_conn


def get_module_stats():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT module, COUNT(*)
    FROM analyses
    GROUP BY module
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def get_risk_stats():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT risk, COUNT(*)
    FROM analyses
    GROUP BY risk
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows