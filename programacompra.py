from funcionesprogramacompra import mostrar_menu, listainformación, contaropcionproductoferta,inputinfoproduct, inputpruductosuper, inputprodinofert

programa_encendido = True

while programa_encendido:   
    opcion_elegida=mostrar_menu()


    if opcion_elegida == 1:
        listainformación()
    if opcion_elegida == 2:
        contaropcionproductoferta()
    if opcion_elegida == 3:
        inputinfoproduct()
    if opcion_elegida == 4:
        inputpruductosuper()
    if opcion_elegida == 5:
        inputprodinofert()
    if opcion_elegida == 6:
        programa_encendido = False
