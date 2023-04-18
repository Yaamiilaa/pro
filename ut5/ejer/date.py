from __future__ import annotations


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
        "domingo": 1,
        "lunes": 2,
        "martes": 3,
        "miercoles": 4,
        "jueves": 5,
        "viernes": 6,
        "sabado": 7,
    }

    CORRECT_YEARS = {"day": [1, 31], "month": [1, 12], "year": [1900, 2050]}

    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos."""
        self.day = day
        self.month = month
        self.year = year
        if (
            self.day < Date.CORRECT_YEARS["day"][0]
            or self.day > Date.CORRECT_YEARS["day"][1]
        ):
            self.day = 1
        if self.month > len(Date.DAYS_IN_MONTH):
            self.month = 1
        if (
            self.year < Date.CORRECT_YEARS["year"][0]
            or self.year > Date.CORRECT_YEARS["year"][1]
        ):
            self.year = 1900

    @staticmethod
    def is_leap_year(year: int) -> bool:
        divby4 = (year % 4 == 0) and (year % 100 != 0)
        divby400 = year % 400 == 0
        return divby4 or divby400

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        ...

    @property
    def days_in_month(self) -> int:
        """Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        if self.is_leap_year(self.year):
            if self.month == 2:
                Date.DAYS_IN_MONTH[2][1] = 29
        days_in_month = Date.DAYS_IN_MONTH[self.month][1]
        return days_in_month

    @property
    def weekday(self) -> int:
        pass

    @property
    def is_weekend(self) -> bool:
        pass

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        if self.day < 10:
            self.day = f"0{self.day}"
        if self.month < 10:
            self.month = f"0{self.month}"
        return f"{self.day}/{self.month}/{self.year}"

    def __str__(self):
        """MARTES 2 DE SEPTIEMBRE DE 2003"""
        pass

    def __add__(self, days: int) -> Date:
        """Sumar un número de días a la fecha"""
        pass

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""
        pass

    def __eq__(self, other: Date) -> bool:
        return (
            (self.day == other.day)
            and (self.month == other.month)
            and (self.year == other.year)
        )

    def __gt__(self, other: Date) -> bool:
        return (
            (self.day > other.day)
            and (self.month > other.month)
            and (self.year > other.year)
        )

    def __lt__(self, other: Date) -> bool:
        return (
            (self.day < other.day)
            and (self.month < other.month)
            and (self.year < other.year)
        )
