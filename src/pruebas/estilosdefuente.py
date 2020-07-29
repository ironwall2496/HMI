from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
KV = '''
Screen:

    MDLabel:
        text: "JetBrainsMono"
        halign: "center"
        font_style: "JetBrainsMono"
'''


class MainApp(MDApp):
    def build(self):
        LabelBase.register(
            name="JetBrainsMono",
            fn_regular="JetBrainsMono-Regular.ttf")

        theme_font_styles.append('JetBrainsMono')
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]
        return Builder.load_string(KV)


MainApp().run()
