from distutils.sysconfig import customize_compiler
import imp


import sqlite3

connection = sqlite3.connect('..\DB\settings.db')
cursor = connection.cursor()

def insert_data(user_name, token, sec_key, len):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT)""")
    connection.commit()
    data = [user_name, token, sec_key, len]
    cursor.execute(f"INSERT INTO setting VALUES(?,?,?,?);", data)
    connection.commit()
    cursor.close()

def checking_on_reg_return_token(user_name):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT)""")
    connection.commit()
    token = cursor.execute(f"SELECT token FROM setting WHERE name='{user_name}'")
    connection.commit()
    return token.fetchone()[0]

def checking_on_reg_return_sec_key(user_name):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT)""")
    connection.commit()
    sec_key = cursor.execute(f"SELECT sec_key FROM setting WHERE name='{user_name}'")
    connection.commit()
    return sec_key.fetchone()[0]

def return_info_about_name(user_name):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT);""")
    connection.commit()
    cursor.execute(f"SELECT name FROM setting WHERE name='{user_name}'")
    info = cursor.fetchone()
    return None if info is None else user_name

def update_data_in_db(new_token, new_sec_key, user_name):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT);""")
    connection.commit()
    cursor.execute(f"UPDATE setting SET token = '{new_token}' WHERE name='{user_name}'")
    connection.commit()
    cursor.execute(f"UPDATE setting SET sec_key = '{new_sec_key}' WHERE name='{user_name}'")
    connection.commit()
    cursor.close()

def update_lan_in_db(user_name, language):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT);""")
    connection.commit()
    cursor.execute(f"UPDATE setting SET langue = '{language}' WHERE name = '{user_name}'")
    connection.commit()


def select_langue(user_name):
    connection = sqlite3.connect('..\DB\settings.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting(
        name TEXT, token TEXT, sec_key TEXT, langue TEXT);""")
    connection.commit()
    langue = cursor.execute(f"SELECT langue FROM setting WHERE name='{user_name}'")
    return langue.fetchone()[0]
