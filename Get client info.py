import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode = 'r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.temp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode = 'w') as f:
        writer = csv.DictWriter(f, fieldnames = CLIENT_SCHEMA)
        writer.writerows(clients)

        #f.close
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)
    #f.close

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))
        #print('{}: {}'.format(idx, client['name']))
    

def update_client(client_id, update_client):
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id] = update_client
    else:
        print('Client is not in client\'s list')


def delete_client(client_id):

    global clients
    for idx, client in enumerate(clients):
        #Se realiza una comparacion del id para verificar si es existente
        if idx == client_id:
            #Se elimina el cliente seleccionado
            del clients[idx]
        else:
            print('Client is not in clients list')


def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welocome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))
    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':

    _initialize_clients_from_storage()
    #_initialize_clients_from_storage()

    _print_welocome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name' : _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position' : _get_client_field('position'),
        }
        #client_name = _get_client_name()
        create_client(client)
        list_clients()
    elif command == 'D':
        #El sig codigo manda a pedir que el usuario ingrese el nombre del cliente a eliminar
        client_id = int(_get_client_field('id'))
        #Mando el nombre del cliente a la funcion de Delete
        delete_client(client_id)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in the client\' list'.format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()