def division():
    valor1 = int(input("Escriba un primer número: "))
    valor2 = int(input("Escriba un segundo número: "))

    try:
        if valor2 == 0:
            raise ZeroDivisionError("Error: División por cero")
    
        resultado = valor1 // valor2
        answer = print(f'{valor1} // {valor2} = {resultado}')
        return answer

    except ZeroDivisionError as e:
        print(e)

division()