"""
==================================================
Fjord-Keyboard-Layout v 0.1
Program to determine the current keyboard layout,
for tiling windows manager i3wm.
==================================================
Author - jadewizzard
Website - jadewizzard.github.io
Repo - https://github.com/jadewizzard/Fjord
==================================================
"""

import os

response = os.popen("xset -q").read()
layout_code = response[76:84]

if layout_code == "00000002":
    print("EN")
else:
    print("RU")