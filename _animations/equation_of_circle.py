from manim import *

def fadeOutObjectsInDictionary(self, dictOfObjects):
    fadeOutObjectsInList(self, list(dictOfObjects.values()))

def fadeOutObjectsInList(self, listOfObjects):
    self.play(*[FadeOut(obj) for obj in listOfObjects])

class DerivationOfEquationOfCircle(Scene):
    def construct(self):
        self.add(NumberPlane())

        # introDict = self.intro()
        # fadeOutObjectsInDictionary(self, introDict)

        centerRadiusDict = self.drawCenterAndRadiusOfCircle()
        self.rotateRadiusToFormCircle(radius=centerRadiusDict["radius"], centerPosition=centerRadiusDict["centerDot"].get_center())
    
    def intro(self):
        text = Text("What is the equation \n of a circle?").move_to(RIGHT * 3)
        circle = Circle(color=BLUE).scale(2).move_to(LEFT * 3)
        self.play(Write(text), Write(circle))
        self.wait(0.5)
        
        return {
            "text": text,
            "circle": circle
        }

    def drawCenterAndRadiusOfCircle(self):
        centerDot = Dot(color=ORANGE)
        centerText = Text("Center").scale(0.5).next_to(centerDot, DOWN)
        
        self.play(Write(centerDot), Write(centerText))
        self.wait(0.5)

        radius = Arrow(start=ORIGIN, end=[2,2,0], color=BLUE, buff=0)
        
        self.play(Write(radius))
        self.wait(0.5)

        # self.play(
        #     Rotate(
        #         radius,
        #         angle=360*DEGREES,
        #         about_point=ORIGIN,
        #     ),
        #     run_time=3
        # )
        return {
            "centerDot": centerDot, 
            "centerText": centerText, 
            "radius": radius
        }

    def rotateRadiusToFormCircle(self, radius, centerPosition):
        angleInDegrees = ValueTracker(0)

        radiusRef = radius.copy()
        radius.add_updater(
            lambda z: z.become(radiusRef).rotate(angleInDegrees.get_value() * DEGREES, about_point=centerPosition)
        )

        circlePath = VMobject()
        circlePath.set_points_as_corners([radius.get_end(), radius.get_end()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([radius.get_end()])
            path.become(previous_path)
        circlePath.add_updater(update_path)
        
        self.add(circlePath)
        self.play(
            angleInDegrees.animate.set_value(360),
            run_time=2.5
        )

        self.wait(0.5)



    

    