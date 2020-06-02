from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")        
        self.play(Write(my_first_text))