from __future__ import annotations

import re
import sqlite3

DB_PATH = "twitter.db"
TWEET_EMOJI = "🐦"
RETWEET_EMOJI = "🔁"
MAX_TWEET_LENGTH = 280


def create_db(db_path: str = DB_PATH) -> None:
    """Crea la base de datos y las siguientes tablas:
    - user (id, username, password, bio)
    - tweet (id, content, user_id, retweet_from)
        └ user_id es clave ajena de user(id)
        └ retweet_from es clave ajena de tweet(id)"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    bio TEXT
                )"""
    cur.execute(sql)
    con.commit()
    sql = """CREATE TABLE IF NOT EXISTS tweet (
                    id INTEGER PRIMARY KEY,
                    content TEXT,
                    user_id INTEGER,
                    retweet_from INTEGER,
                    FOREIGN KEY(user_id) REFERENCES user(id),                  
                    FOREIGN KEY(retweet_from) REFERENCES tweet(id)                  
                )"""
    cur.execute(sql)
    con.commit()
    # Cambiar por script


class User:
    def __init__(self, username: str, password: str, bio: str = "", user_id: int = 0):
        """Constructor de la clase User.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row).
        - Crea los atributos username, password, bio, id y logged.
        """
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.username = username
        self.password = password
        self.bio = bio
        self.id = user_id
        self.logged = False

    def save(self) -> None:
        """Guarda en la base de datos un objeto de tipo User.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        sql = "INSERT INTO user (username, password, bio) VALUES (?, ?, ?)"
        self.cur.execute(sql, (self.username, self.password, self.bio))
        self.con.commit()
        self.id = self.cur.lastrowid

    def login(self, password: str) -> None:
        """Realiza el login del usuario."""
        sql = f'SELECT COUNT(*) FROM user WHERE id = {self.id} and password = "{password}"'
        row = self.cur.execute(sql).fetchone()
        self.logged = row[0] > 0

    def tweet(self, content: str) -> Tweet:
        """Crea un tweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si el tweet supera el límite de caracteres hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet has more than 280 chars!"""
        if self.logged == False:
            raise TwitterError(f"User {self.username} is not logged in!")
        if len(content) > MAX_TWEET_LENGTH:
            raise TwitterError(f"Tweet has more than {MAX_TWEET_LENGTH} chars!")
        new_tweet = Tweet(content)
        new_tweet.save(self)
        return new_tweet

    def retweet(self, tweet_id: int) -> Tweet:
        """Crea un retweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si tweet_id no existe en la base de datos hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet with id <id> does not exist!"""
        if self.logged == False:
            raise TwitterError(f"User {self.username} is not logged in!")
        sql = f"SELECT COUNT(*) FROM tweet WHERE id = {tweet_id}"
        result = self.cur.execute(sql).fetchone()
        if result[0] == 0:
            raise TwitterError(f"Tweet with id {tweet_id} does not exist!")
        new_tweet = Tweet(retweet_from=tweet_id)
        new_tweet.save(self)
        return new_tweet

    @property
    def tweets(self):
        """Función generadora que devuelve todos los tweets propios del usuario.
        - Lo que se devuelven son objetos de tipo Tweet (usar el método from_db_row)."""
        for row in self.cur.execute(f"SELECT * FROM tweet WHERE user_id = {self.id}"):
            yield Tweet.from_db_row(row)

    def __repr__(self):
        """Representa un usuario con el formato:
        <usuario>: <bio>"""
        return f"{self.username}: {self.bio}"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> User:
        """Crea un objeto de tipo User a partir de una fila de consulta SQL"""
        return User(row["username"], row["password"], row["bio"], row["id"])
        # return User(**row)


class Tweet:
    def __init__(self, content: str = "", retweet_from: int = 0, tweet_id: int = 0):
        """Constructor de la clase Tweet.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        - Crea los atributos _content, retweet_from e id.
        - retweet_from indica el id del tweet que se retuitea.
        - Si es un retweet el contenido debe ser la cadena vacía.
        """
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self._content = "" if retweet_from > 0 else content
        self.id = tweet_id
        self.retweet_from = retweet_from

    @property
    def is_retweet(self) -> bool:
        """Indica si el tweet es un retweet."""
        return self.retweet_from > 0

    @property
    def content(self) -> str:
        """Devuelve el contenido del tweet.
        - Si es un retweet el contenido habrá que buscarlo en el tweet retuiteado."""
        if self.is_retweet:
            sql = f"SELECT content FROM tweet WHERE id = {self.retweet_from}"
            result = self.cur.execute(sql).fetchone()
            return result["content"]
        return self._content

    def save(self, user: User) -> None:
        """Guarda el tweet en la base de datos.
        - El parámetro user es el usuario que escribe el tweet.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        sql = "INSERT INTO tweet (content, user_id, retweet_from) VALUES (?, ?, ?)"
        self.cur.execute(sql, (self._content, user.id, self.retweet_from))
        self.con.commit()
        self.id = self.cur.lastrowid

    def __repr__(self):
        """Representa un tweet con el formato:
        <emoji> <content> (id=<id>)"""
        emoji = RETWEET_EMOJI if self.is_retweet else TWEET_EMOJI
        return f"{emoji} {self.content} (id={self.id})"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        """Crea un objeto de tipo Tweet a partir de una fila de consulta SQL"""
        return Tweet(row["content"], row["retweet_from"], row["id"])


class Twitter:
    def __init__(self):
        """Constructor de la clase Twitter.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        """
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def add_user(self, username: str, password: str, bio: str = "") -> User:
        """Crea un objeto de tipo User y lo guarda en la base de datos.
        - Haz uso de los métodos ya creados.
        - Hay que retornar el objeto creado.
        - La contraseña debe seguir el siguiente formato:
        * Empezar con una arroba o un signo igual.
        * Continuar con 2, 3 o 4 dígitos.
        * Continuar con 2, 3 o 4 letras de la A-Z (incluyendo minúsculas).
        * Terminar con una exclamación o un asterisco.
        Si no sigue este formato hay que elevar una excepción de tipo TwitterError
        con el mensaje: Password does not follow security rules!"""
        regex = r"^[@=]\d{2,4}\w{2,4}[!*]$"
        output = re.match(regex, password)
        if output == None:
            raise TwitterError("Password does not follow security rules!")
        new_user = User(username, password, bio)
        new_user.save()
        return new_user

    def get_user(self, user_id: int) -> User:
        """Devuelve el usuario con el user_id indicado.
        Si el usuario no existe hay elevar una excepción de tipo TwitterError con el mensaje:
        User with id <id> does not exist!"""
        sql = f"SELECT * FROM user WHERE id = {user_id}"
        result = self.cur.execute(sql).fetchone()
        if result == None:
            raise TwitterError(f"User with id {user_id} does not exist!")
        return User.from_db_row(result)


class TwitterError(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)
