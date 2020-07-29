from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import BaseFlatButton

KV = '''
#<KvLang>
Screen:
    #radius: [25, 0, 0, 0]
    #md_bg_color: [0,0,0,0]
    MDBoxLayout:
        spacing: dp(10)
        padding: dp(20)
        orientation:"horizontal"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: [0,0,0,0]
        radius: [25, 25, 25, 25]

        MDRaisedButton:
            text: "Automático"
            font_size: "50sp"
            size_hint_y: "0.3sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: app.theme_cls.primary_dark

        MDRaisedButton:
            text: "Semi-Automático"
            font_size: "50sp"
            size_hint_y: "0.3sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: app.theme_cls.primary_dark

#</KvLang>
'''


class MyBoxLayout(MDBoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primaty_palette = "DeepPurple"
        #self.theme_cls.primary_hue = "900"
        #self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


MainApp().run()
