from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty 

class TextWidget(Widget):
    text = StringProperty() # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonEnglishClicked(self): # ボタンをクリック時
        self.text = 'Hello'

    def buttonJapaneseClicked(self): # ボタンをクリック時
        self.text = 'Konnichiha'


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()
