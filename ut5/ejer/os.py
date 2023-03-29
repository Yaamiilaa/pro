# Crear una clase de un sistema operativo que tenga los tipos de kernel, una opción de encendido y de apagado, la
# versión y un sistema de archivos al que le puedes añadir o borrar dichos archivos.


class OS:
    count_files = 0
    delete_files = 0
    status = "Apagado"
    errors = {
        "E1": "El archivo ya está en el sistema de archivos",
        "E2": "El archivo no se encuentra en el sistema de archivos",
    }

    def __init__(self, file_system=[], version="6.0.1"):
        self.file_system = file_system
        self.version = version

    @staticmethod
    def boot(method):
        """método decorador que dice si el sistema operativo esá apagado o encendido"""

        def wrapper(self, *args, **kwargs):
            print(f"El sistema operativo esta {OS.status}")
            return method(self, *args, **kwargs)

        return wrapper

    @boot
    def switch_status(self):
        """Aplicamos el decorador"""
        if OS.status == "Apagado":
            OS.status = "Encendido"
        else:
            OS.status = "Apagado"

    def add_file_system(self, file):
        if file not in self.file_system:
            self.file_system.append(file)
            OS.count_files += 1
        else:
            print(OS.errors["E1"])

    def remove_file_system(self, file):
        if file in self.file_system:
            self.file_system.remove(file)
            OS.delete_files += 1
        else:
            print(OS.errors["E2"])

    def get_file_system(self):
        for file in self.file_system:
            print(file)

    @staticmethod
    def get_types_of_kernel() -> list:
        """métodos estáticos que muestra los tipos de kernel"""
        return ["Monolithic", "Microkernel", "Hybrid"]

    def get_version(self):
        print(self.version)

    @classmethod
    def get_count_files(cls):
        """método de clase que cuenta los archivos añadidos"""
        return cls.count_files

    @classmethod
    def get_delete_files(cls):
        """método de clase que cuenta los archivos borrados"""
        return cls.delete_files


# PRUEBAS

l = OS()
l.switch_status()
l.add_file_system("etc/passwd")
l.add_file_system("etc/passwd")
l.get_file_system()
l.remove_file_system("etc/passwd")
l.remove_file_system("etc/passwd")
print(OS.get_types_of_kernel())
l.get_version()
print(OS.get_count_files())
print(OS.get_delete_files())
