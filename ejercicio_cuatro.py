 #EJERCICIO 4
for curso in range(1, 5):
    asistieron = 0
    faltaron = 0

    print("CURSO", curso)

    for estudiante in range(1, 7):
        asistencia = int(input(
            f"Estudiante {estudiante} (1 = asistió, 0 = faltó): "
        ))

        if asistencia == 1:
            asistieron = asistieron + 1
        else:
            faltaron = faltaron + 1

    print("Asistieron:", asistieron)
    print("Faltaron:", faltaron)
    print()
