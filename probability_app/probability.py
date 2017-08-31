def menu():
    print(" ========================")
    print("| *** Probability app ***|")
    print(" ========================")
    print("|       1. Start         |")
    print("|       2. About us      |")
    print("|       3. Exit          |")
    print(" ========================")

def start():
    sample = []
    promedio = 0.0


    # Se establece el total de datos y se agregan a una lista que se ordena de menor a mayor.
    n = int(input("Write the total of data: "))
    print("")
    for i in range(n):
        data = float(input("Write the numbers: "))
        print("")
        sample.append(data)
    sample.sort()

    # Calculamos el promedio y lo imprimimos.
    for j in sample:
        promedio += j
    promedio /= len(sample)
    print("El promedio es: " + str(promedio))

    # Calculamos la mediana y la imprimimos.
    if (len(sample) % 2 == 0):
        mediana = (sample[(n-1)/2] + sample[((n-1)/2)+1])/2
    else:
        mediana = sample[n/2]
    print("La mediana es: " + str(mediana))

# Definicion donde viene los datos del desarrollador.
def about():
    print("Developer: Fabian Camp Mussa\n")
    print("Git Hub: fcampm\n")
    print("Mail: fabian.camp@yahoo.com\n")

# Definicion main que corre todo el programa.
def main():
    while (True):
        menu()
        option = int(input("Select an option: "))
        if option == 1:
            start()
        elif option == 2:
            about()
        elif option == 3:
            print("Thanks for using the app")
            break
        else:
            print("Invalid option, try again")

main()
