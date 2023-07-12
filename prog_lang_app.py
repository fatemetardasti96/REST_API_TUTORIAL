import sqlite3

from flask import Flask, request

app = Flask(__name__)

def get_database_connection():
    connection = sqlite3.connect("database.db")
    return connection


def list_programming_languages():
    conn = get_database_connection()
    prog_langs = conn.execute("SELECT * FROM programming_languages").fetchall()
    conn.close()
    return prog_langs
    
    
@app.route("/programming_languages/<name>")
def get_programming_language(name):
    conn = get_database_connection()
    prog_lang = conn.execute(f"SELECT * FROM programming_languages WHERE language_name='{name}'").fetchall()
    conn.close()
    return prog_lang

def create_programming_language(lang):
    conn = get_database_connection()
    name = request.json["name"]
    year = request.json["publication_year"]
    contribution = request.json["contribution"]
    conn.execute('INSERT INTO programming_languages (language_name, publication_year, contribution) VALUES (?, ?, ?)',
                         (name, year, contribution))
    conn.commit()
    conn.close()
    return lang


@app.route("/programming_languages", methods=["GET", "POST"])
def programming_languages_route():
    if request.method == "GET":
        return list_programming_languages()
    elif request.method == "POST":
        return create_programming_language(request.get_json(force=True))

def update_programming_language(name, language_attrib):
    conn = get_database_connection()
    contribution = request.json["contribution"]
    sql = f'''
         UPDATE programming_languages SET  
         contribution = "{contribution}" 
         WHERE language_name = "{name}"
        '''
    conn.execute(sql)
    conn.commit()
    conn.close()
    return language_attrib

def delete_programming_language(language_name):
    sql = f'''
        DELETE FROM programming_languages 
        WHERE language_name="{language_name}"
        '''
    conn = get_database_connection()
    conn.execute(sql)
    conn.commit()
    conn.close()
    return language_name 


@app.route("/programming_languages/<language_name>", methods=["GET", "PUT", "DELETE"])
def programming_language_route(language_name):
    if request.method == "GET":
        return get_programming_language(language_name)
    elif request.method == "PUT":
        return update_programming_language(language_name, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_programming_language(language_name)