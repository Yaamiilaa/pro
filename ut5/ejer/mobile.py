class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["Twitter", "Drive", "Google", "Spotify"]
        self.battery = 100
        self.POWER_ON_CONSUPTION = 5
        self.POWER_OFF_CONSUPTION = 2.5

    def power_on(self):
        self.status = 1
        print("Encendiendo")
        self.battery -= self.POWER_ON_CONSUPTION
        print(f"La batería es de {self.battery}")

    def power_off(self):
        self.status = 0
        print("Apagando")
        self.battery -= self.POWER_OFF_CONSUPTION
        print(f"La batería es de {self.battery}")

    def install_app(self, app):
        if self.status == 1:
            if app not in self.apps:
                self.apps.append(app)
                print(f"La app {app} se instaló correctamente")
                self.battery -= self.POWER_OFF_CONSUPTION
            else:
                self.battery -= self.POWER_OFF_CONSUPTION
                print(f"La app {app} ya está instalada")
        print(f"La batería es de {self.battery}")

    def unistall_app(self, app):
        if self.status == 1:
            if app in self.apps:
                self.apps.remove(app)
            print(f"La app {app} se desinstaló correctamente")
            self.battery -= self.POWER_OFF_CONSUPTION
        else:
            self.battery -= self.POWER_OFF_CONSUPTION
        print(f"La batería es de {self.battery}")


mobile = MobilePhone("Samsung", 7.0, 2)
mobile.power_on()
mobile.install_app("Spotify")
mobile.unistall_app("Twitter")
