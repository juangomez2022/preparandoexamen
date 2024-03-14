bandas=[]


opcion=233
while(opcion != 5):
    print("***FESTIVAL ALTAVOZ***")
    print("**********************")
    print("1.Resgistrar Banda")
    print("2.Ver el cartel del festival")
    print("3.Buscar Banda")
    print("4.Modificar Banda")
    print("5.finalizar")
    opcion=int(input("Digita una opcion: "))

    if opcion == 1:
        banda={}
        #se llena el objeto de banda
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=input("nombre: ")
        banda["genero"]=input("Genero ")
        banda["costo"]=int(input("Costo "))
        
        #como agrego un diccionario a una lista
        bandas.append(banda)


        
    elif opcion == 2:

        #Recorriendo una lista para imprimir sus elementos 
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")


    elif opcion ==3:

        #Buscando un elemento dentro de una lista
        bandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                print("oe la encontré")
            else:
                print("no lo encontraste")

    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("opcion invalida")



