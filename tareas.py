def agregar_tarea(lista, tarea):
    lista.append(tarea)
    return lista

def listar_tareas(listar):
    tareas = []
    for i in listar:
        tareas.append(i)

def eliminar_tarea(lista, tarea):
    lista.remove(tarea)
    return lista