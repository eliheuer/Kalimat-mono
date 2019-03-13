# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLES
W,H,M = 1000,1000,20  # WIDTH, HEIGHT, MARGIN
VAR_WGHT = 100        # VARIABLE FONT WEIGHT
U = 32                # ONE GRID UNIT

font("fonts/Kalimat-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

print("\nGlyph names:\n")
gnames = listFontGlyphNames()
print(gnames)
