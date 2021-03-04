from manim import *


class ShowPositionalValues2d(Scene):
    """A set of static methods which can be applied on 2d objects, to visually
    show the properties of the dimensions in the animation itself. This can
    be used for reasons such as aiding positioning.

    Sources
    -------

    https://github.com/abhinandshibu/ThreeAnimators

    Methods
    -------

    show_positional_values_2d(obj)
        Combines `show_critical_points_2d(obj)`, `show_half_length_2d(obj)`,
        `show_critical_coordinates_2d(obj)` and returns one `VMobject`
    show_critical_points_2d(obj)
        Returns a `VMobject` consisting of a dot on all of the critical points
        of the object passed in.
    show_half_length_2d(obj)
        Returns a `VMobject` consisting of the half the length of height and
        width (as `Text`) and displays them along with lines in the bottom left.
    show_critical_coordinates_2d(obj)
        Returns a `VMobject` consisting of the coordinates values
        (as `Text`) on all the critical points excluding midpoints.

    Examples
    --------

    Showing all the positional attributes of a circle.

    class PosOfCircle(Scene):
        def construct(self):
            circle = Circle()
            self.add(circle)
            self.add(ShowPositionalValues2d.show_positional_values_2d(circle))

    Showing all of the critical points of a triangle

    class CriticalPointsOfCircle(Scene):
        def construct(self):
            triangle = Polygon(RIGHT, 4*RIGHT+2*UP, LEFT+3*UP)
            self.add(triangle)
            self.add(ShowPositionalValues2d.show_critical_points_2d(triangle))
    """

    @staticmethod
    def show_positional_values_2d(obj):
        return VGroup(
            ShowPositionalValues2d.show_critical_points_2d(obj),
            ShowPositionalValues2d.show_half_length_2d(obj),
            ShowPositionalValues2d.show_critical_coordinates_2d(obj)
        )

    @staticmethod
    def show_critical_points_2d(obj):
        return VGroup(
            Dot(obj.get_critical_point(DOWN + LEFT)),
            Dot(obj.get_critical_point(DOWN)),
            Dot(obj.get_critical_point(DOWN + RIGHT)),
            Dot(obj.get_critical_point(LEFT)),
            Dot(obj.get_critical_point(ORIGIN)),
            Dot(obj.get_critical_point(RIGHT)),
            Dot(obj.get_critical_point(UP + LEFT)),
            Dot(obj.get_critical_point(UP)),
            Dot(obj.get_critical_point(UP + RIGHT)),
        )

    @staticmethod
    def show_half_length_2d(obj):
        horizontal_distance = obj.get_width() / 2
        vertical_distance = obj.get_height() / 2
        horizontal_line = DashedLine(
            start=obj.get_critical_point(DOWN + LEFT),
            end=obj.get_critical_point(DOWN)
        )
        vertical_line = DashedLine(
            start=obj.get_critical_point(DOWN + LEFT),
            end=obj.get_critical_point(LEFT)
        )

        return VGroup(
            horizontal_line,
            vertical_line,
            Text(str(horizontal_distance)).scale(0.75)
                .next_to(horizontal_line, DOWN),
            Text(str(vertical_distance)).scale(0.75)
                .next_to(vertical_line, LEFT),
        )

    @staticmethod
    def show_critical_coordinates_2d(obj):
        bottom_left = obj.get_critical_point(LEFT + DOWN).tolist()
        bottom_right = obj.get_critical_point(RIGHT + DOWN).tolist()
        top_left = obj.get_critical_point(LEFT + UP).tolist()
        top_right = obj.get_critical_point(RIGHT + UP).tolist()
        center = obj.get_critical_point(ORIGIN).tolist()

        bottom_left_text = "(" + str(bottom_left[0]) + ", " \
                           + str(bottom_left[1]) + ")"
        bottom_right_text = "(" + str(bottom_right[0]) + ", " \
                            + str(bottom_right[1]) + ")"
        top_left_text = "(" + str(top_left[0]) + ", " + str(top_left[1]) + ")"
        top_right_text = "(" + str(top_right[0]) + ", " + str(
            top_right[1]) + ")"
        center_text = "(" + str(center[0]) + ", " + str(center[1]) + ")"

        return VGroup(
            Text(bottom_left_text).scale(0.6)
                .next_to(obj.get_critical_point(LEFT + DOWN), LEFT + DOWN),
            Text(bottom_right_text).scale(0.6)
                .next_to(obj.get_critical_point(RIGHT + DOWN), RIGHT + DOWN),
            Text(top_left_text).scale(0.6)
                .next_to(obj.get_critical_point(LEFT + UP), LEFT + UP),
            Text(top_right_text).scale(0.6)
                .next_to(obj.get_critical_point(RIGHT + UP), RIGHT + UP),
            Text(center_text).scale(0.6)
                .next_to(obj.get_critical_point(ORIGIN), UP)
        )
