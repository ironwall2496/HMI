from kivymd.uix.screen import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        # theme_style es otra opcion de las propiedades de theme_cls
        # su valor por defecto es Light

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hola mundo",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()
