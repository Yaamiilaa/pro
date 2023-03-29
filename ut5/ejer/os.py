# Crear una clase de un sistema operativo que tenga los tipos de kernel, una opción de encendido y de apagado, la
# versión y un sistema de archivos al que le puedes añadir o borrar dichos archivos.


class OS:
    count_files = 0
    delete_files = 0
    status = "Apagado"

    def __init__(self, file_system=[], version="6.0.1"):
        self.file_system = file_system
        self.version = version

    # MÉTODO DECORADOR QUE DICE SI EL SO ESTÁ ENCENDIDO O APAGADO
    @staticmethod
    def boot(method):
        def wrapper(self, *args, **kwargs):
            print(f"El sistema operativo esta {OS.status}")
            return method(self, *args, **kwargs)

        return wrapper

    # APLICAMOS EL DECORADOR
    @boot
    def switch_status(self):
        if OS.status == "Apagado":
            OS.status = "Encendido"
        else:
            OS.status = "Apagado"

    def add_file_system(self, file):
        if file not in self.file_system:
            self.file_system.append(file)
            OS.count_files += 1
        else:
            print(f"El fichero {file} ya está en el sistema de ficheros")

    def remove_file_system(self, file):
        if file in self.file_system:
            self.file_system.remove(file)
            OS.delete_files += 1
        else:
            print(f"El fichero {file} no se encuentra en el sistema de ficheros")

    def get_file_system(self):
        for file in self.file_system:
            print(file)

    # MÉTODO ESTÁTICO QUE MUESTRA LOS TIPOS DE KERNEL
    @staticmethod
    def get_types_of_kernel() -> list:
        return ["Monolithic", "Microkernel", "Hybrid"]

    def get_version(self):
        print(self.version)

    # MÉTODO DE CLASE QUE CUENTA LOS ARCHIVOS AÑADIDOS
    @classmethod
    def get_count_files(cls):
        return cls.count_files

    # MÉTODO DE CLASE QUE CUENTA LOS ARCHIVOS BORRADOS
    @classmethod
    def get_delete_files(cls):
        return cls.delete_files


# PRUEBAS

l = OS()
l.switch_status()
l.add_file_system("etc/passwd")
l.add_file_system("etc/passwd")
l.get_file_system()
print("******")
l.remove_file_system("etc/passwd")
l.remove_file_system("etc/passwd")
print(OS.get_types_of_kernel())
l.get_version()
print(OS.get_count_files())
print("*******")
print(OS.get_delete_files())
