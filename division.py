def division():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    # evita la división por cero
    if b != 0:
        # realiza la división
        print(f"Resultado = {a / b}")
    else:
        print("No se puede dividir entre cero.")

division()