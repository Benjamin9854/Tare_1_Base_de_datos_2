from rpg import Personaje, Enemigo, Habilidad, Objeto, Pocion, Tienda

# CREACION DEL JUGADOR
jugador = Personaje("Kratos", 1, 1, 1)

# CREACION DE OBJETOS
manzana_dorada = Objeto(
    "Manzana dorada", "El siguiente enemigo asesinado otorga el doble de exp"
)
plumas_de_fenix = Objeto("Plumas de Fenix", "El siguiente ataque sera un critico")
piedra_de_mana = Objeto(
    "Piedra de mana", "La siguiguiente habilidad a usar no costara nada de energia"
)

# CREACION DE POCIONES
pocion_curacion = Pocion("Pocion de curacion", "Regenera un 30 por ciento de salud", 1)
pocion_curacion_II = Pocion(
    "Pocion de curacion", "Regenera un 50 por ciento de salud", 2
)
pocion_curacion_III = Pocion(
    "Pocion de curacion", "Regenera un 70 por ciento de salud", 3
)
pocion_energia = Pocion(
    "Pocion de energia", "Regenera un 30 por ciento de la energia", 1
)
pocion_energia_II = Pocion(
    "Pocion de energia", "Regenera un 50 por ciento de la energia", 2
)
pocion_energia_III = Pocion(
    "Pocion de energia", "Regenera un 70 por ciento de la energia", 3
)

# CREACION DE TIENDA
objetos: list[Objeto] = [manzana_dorada, plumas_de_fenix, piedra_de_mana]
pociones: list[Pocion] = [
    pocion_curacion,
    pocion_energia,
    pocion_curacion_II,
    pocion_energia_II,
    pocion_curacion_III,
    pocion_energia_III,
]
tienda_1 = Tienda(objetos, pociones)

# CREACION DE LOS ENEMIGOS
duendes: list[Enemigo] = []
esqueletos: list[Enemigo] = []
orcos: list[Enemigo] = []
for i in range(10):
    duende = Enemigo(
        "Duende nivel " + str(i + 1), 2 + i, 2 + i, 2 + i, 20 + (i * 20), manzana_dorada
    )
    duendes.append(duende)
    esqueleto = Enemigo(
        "Esqueleto nivel " + str(i + 1),
        4 + i,
        4 + i,
        4 + i,
        35 + (i * 35),
        plumas_de_fenix,
    )
    esqueletos.append(esqueleto)
    orco = Enemigo(
        "Orco nivel " + str(i + 1), 8 + i, 8 + i, 8 + i, 50 + (i * 50), piedra_de_mana
    )
    orcos.append(orco)


# CREACION DE HABILIDADES
fuego = Habilidad("Bola de fuego", 6, 5)
fuego_II = Habilidad("Super bola de fuego", 12, 10)
fuego_III = Habilidad("Mega bola de fuego", 24, 20)
lanzas = Habilidad("Lanzas afiladas", 5, 3)
lanzas_II = Habilidad("Lanzas mortales", 10, 6)
lanzas_III = Habilidad("Lanzas celestiales", 15, 12)
cuchillas = Habilidad("Cuchillas cortantes", 4, 2)
cuchillas_II = Habilidad("Cuchillas venenosas", 8, 4)
cuchillas_III = Habilidad("Cuchillas infernales", 16, 8)
torbellino = Habilidad("Torbellino desorientador", 2, 1)
torbellino_II = Habilidad("Torbellino devastador", 4, 2)
torbellino_III = Habilidad("Torbellino titan", 8, 4)


