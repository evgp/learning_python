#!/usr/bin/python
# -*- coding: utf-8 -*-
# Запись значения по ключу

# > storage.py --key key_name --val value

# Получение значения по ключу

# > storage.py --key key_name

# with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
#     fh.write(json.dumps(data, enimsure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл

# #загрузить из json
# with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
#     data = json.load(fh) #загружаем из файла данные в словарь data

import os, argparse, json, tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
storage_data = {}

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Enter key of the data in your storage to display")
parser.add_argument("--val", help="Enter value for the key" )
args = parser.parse_args()

if (args.key is None) or ((args.val is None) and not os.path.isfile(os.path.join(tempfile.gettempdir(), 'storage.data'))):
        print(None)
        exit()
elif args.key and args.val:
    if os.path.isfile(os.path.join(tempfile.gettempdir(), 'storage.data')):
         with open(storage_path, 'r') as f:
             storage_data = json.load(f)    
    
    if args.key in storage_data:
        storage_data[args.key] = storage_data[args.key] + ", " + args.val
    else:
        storage_data.update({
            args.key: args.val
        }) 

    with open(storage_path, 'w') as f:
             f.write(json.dumps(storage_data))
elif args.key:
    with open(storage_path, 'r') as f:
        storage_data = json.load(f)
    if args.key in storage_data:
        print(storage_data[args.key])
    else:
        print(None)        
