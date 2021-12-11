import io
tablero_inicial='\u265c\t\u265e\t\u265d\t\u265b\t\u265a\t\u265d\t\u265e\t\u265c\n\u265f\t\u265f\t\u265f\t\u265f\t\u265f\t\u265f\t\u265f\t\u265f\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\u2659\t\u2659\t\u2659\t\u2659\t\u2659\t\u2659\t\u2659\t\u2659\n\u2656\t\u2658\t\u2657\t\u2655\t\u2654\t\u2657\t\u2658\t\u2656'
tablero=[]
movimiento=0
nombreFichero=''

def inicializar_fichero():
    nombreFichero=input("introduzca un nombre para el fichero de movimientos: ")
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))
        f=io.open(nombreFichero, mode= "w", encoding="utf-8")
        f.write('movimiento '+ str(movimiento)+ '\n')
        for i in tablero:
            f.write('\t'.join(i)+'\n')
        f.close()  
    return nombreFichero  
    

def actualizar_fichero(nombre_fichero):
    f=io.open(nombre_fichero, mode="a", encoding="utf-8")
    f.write('movimiento '+ str(movimiento)+ '\n')
    for i in tablero:
        f.write('\t'.join(i)+'\n')
    f.close()  

nombreFichero=inicializar_fichero()
print()
print(tablero_inicial)
print()

while True:
    print('Menú')
    print('1-Hacer un movimiento ')
    print('2-Ver un movimiento ')
    print('3-Salir ')
    print()
    opcion=int(input('Elija una opción: '))
    
    if opcion==1:
        tablero_nuevo=''
        movimiento=movimiento+1
        while True:
            fila_origen=int(input('introduce la fila de la pieza a mover: '))
            if(fila_origen>=1 and fila_origen<=8):
                break
        while True:
            columna_origen=int(input('introduce la columna de la pieza a mover: '))
            if(columna_origen>=1 and columna_origen<=8):
                break
        while True:
            fila_destino=int(input('introduce la fila de destino de la pieza a mover: '))
            if(fila_destino>=1 and fila_destino<=8):
                break
        while True:
            columna_destino=int(input('introduce la columna de destino de la pieza a mover: '))
            if(columna_destino>=1 and columna_destino<=8):
                break
        
        tablero[fila_destino-1][columna_destino-1]=tablero[fila_origen-1][columna_origen-1]
        tablero[fila_origen-1][columna_origen-1]=''
    
        actualizar_fichero(nombreFichero)

        for i in tablero:
            tablero_nuevo=tablero_nuevo+ '\t'.join(i)+ '\n'

        print()
        print(tablero_nuevo)
        print()
