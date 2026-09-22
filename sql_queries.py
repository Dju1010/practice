import sqlite3

conn = sqlite3.connect("instance/notes.db")
cur = conn.cursor()

# вывести все заметки
print("все заметки:")
for row in cur.execute("SELECT id, title FROM note"):
    print(row)

# заметки с тегами через join
print("\nзаметки + теги:")
q = "SELECT note.title, tag.name FROM note JOIN tag ON tag.note_id = note.id"
for row in cur.execute(q):
    print(row)

# добавить
cur.execute("INSERT INTO note (title, body, created_at) VALUES (?, ?, datetime('now'))",
            ("Тест", "из SQL"))
conn.commit()
new_id = cur.lastrowid

# обновить
cur.execute("UPDATE note SET title = ? WHERE id = ?", ("Обновлено", new_id))
conn.commit()

# удалить
cur.execute("DELETE FROM note WHERE id = ?", (new_id,))
conn.commit()

# посчитать
cnt = cur.execute("SELECT COUNT(*) FROM note").fetchone()[0]
print("\nвсего заметок:", cnt)

conn.close()