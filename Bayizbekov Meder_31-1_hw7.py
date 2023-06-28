import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    try:
        sql = '''insert into products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''select * from products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_limit(conn):
    try:
        sql = '''select * from products where price <= 100 and quantity >= 5 '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_name(conn):
    try:
        sql = '''select * from products where product_title like '%жидкость%' '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(conn, product):
    try:
        sql = '''update products set quantity = ? where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product):
    try:
        sql = '''update products set price = ? where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

database = 'hw.db'

create_products_table_sql = ''' 
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price double(10, 2) not null default 0.0,
quantity integer not null default 0)
'''

connection = create_connection(database)
if connection is not None:
    print('Successfully Connected!')
    create_table(connection, create_products_table_sql)
    # insert_product(connection, ('Большая упаковка порошка April', 750.56, 2))
    # insert_product(connection, ('Шампунь против перхоти мужской', 160.89, 3))
    # insert_product(connection, ('Шампунь против перхоти женский', 250.54, 5))
    # insert_product(connection, ('Мыло жидкое персик', 120.12, 10))
    # insert_product(connection, ('Мыло жидкое ваниль', 150.35, 11))
    # insert_product(connection, ('Мыло жидкое апельсин', 160.52, 12))
    # insert_product(connection, ('Гель для мытья посуды GSuper class', 260.95, 3))
    # insert_product(connection, ('Гель для мытья посуды High class', 500.42, 5))
    # insert_product(connection, ('Гель для чистки утюга', 550.23, 6))
    # insert_product(connection, ('Порошок Тайд', 95.59, 7))
    # insert_product(connection, ('Порошок Миф', 99.65, 8))
    # insert_product(connection, ('Порошок Стандартный', 85.79, 13))
    # insert_product(connection, ('Жидкость для мытья посуды Алоэ', 188.93, 14))
    # insert_product(connection, ('Жидкость для мытья посуды Крапива', 350.63, 2))
    # insert_product(connection, ('Жидкость для мытья посуды Элита', 450.55, 1))
    # select_all_products(connection)
    # select_products_by_price_limit(connection)
    # select_products_by_name(connection)
    # update_product_quantity(connection, (55, 50))
    # update_product_price(connection, (600, 52))
    # delete_product(connection, (58))
    connection.close()