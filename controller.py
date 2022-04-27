from models.LinkedList import LinkedList


### Lista ###
def linked_list():
    a_list = LinkedList()
    return a_list

### Lista ###


###
def numero(lista:list):
    lista_1:list = []
    a = lista.start_node
    while True:
        lista_1.append(a.item)
        if a.ref is None:
            return lista_1
        a = a.ref
###


### Registar país no inicio da lista ###
def inserir_no_inicio(lista:list,pais): # Função que regista no inicio
    lista.insert_at_start(pais)
    return numero(lista)
        


### Registar país no fim da lista ###
def inserir_no_final(lista:list,pais): # Função que regista no final
    lista.insert_at_end(pais)
    return numero(lista)
### Registar país no fim da lista ###


### Registar país depois de outro elemento já registado ###
def inserir_depois_do_elemento(lista:list,pais_1,pais_2): # Função que regista depois do elemento
    lista.insert_after_item(pais_1,pais_2)
    return numero(lista)
### Registar país depois de outro elemento já registado ###


### Registar país antes de outro elemento já registado ###
def inserir_antes_do_item(lista:list,pais_1,pais_2): # Função que regista antes do elemento
    lista.insert_before_item(pais_1,pais_2)
    return numero(lista)
### Registar país antes de outro elemento já registado ###


### Registar pais num determinado indice ###
def inserir_no_indice(lista:list,indice,pais): # Função que regista na posição inserida
    lista.insert_at_index(int(indice),pais)
    return numero(lista)
### Registar pais num determinado indice ###


### Verificar número de elementos da lista ###
def verificar_numero_de_elementos(lista:list): # Função que verifica o numero de elementos
    lista.get_count()
    return numero(lista)
### Verificar número de elementos da lista ###


### Verificar se um país se encontra na lista ###
def verificar_se_pais_existe(lista:list,pais): # Função que verifica se o pais existe na lista
    valor = lista.search_item(pais)
    return valor
### Verificar se um país se encontra na lista ###


### Eliminar o primeiro elemento da lista ###
def eliminar_primeiro_elemento(lista:list): # Função que elimina o primeiro elemento
    nome =lista.start_node.item
    lista.delete_at_start()
    return nome
### Eliminar o primeiro elemento da lista ###


### Eliminar o último elemento da lista ###
def eliminar_ultimo_elemento(lista:list): # Função que elimina o último elemento
    nome = lista.get_last_node()
    lista.delete_at_end()
    return nome
### Eliminar o último elemento da lista ###


### Eliminar um determinado país da lista ###
def eliminar_um_determinado_elemento(lista:list,pais): # Função que elimina o elemento selecionado
    lista.delete_element_by_value(pais)
    return numero(lista)
### Eliminar um determinado país da lista ###