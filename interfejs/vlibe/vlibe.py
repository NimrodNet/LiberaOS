import remi.gui as gui
from remi import start, App

class vlibe(App):

    def main(self):
        container = gui.VBox(width=120, height=100)

        # Create a button, with the label "Hello, World!"
        self.bt = gui.Button('vlibe.')
        self.bt.onclick.do(self.on_button_pressed)

        # Add the button to the container, and return it.
        container.append(self.bt)
        return container

    def on_button_pressed(self, widget):
        self.bt.set_text('Witaj vlibe!')

start(vlibe)
