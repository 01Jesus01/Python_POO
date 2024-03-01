
class FS3:
    def __init__(self, *equipos):
        self.equipos = equipos

    def __str__(self):
        return "\n--------------------------------------------------\n".join([str(equipo) for equipo in self.equipos])


class EquipoUwU:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)

class EquipoToyotaLegacy:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)

class EquipoPingüinosGalácticos:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)

class EquipoLos_3_Mosqueteros:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)

class EquipoWebHeros:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)

class EquipoLos_Polystation:
    nombre_equipo = ""
    nombre_de_integrante = ""
    eslogan = ""

    def __init__(self, local_equipo, local_integrantes, local_eslogan):
        self.nombre_equipo = local_equipo
        self.nombre_de_integrantes = local_integrantes
        self.eslogan = local_eslogan
    
    def __str__(self):
        integrantes_str = "Los integrantes del equipo {}".format(self.nombre_equipo)  + " son: " + "\n\n" + "\n".join(self.nombre_de_integrantes)
        eslogan_str = "Eslogan: {}".format(self.eslogan)
        return "{} {}".format(integrantes_str, "\n\n" + eslogan_str)


if  __name__ == "__main__":
    equipo = "Los UwU"
    integrantes = (
        "1-Leonardo Alberto Gonzáles Carmona - 19550747",
        "2-Norma Graciela Mendoza Ruiz - C16550498",
        "3-Jonathan Durán Mendoza - 20550401"
    )
    eslogan = "Respiración de Programación, Pose de HTML, Codificar"
    uwu = EquipoUwU(equipo, integrantes, eslogan)

    equipo = "Toyota Legacy"
    integrantes = (
        "1-Israel Chacon Rojo - 21550250",
        "2-Dilan Mauricio Garcia Hernandez - 21550132",
        "3-Jesus Elias Sierra Ruiz - 21550135"
    )
    eslogan = "Transformamos líneas de código en experiencias excepcionales"
    legacy = EquipoToyotaLegacy(equipo, integrantes, eslogan)

    equipo = "Pingüinos Galácticos"
    integrantes = (
        "1-Yahir Antonio Monje Ochoa - 20550740",
        "2-Yesica Cristina Rodriguez Renteria - 20550739",
        "3-"
    )
    eslogan = "SIC•PARVIS•MAGNA"
    pinguinos = EquipoPingüinosGalácticos(equipo, integrantes, eslogan)

    equipo = "Los 3 Mosqueteros"
    integrantes = (
        "1-Dania Denisse Benavides Figueroa - 20550402",
        "2-Erick Lozano Duarte - 20550353",
        "3-Ana Cristina Valenzuela Ruiz - 20550380"
    )
    eslogan = "Todos para uno, uno para todos"
    mosqueteros = EquipoLos_3_Mosqueteros(equipo, integrantes, eslogan)

    equipo = "WebHeros"
    integrantes = (
        "1-Jesus Manuel Arellano Merendon - 21550158",
        "2-Axel Felipe Reyes Valadez - 21550156",
        "3-Luis Daniel Delgado Enriquez - 1550145"
    )
    eslogan = "La verdad solo se puede encontrar en un lugar: el codigo"
    heros = EquipoWebHeros(equipo, integrantes, eslogan)


    equipo = "Los Polystation"
    integrantes = (
    "1-Erick Fernando Siqueiros Zúñiga - 21550138",
    "2-Paulina Ixchel Arreguin Ruiz - 20550417",
    "3-"
    )
    eslogan = "Conectando el futuro, hoy"
    polystation = EquipoLos_Polystation(equipo, integrantes, eslogan)

    fs3 = FS3(uwu, legacy, pinguinos, mosqueteros, heros, polystation)
    print(fs3)


