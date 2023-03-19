#########################################################################################################################################################################
#################################################################### LIBRERIAS ##########################################################################################
#########################################################################################################################################################################
from array import array
from ast import Return
from calendar import c
from ctypes.wintypes import HLOCAL

from operator import length_hint
import os
import os.path
import time
from tkinter import CENTER
#from turtle import pos
from colorama import init, Fore, Back, Style

import pickle
from datetime import datetime, timedelta, date
import datetime

if os.name == "posix":
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

#########################################################################################################################################################################
########################################################## REGISTROS Y ARCHIVOS ##########################################################################################
#########################################################################################################################################################################

AFOp = "D:\\AyEDD\\operaciones.dat"
AFPro = "D:\\AyEDD\\productos.dat"
AFRu = "D:\\AyEDD\\rubros.dat"
AFRuPro = "D:\\AyEDD\\rubrosxproductos.dat"
AFSilos = "D:\\AyEDD\\silos.dat"
AFExtras = "D:\\AyEDD\\extra.dat"

if not os.path.exists(AFOp):
    ALOp = open(AFOp, "w+b")
else:
    ALOp = open(AFOp, "r+b")

if not os.path.exists(AFPro):
    ALPro = open(AFPro, "w+b")
else:
    ALPro = open(AFPro, "r+b")

if not os.path.exists(AFRu):
    ALRu = open(AFRu, "w+b")
else:
    ALRu = open(AFRu, "r+b")
if not os.path.exists(AFRuPro):
    ALRuPro = open(AFRuPro, "w+b")
else:
    ALRuPro = open(AFRuPro, "r+b")
if not os.path.exists(AFSilos):
    ALSilos = open(AFSilos, "w+b")
else:
    ALSilos = open(AFSilos, "r+b")
if not os.path.exists(AFExtras):
    ALExtras = open(AFExtras, "w+b")
else:
    ALExtras = open(AFExtras, "r+b")


class Operacion():
    def __init__(self):
        self.patente = ""
        self.codpro = 0
        self.fechacup = ""
        self.estado = ""
        self.pbruto = 0
        self.tara = 0


class Producto():
    def __init__(self):
        self.nombreprod = ""
        self.codpro = 0
        self.vigencia = ""


class Rubro():
    def __init__(self):
        self.codru = 0
        self.nombreru = ""


class Silos():
    def __init__(self):
        self.codsilo = 0
        self.nombresilo = ""
        self.codpro = 0
        self.stock = 0


class Rubrosxproducto():
    def __init__(self):
        self.codru = 0
        self.valminadm = 0.0
        self.codpro = 0
        self.valmaxadm = 0.0


class Extra():
    def __init__(self):
        self.contcupos = 0
        self.cantotcam = 0.0
        self.cantcamprod = [0]*3
        self.pnprod = [0.0]*3
        self.prompnprod = [0.0]*3
        self.patminprod = [""]*3


regop = Operacion()
regprod = Producto()
regrub = Rubro()
regsi = Silos()
regrubxprod = Rubrosxproducto()
regext = Extra()


def formatearOp(vrOp):
    vrOp.patente = str(vrOp.patente)
    vrOp.patente = vrOp.patente.ljust(7, ' ')
    vrOp.codpro = str(vrOp.codpro)
    vrOp.codpro = vrOp.codpro.ljust(1, ' ')
    vrOp.fechacup = str(vrOp.fechacup).ljust(10, ' ')
    vrOp.estado = vrOp.estado.ljust(1, ' ')
    vrOp.pbruto = str(vrOp.pbruto)
    vrOp.pbruto = vrOp.pbruto.ljust(5, ' ')
    vrOp.tara = str(vrOp.tara)
    vrOp.tara = vrOp.tara.ljust(5, ' ')


def formatearProducto(vrprod):
    vrprod.codpro = str(vrprod.codpro).ljust(2, ' ')
    vrprod.nombreprod = str(vrprod.nombreprod).ljust(20, ' ')
    vrprod.vigencia = str(vrprod.vigencia).ljust(15)


def formatearRubro(vrRubro):
    vrRubro.codru = str(vrRubro.codru)
    vrRubro.codru = vrRubro.codru.ljust(1, ' ')
    vrRubro.nombreru = vrRubro.nombreru.ljust(30, ' ')


def formatearSilos(vrSilos):
    vrSilos.codsilo = str(vrSilos.codsilo)
    vrSilos.codsilo = vrSilos.codsilo.ljust(1, ' ')
    vrSilos.nombresilo = vrSilos.nombresilo.ljust(30, ' ')
    vrSilos.codpro = str(vrSilos.codpro)
    vrSilos.codpro = vrSilos.codpro.ljust(1, ' ')
    vrSilos.stock = str(vrSilos.stock)
    vrSilos.stock = vrSilos.stock.ljust(5, ' ')


def formatearRxP(vrRxP):
    vrRxP.codru = str(vrRxP.codru)
    vrRxP.codru = vrRxP.codru.ljust(1, ' ')
    vrRxP.codpro = str(vrRxP.codpro)
    vrRxP.codpro = vrRxP.codpro.ljust(1, ' ')
    vrRxP.valminadm = str(vrRxP.valminadm)
    vrRxP.valminadmadm = vrRxP.valminadm.ljust(5, ' ')
    vrRxP.valmaxadm = str(vrRxP.valmaxadm)
    vrRxP.valmaxadm = vrRxP.valmaxadm.ljust(5, ' ')


