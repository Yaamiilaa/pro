class Date:
    DAYS_IN_MONTH = {
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31,
    }
    DAYS_IN_WEEK = {
        "domiengo": 0,
        "lunes": 1,
        "martes": 2,
        "miercoles": 3,
        "jueves": 4,
        "viernes": 5,
        "sabado": 6,
    }

    CORRECT_YEARS = {"day": [1, 31], "month": [1, 12], "year": [1900, 2050]}

    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self) -> bool:
        divby4 = (self.year % 4 == 0) and (self.year % 100 != 0)
        divby400 = self.year % 400 == 0
        return divby4 or divby400

    # INTENTAR HACER DECORADOR PARA COMPROBAR SI LA FECHA INTRODUCIDA ESTA ENTRE LAS FECHAS INDICADAS. (CUIDADO CON EL MES DE FEBRERO QUE NUNCA TIENE 31 DIAS, PARA ESO HAY QUE PONER QUE SI EL MES 2
    # TIENE MENOS DE 28 EN EL CASO DEL AÑO NO BISIESTO) TAMBIÉN HAY QUE TENER EN CUENTA QUE LOS MESES DE 30 TAMPOCO VAN A TENER 31 DIAS.

    def verify_correct_date(self, month: str):
        if (
            self.day > Date.CORRECT_YEARS["day"][0]
            and self.day < Date.CORRECT_YEARS["day"][1]
        ):
            if not self.is_leap_year():
                if self.day > Date.DAYS_IN_MONTH[month]:
                    self.day = 1
                elif self.month > len(Date.DAYS_IN_MONTH):
                    self.month = 1
                elif (
                    self.year < Date.CORRECT_YEARS["year"][0]
                    and self.year > Date.CORRECT_YEARS["year"][1]
                ):
                    self.year = 1900

    def days_in_month(self) -> int:
        pass

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        pass

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        pass

    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        """02/09/2003"""
        pass

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        pass

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra
