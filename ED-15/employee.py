# clase empleado en donde se crearan los diferentes empleados dentro de la empresa
class Empleado:

    def __init__(self, nombre: str, edad: int, salario: float, AnioIngreso: int, TiempoTrabajando: int,
                 email: str, rol: str, id: int = None, horas_por_dia: float = 8,
                 vacaciones_anuales: int = 15, bonos: float = 0.0,
                 recibe_comision: bool = False, porcentaje_comision: float = 0.0,
                 telefono: str = ""):
        # atributos publicos del empleado
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.AnioIngreso = AnioIngreso
        self.TiempoTrabajando = TiempoTrabajando
        self.email = email
        self.rol = rol
        self.horas_por_dia = horas_por_dia
        self.vacaciones_anuales = vacaciones_anuales
        self.bonos = bonos
        self.recibe_comision = recibe_comision
        self.porcentaje_comision = porcentaje_comision
        # los empleados antiguos sin telefono se cargan con "" (sin validar)
        self.telefono = self.validar_telefono(telefono) if telefono else ""

    @staticmethod
    def validar_telefono(telefono):
        """Valida un telefono.
        Recibe el telefono como texto y lo devuelve sin espacios al inicio/final.
        Lanza ValueError si esta vacio o tiene caracteres no permitidos."""
        telefono = str(telefono).strip()
        if not telefono:
            raise ValueError("El telefono no puede estar vacio.")
        solo_digitos = telefono.lstrip("+").replace(" ", "").replace("-", "")
        if not solo_digitos.isdigit():
            raise ValueError("El telefono solo puede tener numeros, espacios, guiones o '+' al inicio.")
        return telefono

    def a_diccionario(self):
        """Convierte el empleado en un diccionario para guardarlo en el JSON.
        No recibe nada y devuelve un dict con todos los campos."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "salario": self.salario,
            "AnioIngreso": self.AnioIngreso,
            "TiempoTrabajando": self.TiempoTrabajando,
            "email": self.email,
            "rol": self.rol,
            "horas_por_dia": self.horas_por_dia,
            "vacaciones_anuales": self.vacaciones_anuales,
            "bonos": self.bonos,
            "recibe_comision": self.recibe_comision,
            "porcentaje_comision": self.porcentaje_comision,
            "telefono": self.telefono,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un Empleado a partir de un diccionario leido del JSON.
        Recibe un dict y devuelve un Empleado. Si falta "telefono" usa ""."""
        datos = dict(datos)
        datos.setdefault("telefono", "")
        return cls(**datos)

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, "
                f"AnioIngreso: {self.AnioIngreso}, TiempoTrabajando: {self.TiempoTrabajando}, "
                f"Email: {self.email}, Telefono: {self.telefono}, Rol: {self.rol}")

    def __repr__(self):
        return (f"Empleado(id={self.id}, nombre={self.nombre}, edad={self.edad}, salario={self.salario}, "
                f"AnioIngreso={self.AnioIngreso}, TiempoTrabajando={self.TiempoTrabajando}, "
                f"email={self.email}, telefono={self.telefono}, rol={self.rol})")