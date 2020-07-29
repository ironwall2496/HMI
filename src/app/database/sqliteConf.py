import sqlite3
from sqlite3 import Error

sql_create_table_variables_control = """
    CREATE TABLE IF NOT EXISTS VariablesDeControl (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        setRPM1    INTEGER NOT NULL,
        setRPM2    INTEGER NOT NULL,
        compuerta1 INTEGER NOT NULL,
        compuerta2 INTEGER NOT NULL,
        compuerta3 INTEGER NOT NULL,
        ingreso1   INTEGER NOT NULL,
        quemador1  INTEGER NOT NULL
    )
    """
sql_create_table_temperatura_control = """
    CREATE TABLE IF NOT EXISTS Temp_de_control (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_control INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeControl
    )
"""

sql_create_table_variables_medidas = """
    CREATE TABLE IF NOT EXISTS VariablesDeMedida (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        humedad_tolva INTEGER NOT NULL,
        nivel_tolva   INTEGER NOT NULL,
        RPM1          INTEGER NOT NULL,
        RPM2          INTEGER NOT NULL,
        RPM3          INTEGER NOT NULL,
        valvula1      INTEGER NOT NULL,
        flujo1        INTEGER NOT NULL
    )
    """

sql_create_table_temperatura_EFTT = """
    CREATE TABLE IF NOT EXISTS TempEFTT (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_EFTT    INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeMedida
    )
"""

sql_create_table_temperatura_ETTT = """
    CREATE TABLE IF NOT EXISTS TempETTT (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_ETTT    INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeMedida
    )
"""

sql_create_table_temperatura_TE = """
    CREATE TABLE IF NOT EXISTS TempTE (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_TE      INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeMedida
    )
"""

sql_create_table_temperatura_GCSQ = """
    CREATE TABLE IF NOT EXISTS TempGCSQ (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_GCSQ    INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeMedida
    )
"""

sql_create_table_temperatura_A = """
    CREATE TABLE IF NOT EXISTS TempA (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura_A       INTEGER NOT NULL,
        tiempo              INTEGER NOT NULL,
        FOREIGN KEY (ID) REFERENCES VariablesDeMedida
    )
"""


def createConnection(path):
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
        return conn

    except Error as e:
        print(e)


def createTable(conn, sql_statements):
    try:
        cur = conn.cursor()
        cur.execute(sql_statements)
    except Error as e:
        print(e)
