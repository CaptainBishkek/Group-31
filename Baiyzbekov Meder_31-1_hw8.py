import sqlite3

conn = sqlite3.connect(f'database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)''')

cursor.execute("INSERT INTO countries (title) VALUES (f'Kyrgyzstan')")
cursor.execute("INSERT INTO countries (title) VALUES (f'Germany')")
cursor.execute("INSERT INTO countries (title) VALUES (f'China')")

cursor.execute('''CREATE TABLE cities
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              area REAL DEFAULT 0,
              country_id INTEGER,
              FOREIGN KEY (country_id) REFERENCES countries (id))''')

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'BISHKEK', 1)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'TALAS', 1)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'ISSYK KOL', 2)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'CHUI', 2)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'NARYN', 2)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'OSH', 3)")

cursor.execute("INSERT INTO cities (title,country_id) VALUES (F'BATKEN', 3)")

cursor.execute(''' CREATE TABLE employees
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT NOT NULL ,
              last_name TEXT NOT NULL, 
              city_id INTEGER,
              FOREIGN KEY (city_id) REFERENCES cities (id))''')

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'MEDER', 'BAIYZBEKOV',1)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'BAKAI', 'TALASOV',1)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'LAO', 'KUN',2)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'KURSAN', 'ASANOV',2)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'VLADIMIR', 'PUTIN',2)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'HARLIE', 'QUEEN',3)")

cursor.execute("INSERT INTO employees (first_name, last_name, citi_id) VALUES (f'ALEXEY', 'SENSEY',3)")

conn.commit()
conn.close()

conn = sqlite3.connect(f'database.db')
cursor = conn.cursor()

cursor.execute(f'SELECT title FROM cities')
cities = cursor.fetchall()
print(f'you can export a list of employees by the selected city id '
      f'from the list of cities below, '
      f'to exit the program, enter 0:')
for city in cities:
      print(city[0])
city_id = int(input(f' Enter city id:     '))

cursor.execute('''SELECT employees.first_name,
               employees.last_name, countries.title, cities.title, cities.area
               FROM employees
               INNER JOIN  cities ON employees.city_id = cities.id
               INNER JOIN  countryes ON cities.country_id = countryes.id
               WHERE cities.id = ?''', (city_id,))

employees = cursor.fetchall()

for employee in employees:
      print(f'Name:', employee[0])
      print(f'Surname:', employee[1])
      print(f'Country:', employee[2])
      print(f'City:', employee[3])
      print(f'City square:', employee[4])
      print()

conn.close()