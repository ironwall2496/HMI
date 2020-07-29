from kivymd.app import MDApp
#from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.font_definitions import theme_font_styles
import os
import sqlite3
from database import sqliteConf as db
from database.sqliteConf import (
    sql_create_table_variables_medidas,
    sql_create_table_variables_control,
    sql_create_table_temperatura_TE,
    sql_create_table_temperatura_GCSQ,
    sql_create_table_temperatura_ETTT,
    sql_create_table_temperatura_EFTT,
    sql_create_table_temperatura_control,
    sql_create_table_temperatura_A
)

#Window.size = (1024, 600)
Window.size = (800, 480)
get_path = os.getcwd()
path = get_path + "/src/app/database/roaster.sqlite3"
# ----------------------------------------------------------
# ---------------------Database ----------------------------
# ----------------------------------------------------------

conn = db.createConnection(path)


if conn is not None:
    db.createTable(conn, sql_create_table_variables_control)
    db.createTable(conn, sql_create_table_temperatura_control)
    db.createTable(conn, sql_create_table_variables_medidas)
    db.createTable(conn, sql_create_table_temperatura_EFTT)
    db.createTable(conn, sql_create_table_temperatura_ETTT)
    db.createTable(conn, sql_create_table_temperatura_TE)
    db.createTable(conn, sql_create_table_temperatura_GCSQ)
    db.createTable(conn, sql_create_table_temperatura_A)

else:
    print("Error: cannot create the database connection.")


def create():
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    # date =
    pass


def update():
    pass


def retrieve(sels, *args):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM %s WHERE NAME= %s" % (table, field))
    roast_option = cur.fetchall()

    cur.close()

    pass


def delete():
    pass

# -------------------------------------------------------------
# ------------------------ Main app----------------------------
# -------------------------------------------------------------


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_hue = "900"

        #screen = Builder.load_file(main.kv)
        # return screen


if __name__ == '__main__':
    MainApp().run()
