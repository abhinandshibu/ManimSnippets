from manim import *
from _tools.help_with_positioning.show_background_grid import Grid


class BackgroundGrid(Scene):
    """Provides a background grid which can be used to aid visual positioning
    of objects.

    tools_required:: Grid
    alternate_names::
    related_snippets:: BackgroundAxes
    sources:: https://github.com/abhinandshibu/ThreeAnimators
    """

    def construct(self):
        self.add(Grid())