# PROBANDO LAS CLASES
print("BIENVENIDO A MI JUEGO\nESCRIBE UNA OPCION NUMERICA PARA JUGAR")
while True:
    print(
        "0 -----> SALIR\n1 -----> DESCANSAR\n2 -----> VERIFICAR INVENTARIO\n3 -----> VERIFICAR NIVEL\n4 -----> COMPRAR EN LA TIENDA\n5 -----> APRENDER UNA HABILIDAD\n6 -----> ATACAR\n7 -----> ATACAR CON HABILIDAD\n8 -----> USAR UN OBJETO\n9 -----> VER PERSONAJE\n"
    )
    numero = input()
    try:
        numero = int(numero)
        if numero == 0:
            break
        elif numero == 1:
            jugador.descansar()
        elif numero == 2:
            print("\n\n\n\n\n")
            jugador.verificar_inventario()
        elif numero == 3:
            print("\n\n\n\n\n")
            jugador.verificar_nivel()
        elif numero == 4:
            while True:
                print("\n\t\t\t1 ---> Comprar objetos          2 ---> Comprar pociones")
                numero_2 = input()
                try:
                    numero_2 = int(numero_2)
                    if numero_2 == 1:
                        jugador.comprar_tienda(tienda_1, "objetos")
                        break
                    elif numero_2 == 2:
                        jugador.comprar_tienda(tienda_1, "pociones")
                        break
                    else:
                        print("Error, numero invalido")
                except ValueError:
                    print("Error, debe ingresar un numero valido")
        elif numero == 5:
            while True:
                print("\n\n\n\nELIJE UNA HABILIDAD PARA APRENDER")
                print(
                    "\n\t\t\t1 --> Bola de fuego\t\t2 --> Super bola de fuego\t\t3 --> Mega bola de fuego"
                )
                print(
                    "\n\t\t\t4 --> Lanzas afiladas\t\t5 --> Lanzas mortales\t\t6 --> Lanzas celestiales"
                )
                print(
                    "\n\t\t\t7 --> Cuchilas cortantes\t\t8 --> Cuchilas venenosas\t\t9 --> Cuchilas infernales"
                )
                print(
                    "\n\t\t\t10 --> Torbellino desorientador\t\t11 --> Torbellino devastador\t\t12 --> Torbellino titan"
                )
                numero_3 = input()
                try:
                    numero_3 = int(numero_3)
                    if numero_3 == 1:
                        jugador.aprender_habilidad(fuego)
                        break
                    elif numero_3 == 2:
                        jugador.aprender_habilidad(fuego_II)
                        break
                    elif numero_3 == 3:
                        jugador.aprender_habilidad(fuego_III)
                        break
                    elif numero_3 == 4:
                        jugador.aprender_habilidad(lanzas)
                        break
                    elif numero_3 == 5:
                        jugador.aprender_habilidad(lanzas_II)
                        break
                    elif numero_3 == 6:
                        jugador.aprender_habilidad(lanzas_III)
                        break
                    elif numero_3 == 7:
                        jugador.aprender_habilidad(cuchillas)
                        break
                    elif numero_3 == 8:
                        jugador.aprender_habilidad(cuchillas_II)
                        break
                    elif numero_3 == 9:
                        jugador.aprender_habilidad(cuchillas_III)
                        break
                    elif numero_3 == 10:
                        jugador.aprender_habilidad(torbellino)
                        break
                    elif numero_3 == 11:
                        jugador.aprender_habilidad(torbellino_II)
                        break
                    elif numero_3 == 12:
                        jugador.aprender_habilidad(torbellino_III)
                        break
                    else:
                        print("Error, numero invalido")
                except ValueError:
                    print("Error, debe ingresar un numero valido")
        elif numero == 6:
            while True:
                print("\n\n\n\nELIJE UN ENEMIGO")
                print("\n1 --> Duende\t\t2 --> Esqueleto\t\t3 --> Orco")
                numero_4 = input()
                try:
                    numero_4 = int(numero_4)
                    print(
                        "\nINGRESE UN NUMERO DEL 0 AL 9 PARA ELEGIR EL ENEMIGO DE SU NIVEL"
                    )
                    numero_5 = input()
                    try:
                        numero_5 = int(numero_5)
                        if 0 <= numero_5 <= 9:
                            if numero_4 == 1:
                                jugador.atacar(duendes[numero_5])
                                break
                            elif numero_4 == 2:
                                jugador.atacar(esqueletos[numero_5])
                                break
                            elif numero_4 == 3:
                                jugador.atacar(orcos[numero_5])
                                break
                            else:
                                print("Error, debe ingresar un numero valido")
                    except ValueError:
                        print("Error, debe ingresar un numero valido")
                except ValueError:
                    print("Error, debe ingresar un numero valido")
        elif numero == 7:
            while True:
                print("\n\n\n\nELIJE UN ENEMIGO")
                print("\n1 --> Duende\t\t2 --> Esqueleto\t\t3 --> Orco")
                numero_4 = input()
                try:
                    numero_4 = int(numero_4)
                    print(
                        "\nINGRESE UN NUMERO DEL 0 AL 9 PARA ELEGIR EL ENEMIGO DE SU NIVEL"
                    )
                    numero_5 = input()
                    try:
                        numero_5 = int(numero_5)
                        print("\n¿QUE HABILIDAD VA A USAR?\n")
                        j = 1
                        for i in jugador.habilidades:
                            print(f"{j} ---> {i.nombre}\n")
                            j += 1
                        numero_6 = input()
                        try:
                            numero_6 = int(numero_6)
                            if 0 <= numero_5 <= 9 and 0 < numero_6 <= len(
                                jugador.habilidades
                            ):
                                if numero_4 == 1:
                                    jugador.usar_habilidad(
                                        jugador.habilidades[numero_6 - 1]
                                    )
                                    break
                                elif numero_4 == 2:
                                    jugador.usar_habilidad(
                                        jugador.habilidades[numero_6 - 1]
                                    )
                                    break
                                elif numero_4 == 3:
                                    jugador.usar_habilidad(
                                        jugador.habilidades[numero_6 - 1]
                                    )
                                    break
                                else:
                                    print("Error, debe ingresar un numero valido")
                        except ValueError:
                            print("Error, debe ingresar un numero valido")
                    except ValueError:
                        print("Error, debe ingresar un numero valido")
                except ValueError:
                    print("Error, debe ingresar un numero valido")
        elif numero == 8:
            jugador.usar_objeto(0)
        elif numero == 9:
            print("\n\n\n\n\n")
            print(jugador)
    except ValueError:
        print("Error, debe ingresar un numero valido")
