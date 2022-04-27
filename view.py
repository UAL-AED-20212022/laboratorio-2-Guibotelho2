from controller import *

def main(): # Função main

    lista = linked_list()

    while True:
        try:
            command:list[str] = input().split()
        except EOFError:
            return

        if command[0] == 'RPI':
            RPI(command,lista)

        elif command[0] == 'RPF':
            RPF(command,lista)

        elif command[0] == 'RPDE':
            RPDE(command,lista)

        elif command[0] == 'RPAE':
            RPAE(command,lista)

        elif command[0] == 'RPII':
            RPII(command,lista)

        elif command[0] == 'VNE':
            VNE(command,lista)

        elif command[0] == 'VP':
            VP(command,lista)

        elif command[0] == 'EPE':
            EPE(command,lista)

        elif command[0] == 'EUE':
            EUE(command,lista)

        elif command[0] == 'EP':
            EP(command,lista)


### Registar país no inicio da lista  ###

def RPI(command:list,lista:list): # Função que vai dar print a lista de paises. Sendo o pais inserido o primeiro dessa lista
    if len(command) == 2:
        for a in inserir_no_inicio(lista,command[1]):
         print (a)

### Registar país no inicio da lista  ###


### Registar país no fim da lista #######

def RPF(command:list,lista:list): # Função que vai dar print a lista de paises. Sendo o pais inserido o último dessa lista
    if len(command) == 2:
        for a in inserir_no_final(lista,command[1]):
         print(a)

############ Registar país no fim da lista ################


### Registar país depois de outro elemento já registado ###

def RPDE(command:list,lista:list): # Função que vai dar print a lista de paises e colocar o primeiro inserido depois do segundo existente
    if len(command) == 3:
        for a in inserir_depois_do_elemento(lista,command[2],command[1]):
         print(a)
    
### Registar país depois de outro elemento já registado ###


### Registar país antes de outro elemento já registado ####

def RPAE(command:list,lista:list):# Função que vai dar print a lista de paises e colocar o primeiro inserido antes do segundo existente
    if len(command) == 3:
       for a in inserir_antes_do_item(lista,command[2],command[1]):
         print(a)

### Registar país antes de outro elemento já registado ###


########## Registar pais num determinado indice ##########

def RPII(command:list,lista:list): # Função que vai dar print à lista de paises e colocar o pais inserido na posição indicada
    if len(command) == 3:
        for a in inserir_no_indice(lista,command[2],command[1]):
         print(a)

### Registar país num determinado indice #####


### Verificar número de elementos da lista ###

def VNE(command:list,lista:list): # Função que vai retornar o numero de elementos na lista
    if len(command) == 1:
        verificar_numero_de_elementos(lista)
        print(f"O número de elementos são {len(numero_1(lista))}.")

def numero_1(lista:list):
    lista_1:list = []
    a = lista.start_node
    while True:
        lista_1.append(a.item)
        if a.ref is None:
            return lista_1
        a = a.ref

##### Verificar número de elementos da lista ####


### Verificar se um país se encontra na lista ###

def VP(command:list,lista:list): # Função que printa se o pais se encontrar na lista
    if len(command) == 2:
        valor:bool = verificar_se_pais_existe(lista,command[1])
        if valor == True:
            print(f"O país {command[1]} encontra-se na lista.")

        elif valor == False:
            print(f"O país {command[1]} não se encontra na lista.")

### Verificar se um país se encontra na lista ###


##### Eliminar o primeiro elemento da lista #####

def EPE(command:list,lista:list): # Função que irá printar se o elemento for eliminado da lista
    if len(command) == 1:
        nome = eliminar_primeiro_elemento(lista)
        print(f"O país {nome} foi eliminado da lista.")

### Eliminar o primeiro elemento da lista ###


#### Eliminar o último elemento da lista ####

def EUE(command:list,lista:list): # Função que irá printar se o ultimo elemento for eliminado da lista
    if len(command) == 1:
        nome = eliminar_ultimo_elemento(lista)
        print(f"O país {nome} foi eliminado da lista.")

#### Eliminar o último elemento da lista ####


### Eliminar um determinado país da lista ###

def EP(command:list,lista:list): # Função que irá printar se o elemento inserido for eliminado da lista
    if len(command) == 2:
        eliminar_um_determinado_elemento(lista,command[1])
        print(f"O país {command[1]} foi eliminado da lista.")

### Eliminar um determinado país da lista ###