from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    def calculate(self, expression):
        try:
            # Evaluate the mathematical expression
            self.ids.result.text = str(eval(expression))
        except Exception as e:
            self.ids.result.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()