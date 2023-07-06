from flask import Flask, request

app = Flask(__name__)

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}

# @app.get("/programming_languages")
def list_programming_languages():
    return {"programming_languages": list(in_memory_datastore.values())}

# @app.route("/programming_languages/<name>")
def get_programming_language(name):
    return in_memory_datastore[name]

def create_programming_language(lang):
    in_memory_datastore["name"] = lang["name"]
    in_memory_datastore[lang["name"]] = lang
    return lang


@app.route("/programming_languages", methods=["GET", "POST"])
def programming_languages_route():
    if request.method == "GET":
        return list_programming_languages()
    elif request.method == "POST":
        return create_programming_language(request.get_json(force=True))

def update_programming_language(name, language_attrib):
    updating_lang = in_memory_datastore[name]
    updating_lang.update(language_attrib)
    return updating_lang

def delete_programming_language(language_name):
    deleting_language = in_memory_datastore[language_name]
    del in_memory_datastore[language_name]
    return deleting_language 


@app.route("/programming_languages/<language_name>", methods=["GET", "PUT", "DELETE"])
def programming_language_route(language_name):
    if request.method == "GET":
        return get_programming_language(language_name)
    elif request.method == "PUT":
        return update_programming_language(language_name, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_programming_language(language_name)