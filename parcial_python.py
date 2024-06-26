from queue import Queue as Cola


#1
def alarma_epidemiologica (registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
  dict_enfermedades_alerta : dict[str,float] = {}
  cont_pacientes : int = 0
  proporcion_pacientes_por_enf_infec : float = 0

  for enfermedad in infecciosas:
    cont_pacientes = 0
    for reg in registros:
      if reg[1] == enfermedad:
        cont_pacientes +=1
    proporcion_pacientes_por_enf_infec = cont_pacientes/len(registros)
    if proporcion_pacientes_por_enf_infec >= umbral:
      dict_enfermedades_alerta[enfermedad] = proporcion_pacientes_por_enf_infec

  return dict_enfermedades_alerta


#2
def orden_de_atencion (urgentes: Cola[int], postrgables: Cola[int]) -> Cola[int]:
  nueva_cola : Cola[int] = Cola()
  lista_urgentes_aux : list[int] = []
  lista_postergables_aux : list[int] = []

  #clono las colas con listas auxiliares
  while not urgentes.empty():
    lista_urgentes_aux.append(urgentes.get())

  for paciente_urg in lista_urgentes_aux:
    urgentes.put(paciente_urg)

  while not postrgables.empty():
    lista_postergables_aux.append(postrgables.get())

  for paciente_post in lista_postergables_aux:
    postrgables.put(paciente_post)

  for i in range(len(lista_urgentes_aux)):
    nueva_cola.put(lista_urgentes_aux[i])
    nueva_cola.put(lista_postergables_aux[i])

  return nueva_cola


#3
def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
  lista_porcentajes : list[float] = []
  num_filas : int = len(camas_por_piso)
  num_columnas : int = len(camas_por_piso[0]) # o numero de camas
  proporcion_aux : float = 0
  contador_camas_ocupadas : int = 0

  for fila in range(num_filas):
    contador_camas_ocupadas = 0
    for columna in range(num_columnas):
      if camas_por_piso[fila][columna]: # ==True
        contador_camas_ocupadas += 1
    proporcion_aux =  contador_camas_ocupadas/num_columnas
    lista_porcentajes.append(proporcion_aux)

  return lista_porcentajes


#4
def maximo_lista_int(s: list[int])-> int:
  maximo : int = s[0]

  for num in s:
    if num > maximo:
      maximo = num

  return maximo

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
  lista_empleados_del_mes : list[int] = []
  dict_aux : dict[int, int] = {} #diccionario con el total de horas trabajadas por cada empleado
  lista_total_de_horas_trabajadas : list[int] = []

  for clave in horas.keys():
    dict_aux[clave] = 0
    for i in range(len(horas[clave])):
      dict_aux[clave] += horas[clave][i]

  for valores in dict_aux.values():
    lista_total_de_horas_trabajadas.append(valores)

  for clave in dict_aux.keys():
    if dict_aux[clave] == maximo_lista_int(lista_total_de_horas_trabajadas):
      lista_empleados_del_mes.append(clave)

  return lista_empleados_del_mes
