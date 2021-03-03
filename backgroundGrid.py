from manim import *
from tools.grid import Grid


class BackgroundGrid(Scene):
    """Provides a background grid which can be used to aid visual positioning
    of objects.

    tools_required:: Grid
    alternate_names::
    related_snippets:: BackgroundAxes
    """

    def construct(self):
        self.add(Grid())
