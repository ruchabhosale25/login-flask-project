import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS login_db")

# Select database
cursor.execute("USE login_db")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
)
""")

# Insert sample user
query = """
INSERT INTO users (username, password)
VALUES (%s, %s)
"""

values = [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3"),
    ("user4", "pass4"),
    ("user5", "pass5"),
    ("user6", "pass6"),
    ("user7", "pass7"),
    ("user8", "pass8"),
    ("user9", "pass9"),
    ("user10", "pass10"),
    ("user11", "pass11"),
    ("user12", "pass12"),
    ("user13", "pass13"),
    ("user14", "pass14"),
    ("user15", "pass15"),
    ("user16", "pass16"),
    ("user17", "pass17"),
    ("user18", "pass18"),
    ("user19", "pass19"),
    ("user20", "pass20"),
    ("user21", "pass21"),
    ("user22", "pass22"),
    ("user23", "pass23"),
    ("user24", "pass24"),
    ("user25", "pass25"),
    ("user26", "pass26"),
    ("user27", "pass27"),
    ("user28", "pass28"),
    ("user29", "pass29"),
    ("user30", "pass30"),
    ("user31", "pass31"),
    ("user32", "pass32"),
    ("user33", "pass33"),
    ("user34", "pass34"),
    ("user35", "pass35"),
    ("user36", "pass36"),
    ("user37", "pass37"),
    ("user38", "pass38"),
    ("user39", "pass39"),
    ("user40", "pass40"),
    ("user41", "pass41"),
    ("user42", "pass42"),
    ("user43", "pass43"),
    ("user44", "pass44"),
    ("user45", "pass45"),
    ("user46", "pass46"),
    ("user47", "pass47"),
    ("user48", "pass48"),
    ("user49", "pass49"),
    ("user50", "pass50")
]

cursor.executemany(query, values)

# Save changes
conn.commit()

# Close connection
cursor.close()
conn.close()

print("Database and table created successfully")
