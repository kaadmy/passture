#! /usr/bin/python2

# BSD license
#
# Copyright (c) 2016 KaadmY
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

import pybzw

bzw = pybzw.World("passture.bzw", "KaadmY")

### world options

bzw.add_object("world", [
        ["name", "\"Passture\""],
        ["size", 400],
        ["nowalls"]
        ])

bzw.add_object("options", [
        ["-c"], # ctf
        ["+r"],
        ["-ms", 2],
        ["-mp", "0,10,10,0,0,10"], # only red, green and obs allowed
        ["-set _disableBots", 1],
#        ["-set _sessionTime", 120], # for matches
        ["-set _tankSpeed", 27],
#        ["-set _shotsKeepVerticalVelocity", 1]
        ])

### materials

bzw.add_object("material", [
        ["name", "wall"],
        ["addtexture", "wall"]
        ])

bzw.add_object("material", [
        ["name", "nothing"],
        ["noradar"],
        ["noshadow"],
        ["nolighting"],
        ["diffuse", "0 0 0 0"], # transparent
        ])

### physics drivers
bzw.add_object("physics", [
        ["name", "death"],
        ["death", "Next time, you should stay INSIDE the map!"]
        ])

### edge geometry

bzw.add_tag("define", "halfmap")

# short edge
bzw.add_object("meshbox", [
        ["pos",  pybzw.Vector(3, [0, 351, 0])],
        ["size", pybzw.Vector(3, [152, 1, 6])],
        ["matref", "wall"]
        ])

bzw.add_object("meshbox", [
        ["pos",  pybzw.Vector(3, [0,  375, 0])],
        ["size", pybzw.Vector(3, [49.5, 24.5, 20])],
        ["matref", "nothing"],
        ["phydrv", "death"]
        ])

# long edge
bzw.add_object("meshbox", [
        ["pos",  pybzw.Vector(3, [151, 0, 0])],
        ["size", pybzw.Vector(3, [1, 350, 6])],
        ["matref", "wall"]
        ])

bzw.add_object("meshbox", [
        ["pos",  pybzw.Vector(3, [275, 0, 0])],
        ["size", pybzw.Vector(3, [124.5, 399.5, 20])],
        ["matref", "nothing"],
        ["phydrv", "death"]
        ])

### raised platforms around base areas

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [0, -70, 8])],
        ["size", pybzw.Vector(3, [10, 40, 5.5])]
        ])

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [0, -50, 0])],
        ["size", pybzw.Vector(3, [6, 6, 8])]
        ])

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [0, -140, 0])],
        ["size", pybzw.Vector(3, [15, 15, 15])]
        ])

### scattered boxes around edges

for i in range(5):
    x = (i * 20) + 34
    y = (i * 38) + 38

    r = i * 45
    h = 10.6 - (i * 2.3)

    bzw.add_object("box", [
            ["pos",  pybzw.Vector(3, [-x, y, 0])],
            ["size", pybzw.Vector(3, [8, 8, h])],
            ["rotation", r]
            ])
    
    bzw.add_object("box", [
            ["pos",  pybzw.Vector(3, [x, y, 0])],
            ["size", pybzw.Vector(3, [8, 8, h])],
            ["rotation", r]
            ])

### flag return "house"

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [0, -180, 0])],
        ["size", pybzw.Vector(3, [8, 8, 4])]
        ])

bzw.add_object("pyramid", [
        ["pos",  pybzw.Vector(3, [0, -180, 4])],
        ["size", pybzw.Vector(3, [8, 8, 4])]
        ])

### rico pyramid at mid edge

bzw.add_object("pyramid", [
        ["pos",  pybzw.Vector(3, [-130, 0, 10])],
        ["size", pybzw.Vector(3, [1, 8, -8])]
        ])

