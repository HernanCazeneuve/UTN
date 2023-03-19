# Autores: Alejandro Decaroli, Hernán, Tiziana, Elias y Martin

'''
ARREGLOS:

1) hacer marquitos en los validados de productos etc hacen a la estetica ver espacios
3) en silos cuando muestra el silo maximo hace mucho espaciado
'''

# --------------------------------------------------------------------------------------------------------

# librerias

import datetime
from os import system
import os
import os.path
import pickle
from colorama import init, Fore, Back, Style

# --------------------------------------------------------------------------------------------------------

# clases


class registros():
    def __init__(self):
        self.cant = "0"
        self.cod_prod = "0"
        self.peso_neto = "0"
        self.neto_min = "0"
        self.patente = ""


class producto():
    def __init__(self):
        self.cod_prod = "0"
        self.nombre_pro = ""
        self.estado = "False"


class operaciones():
    def __init__(self):
        self.patente = ""
        self.cod_prod = "0"
        self.fecha_cupo = ""
        self.estado = ""
        self.bruto = "0"
        self.tara = "0"


class rubros():
    def __init__(self):
        self.cod_rub = "0"
        self.nombre = ""


class rubros_x_prod():
    def __init__(self):
        self.cod_rub = "0"
        self.cod_prod = "0"
        self.nombre = ""
        self.valor_min = "0"
        self.valor_max = "0"


class silos():
    def __init__(self):
        self.cod_silo = "0"
        self.nombre = ""
        self.cod_prod = "0"
        self.stock = "0"

# --------------------------------------------------------------------------------------------------------

# Funciones


def clean():
    system("cls")

# --------------------------------------------------------------------------------------------------------


def main_menu():

    clean()
    global cupos
    global productos
    init(autoreset=True)
    print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido al menu principal")
    print()
    init(autoreset=True)
    print("\t\t\t\t\t\t\t Menu")
    print("\t\t\t\t\t\t\t1_ADMININISTRACIONES")
    print("\t\t\t\t\t\t\t2_ENTREGA DE CUPOS")
    print("\t\t\t\t\t\t\t3_RECEPCION")
    print("\t\t\t\t\t\t\t4_REGISTRAR CALIDAD")
    print("\t\t\t\t\t\t\t5_REGISTRAR PESO BRUTO5")
    print("\t\t\t\t\t\t\t6_REGISTRAR DESCARGA")
    print("\t\t\t\t\t\t\t7_REGISTRAR TARA")
    print("\t\t\t\t\t\t\t8_REPORTES")
    print("\t\t\t\t\t\t\t9_LISTADOS DE SILOS Y RECHAZADOS")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\t0_fin del programa")
    print()
    print(Fore.RED+"\t\t\t\t\t\t\tElija una opcion en base a su numero" + Fore.RESET)
    print()

    op = input("\t\t\t\t\t\t\tIngrese el número de opcion: ")
    print()

    while op != "1" and op != "3" and op != "8" and op != "2" and op != "5" and op != "7" and op != "0" and op != "6" and op != "4" and op != "9":
        print()
        op = input(Fore.RED +
                   "\t\t\t\t\t\t\tError de tipeo, elija el número de la opcion que necesite: " + Fore.RESET)

    while op == "6":
        print()
        print(Fore.YELLOW+"\t\t\t\t\t\t\tPagina en construccion" + Fore.RESET)
        op = input("\t\t\t\t\t\t\tIngrese el número de opcion: ")

    return op

# --------------------------------------------------------------------------------------------------------


def admin():

    clean()
    init(autoreset=True)
    print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a administracion")
    print()
    print("\t\t\t\t\t\t\t\t Menu")
    print("\t\t\t\t\t\t\tA- TITULARES")
    print("\t\t\t\t\t\t\tB- PRODUCTOS")
    print("\t\t\t\t\t\t\tC- RUBROS")
    print("\t\t\t\t\t\t\tD- RUBROS x PRODUCTO")
    print("\t\t\t\t\t\t\tE- SILOS")
    print("\t\t\t\t\t\t\tF- SUCURSALES")
    print("\t\t\t\t\t\t\tG- PRODUCTO POR TITULAR")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\tV- VOLVER al MENU PRINCIPAL")
    print()

    op2 = input("\t\t\t\t\t\t\tIngrese la letra de la opcion: ").upper()

    while op2 != "A" and op2 != "B" and op2 != "C" and op2 != "D" and op2 != "E" and op2 != "F" and op2 != "G" and op2 != "V":
        op2 = input(Fore.RED +
                    "\t\t\t\t\t\t\tError de tipeo, ingrese la letra de la opcion: " + Fore.RESET).upper()

    while op2 == "A" or op2 == "F" or op2 == "G":
        print()
        print(Fore.YELLOW+"\t\t\t\t\t\t\tPagina en construccion" + Fore.RESET)
        op2 = input("\t\t\t\t\t\t\tIngrese la letra de la opcion: ").upper()

    return op2

# --------------------------------------------------------------------------------------------------------


def validar_silos(silo, prod, archivo_p, archivo_f):

    tam = os.path.getsize(archivo_f)
    archivo_p.seek(0)

    if archivo_p.tell() == tam:
        pickle.dump(silo, archivo_p)
        archivo_p.flush()
        print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {prod}")

    else:
        repetido = False

        while archivo_p.tell() < tam:
            puntero_actual = pickle.load(archivo_p)

            if puntero_actual.nombre == prod:
                alta = input(
                    f"\t\t\tEl silo {prod} ya se dio de alta previamente, presione cualquier tecla para continuar: ")
                repetido = True

        if repetido == False:
            pickle.dump(silo, archivo_p)
            archivo_p.flush()
            print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {prod}")

# --------------------------------------------------------------------------------------------------------


def validar_rub_x_prod(inst, rubxp, nr, np, arl, arf):

    tam = os.path.getsize(arf)
    arl.seek(0)

    if arl.tell() == tam:
        pickle.dump(inst, arl)
        arl.flush()
        print()
        print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {rubxp}")

    else:
        repetido = False

        while arl.tell() < tam:
            puntero_actual = pickle.load(arl)

            if puntero_actual.cod_rub == nr and puntero_actual.cod_prod == np:
                print()
                alta = input(
                    f"\t\t\tEl rubro por producto {rubxp} ya se dio de alta previamente, presione cualquier tecla para continuar: ")
                repetido = True

        if repetido == False:
            pickle.dump(inst, arl)
            arl.flush()
            print()
            print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {rubxp}")

# --------------------------------------------------------------------------------------------------------


def validar_rub(inst, name, arl, arf):

    tam = os.path.getsize(arf)
    arl.seek(0)

    if arl.tell() == tam:
        pickle.dump(inst, arl)
        arl.flush()
        print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {name}")

    else:
        repetido = False
        while arl.tell() < tam:
            puntero_actual = pickle.load(arl)

            if puntero_actual.nombre == name:
                alta = input(
                    f"\t\t\tEl rubro {name} ya se dio de alta previamente, presione cualquier tecla para continuar: ")
                repetido = True

        if repetido == False:
            pickle.dump(inst, arl)
            arl.flush()
            print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {name}")

# --------------------------------------------------------------------------------------------------------


def validar_prod(inst, name, arl, arf):

    tam = os.path.getsize(arf)
    arl.seek(0)
    validados = 0

    if arl.tell() == tam:
        pickle.dump(inst, arl)
        arl.flush()
        print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {name}")

    else:
        revali = False
        repetido = False
        valido = True

        while arl.tell() < tam:
            puntero_ant = arl.tell()
            puntero_actual = pickle.load(arl)

            if puntero_actual.nombre_prod == name.ljust(20) and puntero_actual.estado == "True".ljust(15):
                alta = input(
                    f"\t\t\t\tEl producto {name} ya se dio de alta previamente, presione cualquier tecla para continuar: ")
                repetido = True

            elif puntero_actual.nombre_prod == name.ljust(20) and puntero_actual.estado == "False".ljust(15):
                print()
                alta = input(
                    f"El producto {name} se encuentra en el archivo pero no esta dado de alta, vaya a 'Modificacion' para cambiar su estado.\n\t\t\t\t\t\t\tPresione cualquier tecla para continuar: ")
                print()
                revali = True
                puntero_definitivo = puntero_ant

        if repetido == False:
            arl.seek(0)

            while arl.tell() < tam:
                puntero_actual = pickle.load(arl)

                if puntero_actual.estado == "True".ljust(15):
                    validados = validados + 1

            if validados > 2:
                valido = False
                print()
                print(f"\t\t\t\t\t\t\tNo se pueden dar de alta mas de 3 productos con estado 'Valido',\n\t\t\t\t\t\t\tsi quiere agregar otro producto primero vaya a 'Baja' e invalide algun producto\n\t\t\t\t\t\t\thecho esto pruebe dar de alta nuevamente este producto")
                print()
                advertencia = input(
                    "Para continuar presione cualquier tecla: ")

        if repetido == False and valido == True:

            pickle.dump(inst, arl)
            arl.flush()
            print(f"\t\t\t\t\t\t\tUsted ha dado de alta: {name}")

