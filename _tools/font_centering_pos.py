from manim import *

""" Contains dictionaries adjusting the position of letters of a particular
font, as ``Text(letter, font=...)`` centered with reference to a circle with
attr ``radius=0.5``
"""

FUTURA_CENTERING_POS = {
    "A": 0.04 * UP, "B": 0.03 * RIGHT, "C": 0.04 * LEFT, "D": 0.04 * RIGHT,
    "E": 0.01 * DOWN, "F": 0.02 * RIGHT + 0.01 * DOWN, "G": ORIGIN,
    "H": 0.004 * RIGHT, "I": ORIGIN, "J": 0.035 * LEFT, "K": 0.025 * RIGHT,
    "L": 0.025 * RIGHT, "M": 0.02 * UP, "N": ORIGIN, "O": ORIGIN,
    "P": 0.035 * RIGHT + 0.01 * DOWN, "Q": ORIGIN, "R": 0.03 * RIGHT,
    "S": ORIGIN, "T": 0.03 * DOWN, "U": 0.02 * DOWN, "V": 0.045 * DOWN,
    "W": 0.05 * DOWN, "X": 0.01 * DOWN, "Y": 0.03 * DOWN, "Z": ORIGIN
}