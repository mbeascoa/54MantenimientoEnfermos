import sys
from datetime import date

def insertar():
    ideptno = int(input("Inserte el número del enfermo : "))
    inombre = input("Inserte el apellido del enfermo")
    idir = input("Inserte la dirección del enfermo")
    ifecnac= input("Inserte la fecha de nacimiento del enfermo")
    isex= input("Inserte el sexo del enfermo")
    inss = input("Inserte el Número de la Seguridad Social del enfermo")



    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        # DEPT_NO  DNOMBRE, LOC así se llaman las columnas de la tabla departamento.

        ConsultaAlta = ("INSERT INTO ENFERMO "
                        "(INSCRIPCION, APELLIDO, DIRECCION, FECHA_NAC, SEXO, NSS) "
                        "VALUES (:P1, :P2, :P3, to_date(:P4, 'dd-mm-yyyy'), :P5, :P6)")

        datosEnfermo = (ideptno, inombre, idir, ifecnac, isex, inss)
        cursor.execute(ConsultaAlta, datosEnfermo)
        connection.commit()

    except connection.Error as error:
        print("Error: ", error)

    connection.close()


#--------------------------------------------------------------


def salir():
    sys.exit()


#--------------------------------------------------------------


def consultar():
    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        consulta = ("SELECT * FROM ENFERMO" )
        cursor.execute(consulta)

        resultado = False
        for ideptno, inombre, idir, ifecnac, isex, inss in cursor:
            print("Número Inscripción Enfermo: ", ideptno)
            print("Nombre del Enfermo: ", inombre)
            print("Dirección donde se ubica : ", idir)
            print("Fecha de Nacimiento del enferno : ", ifecnac)
            print("Sexo del enfermo : ", isex)
            print("Número de la Seguridad Social del Enfermo: ", inss)
            resultado = True
        if resultado == False:
            print("Sin resultados")
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

#--------------------------------------------------------------

def borrar():
    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        ConsultaBaja = ("Delete from enfermo where nss=:param1")

        NumeroSS = input("Indiqueme el Número de la Seguridad Social para eliminar el enfermo:")

        cursor.execute(ConsultaBaja, (NumeroSS,))
        if cursor.rowcount > 0:
            print("Enfermo eliminado satisfactoriamente")
        else:
            print("Dato no encontrado")

        connection.commit()


    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()



def modificar():
    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        ConsultaModificacion = ("Update enfermo set direccion=:Param1 where nss=:Param2")


        NuevoDireccion = input("Nueva localización :")
        NumeroSS = input(" Número de la Seguridad Social para poder modificar la dirección de este enfermo :")

        cursor.execute(ConsultaModificacion, (NuevoDireccion, NumeroSS))
        if cursor.rowcount > 0:
            print("Registro modificado satisfactoriamente")
        else:
            print("Dato no encontrado")

        connection.commit()


    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()
#---------------------------------------------------------



quiereIntentarlo=True
letra="S"

while quiereIntentarlo :
    while letra== "S" or letra =="s" :
            print("Gracias por participar : ..... ")
            print( "1.- ALTA ENFERMO ")
            print("2 .- BAJA ENFERMO ")
            print("3 .- MODIFICAR DIRECCIÓN ENFERMO")
            print("4.- CONSULTAR ")
            print("5.- SALIR")
            print(" ---------------------------------- ")
            opcion = input("Introduzca la opción requerida :  \n")
            if opcion=="1":
                insertar()
            if opcion=="2":
                borrar()
            if opcion == "3":
                modificar()
            if opcion == "4":
                consultar()
            if opcion == "5":
                salir()
            print(" ----------------------------------------------")
            intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
            if intento=="S" or intento=="s" :
                quiereIntentarlo=True
            else:
                quiereIntentarlo=False