### base protection

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [36.5, -300, 0])],
        ["size", pybzw.Vector(3, [30, 2, 6])]
        ])

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [-36.5, -300, 0])],
        ["size", pybzw.Vector(3, [30, 2, 6])]
        ])

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [90, -280, 0])],
        ["size", pybzw.Vector(3, [30, 2, 6])],
        ["rotation", -60]
        ])

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [-90, -280, 0])],
        ["size", pybzw.Vector(3, [30, 2, 6])],
        ["rotation", 60]
        ])

### flag base
bzw.add_object("base", [
        ["pos",  pybzw.Vector(3, [0, -340, 0])],
        ["size", pybzw.Vector(3, [10, 10, 0.2])]
        ])

### teleporters

bzw.add_object("teleporter base", [
        ["pos",  pybzw.Vector(3, [0, -300, 0])],
        ["size", pybzw.Vector(3, [0.125, 4, 4])],
        ["rotation", 90],
        ["border", 1.0]
        ])

bzw.add_object("teleporter platform_outer", [
        ["pos",  pybzw.Vector(3, [0, -140, 15])],
        ["size", pybzw.Vector(3, [0.125, 4, 4])],
        ["rotation", 90],
        ["border", 1.0]
        ])

bzw.add_object("teleporter platform_mid", [
        ["pos",  pybzw.Vector(3, [-38, 0, 12])],
        ["size", pybzw.Vector(3, [0.125, 4, 2.5])],
        ["rotation", 0],
        ["border", 1.0]
        ])

bzw.add_tag("enddef") # "halfmap"

### place groups into map

bzw.add_object("group halfmap", [ 
        ["name", "red"],
        ["shift", pybzw.Vector(3, [0, 0, 0])],
        ["rotation", 0],
        ["team", 1]
        ])

bzw.add_object("group halfmap", [
        ["name", "green"],
        ["shift", pybzw.Vector(3, [0, 0, 0])],
        ["rotation", 180],
        ["team", 2]
        ])

### platform around the middle

bzw.add_object("box", [
        ["pos",  pybzw.Vector(3, [0, 0, 10])],
        ["size", pybzw.Vector(3, [42, 20, 2])]
        ])

### middle teleporters

bzw.add_object("teleporter mid", [
        ["pos",  pybzw.Vector(3, [0, 0, 0])],
        ["size", pybzw.Vector(3, [0.125, 4, 2.5])],
        ["rotation", 0],
        ["border", 1.0]
        ])

### teleport links

for side in ["red", "green"]:
    bzw.add_object("link", [
            ["from", side + ":base:f"],
            ["to", side + ":platform_outer:b"],
            ])

    bzw.add_object("link", [
            ["from", side + ":platform_outer:*"],
            ["to", side + ":base:f"],
            ])

bzw.add_object("link", [
        ["from", "mid:b"],
        ["to", "red:platform_mid:f"],
        ])

bzw.add_object("link", [
        ["from", "mid:f"],
        ["to", "green:platform_mid:f"],
        ])

### flag safety zones

bzw.add_object("zone", [ # red safety 1
        ["pos",  pybzw.Vector(3, [-114, -190, 1.4])],
        ["size", pybzw.Vector(3, [4, 4, 10])],
        ["safety", 1]
        ])

bzw.add_object("zone", [ # red safety 2
        ["pos",  pybzw.Vector(3, [114, -190, 1.4])],
        ["size", pybzw.Vector(3, [4, 4, 10])],
        ["safety", 1]
        ])

bzw.add_object("zone", [ # green safety 1
        ["pos",  pybzw.Vector(3, [-114, 190, 1.4])],
        ["size", pybzw.Vector(3, [4, 4, 10])],
        ["safety", 1]
        ])

bzw.add_object("zone", [ # green safety 2
        ["pos",  pybzw.Vector(3, [114, 190, 1.4])],
        ["size", pybzw.Vector(3, [4, 4, 10])],
        ["safety", 1]
        ])

### save to the .bzw

bzw.save()