def formatearExtra(vrExtra):
    vrExtra.contcupos = str(vrExtra.contcupos)
    vrExtra.contcupos = vrExtra.contcupos.ljust(2, ' ')
    vrExtra.contcupos = str(vrExtra.contcupos)
    vrExtra.contcupos = vrExtra.contcupos.ljust(2, ' ')

#########################################################################################################################################################################
##################################################################### TODOS LOS MENUS ###################################################################################
#########################################################################################################################################################################


def menu1():
    init(autoreset=True)
    print(Fore.YELLOW + "\t\t\t\t\t\t\t\t\t\t\t\t\t Menu")
    print("\t\t\t\t\t\t\t\t\t\t\t\t1_ADMININISTRACIONES")
    print("\t\t\t\t\t\t\t\t\t\t\t\t2_ENTREGA DE CUPOS")
    print("\t\t\t\t\t\t\t\t\t\t\t\t3_RECEPCION")
    print("\t\t\t\t\t\t\t\t\t\t\t\t4_REGISTRAR CALIDAD")
    print("\t\t\t\t\t\t\t\t\t\t\t\t5_REGISTRAR PESO BRUTO5")
    print("\t\t\t\t\t\t\t\t\t\t\t\t6_REGISTRAR DESCARGA")
    print("\t\t\t\t\t\t\t\t\t\t\t\t7_REGISTRAR TARA")
    print("\t\t\t\t\t\t\t\t\t\t\t\t8_REPORTES")
    print("\t\t\t\t\t\t\t\t\t\t\t\t9_LISTADOS DE SILOS Y RECHAZADOS")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\t\t\t\t\t\t0_fin del programa")

# Este es el menu secundario


def menu2():
    init(autoreset=True)
    print(Fore.YELLOW + "\t\t\t\t\t\t\t\t\t\t\t\t\t Menu")
    print("\t\t\t\t\t\t\t\t\t\t\t\tA- TITULARES")
    print("\t\t\t\t\t\t\t\t\t\t\t\tB- PRODUCTOS")
    print("\t\t\t\t\t\t\t\t\t\t\t\tC- RUBROS")
    print("\t\t\t\t\t\t\t\t\t\t\t\tD- RUBROS x PRODUCTO")
    print("\t\t\t\t\t\t\t\t\t\t\t\tE- SILOS")
    print("\t\t\t\t\t\t\t\t\t\t\t\tF- SUCURSALES")
    print("\t\t\t\t\t\t\t\t\t\t\t\tG- PRODUCTO POR TITULAR")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\t\t\t\t\t\tV- VOLVER al MENU PRINCIPAL")

# Menu terciario


def opciones():
    init(autoreset=True)
    print(Fore.YELLOW + "\t\t\t\t\t\t\t\t\t\t\t\t\tOPCIONES")
    print("\t\t\t\t\t\t\t\t\t\t\t\tA. ALTA")
    print("\t\t\t\t\t\t\t\t\t\t\t\tB. BAJA")
    print("\t\t\t\t\t\t\t\t\t\t\t\tC. CONSULTA")
    print("\t\t\t\t\t\t\t\t\t\t\t\tM. MODIFICACION")
    init(autoreset=True)
    print(Fore.WHITE+Back.BLUE +
          "\t\t\t\t\t\t\t\t\t\t\t\tV- VOLVER al MENU PRINCIPAL")

# validacion de la primera eleccion


