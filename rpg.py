class Habilidad:
    def __init__(self, nombre: str, ataque: int, energia_requerida: int):
        self.nombre = nombre
        self.ataque = ataque
        self.energia_requerida = energia_requerida

    def __str__(self):
        return f"Nombre: {self.nombre}, Ataque: {self.ataque}, Energia requerida: {self.energia_requerida}"


class Objeto:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Nombre: {self.nombre}, Descripcion: {self.descripcion}"


class Pocion(Objeto):
    def __init__(self, nombre: str, descripcion: str, nivel: int):
        super().__init__(nombre, descripcion)
        self.nivel: int = nivel


class Tienda:
    def __init__(self, objetos: list[Objeto], pociones: list[Pocion]):
        self.inventario_objetos = objetos
        self.inventario_pociones = pociones
        self.tipo_compra: str = ""

    def __str__(self):
        if self.tipo_compra == "objetos":
            inventario: str = "OBJETOS\n"
            j: int = 0
            for i in self.inventario_objetos:
                inventario += (
                    str(j) + " ----> " + i.nombre + "costo: " + str(15 * (j + 1)) + "\n"
                )
                j += 1
        elif self.tipo_compra == "pociones":
            inventario: str = "POCIONES\n"
            j: int = 0
            for i in self.inventario_pociones:
                inventario += (
                    str(j) + " ----> " + i.nombre + "costo: " + str(5 * (j + 1)) + "\n"
                )
                j += 1

        return inventario


class Entidad:
    def __init__(
        self,
        nombre: str,
        salud: int,
        energia: int,
        ataque_basico: int,
        exp: int,
        dinero: int,
        objeto: [Objeto | None],
    ):
        self.nombre = nombre
        self.salud = salud
        self.energia = energia
        self.salud_maxima = salud * 10
        self.energia_maxima = energia * 10
        self.ataque_basico = ataque_basico
        self.exp = exp
        self.dinero = dinero
        self.inventario: list[Objeto | Pocion] = []
        if objeto != None:
            self.inventario.append(objeto)

    def __str__(self):
        return f"Nombre: {self.nombre}, Salud: {self.salud}, Energia: {self.energia}, Salud maxima: {self.salud_maxima}, Energia maxima: {self.energia_maxima}, Ataque basico: {self.ataque_basico}"

    def atacar(self, objetivo):
        if self.salud > 0:
            # SE COMPRUEBA EL INVENTARIO PARA VER SI EL JUGADOR HA USADO UN OBJETO
            inventario_actualizado: list[Objeto | Pocion] = []
            manzana = 1
            plumas = 1
            for i in self.inventario:
                if i.nombre == "Doble EXP" and manzana == 1:
                    manzana = 2
                else:
                    inventario_actualizado.append(i)
            self.inventario = inventario_actualizado
            inventario_actualizado = []

            for i in self.inventario:
                if i.nombre == "Critico" and plumas == 1:
                    plumas = 2
                else:
                    inventario_actualizado.append(i)
            self.inventario = inventario_actualizado

            # SE PROCEDE A ATACAR AL ENEMIGO CON LA AYUDA DE LOS OBJETOS SI ES QUE SE USARON
            objetivo.salud -= self.ataque_basico * plumas
            if objetivo.recibir_dano() != 0:
                if len(self.inventario) < 10:
                    self.inventario.append(objetivo.inventario[0])
                self.exp += objetivo.exp * manzana
                self.dinero += objetivo.dinero
        else:
            print(f"ERROR. {self.nombre} esta muerto")

    def usar_habilidad(self, habilidad: Habilidad, objetivo):
        if self.salud > 0:
            # SE COMPRUEBA EL INVENTARIO PARA VER SI EL JUGADOR HA USADO UN OBJETO
            inventario_actualizado: list[Objeto | Pocion] = []
            piedra = False
            manzana = 1
            for i in self.inventario:
                if i.nombre == "Doble EXP" and manzana == 1:
                    manzana = 2
                else:
                    inventario_actualizado.append(i)
            self.inventario = inventario_actualizado
            inventario_actualizado = []

            for i in self.inventario:
                if i.nombre == "Habilidad gratis" and piedra == False:
                    piedra = True
                else:
                    inventario_actualizado.append(i)
            self.inventario = inventario_actualizado

            # SE USA LA HABILIDAD CON LA AYUDA DEL OBJETO SI ES QUE SE USO
            if piedra == True or self.energia >= habilidad.energia_requerida:
                if piedra == False:
                    self.energia -= habilidad.energia_requerida
                objetivo.salud -= habilidad.ataque
                if objetivo.recibir_dano() != 0:
                    if len(self.inventario) < 10:
                        self.inventario.append(objetivo.inventario[0])
                    self.exp += objetivo.exp * manzana
                    self.dinero += objetivo.dinero
            else:
                print(f"ERROR. {self.nombre} no tiene la energia requerida")
        else:
            print(f"ERROR. {self.nombre} esta muerto")

    def recibir_dano(self) -> int:
        if self.salud <= 0:
            print(f"¡¡¡¡¡¡ EL ENEMIGO TIPO {self.nombre} HA MUERTO !!!!!!")
            return self.exp
        return 0

    def descansar(self):
        if self.salud > 0:
            self.salud += int(self.salud_maxima * 0.15)
            self.energia += int(self.energia_maxima * 0.15)
        else:
            print(f"ERROR. {self.nombre} esta muerto")


