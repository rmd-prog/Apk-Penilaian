from kivy.app import App
from kivy.uix.label import Label

class AplikasiPenilaianApp(App):
    def build(self):
        return Label(text='Aplikasi Penilaian Siap!')

if __name__ == '__main__':
    AplikasiPenilaianApp().run()
