print("""
Escriba un número para elegir su operación
1) Suma
2) Resta
3) Multiplicación
4) División
5) Potencia
6) Módulo
""")
selection = int(input("Operación: "))

if selection == 1:
    from suma import suma # type: ignore
elif selection == 2:
    from resta import resta # type: ignore
elif selection == 3:
    from mult import mult # type: ignore
elif selection == 4:
    from div import division # type: ignore
elif selection == 5:
    from potencia import potencia # type: ignore
elif selection == 6:
    from modulo import modulo # type: ignore
else:
    print("Opción no válida")