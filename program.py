import recomendaciones_coach

def seleccionar_jugada():
    print("\n--- REGISTRO DE NUEVA JUGADA ---")
    equipo = input("Ingresa las siglas del equipo rival de la NFL (Las opciones son: GB, KC, SF, DAL, BAL): ").upper().strip()
    print("Formaciones a elegir: 1. Escopeta  2. Pistola   3. I-Form   4- Singleback")
    formacion = int(input("Ingresa el número de la formación: "))
    down = int(input("Ingresa el número de down: "))
    yardas = int(input("Ingresa el yardaje por conseguir: "))
    print("¿La jugada fue un:  1.pase  o  2.acarreo?")
    jugada = int(input(""))
    return [equipo, formacion, down, yardas, jugada]

base_de_datos = []

archivo = open("Jugadas_Preseleccionadas.txt", "a+")
archivo.seek(0)
for linea in archivo:
    datos = linea.strip().split(",")
    if len(datos) == 5:
        base_de_datos.append([datos[0], int(datos[1]), int(datos[2]), int(datos[3]), int(datos[4])])
archivo.close()

while True:
    print("\n==================================================")
    print("Escribe 1 para ingresar informacion de nuevas jugadas.")
    print("Escribe 2 para ver jugadas previamente hechas, y revisar porcentajes.")
    print("Escribe 3 para salir del programa.")
    print("==================================================")
    res1 = int(input("Selecciona una opción: "))

    if res1 == 1:
        jugada_registrada = seleccionar_jugada()
        base_de_datos.append(jugada_registrada)
        
        archivo = open("Jugadas_Preseleccionadas.txt", "a")
        linea_guardar = jugada_registrada[0] + "," + str(jugada_registrada[1]) + "," + str(jugada_registrada[2]) + "," + str(jugada_registrada[3]) + "," + str(jugada_registrada[4]) + "\n"
        archivo.write(linea_guardar)
        archivo.close()
        
        print("¡Jugada registrada con éxito!")

    elif res1 == 2:
        print("\nCONSULTA DE TENDENCIAS OFENSIVAS")
        
        if len(base_de_datos) == 0:
            print("No hay jugadas registradas en el sistema aún.")
        else:
            equipo_buscar = input("Ingresa las siglas del equipo a analizar (ej. GB, KC, SF, DAL, BAL): ").upper().strip()
            print("Formaciones a consultar: 1. Escopeta  2. Pistola  3. I-Form  4. Singleback")
            formacion_buscar = int(input("Ingresa la formación que deseas analizar: "))
            down_buscar = int(input("Ingresa el down que deseas analizar (1-4): "))
            print("1. Corto yardaje: De 1 a 3 yardas. 2. Mediano metraje (Medium): De 4 a 6 yardas. 3.Largo metraje (Long): 7 yardas o más ")
            yardas_buscar = int(input("Ingresa el rango de yardas por conseguir: "))

            coincidencias = 0
            total_pases = 0
            total_carreras = 0
            
            for jugada in base_de_datos:
                equipo_actual = jugada[0]
                formacion_actual = jugada[1]
                down_actual = jugada[2]
                yardas_actuales = jugada[3]
                tipo_actual = jugada[4]

                if yardas_actuales <= 3:
                    rango_jugada = 1
                elif 4 <= yardas_actuales <= 6:
                    rango_jugada = 2
                else:
                    rango_jugada = 3

                if equipo_actual == equipo_buscar and formacion_actual == formacion_buscar and down_actual == down_buscar and rango_jugada == yardas_buscar:
                    coincidencias = coincidencias + 1
                    
                    if tipo_actual == 1:
                        total_pases = total_pases + 1
                    elif tipo_actual == 2:
                        total_carreras = total_carreras + 1

            if coincidencias > 0:
                nombre_equipo = recomendaciones_coach.obtener_nombre_equipo(equipo_buscar)
                porcentaje_pase = (total_pases / coincidencias) * 100
                porcentaje_carrera = (total_carreras / coincidencias) * 100
                recomendacion = recomendaciones_coach.sugerir_defensiva(porcentaje_pase, porcentaje_carrera, down_buscar, yardas_buscar)

                print("\n=== REPORTE DE SCOUTING:", nombre_equipo, "===")
                print("Jugadas analizadas:", coincidencias)
                print("Porcentaje de Pase:", porcentaje_pase, "%")
                print("Porcentaje de Carrera:", porcentaje_carrera, "%")
                print("LLAMADA DEL COORDINADOR DEFENSIVO:", recomendacion)
            else:
                print("No se encontraron jugadas registradas para", equipo_buscar, "con esos criterios.")

    elif res1 == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")