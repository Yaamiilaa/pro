class Date:
    DAYS_IN_MONTH = {
        1: ["enero", 31],
        2: ["febrero", 28],
        3: ["marzo", 31],
        4: ["abril", 30],
        5: ["mayo", 31],
        6: ["junio", 30],
        7: ["julio", 31],
        8: ["agosto", 31],
        9: ["septiembre", 30],
        10: ["octubre", 31],
        11: ["noviembre", 30],
        12: ["diciembre", 31],
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

    def verify_correct_date(self) -> bool:
        if (
            self.day > Date.CORRECT_YEARS["day"][0]
            and self.day < Date.CORRECT_YEARS["day"][1]
        ):
            if not self.is_leap_year():
                if self.day > Date.DAYS_IN_MONTH[self.month][1]:
                    self.day = 1
                elif self.month > len(Date.DAYS_IN_MONTH):
                    self.month = 1
                elif (
                    self.year < Date.CORRECT_YEARS["year"][0]
                    and self.year > Date.CORRECT_YEARS["year"][1]
                ):
                    self.year = 1900
                return True
            if self.month == 2:
                Date.DAYS_IN_MONTH[2][1] = 29
                return False

    def days_in_month(self) -> int:
        if self.is_leap_year():
            if self.month == 2:
                Date.DAYS_IN_MONTH[2][1] = 29
        days_in_month = Date.DAYS_IN_MONTH[self.month][1]
        return days_in_month

    # Hay que sumar solos días pero hay que mirar el número de días que tiene un mes y si el día es 15
    # de enero solo hay que sumarle 15 y no los 31 días. Utilizar módulo con el desplazamiento modular
    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        days_passed = 0

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        pass

    # Para ello hayq ue hacer el el método weekday y ver si el día es sabado o domingo
    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        """02/09/2003"""
        pass

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        pass

    def __eq__(self, other) -> bool:

        return (
            (self.day == other.day)
            and (self.month == other.month)
            and (self.year == other.year)
        )

    def __gt__(self, other):
        return (
            (self.day > other.day)
            and (self.month > other.month)
            and (self.year > other.year)
        )

    def __lt__(self, other):
        return (
            (self.day < other.day)
            and (self.month < other.month)
            and (self.year < other.year)
        )

    # operador + suma días a la fecha. Al sumar dos fechas tenemos que ver que llegue hasta el límite de
    # días que tiene el mes, y si se pasa de días hay que sumarselo al mes y si no al año. Una vez que se pase
    # del año que nos indica en el constructor tenemos que aplicar el método verify_correct_date().
    # Utilizar el módulo con el desplazamiento modular.

    # operador - resta días a la fecha o calcula la diferencia entre dos fechas. Comprobar si el dato
    # introducido (other) es de tipo entero date. Si es de tipo date hay que volver la resta de tipo
    # date y si es enterio hay que devolver un entero.

    # operador == dice si dos fechas son iguales.

    # operador > dice si una fecha es mayor que otra. Para ello debemos comparar todos los datos introducidos

    # operador < dice si una fecha es menor que otra. Lo mismo que el operador de arriba.
