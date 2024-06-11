from queue import LifoQueue as Pila

def encontar_en_una_lista(seq: list, lista: list) -> bool:
    
    for i in range(len(lista)-len(seq)+1):
        encontrado = True
        for j in range(len(seq)):
           
            if lista[i+j] != seq[j]:
                encontrado = False
                
                break
        if encontrado:
        
            return True
        
    return False



#print(encontar_en_una_lista([3,4],[1,2,3,4,5]))

#print(encontar_en_una_lista("ol","hola"))


def transponer_matriz(matriz: list[list])-> list[list]:
    matriz_transpuesta : list[list]= []
    lista_temp_col : list = []
    num_filas: int = len(matriz)
    num_columnas: int = len(matriz[0])

    for col in range(num_columnas):
        lista_temp_col = []
        for fila in range(num_filas):
            lista_temp_col.append(matriz[fila][col])
           
        matriz_transpuesta.append(lista_temp_col)
                

    return matriz_transpuesta
'''

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
print(transponer_matriz(m))
'''

def dar_vuelta_lista(lista: list)-> list:
    nueva_lista : list = []
    for i in range(len(lista)-1,-1,-1):
        nueva_lista.append(lista[i])


    return nueva_lista


def dar_vuelta_lista_con_pila(lista: list)-> list:
    pila : Pila = Pila()

    for elem in lista:
        pila.put(elem)

    lista.clear()

    while not pila.empty():
        lista.append(pila.get())

  




def dar_vuelta_string(palabra)-> str:
    nueva_palabra : str = ''
    for c in palabra:
        nueva_palabra = c + nueva_palabra

    return nueva_palabra

l = [1,2,3]

print(dar_vuelta_lista(l))

print(dar_vuelta_string("hodajde"))

l2 = [1,2,3,4,5]
dar_vuelta_lista_con_pila(l2)

print(l2)
