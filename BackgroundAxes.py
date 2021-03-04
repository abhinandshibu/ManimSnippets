from manim import *
from _tools.grid import GridAxes


class BackgroundGrid(Scene):
    """Provides background axes which can be used to aid visual positioning
    of objects.

    tools_required:: GridAxes
    alternate_names::
    related_snippets:: BackgroundGrid
    sources:: https://github.com/abhinandshibu/ThreeAnimators
    """

    def construct(self):
        self.add(GridAxes())
