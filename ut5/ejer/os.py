class OS:
    def __init__(self):
        booted = False
        file_system = []
        self.file_system = file_system
        self.booted = booted
        version = "6.0.1"
        self.version = version

    def boot(self):
        self.booted = not self.booted

    def add_file_system(self, file):
        if file not in self.file_system:
            self.file_system.append(file)
        else:
            print(f"El fichero {file} ya está en el sistema de ficheros")

    def remove_file_system(self, file):
        if file in self.file_system:
            self.file_system.remove(file)
        else:
            print(f"El fichero {file} no se encuentra en el sistema de ficheros")

    def get_file_system(self):
        for file in self.file_system:
            print(file)

    @staticmethod
    def get_types_of_kernel() -> list:
        return ["Monolithic", "Microkernel", "Hybrid"]

    def get_version(self):
        print(self.version)


l = OS()
l.boot()
l.add_file_system("etc/passwd")
l.get_file_system()
print("******")
l.remove_file_system("etc/passwd")
print(OS.get_types_of_kernel())
l.get_version()
