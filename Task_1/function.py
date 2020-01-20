from Task_1.directories import directories
from Task_1.documents import documents

def people(user_input_people):
  for n in documents:
    if n["number"] == user_input_people:
      return (n['name'])
    else:
      return 'Такого документа нет!'

def delete_doc(number_of_doc):
  for doc in documents:
    if doc['number'] == number_of_doc:
      documents.remove(doc)
      remove_doc_from_shelf(number_of_doc)
      return documents, directories

def remove_doc_from_shelf(number_of_doc):
    for number_of_shelf, list_of_docs in directories.items():
        if number_of_doc in list_of_docs:
            list_of_docs.remove(number_of_doc)


def show_docs():
  for list_docs in documents:
    x = list_docs['type']
    y = list_docs['number']
    z = list_docs['name']
    print(x,y,z)



def shelf():
  user_input_shelf = input (str ('Введите номер документа: '))
  for list_dir, list_docs in directories.items ():
    for list_docs_val in list_docs:
      if user_input_shelf == list_docs_val:
        directories_1 =  (list_dir)
        return directories_1
  else:
    return('Такого документа нет')


def add_docs(user_input_number, user_input_type, user_input_directories):
  documents.append ({'type': user_input_type, 'number': user_input_number})
  if user_input_directories in directories.keys():
    directories[user_input_directories].append(user_input_number)
    return directories
  if user_input_directories not in directories.keys():
    directories[user_input_directories] = [user_input_number]
    return directories

def commands():
    user_input = input(str('\nВведите одну из комманд:'
                           ' \np – people – команда, которая спросит номер документа'
                           ' и выведет имя человека, которому он принадлежит;'
                           '\nl– list – команда, которая выведет список всех документов'
                           ' в формате passport "2207 876234" "Василий Гупкин";'
                           '\ns – shelf – команда, которая спросит номер документа'
                           ' и выведет номер полки, на которой он находится;'
                           '\na – add – команда, которая добавит новый документ в каталог'
                           ' и в перечень полок,'
                           ' спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.\n'))
    if user_input == 'p':
      print(people())
    elif user_input == 'l':
      show_docs()
    elif user_input == 's':
      print(shelf())
    elif user_input == 'a':
      print(add_docs(user_input_number=int(input()), user_input_type=input(), user_input_directories=int(input())))
    else:
      print('Такой команды нет!')

