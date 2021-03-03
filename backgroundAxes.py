from manim import *
from tools.grid import GridAxes


class BackgroundGrid(Scene):
    """Provides background axes which can be used to aid visual positioning
    of objects.

    tools_required:: GridAxes
    alternate_names::
    related_snippets:: BackgroundGrid
    """

    def construct(self):
        self.add(GridAxes())
