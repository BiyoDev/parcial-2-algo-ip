from queue import Queue as Cola

#1

def reordenar_cola_priorizando_vips(filaClientes: Cola[(str,str)]) -> Cola[(str)]:
    nueva_cola : Cola[str] = Cola()
   
    cola_vips : Cola[str] = Cola()
    cola_comunes: Cola[str] = Cola()

    filaClientes_copy = []

    while not filaClientes.empty():
        cli = filaClientes.get()
        filaClientes_copy.append(cli)


    for e in filaClientes_copy:
        filaClientes.put(e)


    for cliente in filaClientes_copy:
        if cliente[1] == 'vip':
            cola_vips.put(cliente[0])
        else:
            cola_comunes.put(cliente[0])

    while not cola_vips.empty():
        nueva_cola.put(cola_vips.get())
    
    while not cola_comunes.empty():
        nueva_cola.put(cola_comunes.get())

    return nueva_cola



    
                                                                    

cola_clientes = Cola()
cola_clientes.put(("a","comun"))
cola_clientes.put(("b","vip"))
cola_clientes.put(("c","comun"))


nueva_cola = reordenar_cola_priorizando_vips(cola_clientes)


while not cola_clientes.empty():
    print(cola_clientes.get())

while not nueva_cola.empty():
    print(nueva_cola.get())


#2 

def torneo_de_gallinas(estrategias: dict[(str,str)])-> dict[(str,int)]:
    nuevo_dict: dict[(str,int)]= {}

    
    
    for jugador1 in estrategias.keys():

        nuevo_dict[jugador1] = 0

        for jugador2 in estrategias.keys():

            if jugador1 != jugador2:
                if estrategias[jugador1] == "me la banco":
                    if estrategias[jugador2]== "me la banco":
                        nuevo_dict[jugador1] -= 5
                    else:
                        nuevo_dict[jugador1] += 10
                else:
                    if estrategias[jugador2] == "me la banco":
                        nuevo_dict[jugador1] -= 15
                    else:
                        nuevo_dict[jugador1] -= 10
    

    return nuevo_dict 

        

estrategias_dict = {"a": "me la banco", "b": "me desvio", "c": "me desvio","d": "me la banco"}

resultados = torneo_de_gallinas(estrategias_dict)

print(estrategias_dict)
print(resultados)


#3 

def esta_incluido_estricto(subconjunto: list, lista_grande: list) -> bool:
    lista_aux = []
    res = False
    for i in range(len(lista_grande)- len(subconjunto)+1):
        lista_aux.clear()
        for j in range(len(subconjunto)):
            if len(lista_aux) != subconjunto:
                lista_aux.append(lista_grande[i+j])
        if lista_aux == subconjunto:
            res = True 

    return res





def quien_gano_al_tateti_facilito(tablero: list[list[chr]]) -> int:

    gano_x = False
    gano_o = False
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    lista_columna_temp = []


    for fila in range(num_filas):
        lista_columna_temp.clear()
        for columna in range(num_columnas):
            if len(lista_columna_temp) != num_columnas:
                lista_columna_temp.append(tablero[columna][fila])
        
        if esta_incluido_estricto(['X','X','X'],lista_columna_temp) and esta_incluido_estricto(['O','O','O'], lista_columna_temp): 
            gano_x = True
            gano_o = True
        elif esta_incluido_estricto(['O','O','O'], lista_columna_temp):
            gano_o = True
        elif esta_incluido_estricto(['X','X','X'], lista_columna_temp):
            gano_x = True

    if gano_x and gano_o:
        return 3
    elif gano_x:
        return 1
    elif gano_o:
        return 2
    else:
        return 0       




tablero = [
    ['','','','','',''],
    ['','','X','O','',''],
    ['','','X','O','',''],
    ['','','X','','',''],
    ['','','','','',''],
    ['','','','','','']

]




res_tateti = quien_gano_al_tateti_facilito(tablero)
print(res_tateti)
print(tablero)

#4

def es_palindromo(palabra: str)-> bool:
    palabra_invertida = ''
    for i in range(len(palabra)-1,-1,-1):
        palabra_invertida += palabra[i]

    if palabra == '':
        return False
    if palabra == palabra_invertida:
        return True
    else: 
        return False
def cuantos_sufijos_son_palindromos(texto: str)-> int:
    suf_aux = ''
    cont = 0

    if es_palindromo(texto):
        cont += 1

    for i in range(len(texto)):
        suf_aux = ''
        for j in range(1+i, len(texto)):
            suf_aux += texto[j] 
       
        if es_palindromo(suf_aux):
            cont+=1

    return cont

texto = "acacaca"

print(cuantos_sufijos_son_palindromos(texto))
print(texto)


