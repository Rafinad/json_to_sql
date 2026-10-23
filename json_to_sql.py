# берем директорию до json например: ../data/json
# создаем директорию sql например: ../data/sql 
# директории пишем без слэша на конце!!!

import json
from pathlib import Path
import os
def json_to_sql(path_to_json, path_to_sql):
    # имя файла
    file_name = str(Path(path_to_sql).stem)
    # путь до папки
    direction_path = str(Path(path_to_sql).parent)
    # открываем json на чтение
    with open(path_to_json, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    # открывает sql на запись
    with open((direction_path + "/" + file_name + ".sql"), 'a', encoding='utf-8') as sql_file:
        string_for_paste = ""
        for items in json_data:
            string_for_paste = "INSERT INTO " + file_name +"("
            for key in items:
                string_for_paste += (key+",")
            string_for_paste = string_for_paste.removesuffix(",")
            string_for_paste += ") VALUES ("
            for value in items.values():
                if(type(value) is str):
                    string_for_paste += '\''+(str(value)) + '\'' + ","
                else:
                    string_for_paste += (str(value) + ",")
            string_for_paste = string_for_paste.removesuffix(",")
            string_for_paste += "); \n"
            sql_file.write(string_for_paste)
    return str(direction_path + "/" + file_name + ".sql")
# путь до json
path_to_json= input("Введите путь до json файла или папки с ними:")
path_to_sql= input("Введите путь до sql:")
if(os.path.isdir(path_to_json)):
    files = os.listdir(path_to_json)
    for item in files:
        json_to_sql((path_to_json +"/" + item), path_to_sql+"/"+(Path(item).stem))
    print("Путь до папки с sql: " + path_to_sql)
else:
    path_to_sql = json_to_sql(path_to_json,path_to_sql)   
    print("Путь до sql: " + path_to_sql)
