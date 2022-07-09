from manim import *
import random

def fadeOutObjectsInDictionary(self, dictOfObjects):
    fadeOutObjectsInList(self, list(dictOfObjects.values()))

def fadeOutObjectsInList(self, listOfObjects):
    self.play(*[FadeOut(obj) for obj in listOfObjects])

def generatePointsOnCircle(radius, noOfPoints):
    x = random.randrange

class DerivationOfEquationOfCircle(Scene):
    def construct(self):
        self.add(NumberPlane())

        # introDict = self.intro()
        # fadeOutObjectsInDictionary(self, introDict)

        centerRadiusDict = self.drawCenterAndRadiusOfCircle()
        fadeOutObjectsInList(self, [centerRadiusDict["radiusText"], centerRadiusDict["centerText"]])
        centerRadiusDict = self.rotateRadiusToFormCircle(radius=centerRadiusDict["radiusLine"], centerPosition=centerRadiusDict["centerDot"].get_center())
        # exampleDerivation(self, centerRadiusDict["radiusLine"], radiusLength, circle, xValue, yValue)
    
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
        RADIUS_LENGTH = 2
        STARTING_ANGLE = 45 * DEGREES

        centerDot = Dot(color=ORANGE)
        centerText = Text("Center").scale(0.5).next_to(centerDot, DOWN)
        
        self.play(Write(centerDot), Write(centerText))
        self.wait(1)

        radiusLine = Arrow(start=ORIGIN, end=[RADIUS_LENGTH,0,0], color=BLUE, buff=0).rotate(STARTING_ANGLE, about_point=centerDot.get_center())
        radiusText = Text("r").scale(0.6).move_to([0.8, 1.2, 0])
        
        self.play(Write(radiusLine), Write(radiusText))
        self.wait(1.5)

        return {
            "centerDot": centerDot, 
            "centerText": centerText, 
            "radiusLine": radiusLine,
            "radiusText": radiusText
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
            run_time=3.5
        )

        self.wait(2)

    def exampleDerivation(self, radiusLine, radiusLength, circle, xValue, yValue):
        point = Dot().move_to([xValue, yValue, 0])
        axes = Axes()
        self.play(Write(axes), Write(point))



    # Show a couple example points, that does not lie on the circle because 
    # they do not satisfy the equation.




    

    