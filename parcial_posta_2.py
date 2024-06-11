#1
def es_primo(num: int)-> bool:
    cont_div : int = 0
    for i in range(1,num+1):
        if num % i == 0:
            cont_div +=1

    if cont_div == 2:
        return True
    else: 
        return False


def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    nueva_lista: list[int] = []

    for elem in codigos_barra:
        if es_primo(elem%1000):
            nueva_lista.append(elem)

    return nueva_lista

cods = [12919,2342,23181,9234191]
print(filtrar_codigos_primos(cods))

#2
def minimo(s: list[int]) -> int:
    minimo: int  = s[0]
    for e in s:
        if e < minimo:
            minimo = e

    return minimo


def maximo(s: list[int]) -> int:
    maximo: int = s[0]
    for e in s:
        if e > maximo:
            maximo = e

    return maximo


def stock_productos(stock_cambios: list[(str, int)]) -> dict[(int, int)]:
    dict_cambios: dict = {}
    lista_temp_valores : list[int] = []

    for elem in stock_cambios:
        dict_cambios[elem[0]] = (0,0)

    for c in dict_cambios.keys():
        lista_temp_valores.clear()
        for producto in stock_cambios:
            
            if producto[0] == c:
                lista_temp_valores.append(producto[1])
         
        dict_cambios[c] = (minimo(lista_temp_valores),maximo(lista_temp_valores))

    return dict_cambios
        



stock_prods = [("comida para gatos", 12), ("comida para gatos", 30),("comida para perros", 15),("comida para perros", 40),("comida para gatos", 20)] 
print(stock_productos(stock_prods))


#3

def todos_elementos_iguales(s: list)-> bool:
    elemento = s[0]
    res: bool = True 
    for e in s:
        if elemento != e:
            res = False and res
        if elemento == e:
            res = True and res
    return res

def un_responsable_por_turno(grilla_horaria: list[list[str]])-> list[(bool,bool)]:
    lista_bools: list = []
    lista_temp_columna: list = []
    lista_temp_manana: list = []
    lista_temp_tarde: list = []
    num_filas = len(grilla_horaria) #8
    num_columnas = len(grilla_horaria[0]) #7

    for columna in range(num_columnas): 
        lista_temp_columna.clear()
        lista_temp_manana.clear()
        lista_temp_tarde.clear()
        for fila in range(num_filas):
        
               
            lista_temp_columna.append(grilla_horaria[fila][columna])
        
   
     
        for i in range((num_filas//2)):
            lista_temp_manana.append(lista_temp_columna[i])
        for i in range((num_filas//2), num_filas):
            lista_temp_tarde.append(lista_temp_columna[i])
        #print(lista_temp_manana)
        #print(lista_temp_tarde)
        lista_bools.append((todos_elementos_iguales(lista_temp_manana),todos_elementos_iguales(lista_temp_tarde)))
        
    

    return lista_bools




matriz_encargados =[
    ['a','b','d','a','b','d','b'],
    ['a','b','d','a','b','d','b'],
    ['a','a','d','a','c','d','c'],
    ['a','a','d','a','c','d','c'],

    ['b','c','c','b','c','c','a'],
    ['b','c','c','b','c','c','a'],
    ['b','c','a','b','c','a','d'],
    ['b','c','a','b','c','a','d']

] 

print(un_responsable_por_turno(matriz_encargados))

#4
def indice(e, s:list )-> int:
    for i in range(len(s)):
        if e == s[i]:
            return i



def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str])-> int:
    paciente_flag = tipos_pacientes_atendidos[0]
    cont_consecutivos: list[(int, int)] = []
    cont: int = 0
    lista_indices: list[int] = [0]

    



    for i in range(len(tipos_pacientes_atendidos)):
        
        if paciente_flag != tipos_pacientes_atendidos[i]:
            paciente_flag = tipos_pacientes_atendidos[i]
            
            cont_consecutivos.append(cont)
            cont=1
        else:
            cont +=1

    cont_consecutivos.append(cont)

    paciente_flag = tipos_pacientes_atendidos[0]

    for j in range(len(tipos_pacientes_atendidos)):

        if paciente_flag != tipos_pacientes_atendidos[j]:
            paciente_flag = tipos_pacientes_atendidos[j]
            lista_indices.append(j)

        
    
    return lista_indices[indice(maximo(cont_consecutivos), cont_consecutivos)]



sec = ["perro","gato","gato","gato","gato","perro","perro","gato","gato","gato","gato"]

print(subsecuencia_mas_larga(sec))

'''
def lista_de_secuencias(s: list)-> list:
    nueva_lista = []
    cont = 0
    elem = s[0]
    for i in range(len(s)):
        print(f"{elem}--------{s[i]}")
        if s[i] != elem:   
            nueva_lista.append(cont)
            cont = 0
            elem = s[i]            

        cont+=1



    return nueva_lista

#print(lista_de_secuencias([1,1,2,2,2,3,3,4,4,4,4]))
'''