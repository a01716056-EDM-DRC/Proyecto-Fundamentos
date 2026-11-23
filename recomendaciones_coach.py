def obtener_nombre_equipo(siglas):
    equipos = [
        ["GB", "Green Bay Packers"],
        ["KC", "Kansas City Chiefs"],
        ["SF", "San Francisco 49ers"],
        ["DAL", "Dallas Cowboys"],
        ["BAL", "Baltimore Ravens"],
        ["PHI", "Philadelphia Eagles"],
    ]
    for equipo in equipos:
        if equipo[0] == siglas:
            return equipo[1]
    return siglas

def sugerir_defensiva(porcentaje_pase, porcentaje_carrera, down, yardas_rango):
    if down == 3 and yardas_rango == 3:
        return "Situación obvia de pase (3rd & Long): Mandar paquete Dime (6 DBs) con cobertura Cover 3 o Prevent."
    elif down >= 3 and yardas_rango == 1:
        return "Corto yardaje crítico: Mandar formación Goal Line o 4-4 cerrando los huecos interiores."
    elif porcentaje_pase >= 65:
        return "Tendencia fuerte al PASE: Mandar paquete Nickel (5 DBs) con Cover 2 Man y presionar al QB."
    elif porcentaje_carrera >= 65:
        return "Tendencia fuerte al ACARREO: Cerrar la caja con defensiva Base 4-3 / 3-4 y Blitz por el centro."
    else:
        return "Ofensiva balanceada: Mandar Cover 2 o Cover 3 estándar y leer las llaves de los Linebackers."