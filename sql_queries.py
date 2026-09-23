import psycopg2

conn = psycopg2.connect(host="localhost", port=5432, dbname="notes_db", user="postgres")
cur = conn.cursor()

cur.execute("SELECT id, title FROM note")
print("заметки:", cur.fetchall())

cur.execute("SELECT note.title, tag.name FROM note JOIN tag ON tag.note_id = note.id")
print("с тегами:", cur.fetchall())

cur.execute("INSERT INTO note (title, body, created_at) VALUES (%s, %s, NOW())",
            ("Тест", "из SQL"))
conn.commit()

cur.execute("SELECT id FROM note ORDER BY id DESC LIMIT 1")
nid = cur.fetchone()[0]

cur.execute("UPDATE note SET title = %s WHERE id = %s", ("Обновлено", nid))
conn.commit()

cur.execute("DELETE FROM note WHERE id = %s", (nid,))
conn.commit()

cur.execute("SELECT COUNT(*) FROM note")
print("всего:", cur.fetchone()[0])

conn.close()