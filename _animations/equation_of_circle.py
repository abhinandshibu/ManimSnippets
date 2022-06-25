from manim import *

def fadeOutObjectsInDictionary(self, dictOfObjects):
    fadeOutObjectsInList(self, list(dictOfObjects.values()))

def fadeOutObjectsInList(self, listOfObjects):
    self.play(*[FadeOut(obj) for obj in listOfObjects])

class DerivationOfEquationOfCircle(Scene):
    def construct(self):
        self.add(NumberPlane())
        # objects = self.intro()
        # self.wait(0.5)
        # fadeOutObjectsInDictionary(self, objects)
        self.drawCenterAndRadiusOfCircle()

    def intro(self):
        text = Text("What is the equation \n of a circle?").move_to(RIGHT * 3)
        circle = Circle(color=BLUE).scale(2).move_to(LEFT * 3)
        self.play(Write(text), Write(circle))
        
        return {
            "text": text,
            "circle": circle
        }

    def drawCenterAndRadiusOfCircle(self):
        center = Dot(color=RED)
        radius = VGroup(
                    Line(start=ORIGIN, end=2*RIGHT).set_angle(45*DEGREES),
                    Dot(2*RIGHT)
                )
        self.play(Write(center), Write(radius))
        self.play(
            Rotate(
                radius,
                angle=45*DEGREES,
                about_point=ORIGIN,
            )
        )
        return (center, radius)

    

    