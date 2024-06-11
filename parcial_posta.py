from queue import Queue as Cola
#1
'''

#otra solucion usando bubble sort con recursion

def reordenar_lista(lista : list[tuple])->list[tuple]:
    for i in range(len(lista)-1):
        if lista[i][1] == 'comun' and lista[i+1][1] == 'vip':
            lista[i+1], lista[i] = lista[i], lista[i+1]
            reordenar_lista(lista)

    print(lista)


def reordenar_cola_priorizando_vips(fila_clientes: Cola)-> Cola:
    lista_temp : list[tuple]= [] 
    n_cola : Cola =  Cola()
    while not fila_clientes.empty():
        lista_temp.append(fila_clientes.get())

    reordenar_lista(lista_temp)

    for elem in lista_temp:
        n_cola.put(elem[0])

    return n_cola

'''

def reordenar_cola_priorizando_vips(fila_clientes: Cola)-> Cola:
    res: Cola = Cola()
    cola_vip: Cola = Cola()
    cola_comun: Cola = Cola()
    cliente: str = ""

    while not fila_clientes.empty():
        cliente = fila_clientes.get()
        if cliente[1] =='vip':
            cola_vip.put(cliente[0])
        elif cliente[1] == 'comun':
            cola_comun.put(cliente[0])

    while not cola_vip.empty():
        res.put(cola_vip.get())

    while not cola_comun.empty():
        res.put(cola_comun.get())

    return res

'''
clientes: Cola = Cola()


clientes.put(("d","comun"))
clientes.put(("a", "vip"))
clientes.put(("c","comun"))
clientes.put(("b", "vip"))
clientes.put(("f","vip"))
clientes.put(("g","comun"))

nueva_cola = reordenar_cola_priorizando_vips(clientes)

while not nueva_cola.empty():
    print(nueva_cola.get())
'''

#2

def torneo_de_gallinas(estrategias: dict)-> dict:
    partidos: list = []
    resultados: dict = {}

    for p1 in estrategias.keys():
        resultados[p1] = 0
        for p2  in estrategias.keys():
            if p1 != p2 and ((p1,p2) and (p2,p1) not in partidos):
                partidos.append((p1,p2)) 
    print("partidos: ", partidos)


    for jugador in partidos:
        if estrategias[jugador[0]] == "me la banco y no me desvio" and estrategias[jugador[1]] == "me la banco y no me desvio":
            resultados[jugador[0]] -= 5
            resultados[jugador[1]] -= 5

        elif estrategias[jugador[0]] == "me desvio siempre" and estrategias[jugador[1]] == "me desvio siempre":
            resultados[jugador[0]] -= 10
            resultados[jugador[1]] -= 10
        
        elif estrategias[jugador[0]] == "me la banco y no me desvio" and estrategias[jugador[1]] == "me desvio siempre":
            resultados[jugador[0]] += 10
            resultados[jugador[1]] -= 15

        else:
            resultados[jugador[0]] -= 15
            resultados[jugador[1]] += 10

    return resultados


        
 
estrategias = {"a": "me desvio siempre", "b": "me la banco y no me desvio", "c": "me desvio siempre", "d": "me la banco y no me desvio"}
resultados = torneo_de_gallinas(estrategias)
print(resultados)


#3 

def esta_incluido_estricto(conj: list, lista_grande: list)-> bool:
    res: bool = True
    for i in range(len(lista_grande)- len(conj)+1):
        res = True
        for j in range(len(conj)):
        
            if lista_grande[i+j] != conj[i]:
                res=False
                break
        
        if res:
            return True
    return False

def quien_gano_el_tateti_facilito(tablero : list[list[chr]])-> int:
    gano_x = False
    gano_o = False

    lista_columna_temp : list[chr] = []
    for k in range(len(tablero)):
        lista_columna_temp.clear()
        
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if j==k and len(lista_columna_temp) < len(tablero[i]):
                    lista_columna_temp.append(tablero[i][j])
       
        
        if esta_incluido_estricto(['X','X','X'], lista_columna_temp):
            
            gano_x = True
            
        elif esta_incluido_estricto(['O','O','O'], lista_columna_temp):
            gano_o = True
        
    if gano_x == True and gano_o == False:
        return 1
    elif gano_x == False and gano_o == True:
        return 2
    elif gano_x == True and gano_o == True:
        return 3
    else:
        return 0           
        
     



tablero = [
    ['','','','',''],
    ['','','X','O',''],
    ['','','X','O',''],
    ['','','X','O',''],
    ['','','','','']

]

print(quien_gano_el_tateti_facilito(tablero))

#4 

def es_palindromo(palabra : str) -> bool:
    palabra_invertida : str = ''

    for caracter in palabra:
        palabra_invertida = caracter + palabra_invertida

    if palabra == '':
        return False
    if palabra == palabra_invertida:
        return True
    
    else: 
        return False

def cuantos_sufijos_son_palindromos(texto: str)-> int:
    cont : int = 0
    suf_aux: str = ''
    if es_palindromo(texto):
        cont +=1

    for i in range(len(texto)):
        suf_aux = ''
        for j in range(i+1, len(texto)):
            suf_aux += texto[j]

        if es_palindromo(suf_aux): 
            cont += 1

    return cont

        


print(cuantos_sufijos_son_palindromos("papapapapa"))

    