def ingreso_menu():
    menu2()
    op = str(input(
        "\t\t\t\t\t\t\t\t\t\t\t\tIngrese la opcion a la que que quiere ingresar indicada en el menu: ")).upper()
    while op != "A" and op != "B" and op != "C" and op != "D" and op != "E" and op != "F" and op != "G" and op != "V":
        op = str(
            input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tOpcion incorrecta,intente de nuevo: " + Fore.RESET)).upper()
    os.system(var)
    return op

# validacion de la segunda eleccion(en administraciones)


def ingreso_menu2():
    opciones()
    op2 = str(input(
        "\t\t\t\t\t\t\t\t\t\t\t\tIngrese la opcion a la que que quiere ingresar indicada en el menu: ")).upper()
    while op2 != "A" and op2 != "B" and op2 != "C" and op2 != "M" and op2 != "V":
        op2 = str(
            input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tOpcion incorrecta,intente de nuevo: " + Fore.RESET)).upper()
    os.system(var)
    return op2

# en construccion para titulares, sucursales y producto por titular


def abcm_en_construccion():
    opciones()
    opcion2 = str(
        input("\t\t\t\t\t\t\t\t\t\t\t\tIngrese la opcion deseada: ")).upper()
    os.system(var)
    while opcion2 != "A" and opcion2 != "B" and opcion2 != "C" and opcion2 != "M" and opcion2 != "V":
        opciones()
        opcion2 = str(
            input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tLa opcion ingresada no existe, ingrese una opcion valida: "+Fore.RESET)).upper()
        os.system(var)
    while opcion2 != "V":
        print("\t\t\t\t\t\t\t\t\t\t\t*************************************************************************************")
        print(Fore.BLUE + "\t\t\t\t\t\t\t\t\t\t\t\tEn construcción, aguarde unos segundos para volver al menu anterior " + Fore.RESET)
        print("\t\t\t\t\t\t\t\t\t\t\t*************************************************************************************")
        time.sleep(2)
        os.system(var)
        opciones()
        opcion2 = str(
            input("\t\t\t\t\t\t\t\t\t\t\t\tIngrese la opcion deseada: ")).upper()
        os.system(var)
        while opcion2 != "A" and opcion2 != "B" and opcion2 != "C" and opcion2 != "M" and opcion2 != "V":
            opciones()
            opcion2 = str(
                input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tLa opcion ingresada no existe, ingrese una opcion valida: "+Fore.RESET)).upper()
            os.system(var)
    os.system(var)


def abcm_en_construccion_parte():
    print("\t\t\t\t\t\t\t\t\t\t\t*************************************************************************************")
    print(Fore.BLUE + "\t\t\t\t\t\t\t\t\t\t\t\tEn construcción, aguarde unos segundos para volver al menu anterior " + Fore.RESET)
    print("\t\t\t\t\t\t\t\t\t\t\t*************************************************************************************")
    time.sleep(2)
    os.system(var)
    opciones()
    op2 = str(
        input("\t\t\t\t\t\t\t\t\t\t\t\tIngrese la opcion deseada: ")).upper()
    os.system(var)
    while op2 != "A" and op2 != "B" and op2 != "C" and op2 != "M" and op2 != "V":
        opciones()
        op2 = str(
            input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tLa opcion ingresada no existe, ingrese una opcion valida: "+Fore.RESET)).upper()
        os.system(var)
    os.system(var)
#########################################################################################################################################################################
########################################################## funciones y procedimientos ###################################################################################
#########################################################################################################################################################################


def validaPat():
    global pat
    ciclo = True
    while ciclo:
        pat = input(
            "\t\t\t\t\t\t\tIngrese su patente en forma LLLNNN o LLNNNLL: ").upper()
        if 6 <= len(pat) <= 7:
            if len(pat) == 6:
                letras = pat[0:3].isalpha()
                numeros = pat[3:].isdigit()
                if numeros == True and letras == True:
                    print(Fore.GREEN +
                          "\t\t\t\t\t\t\tES UNA PATENTE VALIDA" + Fore.RESET)
                    ciclo = False
            elif len(pat) == 7:
                letras1 = pat[0:2].isalpha()
                numeros = pat[2:5].isdigit()
                letras2 = pat[5:].isalpha()
                if letras1 == True and numeros == True and letras2 == True:
                    print(Fore.GREEN +
                          "\t\t\t\t\t\t\tES UNA PATENTE VALIDA" + Fore.RESET)
                    ciclo = False
                else:
                    print(
                        Fore.RED + "\t\t\t\t\t\t\tNO ES UNA PATENTE VALIDA" + Fore.RESET)
        else:
            print(
                Fore.RED + "\t\t\t\t\t\t\tNO ES UNA PATENTE VALIDA" + Fore.RESET)
    return pat


def buscaPat(P, F):
    global AFOp, ALOp, posPat
    t = os.path.getsize(AFOp)
    bandP = False
    bandF = False
    ALOp.seek(0)
    while ALOp.tell() < t and bandP == False and bandF == False:
        posPat = ALOp.tell()
        aux = pickle.load(ALOp)
        if str(aux.patente) == str(P).ljust(7):
            bandP = True
        if str(aux.fechacup) == str(F).ljust(10):
            bandF = True
    if bandP and bandF:
        print("El camion de patente", aux.patente,
              "YA tiene un turno asigando el dia", aux.fechacup)
    else:
        ALOp.seek(0, 2)
        regop.patente = P
        regop.fechacup = F
        print("Se le ha asignado un turno al camion de patente", regop.patente)
        return -1


def buscaESTADO(pat):
    global codpro
    global pos3
    global AFPro, ALOp
    t = os.path.getsize(AFPro)
    band = False
    ALOp.seek(0)
    while ALOp.tell() < t and band == False:
        pos3 = ALOp.tell()
        ALOp = pickle.load(ALOp)
        if str(ALOp.patente) == pat:
            band = True
    if band:
        if str(ALOp.estado) == "A":
            codpro = ALOp.codpro
            return band
    else:
        return -1


def buscacodpro():
    global codpro
    global pos3
    global desaprobado
    t = os.path.getsize(AFRuPro)
    band = False
    ALRuPro.seek(0)
    while ALRuPro.tell() < t and band == False:
        pos = ALPro.tell()
        aux = pickle.load(ALPro)
        if int(aux.codpro) == codpro:
            band = True
            ALRuPro.seek(pos, 0)
            a = str(ALRuPro.codru)
            Y = os.path.getsize(AFRu)
            band2 = False
            while AFRu.tell() == Y:
                pos2 = ALRu.tell()
                aux = pickle.load(ALRu)
                if int(aux.codru) == a:
                    band2 = True
                    ALRu.seek(pos2, 0)
                    C = str(input("Ingrese el dato del rubro:", ALRu.nombreru))
                    ALRuPro.seek(pos, 0)
                    if not C > ALRuPro.valminadm and C < ALRuPro.valmaxadm:
                        print("no aprobado")
                        desaprobado = desaprobado+1
    if desaprobado < 2:
        pickle.load(ALOp)
        ALOp.seek(pos3, 0)
        regop.estado == "C"
        pickle.dump(regop, ALOp)
        return "C"
    else:
        pickle.load(ALOp)
        ALOp.seek(pos3, 0)
        regop.estado == "R"
        pickle.dump(regop, ALOp)
        return "R"


def buscaprod():
    alta1 = int(
        input("\t\t\t\t\t\t\tIngrese el codigo de mercaderia que desee dar de alta (ingrese 00 para finalizar): "))
    while alta1 < 0 and alta1 > 99 or alta1 == 0:
        alta1 = int(
            input("\t\t\t\t\t\t\tIngrese un codigo de mercaderia entre 01 y el 99:"))
    time.sleep(2)
    os.system(var)
    if alta1 != 0:
        if busqueda_pord_op(alta1) == -1:
            print(
                "\t\t\t\t\t\t\t##########################################")
            print(
                "\t\t\t\t\t\t\tEste tipo de mercaderia no esta ingresada")
            print(
                "\t\t\t\t\t\t\t#########################################")
            time.sleep(2)
            os.system(var)
        else:
            return(alta1)


def validaFecha():
    band = False
    while not band:
        try:
            fecha = input(
                "Ingrese la fecha para la que desea pedir turno en formato DD/MM/AA: ")
            fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y')
            fecha = fecha.date()
            print("La fecha ingresada", fecha,
                  "ha sido ingresada correctamente")
            band = True
        except ValueError:
            print("La fecha", fecha, "es incorrecta, ingrese nuevamente")
    return fecha


def buscaESTADO(pat):
    global codpro
    global pos3
    global AFPro, ALOp
    t = os.path.getsize(AFPro)
    band = False
    ALOp.seek(0)
    while ALOp.tell() < t and band == False:
        pos3 = ALOp.tell()
        ALOp = pickle.load(ALOp)
        if str(ALOp.patente) == pat:
            band = True
    if band:
        if str(ALOp.estado) == "A":
            codpro = ALOp.codpro
            return band
    else:
        return -1


def recepcion(pat):
    global AFOp, ALOp
    fecha_actual = datetime.datetime.now()
    fecha_real = datetime.datetime.strftime(fecha_actual, "%Y-%m-%d")
    cupo = False
    t = os.path.getsize(AFOp)
    ALOp.seek(0)
    while ALOp.tell() < t:
        pos = ALOp.tell()
        auxx = pickle.load(ALOp)
        if auxx.patente == str(pat).ljust(7) and str(auxx.fechacup) == str(fecha_real):
            cupo = True
            puntero = pos
            registro = auxx
            print(f"La patente {auxx.patente} tiene estado 'Arribado'")
    if cupo == True:
        ALOp.seek(puntero)
        registro.estado = "A".ljust(1)
        pickle.dump(registro, ALOp)
    else:
        print("La patente ingresa no tiene cupo para la fecha de hoy")
        alto = input("Presione cualquier tecla para continuar")


def busquedax_codpro_secuencial(cod):
    global pos1
    x = os.path.getsize(AFPro)
    ALPro.seek(0, 0)
    while ALPro.tell() < x:
        pos1 = ALPro.tell()
        aux = pickle.load(ALPro)
        if aux.codpro == cod:
            return pos1
    return -1


def busqueda_pord_op(cod):
    global pos1
    x = os.path.getsize(AFPro)
    ALPro.seek(0, 0)
    flag = False
    while ALPro.tell() < x or flag:
        pos1 = ALPro.tell()
        aux = pickle.load(ALPro)
        if aux.codpro == cod:
            flag = True
            return cod
    return -1


def busquedax_codru_secuencial(cod):
    global pos2
    x = os.path.getsize(AFRu)
    ALRu.seek(0, 0)
    while ALRu.tell() < x:
        pos2 = ALRu.tell()
        aux = pickle.load(ALRu)
        if aux.codru == cod:
            return pos2
    return -1


def busquedaxvigencia_secuencial(cod):
    global posi
    x = os.path.getsize(AFPro)
    ALPro.seek(0)
    flag = True
    while ALPro.tell() < x and flag == True:
        posi = ALPro.tell()
        aux = pickle.load(ALPro)
        if aux.codpro == cod and aux.vigencia == True:
            flag = False
            return posi

    return -1


def muestra_de_productos():
    formatearOp(regop)
    j = os.path.getsize(AFPro)
    ALPro.seek(0)
    cont = 0
    while ALPro.tell() < j:
        aux = pickle.load(ALPro)
        # ALPro.seek(I,0)
        if aux.vigencia == True:
            print("##############################")
            print("--CODIGO:", aux.codpro)
            print("--NOMBRE:", aux.nombreprod)
            print("##############################")
            cont = cont+1
    if cont == 0:
        print("#####################################")
        print("NO HAY NINGUNA MERCADERIA EN VIGENCIA")
        print("#####################################")


def busqueda_patente_operaciones(x):
    global ALOp
    ALOp.seek(0)
    t = os.path.getsize(AFOp)
    band = False
    while ALOp.tell() < t and band == False:
        pos3 = ALOp.tell()
        ALOp = pickle.load(ALOp)
        if str(ALOp.patente) == x:
            band = True

    if band:
        if str(ALOp.estado) == "C":
            return band
        else:
            print("###########################################")
            print("La patente ya tiene un peso bruto asignado")
            print("###########################################")
    else:
        print("###########################################")
        print("Esta patente no se encuentra en operciones")
        print("###########################################")
        return -1


############################################################################################################################################################################
##################################################################### PROGRAMA PRINCIPAL ###################################################################################
############################################################################################################################################################################
menu = 29
while menu != 0:
    menu1()
    menu = int(
        input("\t\t\t\t\t\t\t\t\t\t\t\tElija el que menu al se quiere dirigir: "))
    if menu == chr:
        print("ingrese un numero")
        menu = int(
            input("\t\t\t\t\t\t\t\t\t\t\t\tElija el que menu al se quiere dirigir: "))
    while menu == 0 and menu == 8:
        menu = int(
            input(Fore.RED + "\t\t\t\t\t\t\t\t\t\t\t\tOpcion incorrecta,intente de nuevo: " + Fore.RESET))
    os.system(var)
    match menu:
        case 1:
            opcion = ingreso_menu()
            os.system(var)
            while opcion != 'V':
                match opcion:
                    case 'A':
                        abcm_en_construccion()
                        os.system(var)
                    case 'B':
                        op2 = ingreso_menu2()
                        while op2 != 'V':
                            match op2:
                                case 'A':
                                    alta1 = int(
                                        input("Ingrese el codigo de mercaderia que desee:(ingrese 00 para finalizar)"))
                                    while alta1 > 99:
                                        alta1 = int(
                                            input("ingrese un codigo de mercaderia correcel 01 y el 99:"))
                                    time.sleep(2)
                                    os.system(var)
                                    while alta1 != 0:
                                        if busquedax_codpro_secuencial(alta1) != -1:
                                            print(
                                                "##########################################")
                                            print(
                                                "Este tipo de mercaderia ya esta ingresada")
                                            print(
                                                "#########################################")
                                            time.sleep(2)
                                            os.system(var)
                                        else:
                                            regprod.codpro = alta1
                                            regprod.nombreprod = input(
                                                str("ingrese el nombre de medel codigo:")).upper()
                                            regprod.vigencia = True
                                            formatearProducto(regprod)
                                            pickle.dump(regprod, ALPro)
                                            ALPro.flush()
                                            print(
                                                "##############################################")
                                            print(
                                                "El tipo de mercaderia se guardo correctamente")
                                            print(
                                                "##############################################")
                                            ALPro.seek(alta1, 0)
                                            print(
                                                "##############################")
                                            print("--CODIGO:", regprod.codpro)
                                            print("--NOMBRE:",
                                                  regprod.nombreprod)
                                            print(
                                                "##############################")

                                            time.sleep(2)
                                            os.system(var)
                                        alta1 = int(
                                            input("Ingrese el codigo de mercaderia que desee:(ingrese 00 para finalizar)"))
                                        while alta1 > 99:
                                            alta1 = int(
                                                input("ingrese un codigo de mercaderia correcto entre el 01 y el 99:"))
                                        time.sleep(2)
                                        os.system(var)
                                    op2 = ingreso_menu2()
                                case'B':
                                    muestra_de_productos()
                                    baja1 = int(input(
                                        "Ingrese el codigo de producto que desee dar de baja:(0 para volver al menu anterior)"))
                                    while baja1 > 99:
                                        baja1 = int(input(
                                            "Ingrese el codigo de producto que desee dar de baja:(0 para volver al menu anterior)"))
                                    while baja1 != 0:
                                        if busquedaxvigencia_secuencial(baja1) != -1:
                                            ALPro.seek(posi, 0)
                                            regprod.vigencia = False
                                            formatearProducto(regprod)
                                            pickle.dump(regprod, ALPro)
                                            ALPro.flush()
                                        else:
                                            print(
                                                "Esta mercaderia no se encuentra en vigencia")
                                        muestra_de_productos()
                                        baja1 = int(input(
                                            "Ingrese el codigo de producto que desee dar de baja:(0 para volver al menu anterior)"))
                                        while baja1 > 99:
                                            baja1 = int(input(
                                                "Ingrese el codigo de producto que desee dar de baja:(0 para volver al menu anterior)"))
                                    os.system(var)
                                    op2 = ingreso_menu2()
                                case 'C':
                                    muestra_de_productos()
                                    print()
                                    time.sleep(4)
                                    os.system(var)
                                    op2 = ingreso_menu2()
                                case 'M':
                                    muestra_de_productos()
                                    codigo = int(input(
                                        "Ingrese el codigo de lo que quiera modificar:(0 para volver al menu anterior)"))
                                    while codigo != 0:
                                        if busquedaxvigencia_secuencial(codigo) != -1:
                                            print(
                                                "modificar nombre(N), codigo(C) o ninguna(X)")
                                            modificacion = str(
                                                input("Ingrese la abreviatura que desea:")).upper()
                                            while modificacion != "N" and modificacion != "C" and modificacion != "X":
                                                print(
                                                    "modificar nombre(N), codigo(C) o ninguna(X)")
                                                modificacion = str(
                                                    input("Ingrese la abreviatura que desea:")).upper()
                                            if modificacion == "N":
                                                ALPro.seek(posi, 0)
                                                regprod.nombreprod = input(
                                                    str("ingrese el nuevo nombre del producto:"))
                                                formatearProducto(regprod)
                                                pickle.dump(regprod, ALPro)
                                                ALPro.flush()
                                            elif modificacion == "C":
                                                ALPro.seek(posi, 0)
                                                a = int(
                                                    input("Ingrese el nuevo codigo de producto:(0 para volver al menu anterior)"))
                                                while a > 99:
                                                    a = int(
                                                        input("Ingrese el nuevo codigo de producto:(0 para volver al menu anterior)"))
                                                regprod.codpro = a
                                                formatearProducto(regprod)
                                                pickle.dump(regprod, ALPro)
                                                ALPro.flush()
                                        else:
                                            print(
                                                "###############################################")
                                            print(
                                                "ESE CODIGO DE  MERCADERIA NO ESTA EN  VIGENCIA")
                                            print(
                                                "###############################################")

                                        codigo = int(input(
                                            "Ingrese el codigo de lo que quiera modificar:(0 para volver al menu anterior)"))
                                    op2 = ingreso_menu2()
                        opcion = ingreso_menu2()
                    case 'C':
                        op2 = ingreso_menu2()
                        while op2 != 'V':
                            match op2:
                                case 'A':
                                    alta1 = int(
                                        input("\t\t\t\t\t\t\tIngrese el codigo del rubro que desee dar de alta:(ingrese 0 para finalizar)"))
                                    while alta1 > 99:
                                        alta1 = int(
                                            input("\t\t\t\t\t\t\tIngrese un codigo de rubro 01 y el 99:(ingrese 0 para finalizar)"))
                                    time.sleep(2)
                                    os.system(var)
                                    while alta1 != 0:
                                        if busquedax_codru_secuencial(alta1) != -1:
                                            print(
                                                "\t\t\t\t\t\t\t####################################")
                                            print(
                                                "\t\t\t\t\t\t\tEste tipo de rubro ya esta ingresado")
                                            print(
                                                "\t\t\t\t\t\t\t####################################")
                                            time.sleep(2)
                                            os.system(var)
                                        else:
                                            regrub.codru = alta1
                                            regrub.nombreru = input(
                                                str("\t\t\t\t\t\t\tIngrese el nombre del rubro:")).upper()
                                            pickle.dump(regrub, ALRu)
                                            # formatearlo bien
                                            formatearProducto(regrub)
                                            ALRu.flush()
                                            print(
                                                "\t\t\t\t\t\t\t##############################################")
                                            print(
                                                "\t\t\t\t\t\t\tEl tipo de mercaderia se guardo correctamente")
                                            print(
                                                "\t\t\t\t\t\t\t##############################################")
                                            ALRu.seek(alta1, 0)
                                            print(
                                                "\t\t\t\t\t\t\t##############################")
                                            print(
                                                "\t\t\t\t\t\t\t--CODIGO:", regrub.codru)
                                            print(
                                                "\t\t\t\t\t\t\t--NOMBRE:", regrub.nombreru)
                                            print(
                                                "\t\t\t\t\t\t\t##############################")

                                            time.sleep(2)
                                            os.system(var)
                                    op2 = ingreso_menu2()
                                case'B':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'C':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'M':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'V':
                                    print("volviendo al menu anterior")
                                    os.system(var)
                        opcion = ingreso_menu2()
                    case 'D':
                        op2 = ingreso_menu2()
                        while op2 != 'V':
                            match op2:
                                case 'A':
                                    alta1 = int(
                                        input("\t\t\t\t\t\t\tIngrese el codigo de la mercaderia que desee:(ingrese 0 para finalizar)"))
                                    while alta1 < 99:
                                        alta1 = int(input(
                                            "\t\t\t\t\t\t\tIngrese un codigo de mercaderia entre 01 y el 99:(ingrese 0 para finalizar)"))
                                    time.sleep(2)
                                    os.system(var)
                                    while alta1 != 0:
                                        if busquedax_codpro_secuencial(alta1) != -1:
                                            alta2 = int(
                                                input("\t\t\t\t\t\t\tIngrese el codigo de la mercaderia que desee:(ingrese 0 para finalizar)"))
                                            while alta2 < 99:
                                                alta2 = int(input(
                                                    "\t\t\t\t\t\t\tIngrese un codigo de mercaderia entre 01 y el 99:(ingrese 0 para finalizar)"))
                                            time.sleep(2)
                                            os.system(var)
                                            while alta2 != 0:
                                                if busquedax_codru_secuencial(alta2) != -1:

                                                    while a < b:
                                                        a = int(
                                                            input("\t\t\t\t\t\t\tIngrese el valor maximo del rubro que desea:"))
                                                        while a < 100 and a > 0:
                                                            a = int(
                                                                input("\t\t\t\t\t\t\tIngrese el valor maximo del rubro que desea(menor a 100):"))
                                                        b = int(
                                                            input("\t\t\t\t\t\t\tIngrese el valor maximo del rubro que desea:"))
                                                        while b < 100 and b > 0:
                                                            b = int(
                                                                input("\t\t\t\t\t\t\tIngrese el valor minimo del rubro que desea(menor a 100):"))
                                                        if a < b:
                                                            print(
                                                                "\t\t\t\t\t\t\t#################################")
                                                            print(
                                                                "\t\t\t\t\t\t\tEl peso minimo es mayor al maximo")
                                                            print(
                                                                "\t\t\t\t\t\t\t#################################")
                                                    ALRuPro.seek(2, 0)
                                                    regrubxprod.codru = alta2
                                                    regrubxprod.codpro = alta1
                                                    regrubxprod.valmaxadm = a
                                                    regrubxprod.valminadm = b
                                                    pickle.dump(
                                                        regrubxprod, ALRuPro)
                                                    # formatearlo bien
                                                    formatearProducto(
                                                        regrubxprod)
                                                    ALRuPro.flush
                                                    print(
                                                        "\t\t\t\t\t\t\t##############################################")
                                                    print(
                                                        "\t\t\t\t\t\t\tEl tipo de mercaderia se guardo correctamente")
                                                    print(
                                                        "\t\t\t\t\t\t\t##############################################")

                                                    print(
                                                        "\t\t\t\t\t\t\t#########################################")
                                                    print(
                                                        "\t\t\t\t\t\t\t--CODIGO MERCADERIA:", regrubxprod.codpro)
                                                    print("\t\t\t\t\t\t\t--CODIGO RUBRO:",
                                                          regrubxprod.codru)
                                                    print("\t\t\t\t\t\t\t--EL MAXIMO:",
                                                          regrubxprod.valmaxadm)
                                                    print("\t\t\t\t\t\t\t--EL MINIMO",
                                                          regrubxprod.valminadm)
                                                    print(
                                                        "\t\t\t\t\t\t\t#########################################")
                                        else:
                                            print(
                                                "\t\t\t\t\t\t\t#################################################")
                                            print(
                                                "\t\t\t\t\t\t\tEste tipo de mercaderia se encuentra en vigencia")
                                            print(
                                                "\t\t\t\t\t\t\t#################################################")
                                        time.sleep(2)
                                        os.system(var)
                                    op2 = ingreso_menu2()
                                case'B':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'C':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'M':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'V':
                                    print("volviendo al menu anterior")
                                    os.system(var)

                        opcion = ingreso_menu2()
                    case 'E':
                        op2 = ingreso_menu2()
                        while op2 != 'V':
                            match op2:
                                case'A':
                                    pregunta = chr(
                                        input("Desea ingresar un silo?(S-si N-no)"))
                                    while pregunta != "S" and pregunta != "N":
                                        pregunta = chr(
                                            input("ingrese una opcion correcta(S-si N-no):"))
                                    while pregunta == "S":
                                        codigopro = int(
                                            input("ingrese el codigo del producto para verificar su vigencia:(0 para )"))
                                        if busquedax_codpro_secuencial(codigopro) != -1:
                                            reintentar = True
                                            ALSilos.seek(0)
                                            tams = os.os.path.getsize(AFSilos)
                                            while ALSilos.tell() < tams:
                                                pun = pickle.load(ALSilos)
                                            if codigopro == pun.cod_prod:
                                                reintentar = False
                                                print()
                                                print(
                                                    "Ese codigo de producto ya fue asignado a un silo, use otro")

                                            if reintentar:
                                                ALSilos.seek(2, 0)
                                                regsi.codpro = codigopro
                                                regsi.nombresilo = str(
                                                    input("Ingrese el nombre del silo:"))
                                                a = int(
                                                    input("ingrese el codigo del silo(entre 01 y 99):"))
                                                while a > 99:
                                                    a = int(
                                                        input("ingrese el codigo del silo(entre 01 y 99):"))
                                                regsi.codsilo = a
                                                pickle.dump(regsi, ALSilos)
                                                formatearSilos(regsi)
                                                ALSilos.flush
                                                print(
                                                    "##############################################")
                                                print(
                                                    "El tipo de mercaderia se guardo correctamente")
                                                print(
                                                    "##############################################")

                                                print(
                                                    "#########################################")
                                                print(
                                                    "--CODIGO MERCADERIA:", regsi.codpro)
                                                print("--CODIGO SILO:",
                                                      regsi.codsilo)
                                                print(
                                                    "--EL NOMBRE DEL SILO:", regsi.nombresilo)
                                                print(
                                                    "#########################################")
                                case'B':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'C':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'M':
                                    abcm_en_construccion_parte()
                                    os.system(var)
                                case'V':
                                    print("volviendo al menu anterior")
                                    os.system(var)
                        opcion = ingreso_menu2()
                    case 'F':
                        abcm_en_construccion()
                        os.system(var)
                    case 'G':
                        abcm_en_construccion()
                        os.system(var)
                    case 'v':
                        print("volviendo al menu anterior")
                        os.system(var)
                opcion = ingreso_menu()
                os.system(var)
        case 2:
            rta = str(
                input("Desea solicitar cupo para un camion?(si o no): ")).upper()
            os.system(var)
            while rta != "SI" and rta != "NO":
                print("Respuesta no valida, ingrese si o no")
                rta = str(
                    input("Desea solicitar cupo para un camion?: ")).upper()
            if rta == "NO":
                opcion = menu1()
                os.system(var)
            else:
                os.system(var)
                while rta == "SI":
                    patente = validaPat()
                    fechacup = validaFecha()
                    buscaPat(patente, fechacup)
                    rta = str(
                        input("Desea solicitar otro cupo para un camion?: ")).upper()
                    formatearOp(regop)
                    pickle.dump(regop, ALOp)
                    ALOp.flush()
                opcion = menu1()
                os.system(var)
        case 3:
            ingresa = True
            while ingresa == True:
                recepcion(validaPat())

                pregunta = input(
                    "\t\t\t\t\t\t\t¿Desea ingresar otra patente? SI/NO: ").upper()

                while pregunta != "SI" and pregunta != "NO":
                    pregunta = input(
                        "\t\t\t\t\t\t\tError, solo responda SI/NO: ").upper()

                if pregunta == "NO":
                    ingresa = False
                    opcion = menu1()
                    os.system(var)
        case 4:
            validaPat()
            buscaESTADO(validaPat())
            if buscaESTADO(validaPat()) == "-1":
                print("\t\t\t\t\t\t\t--------------------------------------------")
                print("\t\t\t\t\t\t\tPatende no encontrada / Camion no arribado ")
                print("\t\t\t\t\t\t\t-----------------------------------------------")
            else:
                if buscacodpro() == "C":
                    print("\t\t\t\t\t\t\tEstado del camion : Con calidad")
                else:
                    print("\t\t\t\t\t\t\tEstado del camion : Rechazado")

        case 4:
            global pat
            validaPat()
            buscaESTADO(validaPat())
            if buscaESTADO(validaPat()) == "-1":
                print("--------------------------------------------")
                print("Patende no encontrada / Camion no arribado ")
                print("-----------------------------------------------")
            else:
                if buscacodpro() == "C":
                    print("Estado del camion : Con calidad")
                else:
                    print("Estado del camion : Rechazado")

        case 5:
            validaPat
            if busqueda_patente_operaciones(pat) != -1:
                ALOp.seek(pos3)
                a = float(input("ingrese el peso bruto del camion:"))
                if a < 0:
                    a = float(
                        input("ingrese correctamente el peso bruto del camion:"))
                regop.pbruto = a
                regop.estado = 'B'
                pickle.dump(regop, ALOp)
                formatearOp(regop)
                ALOp.flush
                print("##############################################")
                print("El tipo de mercaderia se guardo correctamente")
                print("##############################################")

                print("#########################################")
                print("--PATENTE:", pat)
                print("--PESO BRUTO:", regop.pbruto)
                print("--EL NOMBRE DEL SILO:", regsi.nombresilo)
                print("#########################################")

        case 9:
            print("\t\t\t\t\t\t\tBienvenido al listado de silos y rechazos")
            print()
            tam_silo = os.path.getsize(AFSilos)
            if tam_silo == 0:
                print("\t\t\t\t\t\t\tEl archivo de silos esta vacio. Verificar")
                advertencia = input(
                    "\t\t\t\t\t\t\tPara continuar presione cualquier tecla")
            else:
                peso_neto = 0
                puntero_id = 0
                ALSilos.seek(0)
                while ALSilos.tell() < tam_silo:
                    puntero = pickle.load(ALSilos)
                    if int(puntero.stock) > int(peso_neto):
                        peso_neto = int(puntero.stock)
                        puntero_id = puntero
                print(
                    f"\t\t\t\t\t\t\tEl silo que mas stock acumulo es: {puntero_id.nombresilo} y su stock es de: {peso_neto}")
                print()
                fecha_inva = True
                while fecha_inva == True:
                    try:
                        fecha_cupo = input(
                            "\t\t\t\t\t\t\tIngrese fecha para ver los camiones rechazados ese dia (Ejemplo: 25/3/2010): ")
                        fecha = datetime.datetime.strptime(
                            fecha_cupo, '%d/%m/%Y')
                        fecha_inva = False
                    except ValueError:
                        print("\t\t\t\t\t\t\tError fecha invalida, pruebe nuevamente")
                print()
                print("\t\t\t\t\t\t\tListado de camiones rechazados:")
                print()
                tam_operacion = os.path.getsize(AFOp)
                ALOp.seek(0)
                while ALOp.tell() < tam_operacion:
                    puntero = pickle.load(ALOp)
                    if puntero.estado == "Rechazado".ljust(15) and puntero.fecha_cupo == str(fecha.date()).ljust(20):
                        print(
                            f"Patente: {puntero.patente} Fecha: {puntero.fechacup} Estado: {puntero.estado} Codigo de producto: {puntero.codpro}")
                        print()
            advertencia = input(
                "Fin de silos y rechazos, para continuar presione cualquier tecla")
