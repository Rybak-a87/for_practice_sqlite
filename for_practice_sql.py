import sqlite3 as sq


db = "temp_db/prac.db"
print("---------------------------------------------------------------------------")
print(f"Практика по SQL запросам с файлом <{db}>\n")
while True:
    with sq.connect(db) as con:
        cur = con.cursor()
        in_text = input("Введите SQL запрос:\n>>> ")
        if in_text.lower() in ("exit", "quit", "stop"):
            break

        try:
            cur.execute(in_text)
            if "select" in in_text.lower():
                for res in cur:
                    print(res)
        except Exception as exc:
            print(f"Что-то не так... << {exc} >>")

print("Практика закончена, до новых встречь...")