class Personaje(Entidad):
    def __init__(self, nombre: str, salud: int, energia: int, ataque_basico: int):
        super().__init__(nombre, salud, energia, ataque_basico, 0, 0, None)
        self.habilidades: list[Habilidad] = []
        self.nivel: int = 1

    def __str__(self):
        habilidades_str = ", ".join(
            [habilidad.nombre for habilidad in self.habilidades]
        )
        return f"{super().__str__()}, EXP: {self.exp}/{self.nivel*50}, Habilidades: [{habilidades_str}], Dinero: {self.dinero}"

    def aprender_habilidad(self, nueva_habilidad: Habilidad):
        if len(self.habilidades) < 3:
            self.habilidades.append(nueva_habilidad)
        else:
            print(
                f"\n1 {self.habilidades[0]}\n2 {self.habilidades[1]}\n3 {self.habilidades[2]}\nEscribe un numero para reemplazar una habilidad:"
            )
            while True:
                numero = input()
                try:
                    numero = int(numero)
                    if 1 <= numero <= 3:
                        self.habilidades[numero - 1] = nueva_habilidad
                        break
                    else:
                        print("Error, ingrese un numero valido entre 1 y 3")
                except ValueError:
                    print("Error, debe ingresar un solo numero")

    def verificar_inventario(self):
        j = 0
        for i in self.inventario:
            print(f"{j} ----> {i}")
            j += 1

    def usar_objeto(self, poscicion_objeto: int):
        inventario_actualizado: list[Objeto | Pocion] = []
        if poscicion_objeto >= 0 and poscicion_objeto < len(self.inventario):
            if self.inventario[poscicion_objeto].nombre == "Manzana dorada":
                self.inventario[poscicion_objeto].nombre = "Doble EXP"
            elif self.inventario[poscicion_objeto].nombre == "Plumas de Fenix":
                self.inventario[poscicion_objeto].nombre = "Critico"
            elif self.inventario[poscicion_objeto].nombre == "Piedra de mana":
                self.inventario[poscicion_objeto].nombre = "Habilidad gratis"
            elif self.inventario[poscicion_objeto].nombre == "Pocion de curacion":
                if self.inventario[poscicion_objeto].nivel == 1:
                    self.salud += int(self.salud_maxima * 0.30)
                elif self.inventario[poscicion_objeto].nivel == 2:
                    self.salud += int(self.salud_maxima * 0.50)
                else:
                    self.salud += int(self.salud_maxima * 0.70)
                for i in range(len(self.inventario)):
                    if i != poscicion_objeto:
                        inventario_actualizado.append(self.inventario[i])
                self.inventario = inventario_actualizado
            elif self.inventario[poscicion_objeto].nombre == "Pocion de energia":
                if self.inventario[poscicion_objeto].nivel == 1:
                    self.energia += int(self.energia_maxima * 0.30)
                elif self.inventario[poscicion_objeto].nivel == 2:
                    self.energia += int(self.energia_maxima * 0.50)
                else:
                    self.energia += int(self.energia_maxima * 0.70)
                for i in range(len(self.inventario)):
                    if i != poscicion_objeto:
                        inventario_actualizado.append(self.inventario[i])
                self.inventario = inventario_actualizado
            else:
                print("ERROR. Este objeto ya ha sido usado")

    def verificar_nivel(self):
        if self.exp >= 50 * self.nivel:
            self.nivel += 1
            print(f"{self.nombre} ha subido a nivel {self.nivel}")
            self.ataque_basico += 1
            self.salud_maxima += 2
            self.energia_maxima += 1

    def comprar_tienda(self, tienda: Tienda, tipo_compra: str):
        if len(self.inventario) == 10:
            print(f"No puedes comprar, tu inventario esta lleno")
        else:
            tienda.tipo_compra = tipo_compra
            print(f"Escriba el numero del producto que desea comprar\n\n")
            print(tienda)
            while True:
                numero = input()
                try:
                    numero = int(numero)
                    if tipo_compra == "objetos" and 0 <= numero < len(
                        tienda.inventario_objetos
                    ):
                        if self.dinero >= (15 * (numero + 1)):
                            self.inventario.append(tienda.inventario_objetos[numero])
                            break
                        else:
                            print(f"No tienes suficiente dinero")
                            break

                    elif tipo_compra == "pociones" and 0 <= numero < len(
                        tienda.inventario_pociones
                    ):
                        if self.dinero >= (5 * (numero + 1)):
                            self.inventario.append(tienda.inventario_pociones[numero])
                            break
                        else:
                            print(f"No tienes suficiente dinero")
                            break
                    else:
                        print("Error, ingrese un numero valido")
                except ValueError:
                    print("Error, debe ingresar un solo numero")


class Enemigo(Entidad):
    def __init__(
        self,
        nombre: str,
        salud: int,
        energia: int,
        ataque_basico: int,
        exp: int,
        objeto: Objeto,
    ):
        super().__init__(nombre, salud, energia, ataque_basico, exp, 5, objeto)
