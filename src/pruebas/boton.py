from kivymd.uix.screen import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

"""definiendo un boton rectangular con kivymd
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        # prmary palette es una opcion de propiedades y
        # por defecto es azul
        self.theme_cls.primary_hue = "A700"
        # primary_hue es para el tono de color de la aplicacion
        # los valores disponibles son:
        # ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.
        # por defecto esta en 500
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hola mundo",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()