# --------------------------------------------------------------------------------------------------------


def alta():

    global producto
    inicio = 1

    while inicio == 1:

        clean()
        print()
        print(Fore.YELLOW+"\t\t\tIngrese que producto que desea agregar, puede ser de la siguiente lista o uno nuevo que no este en la lista:" + Fore.RESET)
        print()
        print(" \t\t\t\t\t\t\t1 - Trigo\n\t\t\t\t\t\t\t2 - Maiz\n\t\t\t\t\t\t\t3 - Soja\n\t\t\t\t\t\t\t4 - Girasol\n\t\t\t\t\t\t\t5 - Cebada")
        print()

        prod = input("\t\t\t\t\t\t\tEscriba el producto: ").capitalize()

        while prod[0] == "0" or prod[0] == "1" or prod[0] == "2" or prod[0] == "3" or prod[0] == "4" or prod[0] == "5" or prod[0] == "6" or prod[0] == "7" or prod[0] == "8" or prod[0] == "9":
            prod = input("Error de tipeo: ").capitalize()

        tamp = os.path.getsize(archivo_pro)

        instancia = prod
        instancia = producto()
        reintentar = True

        while reintentar == True:
            reintentar = False

            while True:
                try:
                    print()
                    instancia.cod_prod = int(
                        input("\t\t\t\t\t\t\tIngrese el codigo numerico de producto: "))
                    while instancia.cod_prod > 99 or instancia.cod_prod < 0:
                        print(
                            Fore.RED+"\t\t\t\t\t\t\tEl codigo debe estar entre 0 y 99" + Fore.RESET)
                        instancia.cod_prod = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo numerico de producto: "))
                    break
                except ValueError:
                    print()
                    print(
                        Fore.RED+"\t\t\t\t\t\t\tIngrese un numero, no letras o palabras" + Fore.RESET)

            archivo_prolo.seek(0)
            while archivo_prolo.tell() < tamp:
                puntero = pickle.load(archivo_prolo)

                if str(instancia.cod_prod).ljust(2) == puntero.cod_prod:
                    reintentar = True
                    print()
                    print(Fore.RED +
                          "\t\t\t\t\t\t\tEse codigo ya fue asignado a un producto, use otro" + Fore.RESET)

        instancia.cod_prod = str(instancia.cod_prod).ljust(2)
        instancia.nombre_prod = prod.ljust(20)
        instancia.estado = "True".ljust(15)

        validar_prod(instancia, prod, archivo_prolo, archivo_pro)

        pregunta = input(
            "\t\t\t\t\t\t\t¿Desea ingresar otro producto? SI/NO: ").upper()

        while pregunta != "SI" and pregunta != "NO":
            pregunta = input(Fore.RED +
                             "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()

        if pregunta == "NO":
            inicio = 0

# --------------------------------------------------------------------------------------------------------


def alta_rub():

    global rubros
    inicio = 1

    while inicio == 1:
        clean()
        print()
        print(Fore.YELLOW+"\t\t\tIngrese el rubro que desea agregar de la siguiente lista o agregue uno nuevo que no se encuentre en la lista:" + Fore.RESET)
        print()
        print("\t\t\t\t\t\t\t1 - Humedad\n\t\t\t\t\t\t\t2 - Tamaño de grano\n\t\t\t\t\t\t\t3 - Deterioro\n\t\t\t\t\t\t\t4 - Impurezas\n\t\t\t\t\t\t\t5 - Semillas toxicas\n")
        print()

        rub = input(
            "\t\t\t\t\t\t\tEscriba el rubro a dar de alta: ").capitalize()

        while rub[0] == "0" or rub[0] == "1" or rub[0] == "2" or rub[0] == "3" or rub[0] == "4" or rub[0] == "5" or rub[0] == "6" or rub[0] == "7" or rub[0] == "8" or rub[0] == "9":
            rub = input("Error de tipeo: ")

        instancia = rub
        tamr = os.path.getsize(archivo_rub)
        instancia = rubros()
        instancia.nombre = rub.ljust(20)
        reintentar = True

        while reintentar == True:
            reintentar = False

            while True:
                try:
                    print()
                    instancia.cod_rub = int(
                        input("\t\t\t\t\t\t\tIngrese el codigo númerico de rubro: "))
                    while instancia.cod_rub > 99 or instancia.cod_rub <= 0:
                        print(Fore.RED +
                              "\t\t\t\t\t\t\tEl codigo de rubro debe estar entre 1 y 99" + Fore.RESET)
                        instancia.cod_rub = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo númerico de rubro: "))
                    break
                except ValueError:
                    print()
                    print(
                        Fore.RED+"\t\t\t\t\t\t\tIngrese un número, no letras o palabras" + Fore.RESET)

            archivo_rublo.seek(0)

            while archivo_rublo.tell() < tamr:
                puntero = pickle.load(archivo_rublo)

                if str(instancia.cod_rub).ljust(2) == puntero.cod_rub:
                    reintentar = True
                    print()
                    print(Fore.RED +
                          "\t\t\t\t\t\t\tEse codigo ya fue asignado a un rubro, use otro" + Fore.RESET)

        instancia.cod_rub = str(instancia.cod_rub).ljust(2)

        validar_rub(instancia, rub, archivo_rublo, archivo_rub)

        pregunta = input(
            "\t\t\t\t\t\t\t¿Desea ingresar otro rubro? SI/NO: ").upper()

        while pregunta != "SI" and pregunta != "NO":
            pregunta = input(Fore.RED +
                             "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()

        if pregunta == "NO":
            inicio = 0


# --------------------------------------------------------------------------------------------------------

def alta_rub_x_prod():

    clean()
    global rubros_x_prod

    tamp = os.path.getsize(archivo_pro)
    tamr = os.path.getsize(archivo_rub)

    if tamp == 0 or tamr == 0:
        print("\t\t\t\t\t\t\tNo se puede proseguir porque el archivo de productos o de rubros esta vacio.\n\t\t\t\t\t\t\tVerifique y regrese a esta opcion.")
        advertencia = input(Fore.WHITE+Back.BLUE +
                            "\t\t\t\t\t\t\tPresione cualquier tecla para continuar: " + Fore.RESET)

    else:
        inicio = 1

        while inicio == 1:
            clean()

            tamrxp = os.path.getsize(archivo_rxp)
            archivo_rxplo.seek(0)

            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tLista de rubros por producto:" + Fore.RESET)

            while archivo_rxplo.tell() < tamrxp:
                elemento = pickle.load(archivo_rxplo)

                print()
                print(
                    f"\t\t\t\t\t\t\tNombre: {elemento.nombre}\n\t\t\t\t\t\t\tCodigo de rubro: {elemento.cod_rub}\n\t\t\t\t\t\t\tCodigo de producto: {elemento.cod_prod}")
            print()

            rubxp = input(
                "\t\t\t\t\t\t\tEscriba el rubro por producto a dar de alta: ").capitalize()

            while rubxp[0] == "0" or rubxp[0] == "1" or rubxp[0] == "2" or rubxp[0] == "3" or rubxp[0] == "4" or rubxp[0] == "5" or rubxp[0] == "6" or rubxp[0] == "7" or rubxp[0] == "8" or rubxp[0] == "9":
                rubxp = input(
                    Fore.RED+"\t\t\t\t\t\t\tError de tipeo: " + Fore.RESET).capitalize()

            instancia = rubxp
            instancia = rubros_x_prod()
            archivo_prolo.seek(0)

            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tLista de productos:" + Fore.RESET)

            while archivo_prolo.tell() < tamp:
                elemento = pickle.load(archivo_prolo)
                print()
                print(
                    f"\t\t\t\t\t\t\tNombre: {elemento.nombre_prod}\n\t\t\t\t\t\t\tCodigo: {elemento.cod_prod}")

            flagp = False

            while flagp == False:

                print()
                print(
                    "\t\t\tIngrese el codigo, el programa le notificara si corresponde con algun codigo del archivo de productos")
                print()

                while True:
                    try:
                        instancia.cod_prod = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo de producto: "))
                        while instancia.cod_prod > 99 or instancia.cod_prod < 0:
                            print(Fore.RED +
                                  "\t\t\t\t\t\t\tEl codigo de producto debe estar entre 0 y 99" + Fore.RESET)
                            instancia.cod_prod = int(
                                input("\t\t\t\t\t\t\tIngrese el codigo de producto: "))
                        break
                    except ValueError:
                        print()
                        advertencia = input(Fore.RED +
                                            "\t\t\t\t\t\t\tError de tipeo pruebe nuevamente (presione enter)" + Fore.RESET)
                        print()

                archivo_prolo.seek(0)
                while archivo_prolo.tell() < tamp:
                    elemento = pickle.load(archivo_prolo)

                    if elemento.cod_prod == str(instancia.cod_prod).ljust(2):
                        print()
                        print("\t\t\t\t\t\t\t-----------------|")
                        print(Fore.GREEN +
                              "\t\t\t\t\t\t\t| Codigo correcto |" + Fore.RESET)
                        print("\t\t\t\t\t\t\t|-----------------|")
                        flagp = True

            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tLista de rubros:" + Fore.RESET)

            archivo_rublo.seek(0)

            while archivo_rublo.tell() < tamr:
                elemento = pickle.load(archivo_rublo)

                print()
                print(
                    f"\t\t\t\t\t\t\tNombre: {elemento.nombre}\n\t\t\t\t\t\t\tCodigo: {elemento.cod_rub}")

            flagr = False

            while flagr == False:

                print()
                print(
                    "Ingrese el codigo, el programa le notificara si corresponde con algun codigo del archivo de rubros")
                print()

                while True:
                    try:
                        instancia.cod_rub = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo de rubro: "))
                        while instancia.cod_rub > 99 or instancia.cod_rub <= 0:
                            print(Fore.RED +
                                  "\t\t\t\t\t\t\tEl codigo de rubro debe estar entre 1 y 99" + Fore.RESET)
                            instancia.cod_rub = int(
                                input("\t\t\t\t\t\t\tIngrese el codigo de rubro: "))
                        break
                    except ValueError:
                        advertencia = input(Fore.RED +
                                            "\t\t\t\t\t\t\tError de tipeo pruebe nuevamente (presione enter)" + Fore.RESET)

                archivo_rublo.seek(0)

                while archivo_rublo.tell() < tamr:
                    elemento = pickle.load(archivo_rublo)

                    if elemento.cod_rub == str(instancia.cod_rub).ljust(2):
                        print("\t\t\t\t\t\t\t|-----------------|")
                        print(Fore.GREEN +
                              "\t\t\t\t\t\t\t| Codigo correcto |" + Fore.RESET)
                        print("\t\t\t\t\t\t\t|-----------------|")
                        flagr = True

            instancia.nombre = rubxp.ljust(20)

            while True:
                try:
                    print()
                    instancia.valor_min = int(
                        input("\t\t\t\t\t\t\tIngrese el valor minimo aceptado: "))
                    while instancia.valor_min < 0 or instancia.valor_min > 99:
                        instancia.valor_min = int(
                            input("\t\t\t\t\t\t\tIngrese el valor entre 0 y 99: "))
                    instancia.valor_max = int(
                        input("\t\t\t\t\t\t\tIngrese el valor maximo aceptado: "))
                    while instancia.valor_max < 0 or instancia.valor_max > 99:
                        instancia.valor_max = int(
                            input("\t\t\t\t\t\t\tIngrese el valor entre 0 y 99: "))
                    while instancia.valor_max < instancia.valor_min:
                        instancia.valor_max = int(
                            input("\t\t\t\t\t\t\tEl valor maximo debe ser superior al minimo: "))
                    break
                except ValueError:
                    advertencia = input(Fore.RED +
                                        "\t\t\t\t\t\t\tError de tipeado pruebe nuevamente (presione enter)" + Fore.RESET)
                    print()

            instancia.cod_rub = str(instancia.cod_rub).ljust(2)
            instancia.cod_prod = str(instancia.cod_prod).ljust(2)
            instancia.valor_min = str(instancia.valor_min).ljust(2)
            instancia.valor_max = str(instancia.valor_max).ljust(2)

            validar_rub_x_prod(instancia, rubxp, instancia.cod_rub,
                               instancia.cod_prod, archivo_rxplo, archivo_rxp)

            pregunta = input(
                "\t\t\t\t\t\t\t¿Desea ingresar otro rubro por producto? SI/NO: ").upper()

            while pregunta != "SI" and pregunta != "NO":
                pregunta = input(Fore.RED +
                                 "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()
            if pregunta == "NO":

                inicio = 0

# --------------------------------------------------------------------------------------------------------


def alta_silos():
    clean()

    global silos
    tamp = os.path.getsize(archivo_pro)
    inicio = 1

    if tamp == 0:
        print()
        print(
            "\t\t\t\t\t\t\tEl archivo de productos esta vacio cargue primero un producto y luego vuelva")
        advertencia = input(Fore.WHITE+Back.BLUE +
                            "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)
        inicio = 0

    else:
        while inicio == 1:

            clean()
            print()
            print("\t\t\t\t\t\t\tIngrese el silo que desea agregar")
            print()

            prod = input(
                "\t\t\t\t\t\t\tEscriba el nombre del silo a dar de alta: ").capitalize()

            while prod[0] == "0" or prod[0] == "1" or prod[0] == "2" or prod[0] == "3" or prod[0] == "4" or prod[0] == "5" or prod[0] == "6" or prod[0] == "7" or prod[0] == "8" or prod[0] == "9":
                prod = input(Fore.RED +
                             "\t\t\t\t\t\t\tError de tipeo, pruebe de nuevo: " + Fore.RESET).capitalize()

            silo = prod
            tams = os.path.getsize(archivo_silo)
            silo = silos()
            reintentar = True

            while reintentar == True:
                reintentar = False
                while True:
                    try:
                        print()
                        silo.cod_silo = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo númerico de silo: "))
                        while silo.cod_silo < 0 or silo.cod_silo > 99:
                            print()
                            print(Fore.RED +
                                  "\t\t\t\t\t\t\tEl codigo de silo solo puede estar entre 0 y 99" + Fore.RESET)
                            print()
                            silo.cod_silo = int(
                                input("\t\t\t\t\t\t\tIngrese el codigo númerico de silo: "))
                        break
                    except ValueError:
                        print()
                        print(
                            Fore.RED+"\t\t\t\t\t\t\tIngrese un número, no letras o palabras" + Fore.RESET)

                archivo_silolo.seek(0)
                while archivo_silolo.tell() < tams:
                    puntero = pickle.load(archivo_silolo)

                    if str(silo.cod_silo).ljust(2) == puntero.cod_silo:
                        reintentar = True
                        print()
                        print(Fore.RED +
                              "\t\t\t\t\t\t\tEse codigo ya fue asignado a un silo, use otro" + Fore.RESET)

            silo.nombre = prod.ljust(20)
            silo.stock = "0".ljust(10)
            archivo_prolo.seek(0)
            tamp = os.path.getsize(archivo_pro)

            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tLista de productos:" + Fore.RESET)

            while archivo_prolo.tell() < tamp:
                elemento = pickle.load(archivo_prolo)
                print()
                print(
                    f"\t\t\t\t\t\t\tNombre: {elemento.nombre_prod}\n\t\t\t\t\t\t\tCodigo: {elemento.cod_prod}")

            reintentar = True
            while reintentar == True:
                reintentar = False
                while True:
                    try:
                        print()
                        silo.cod_prod = int(
                            input("\t\t\t\t\t\t\tIngrese el codigo de producto: "))
                        while silo.cod_prod < 0 or silo.cod_prod > 99:
                            print()
                            print(Fore.RED +
                                  "\t\t\t\t\t\t\tEl codigo de producto debe estar entre 0 y 99" + Fore.RESET)
                            print()
                            silo.cod_prod = int(
                                input("\t\t\t\t\t\t\tIngrese el codigo de producto: "))
                        break
                    except ValueError:
                        print()
                        print(
                            Fore.RED+"\t\t\t\t\t\t\tIngrese un número, no letras o palabras" + Fore.RESET)

                archivo_silolo.seek(0)
                while archivo_silolo.tell() < tams:
                    puntero = pickle.load(archivo_silolo)

                    if str(silo.cod_prod).ljust(2) == puntero.cod_prod:
                        reintentar = True
                        print()
                        print(Fore.RED +
                              "\t\t\t\t\t\t\tEse codigo de producto ya fue asignado a un silo, use otro" + Fore.RESET)

            print()

            silo.cod_prod = str(silo.cod_prod).ljust(2)
            silo.cod_silo = str(silo.cod_silo).ljust(2)

            validar_silos(silo, prod, archivo_silolo, archivo_silo)

            pregunta = input(
                "\t\t\t\t\t\t\t¿Desea ingresar otro silo? SI/NO: ").upper()

            while pregunta != "SI" and pregunta != "NO":
                pregunta = input(Fore.RED +
                                 "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()

            if pregunta == "NO":
                inicio = 0

# --------------------------------------------------------------------------------------------------------


def baja():

    clean()
    eliminar = 1

    while eliminar == 1:
        print()
        confirmacion = input(
            "\t\t\t\t\t\t\t¿Queres dar de baja algún elemento? SI/NO: ").upper()

        while confirmacion != "SI" and confirmacion != "NO":
            confirmacion = input(Fore.RED +
                                 "\t\t\t\t\t\t\tError de tipeo, responda solo SI o NO: " + Fore.RESET).upper()

        if confirmacion == "SI":
            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tListado de productos:" + Fore.RESET)
            print()

            tam = os.path.getsize(archivo_pro)

            if tam > 0:
                archivo_prolo.seek(0)

                while archivo_prolo.tell() < tam:
                    puntero_actual = pickle.load(archivo_prolo)

                    if puntero_actual.estado == "True".ljust(15):
                        print("\t\t\t\t\t\t\t", puntero_actual.nombre_prod)
                print()

                pregunta = input(
                    "\t\t\t¿Que producto desea dar de baja? (elija el nombre su nombre): ").capitalize()
                archivo_prolo.seek(0)
                tipeo_mal = True
                while archivo_prolo.tell() < tam:
                    puntero_ant = archivo_prolo.tell()
                    puntero_pos = pickle.load(archivo_prolo)

                    if puntero_pos.nombre_prod == pregunta.ljust(20):
                        puntero_pos.estado = "False".ljust(15)
                        archivo_prolo.seek(puntero_ant)
                        pickle.dump(puntero_pos, archivo_prolo)
                        archivo_prolo.flush()
                        tipeo_mal = False
                        advertencia = input(
                            f"\t\t\tEl producto {pregunta} fue dado de baja, para continuar presione cualquier tecla: ")

                if tipeo_mal == True:
                    print("\t\t\t\t\t\t\tProducto no encontrado, pruebe nuevamente")
                    advertencia = input(Fore.WHITE+Back.BLUE +
                                        "\t\t\t\t\t\t\tPara continuar presione cualquier tecla: " + Fore.RESET)

                print()
                advertencia = input(Fore.WHITE+Back.BLUE +
                                    "\t\t\tNo hay productos para dar de baja, para continuar presione cualquier tecla " + Fore.RESET)
                eliminar = 0

        else:
            eliminar = 0

# --------------------------------------------------------------------------------------------------------


def consulta():

    clean()

    tam = os.path.getsize(archivo_pro)

    if tam > 0:
        print()
        print(Fore.BLUE+"\t\t\t\t\t\t\tListado de productos:" + Fore.RESET)
        print()

        archivo_prolo.seek(0)
        while archivo_prolo.tell() < tam:
            puntero_actual = pickle.load(archivo_prolo)

            print(
                f"\t\t\t\t\t\t\tCodigo de producto: {puntero_actual.cod_prod}\n\t\t\t\t\t\t\tNombre: {puntero_actual.nombre_prod}\n\t\t\t\t\t\t\tEstado: {puntero_actual.estado}")
            print()

        advertencia = input(Fore.WHITE+Back.BLUE +
                            "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)

    else:
        advertencia = input(Fore.WHITE+Back.BLUE +
                            "\t\t\tNo hay productos en el archivo, para continuar presione cualquier tecla" + Fore.RESET)

# --------------------------------------------------------------------------------------------------------


def modificacion():

    clean()
    modificar = 1

    while modificar == 1:
        print()
        confirmacion = input(
            "\t\t\t\t\t\t\t¿Quiere modificar algun elemento? SI/NO: ").upper()
        while confirmacion != "SI" and confirmacion != "NO":
            confirmacion = input(Fore.RED +
                                 "\t\t\t\t\t\t\tError de tipeo, responda solo SI o NO: " + Fore.RESET).upper()
        if confirmacion == "SI":

            tam = os.path.getsize(archivo_pro)

            if tam > 0:
                print()
                print(Fore.BLUE+"\t\t\t\t\t\t\tListado de productos:" + Fore.RESET)
                print()

                archivo_prolo.seek(0)
                while archivo_prolo.tell() < tam:
                    puntero_actual = pickle.load(archivo_prolo)

                    print(
                        f"\t\t\t\t\t\t\tCodigo de producto: {puntero_actual.cod_prod}\n\t\t\t\t\t\t\tNombre: {puntero_actual. nombre_prod}\n\t\t\t\t\t\t\tEstado: {puntero_actual.estado}")
                    print()
                advertencia = input(Fore.WHITE+Back.BLUE +
                                    "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)

            else:
                advertencia = input(Fore.WHITE+Back.BLUE +
                                    "\t\t\tNo hay productos en el archivo, para continuar presione cualquier tecla" + Fore.RESET)
            print()

            pregunta = input(
                "\t\t\t¿Que producto desea modificar? (elija el nombre del elemento a cambiar): ").capitalize()
            print()
            existe = False

            if tam > 0:
                archivo_prolo.seek(0)
                while archivo_prolo.tell() < tam:
                    puntero_ant = archivo_prolo.tell()
                    puntero_actual = pickle.load(archivo_prolo)

                    if puntero_actual.nombre_prod == pregunta.ljust(20):

                        puntero_definitivo = puntero_ant
                        registro = puntero_actual
                        existe = True

                if existe == True:
                    reintentar = True
                    pregunta_2 = input(
                        "\t\t\t¿Que quiere modificar? (1 - Nombre, 2 - Codigo, 3 - Estado): ").capitalize()

                    if pregunta_2 == "Nombre":
                        while reintentar == True:
                            reintentar = False

                            nuevo_nom = input(
                                "\t\t\t\t\t\t\tElija el nuevo nombre: ").capitalize()

                            archivo_prolo.seek(0)
                            while archivo_prolo.tell() < tam:
                                puntero = pickle.load(archivo_prolo)

                                if nuevo_nom.ljust(20) == puntero.nombre_prod:
                                    reintentar = True
                                    print()
                                    print(Fore.RED +
                                          "\t\t\t\t\t\t\tEse nombre ya fue asignado a un producto, use otro" + Fore.RESET)

                        registro.nombre_prod = nuevo_nom.ljust(20)
                        archivo_prolo.seek(puntero_definitivo)
                        pickle.dump(registro, archivo_prolo)
                        archivo_prolo.flush()
                        print()
                        advertencia = input(
                            "\t\t\t\t\t\t\tCambio de nombre exitoso!")

                    elif pregunta_2 == "Codigo":
                        while reintentar == True:
                            reintentar = False
                            while True:
                                try:
                                    print()
                                    nuevo_cod = int(
                                        input("\t\t\t\t\t\t\tElija el nuevo codigo: "))
                                    while nuevo_cod < 0 or nuevo_cod > 99:
                                        print()
                                        print(
                                            "\t\t\t\t\t\t\tEl codigo de producto debe estar entre 0 y 99")
                                        print()
                                        nuevo_cod = int(
                                            input("\t\t\t\t\t\t\tElija el nuevo codigo: "))
                                    break
                                except ValueError:
                                    print()
                                    print(
                                        "\t\t\t\t\t\t\tEscriba un codigo numerico, no palabras o letras")

                            archivo_prolo.seek(0)
                            while archivo_prolo.tell() < tam:
                                puntero = pickle.load(archivo_prolo)

                                if str(nuevo_cod).ljust(2) == puntero.cod_prod:
                                    reintentar = True
                                    print()
                                    print(Fore.RED +
                                          "\t\t\t\t\t\t\tEse codigo ya fue asignado a un producto, use otro" + Fore.RESET)
                        registro.cod_prod = nuevo_cod.ljust(2)
                        archivo_prolo.seek(puntero_definitivo)
                        pickle.dump(registro, archivo_prolo)
                        archivo_prolo.flush()
                        print()
                        advertencia = input(Fore.GREEN +
                                            "\t\t\t\t\t\t\tCambio de codigo exitoso!" + Fore.RESET)
                    elif pregunta_2 == "Estado":
                        validados = 0
                        valido = True
                        archivo_prolo.seek(0)
                        while archivo_prolo.tell() < tam:
                            puntero_actual = pickle.load(archivo_prolo)
                            if puntero_actual.estado == "True".ljust(15):
                                validados = validados + 1
                        if validados > 2:
                            valido = False
                            print()
                            print(f"\t\t\t\t\t\t\tNo se pueden dar de alta mas de 3 productos con estado 'Valido'\n\t\t\t\t\t\t\tsi quiere agregar otro producto primero vaya a 'Baja'e invalide algun producto\nhecho esto pruebe dar de alta nuevamente este producto")
                            print()
                            advertencia = input(Fore.WHITE+Back.BLUE +
                                                "\t\t\t\t\t\t\tPara continuar presione cualquier tecla: " + Fore.RESET)

                        if valido == True:
                            archivo_prolo.seek(0)
                            while archivo_prolo.tell() < tam:
                                puntero = pickle.load(archivo_prolo)
                                if puntero.nombre_prod == pregunta.ljust(20):
                                    if puntero.estado == "False".ljust(15):
                                        registro.estado = "True".ljust(15)
                                    if puntero.estado == "True".ljust(15):
                                        registro.estado = "False".ljust(15)

                            archivo_prolo.seek(puntero_definitivo)
                            pickle.dump(registro, archivo_prolo)
                            archivo_prolo.flush()
                            print()
                            advertencia = input(Fore.GREEN +
                                                "\t\t\t\t\t\t\tCambio de estado exitoso!" + Fore.RESET)
                    else:
                        print(Fore.RED +
                              "\t\t\t\t\t\t\tError de tipeo, solo puede escribir 'Nombre', 'Codigo' o 'Estado'" + Fore.RESET)
                        advertencia = input(Fore.WHITE+Back.BLUE +
                                            "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)

                else:
                    print(
                        Fore.RED+"\t\t\t\t\t\t\tNo se encontro ese nombre en el archivo de productos. Intente nuevamente." + Fore.RESET)
                    print()
                    advertencia = input(Fore.WHITE+Back.BLUE +
                                        "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)

            else:
                advertencia = input(
                    Fore.RED+"\t\t\t\t\t\t\tNo hay productos en el archivo, para continuar presione cualquier tecla" + Fore.RESET)

        else:
            modificar = 0

# --------------------------------------------------------------------------------------------------------


def sec_menu():

    clean()

    init(autoreset=True)
    print(Fore.BLUE + "\t\t\t\t\t\t\t\tOPCIONES")
    print("\t\t\t\t\t\t\tA. ALTA")
    print("\t\t\t\t\t\t\tB. BAJA")
    print("\t\t\t\t\t\t\tC. CONSULTA")
    print("\t\t\t\t\t\t\tM. MODIFICACION")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\tV- VOLVER al MENU PRINCIPAL")
    print()

    op3 = input("\t\t\t\t\t\t\tIngrese la letra de la opcion: ").upper()

    while op3 != "A" and op3 != "B" and op3 != "C" and op3 != "M" and op3 != "V":
        op3 = input(Fore.RED +
                    "\t\t\t\t\t\t\tError de tipeo, ingrese la letra de la opcion: " + Fore.RESET).upper()

    if op2 == "B":

        if op3 == "A":
            alta()
            ant = 3
        elif op3 == "B":
            baja()
            ant = 3
        elif op3 == "C":
            consulta()
            ant = 3
        elif op3 == "M":
            modificacion()
            ant = 3
        else:
            ant = 2

    if op2 == "C":

        if op3 == "A":
            alta_rub()
            ant = 3
        elif op3 == "V":
            ant = 2
        elif op3 != "V" and op3 != "A":
            print(Fore.YELLOW+"\t\t\t\t\t\t\tFuncionalidad en construccion" + Fore.RESET)
            hola = input(Fore.WHITE+Back.BLUE +
                         "\t\t\t\t\t\t\tPresione enter para continuar" + Fore.RESET)
            ant = 2

    if op2 == "D":

        if op3 == "A":
            alta_rub_x_prod()
            ant = 3
        elif op3 == "V":
            ant = 2
        elif op3 != "V" and op3 != "A":
            print()
            print(Fore.YELLOW+"\t\t\t\t\t\t\tFuncionalidad en construccion" + Fore.RESET)
            hola = input(Fore.WHITE+Back.BLUE +
                         "\t\t\t\t\t\t\tPresione enter para continuar" + Fore.RESET)
            ant = 2

    if op2 == "E":

        if op3 == "A":
            alta_silos()
            ant = 3
        elif op3 == "V":
            ant = 2
        elif op3 != "V" and op3 != "A":
            print(Fore.YELLOW+"\t\t\t\t\t\t\tFuncionalidad en construccion" + Fore.RESET)
            hola = input(Fore.WHITE+Back.BLUE +
                         "\t\t\t\t\t\t\tPresione enter para continuar" + Fore.RESET)
            ant = 2

    return ant

# --------------------------------------------------------------------------------------------------------

# Variables


cupos_otorgados = 0
cam_arribado = 0

# --------------------------------------------------------------------------------------------------------

# Archivos fisicos

archivo_pro = r"C:\TP3\productos.dat"
archivo_rxp = r"C:\TP3\rubros_x_prod.dat"
archivo_rub = r"C:\TP3\rubros.dat"
archivo_silo = r"C:\TP3\silos.dat"
archivo_ope = r"C:\TP3\operaciones.dat"
archivo_regi = r"C:\TP3\registro.dat"

# --------------------------------------------------------------------------------------------------------

# Apertura

if not os.path.exists(archivo_ope):
    archivo_opelo = open(archivo_ope, "w+b")
else:
    archivo_opelo = open(archivo_ope, "r+b")

if not os.path.exists(archivo_pro):
    archivo_prolo = open(archivo_pro, "w+b")
else:
    archivo_prolo = open(archivo_pro, "r+b")

if not os.path.exists(archivo_rub):
    archivo_rublo = open(archivo_rub, "w+b")
else:
    archivo_rublo = open(archivo_rub, "r+b")

if not os.path.exists(archivo_rxp):
    archivo_rxplo = open(archivo_rxp, "w+b")
else:
    archivo_rxplo = open(archivo_rxp, "r+b")

if not os.path.exists(archivo_silo):
    archivo_silolo = open(archivo_silo, "w+b")
else:
    archivo_silolo = open(archivo_silo, "r+b")

if not os.path.exists(archivo_regi):
    archivo_regilo = open(archivo_regi, "w+b")
else:
    archivo_regilo = open(archivo_regi, "r+b")


# --------------------------------------------------------------------------------------------------------

# Inicio del programa
ant = 1

while ant == 1:
    ant = 0
    print()
    op = main_menu()

# --------------------------------------------------------------------------------------------------------

# Administracion

    if op == "1":
        ant = 2

        while ant == 2:
            ant = 0
            op2 = admin()

            if op2 == "V":
                ant = 1

            else:
                ant = 3
                while ant == 3:
                    ant = 0
                    ant = sec_menu()

# --------------------------------------------------------------------------------------------------------

# Entrega de cupos

    elif op == "2":

        tamp = os.path.getsize(archivo_pro)
        validados = 0

        archivo_prolo.seek(0)

        while archivo_prolo.tell() < tamp:
            numeros = pickle.load(archivo_prolo)

            if numeros.estado == "True".ljust(15):
                validados = validados + 1

        if validados == 0:
            print("\t\t\tNo hay producto validados en el archivo productos, valide un producto como minimo y vuelva a esta opcion")
            advertencia = input(Fore.WHITE+Back.BLUE +
                                "\t\t\t\t\t\t\tPresione cualquier tecla para continuar" + Fore.RESET)
            ant = 1

        else:
            clean()
            print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a entrega de cupos" + Fore.RESET)
            entrega = 1
            while entrega == 1:

                entrega = 0
                tamp = os.path.getsize(archivo_pro)
                tamope = os.path.getsize(archivo_ope)

                print()

                patente_camion = input(
                    "\t\t\t\t\t\t\t¿Qué patente va a ocupar el cupo? (Ejemplo de patente: 123ASDB): "). upper()
                print()

                while len(patente_camion) < 6 or len(patente_camion) > 7:
                    patente_camion = input(Fore.RED +
                                           "\t\t\t\t\t\t\tError, la patente debe tener entre 6 y 7 caracteres: " + Fore.RESET).upper()

                for k in range(0, 3):
                    while patente_camion[k] != "1" and patente_camion[k] != "2" and patente_camion[k] != "3" and patente_camion[k] != "4" and patente_camion[k] != "5" and patente_camion[k] != "6" and patente_camion[k] != "7" and patente_camion[k] != "8" and patente_camion[k] != "9" and patente_camion[k] != "0":
                        patente_camion = input(Fore.RED +
                                               "\t\t\t\t\t\t\tError, la patente tiene que tener 3 números al principio: " + Fore.RESET).upper()

                fecha_inva = True

                while fecha_inva == True:
                    try:
                        fecha_cupo = input(
                            "\t\t\t\t\t\t\tIngrese fecha de recepcion dia/mes/año (Ejemplo: 25/3/2010): ")
                        fecha_conv = datetime.datetime.strptime(
                            fecha_cupo, '%d/%m/%Y')
                        fecha_inva = False
                    except ValueError:
                        print(
                            Fore.RED+"\t\t\t\t\t\t\tError fecha invalida, pruebe nuevamente" + Fore.RESET)

                print()
                print(
                    f"\t\t\t\t\t\t\tFecha ingresada: {fecha_conv.day}/{fecha_conv.month}/{fecha_conv.year}")
                print()
                print(
                    "\t\t\t----------------------------------------------------------------------------------------------")
                print()
                print(Fore.BLUE+"\t\t\t\t\t\t\tListado de productos:" + Fore.RESET)
                print()

                archivo_prolo.seek(0)

                while archivo_prolo.tell() < tamp:
                    puntero_actual = pickle.load(archivo_prolo)

                    if puntero_actual.estado == "True".ljust(15):
                        print()
                        print(
                            f"\t\t\t\t\t\t\tCodigo de producto: {puntero_actual.cod_prod}\n\t\t\t\t\t\t\tNombre: {puntero_actual. nombre_prod}")

                flagp = False

                while flagp == False:

                    print()
                    print(
                        "\t\t\tIngrese el codigo, el programa le notificara si corresponde con algun codigo del archivo de productos")
                    print()

                    camion_cupo = operaciones()
                    camion_cupo.cod_prod = int(
                        input("Ingrese el codigo del producto: "))

                    archivo_prolo.seek(0)

                    while archivo_prolo.tell() < tamp:
                        elemento = pickle.load(archivo_prolo)

                        if elemento.cod_prod == str(camion_cupo.cod_prod).ljust(2):
                            print()
                            print(Fore.GREEN +
                                  "\t\t\t\t\t\t\tCodigo correcto" + Fore.RESET)
                            flagp = True

                camion_cupo.patente = patente_camion.ljust(20)
                camion_cupo.fecha_cupo = str(fecha_conv.date()).ljust(20)
                camion_cupo.cod_prod = str(camion_cupo.cod_prod).ljust(2)
                camion_cupo.estado = "Pendiente".ljust(15)
                camion_cupo.tara = "0".ljust(4)
                camion_cupo.bruto = "0".ljust(10)

                repetido = False
                archivo_opelo.seek(0)
                while archivo_opelo.tell() < tamope:
                    puntero_actual = pickle.load(archivo_opelo)
                    if puntero_actual.patente == patente_camion.ljust(20) and puntero_actual.fecha_cupo == str(camion_cupo.fecha_cupo).ljust(20):

                        alta = input(
                            f"La patente {camion_cupo.patente} ya tiene un cupo otorgado para esa fecha, presione cualquier tecla para continuar: ")
                        repetido = True

                if repetido == False:
                    archivo_opelo.seek(0, 2)
                    pickle.dump(camion_cupo, archivo_opelo)
                    archivo_opelo.flush()
                    cupos_otorgados = cupos_otorgados + 1
                    print()
                    print(
                        f"\t\t\t\t\t\t\tSe le otorgo un cupo a la patente: {camion_cupo.patente}")

                print()
                print(
                    "\t\t\t----------------------------------------------------------------------------------------------")
                print()

                pregunta = input(
                    "\t\t\t\t\t\t\t¿Desea ingresar otra pratente? SI/NO: ").upper()

                while pregunta != "SI" and pregunta != "NO":
                    print()
                    pregunta = input(Fore.RED +
                                     "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()
                if pregunta == "SI":
                    entrega = 1

                else:
                    ant = 1

# --------------------------------------------------------------------------------------------------------

# Recepcion

    elif op == "3":

        clean()
        print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a recepcion" + Fore.RESET)
        print()

        c = 1

        while c == 1:
            c = 0
            validados = 0
            tamope = os.path.getsize(archivo_ope)

            archivo_opelo.seek(0)
            while archivo_opelo.tell() < tamope:
                puntero_actual_2 = pickle.load(archivo_opelo)

                if puntero_actual_2.estado == "Pendiente".ljust(15):
                    validados = validados + 1

            if validados == 0:
                print(
                    "\t\t\t\t\t\t\tNo hay camiones con cupo en el archivo de operaciones, asigne un cupo como minimo")
                advertencia = input(Fore.WHITE+Back.BLUE +
                                    "\t\t\t\t\t\t\tPresione cualquier tecla para continuar" + Fore.RESET)
                archivo_opelo.close()
                ant = 1

            else:
                print()

                cam = input(
                    "\t\t\t\t\t\t\tIngrese la patente del camion: ").upper()

                while len(cam) < 6 or len(cam) > 7:
                    cam = input(Fore.RED +
                                "\t\t\t\t\t\t\tError, la patente debe tener entre 6 y 7 caracteres: " + Fore.RESET).upper()

                for k in range(0, 3):
                    while cam[k] != "1" and cam[k] != "2" and cam[k] != "3" and cam[k] != "4" and cam[k] != "5" and cam[k] != "6" and cam[k] != "7" and cam[k] != "8" and cam[k] != "9" and cam[k] != "0":
                        cam = input(Fore.RED +
                                    "\t\t\t\t\t\t\tError, la patente tiene que tener 3 números al principio: " + Fore.RESET).upper()
                print()

                fecha_actual = datetime.datetime.now()
                fecha_real = datetime.datetime.strftime(
                    fecha_actual, "%Y-%m-%d")
                cupo = False

                archivo_opelo.seek(0)
                while archivo_opelo.tell() < tamope:
                    puntero_ant = archivo_opelo.tell()
                    puntero_actual_3 = pickle.load(archivo_opelo)

                    if puntero_actual_3.patente == cam.ljust(20) and puntero_actual_3.estado == "Pendiente".ljust(15) and puntero_actual_3.fecha_cupo == str(fecha_real).ljust(20):

                        registro = puntero_actual_3
                        puntero_definitivo = puntero_ant
                        cupo = True

                if cupo == True:
                    registro.estado = "Arribado".ljust(15)
                    archivo_opelo.seek(puntero_definitivo)
                    pickle.dump(registro, archivo_opelo)
                    archivo_opelo.flush()
                    cam_arribado = cam_arribado + 1

                    print("\t\t\t\t\t\t\tPatente arribada")
                    print()

                    pregunta = input(
                        "\t\t\t\t\t\t\t¿Desea ingresar otra patente? SI/NO: ").upper()

                    while pregunta != "SI" and pregunta != "NO":
                        pregunta = input(Fore.RED +
                                         "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()
                    if pregunta == "NO":
                        ant = 1

                    else:
                        c = 1
                else:
                    print()
                    print(Fore.RED +
                          "\t\t\t\t\t\t\tLa patente ingresada no tiene cupo para esta fecha" + Fore.RESET)
                    print()

                    pregunta = input(
                        "\t\t\t\t\t\t\t¿Desea ingresar otra patente? SI/NO: ").upper()

                    while pregunta != "SI" and pregunta != "NO":
                        pregunta = input(Fore.RED +
                                         "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()

                    if pregunta == "NO":
                        ant = 1

                    else:
                        c = 1

# --------------------------------------------------------------------------------------------------------

# Registrar calidad

    elif op == "4":

        clean()
        print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a calidad" + Fore.RESET)
        print()

        c = 1
        while c == 1:
            c = 0
            tamope = os.path.getsize(archivo_ope)
            validados = 0
            archivo_opelo.seek(0)
            while archivo_opelo.tell() < tamope:
                puntero_actual = pickle.load(archivo_opelo)

                if puntero_actual.estado == "Arribado".ljust(15):
                    validados = validados + 1

            if validados == 0:
                print(
                    "\t\t\t\t\t\t\tNo hay camiones con estado 'arribado' en el archivo de operaciones")
                advertencia = input(Fore.WHITE+Back.BLUE +
                                    "\t\t\t\t\t\t\tPresione cualquier tecla para continuar" + Fore.RESET)
                ant = 1

            else:
                print()
                cam = input(
                    "\t\t\t\t\t\t\tIngrese la patente del camion: ").upper()

                while len(cam) < 6 or len(cam) > 7:
                    cam = input(Fore.RED +
                                "\t\t\t\t\t\t\tError, la patente debe tener entre 6 y 7 caracteres: " + Fore.RESET).upper()

                for k in range(0, 3):
                    while cam[k] != "1" and cam[k] != "2" and cam[k] != "3" and cam[k] != "4" and cam[k] != "5" and cam[k] != "6" and cam[k] != "7" and cam[k] != "8" and cam[k] != "9" and cam[k] != "0":
                        cam = input(Fore.RED +
                                    "\t\t\t\t\t\t\tError, la patente tiene que tener 3 números al principio: " + Fore.RESET).upper()

                print()

                estado = False
                archivo_opelo.seek(0)
                while archivo_opelo.tell() < tamope:
                    puntero_ant = archivo_opelo.tell()
                    puntero_actual = pickle.load(archivo_opelo)

                    if puntero_actual.estado == "Arribado".ljust(15) and puntero_actual.patente == cam.ljust(20):
                        codigo_producto = puntero_actual.cod_prod
                        puntero_definitivo = puntero_ant
                        registro = puntero_actual
                        estado = True

                if estado == True:
                    tamrxp = os.path.getsize(archivo_rxp)
                    tamr = os.path.getsize(archivo_rub)

                    archivo_rxplo.seek(0)
                    while archivo_rxplo.tell() < tamrxp:
                        puntero_rubxp = pickle.load(archivo_rxplo)

                        if puntero_rubxp.cod_prod == codigo_producto:
                            print(
                                f"\t\t\t\t\t\t\tEl rubro por producto es: {puntero_rubxp.nombre} y el codigo de rubro es: {puntero_rubxp.cod_rub}")
                            print()

                            archivo_rublo.seek(0)

                            while archivo_rublo.tell() < tamr:
                                puntero_actual = pickle.load(archivo_rublo)

                                if puntero_actual.cod_rub == puntero_rubxp.cod_rub:
                                    print(
                                        f"\t\t\t\t\t\t\tEl nombre del rubro es {puntero_actual.nombre}")
                                    print()

                    probar = 1
                    mal = 2
                    while probar == 1:
                        rubro = input(
                            "\t\t\t\t\t\t\t¿Que rubro desea evaluar? (Ingrese codigo de rubro): ")

                        archivo_rxplo.seek(0)
                        while archivo_rxplo.tell() < tamrxp:
                            puntero_ant = archivo_rxplo.tell()
                            puntero_rubxp = pickle.load(archivo_rxplo)

                            if puntero_rubxp.cod_rub == rubro.ljust(2) and puntero_rubxp.cod_prod == codigo_producto:
                                print()
                                valor = int(
                                    input("\t\t\t\t\t\t\tIngrese un valor para este rubro por producto: "))

                                if int(puntero_rubxp.valor_min) > valor or int(puntero_rubxp.valor_max) < valor:

                                    print()
                                    print(Fore.RED +
                                          "\t\t\t\t\t\t\tEl camion no cumple con los parametros" + Fore.RESET)

                                    mal = mal - 1
                                    if mal <= 0:
                                        registro.estado = "Rechazado".ljust(15)

                                elif int(puntero_rubxp.valor_min) < valor and int(puntero_rubxp.valor_max) > valor:

                                    print()
                                    print(Fore.GREEN +
                                          "\t\t\t\t\t\t\tEl camion cumple con los parametros" + Fore.RESET)
                                    registro.estado = "Calidad".ljust(15)

                        archivo_opelo.seek(puntero_definitivo)
                        pickle.dump(registro, archivo_opelo)
                        archivo_opelo.flush()
                        ant = 1

                        pregunta = input(
                            "\t\t\t\t\t\t\t¿Desea evaluar otro rubro? SI/NO: ").upper()
                        while pregunta != "SI" and pregunta != "NO":
                            pregunta = input(Fore.RED +
                                             "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()
                        if pregunta == "NO":
                            probar = 0
                            ant = 1

                else:
                    print("\t\t\t\t\t\t\tEl camion no tiene estado 'Arribado'")
                    print()
                    advertencia = input(Fore.WHITE+Back.BLUE +
                                        "\t\t\t\t\t\t\tPresione cualquier tecla para continuar" + Fore.RESET)
                    ant = 1

# --------------------------------------------------------------------------------------------------------

# Registrar peso bruto

    elif op == "5":

        repetir = 1
        while repetir == 1:
            clean()
            tamope = os.path.getsize(archivo_ope)

            print(
                Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a registro de peso bruto" + Fore.RESET)
            print()

            cam = input(
                "\t\t\t\t\t\t\tIngrese la patente del camion: ").upper()

            while len(cam) < 6 or len(cam) > 7:
                cam = input(Fore.RED +
                            "\t\t\t\t\t\t\tError, la patente debe tener entre 6 y 7 caracteres: " + Fore.RESET).upper()
            for k in range(0, 3):
                while cam[k] != "1" and cam[k] != "2" and cam[k] != "3" and cam[k] != "4" and cam[k] != "5" and cam[k] != "6" and cam[k] != "7" and cam[k] != "8" and cam[k] != "9" and cam[k] != "0":
                    cam = input(Fore.RED +
                                "\t\t\t\t\t\t\tError, la patente tiene que tener 3 números al principio: " + Fore.RESET).upper()

            calidad = False
            archivo_opelo.seek(0)

            while archivo_opelo.tell() < tamope:
                puntero_ant = archivo_opelo.tell()
                puntero = pickle.load(archivo_opelo)

                if puntero.estado == "Calidad".ljust(15) and puntero.patente == cam.ljust(20):
                    calidad = True
                    puntero_definitivo = puntero_ant
                    registro_definitivo = puntero
                    flag = True
                    while flag == True:
                        try:
                            print()
                            print(
                                f"\t\t\t\t\t\t\tEl camion a pesar tiene el codigo de producto: {puntero.cod_prod}")
                            print()
                            print()
                            puntero.bruto = input(
                                "\t\t\t\t\t\t\tIngrese su peso bruto: ")
                            if puntero.bruto <= "1000":
                                print()
                                print(Fore.YELLOW +
                                      "\t\t\t\t\t\t\tEscriba un valor númerico superior a 1000" + Fore.RESET)
                            else:
                                flag = False
                        except ValueError:
                            print()
                            print(
                                Fore.RED+"\t\t\t\t\t\t\tEscriba un valor númerico" + Fore.RESET)

                    puntero.bruto = puntero.bruto.ljust(10)
                    puntero.estado = "Bruto".ljust(15)
                    archivo_opelo.seek(puntero_definitivo)
                    pickle.dump(registro_definitivo, archivo_opelo)
                    archivo_opelo.flush()

                    print(
                        f"El camion de patente: {puntero.patente} Codigo de producto: {puntero.cod_prod} Peso bruto: {puntero.bruto} ya fue registrado")
                    print()

                    advertencia = input(Fore.WHITE+Back.BLUE +
                                        "\t\t\t\t\t\t\tPresione cualquier tecla para continuar: " + Fore.RESET)

            if calidad == False:

                advertencia = input(Fore.YELLOW +
                                    "La patente ingresada no tiene estado 'Calidad' o no se encuentra en lista de cupos. Presione cualquier tecla para volver al menu principal y corregir la patente: " + Fore.RESET)
                repetir = 0
                ant = 1

            else:

                pregunta = input(
                    "\t\t\t\t\t\t\t¿Desea ingresar otra patente? SI/NO: ").upper()

                while pregunta != "SI" and pregunta != "NO":
                    pregunta = input(Fore.RED +
                                     "\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()
                if pregunta == "NO":
                    repetir = 0
                    ant = 1

# --------------------------------------------------------------------------------------------------------

 # Registrar tara

    elif op == "7":

        repetir = 1
        while repetir == 1:
            clean()
            repetir = 0
            tamr = os.path.getsize(archivo_regi)
            tams = os.path.getsize(archivo_silo)
            tamope = os.path.getsize(archivo_ope)

            print(Fore.BLUE+"Bienvenido a registro de tara" + Fore.RESET)
            print()

            cam = input(
                "\t\t\t\t\t\t\tIngrese la patente del camion: ").upper()

            while len(cam) < 6 or len(cam) > 7:
                cam = input(Fore.RED +
                            "\t\t\t\t\t\t\tError, la patente debe tener entre 6 y 7 caracteres: " + Fore.RESET).upper()

            for k in range(0, 3):
                while cam[k] != "1" and cam[k] != "2" and cam[k] != "3" and cam[k] != "4" and cam[k] != "5" and cam[k] != "6" and cam[k] != "7" and cam[k] != "8" and cam[k] != "9" and cam[k] != "0":
                    cam = input(Fore.RED +
                                "\t\t\t\t\t\t\tError, la patente tiene que tener 3 números al principio: " + Fore.RESET).upper()

            archivo_opelo.seek(0)
            flag = False
            while archivo_opelo.tell() < tamope:
                puntero_ant = archivo_opelo.tell()
                puntero = pickle.load(archivo_opelo)

                if puntero.estado == "Bruto".ljust(15) and puntero.patente == cam.ljust(20):
                    puntero_defi_1 = puntero_ant
                    registro_defi_1 = puntero
                    flag = True

                    bucle = True
                    while bucle == True:
                        try:
                            puntero.tara = input("Ingrese la tara: ")
                            if puntero.tara > "1000":
                                print()
                                print(Fore.RED +
                                      "\t\t\t\t\t\t\tEscriba un valor númerico inferior o igual a 1000" + Fore.RESET)
                            else:
                                bucle = False
                        except ValueError:
                            print()
                            print(
                                Fore.RED+"\t\t\t\t\t\t\tEscriba un valor númerico" + Fore.RESET)

                    si = False
                    archivo_silolo.seek(0)
                    while archivo_silolo.tell() < tams and si == False:
                        puntero_ant_2 = archivo_silolo.tell()
                        cont = pickle.load(archivo_silolo)

                        if puntero.cod_prod == cont.cod_prod:
                            registro_silo = cont
                            puntero_silo = puntero_ant_2
                            si = True

                    if si == True:
                        registro_silo.stock = int(
                            registro_silo.stock) + (int(puntero.bruto) - int(puntero.tara))
                        registro_silo.stock = str(
                            registro_silo.stock).ljust(10)
                        puntero.estado = "Finalizada".ljust(15)
                        igual = False
                        patente_m = puntero.pantente.ljust(20)

                        archivo_regilo.seek(0)
                        while archivo_regilo.tell() < tamr:
                            puntero_ant3 = archivo_regilo.tell()
                            punregi = pickle.load(archivo_regilo)

                            if str(punregi.cod_prod).ljust(2) == registro_silo.cod_prod:
                                registro_defi_2 = puntero_ant3
                                registro_defi_4 = punregi
                                igual = True

                        if igual == True:
                            registro_defi_4.peso_neto = int(
                                registro_silo.stock)
                            registro_defi_4.peso_neto = str(
                                registro_defi_4.peso_neto).ljust(10)
                            registro_defi_4.cant = int(
                                registro_defi_4.cant) + 1
                            registro_defi_4.cant = str(
                                registro_defi_4.cant).ljust(2)

                            if int(registro_defi_4.neto_min) > (int(registro_defi_1.bruto) - int(registro_defi_1.tara)):
                                registro_defi_4.neto_min = (
                                    int(registro_defi_1.bruto) - int(registro_defi_1.tara))
                                registro_defi_4.neto_min = str(
                                    registro_defi_4.neto_min).ljust(10)
                                registro_defi_4.patente = patente_m

                            archivo_regilo.seek(registro_defi_2)
                            pickle.dump(registro_defi_4, archivo_regilo)

                        else:

                            regio = registros()
                            regio.cod_prod = registro_silo.cod_prod
                            regio.peso_neto = int(
                                registro_silo.stock) + int(regio.peso_neto)
                            regio.peso_neto = str(regio.peso_neto).ljust(10)
                            regio.cant = int(regio.cant) + 1
                            regio.cant = str(regio.cant).ljust(2)
                            regio.patente = cam.ljust(20)
                            regio.neto_min = int(
                                registro_defi_1.bruto) - int(registro_defi_1.tara)
                            regio.neto_min = str(regio.neto_min).ljust(10)
                            archivo_regilo.seek(0, 2)
                            pickle.dump(regio, archivo_regilo)

                        puntero.tara = puntero.tara.ljust(4)
                        archivo_opelo.seek(puntero_defi_1)
                        archivo_silolo.seek(puntero_silo)
                        pickle.dump(puntero, archivo_opelo)
                        pickle.dump(cont, archivo_silolo)
                        archivo_regilo.flush()
                        archivo_silolo.flush()
                        archivo_opelo.flush()

                        print()
                        print(
                            f"El camion de patente: {puntero.patente} Codigo de producto: {puntero.cod_prod} Tara: {puntero.tara} ya fue registrado")
                        print()
                        advertencia = input(Fore.WHITE+Back.BLUE +
                                            "Presione cualquier tecla para continuar: " + Fore.RESET)

                    else:
                        print()
                        print(
                            f"No existe silo para el codigo de producto: {puntero.cod_prod} , de alta dicho silo e intente nuevamente")
                        print()

                        advertencia = input(Fore.WHITE+Back.BLUE +
                                            "Presione cualquier tecla para continuar: " + Fore.RESET)

            if flag == False:
                advertencia = input(Fore.YELLOW +
                                    "La patente ingresada no tiene estado 'Bruto' o no se encuentra en lista de cupos. Presione cualquier tecla para vovler al menu principal y corregir la patente: " + Fore.RESET)
                ant = 1

            else:
                pregunta = input(
                    "\t\t\t\t\t\t\t¿Desea ingresar otra patente? SI/NO: ").upper()

                while pregunta != "SI" and pregunta != "NO":
                    pregunta = input(
                        Fore.RED+"\t\t\t\t\t\t\tError, solo responda SI/NO: " + Fore.RESET).upper()

                if pregunta == "NO":
                    ant = 1
                else:
                    repetir = 1

# --------------------------------------------------------------------------------------------------------
# Reportes

    elif op == "8":

        clean()
        tams = os.path.getsize(archivo_silo)
        tamr = os.path.getsize(archivo_regi)
        tamope = os.path.getsize(archivo_ope)

        print()
        print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a reportes" + Fore.RESET)
        print()
        print(f"\t\t\t\t\t\t\tCantidad de cupos otorgados: {cupos_otorgados}")
        print()
        print(f"\t\t\t\t\t\t\tCantidad de camiones recibidos {cam_arribado}")
        print()

        if tams == 0 and tamope == 0:
            print(
                "\t\t\t\t\t\t\tEl archivo de silos o de operaciones esta vacio. Verificar")
            advertencia = input(Fore.WHITE+Back.BLUE +
                                "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)
            ant = 1

        else:
            archivo_regilo.seek(0)
            while archivo_regilo.tell() < tamr:
                puntero = pickle.load(archivo_regilo)

                print()
                print(
                    f"\t\t\t\t\t\t\tLa cantidad de camiones para el codigo de producto {puntero.cod_prod} es de: {puntero.cant} camiones")
                print()
                print(
                    f"\t\t\t\t\t\t\tEl promedio del peso neto del codigo de producto {puntero.cod_prod} es de: {int(puntero.peso_neto)/int(puntero.cant)}")
                print()
                print(
                    f"\t\t\tEl camion de patente {puntero.patente} es el que menos descargo el producto, de codigo de producto {puntero.cod_prod}")

            print()
            print(
                Fore.BLUE+"\t\t\t\t\t\t\tListado de peso neto por codigo de producto" + Fore.RESET)
            archivo_silolo.seek(0)

            while archivo_silolo.tell() < tams:
                puntero = pickle.load(archivo_silolo)

                print()
                print(
                    f"\t\t\t\t\t\t\tCodigo de producto: {puntero.cod_prod} Peso neto: {puntero.stock}")

        print()
        advertencia = input(Fore.WHITE+Back.BLUE +
                            "\t\t\t\t\t\t\tFin de reportes, para continuar presione cualquier tecla" + Fore.RESET)
        ant = 1

# --------------------------------------------------------------------------------------------------------

#  SILOS

    elif op == "9":

        clean()
        print(Fore.BLUE+"\t\t\t\t\t\t\tBienvenido a silos y rechazos" + Fore.RESET)
        print()

        tams = os.path.getsize(archivo_silo)
        tamope = os.path.getsize(archivo_ope)

        if tams == 0 and tamope == 0:
            print(Fore.YELLOW +
                  "\t\t\t\t\t\t\tEl archivo de silos o de operaciones esta vacio. Verificar" + Fore.RESET)
            advertencia = input(Fore.WHITE+Back.BLUE +
                                "\t\t\t\t\t\t\tPara continuar presione cualquier tecla" + Fore.RESET)
            ant = 1

        else:
            peso_neto = 0
            puntero_in = 0

            archivo_silolo.seek(0)

            while archivo_silolo.tell() < tams:
                puntero = pickle.load(archivo_silolo)

                if int(puntero.stock) > int(peso_neto):
                    peso_neto = int(puntero.stock)
                    puntero_in = puntero

            print(
                f"\t\t\t\t\t\t\tEl silo que mas stock acumulo es: {puntero_in.nombre} y su stock es de: {peso_neto}")
            print()

            fecha_inva = True
            while fecha_inva == True:
                try:
                    fecha_cupo = input(
                        "\t\t\t\t\t\t\tIngrese fecha para ver los camiones rechazados ese dia (Ejemplo: 25/3/2010): ")
                    fecha = datetime.datetime.strptime(fecha_cupo, '%d/%m/%Y')
                    fecha_inva = False
                except ValueError:
                    print(
                        Fore.RED+"\t\t\t\t\t\t\tError fecha invalida, pruebe nuevamente" + Fore.RESET)

            print()
            print(Fore.BLUE+"\t\t\t\t\t\t\tListado de camiones rechazados:" + Fore.RESET)
            print()

            archivo_opelo.seek(0)
            while archivo_opelo.tell() < tamope:
                puntero = pickle.load(archivo_opelo)

                if puntero.estado == "Rechazado".ljust(15) and puntero.fecha_cupo == str(fecha.date()).ljust(20):
                    print(
                        f"Patente: {puntero.patente} Fecha: {puntero.fecha_cupo} Estado: {puntero.estado} Codigo de producto: {puntero.cod_prod}")
                    print()

        advertencia = input(
            Fore.WHITE+Back.BLUE + "\t\t\t\t\t\t\tFin de silos y rechazos, para continuar presione cualquier tecla"+Fore.RESET)
        ant = 1

# --------------------------------------------------------------------------------------------------------

# Fin del programa

    elif op == "0":

        clean()
        archivo_opelo.close()
        archivo_prolo.close()
        archivo_regilo.close()
        archivo_silolo.close()
        archivo_rxplo.close()
        archivo_rublo.close()
        print()
        print("\t\t\t\t\t\t\tCerrando programa, hasta luego.")
        print()
