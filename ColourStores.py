html40colours = """# HTML 4.0 colour names
Black	#000000
Silver	#c0c0c0
Gray	#808080
White	#ffffff
Maroon	#800000
Red	#ff0000
Purple	#800080
Fuchsia	#ff00ff
Green	#008000
Lime	#00ff00
Olive	#808000
Yellow	#ffff00
Navy	#000080
Blue	#0000ff
Teal	#008080
Aqua	#00ffff"""

try:
    namedcolours_f=open("palettes/namedcolors.txt","rU")
except EnvironmentError:
    namedcolours=None
else:
    namedcolours=namedcolours_f.read()
    namedcolours_f.close()

webcolours = """# De-facto NS & MSIE recognized HTML colour names
AliceBlue   	 #f0f8ff
AntiqueWhite   	 #faebd7
Aqua    	 #00ffff
Aquamarine   	 #7fffd4
Azure   	 #f0ffff
Beige   	 #f5f5dc
Bisque   	 #ffe4c4
Black   	 #000000
BlanchedAlmond 	 #ffebcd
Blue    	 #0000ff
BlueViolet   	 #8a2be2
Brown   	 #a52a2a
BurlyWood   	 #deb887
CadetBlue   	 #5f9ea0
Chartreuse   	 #7fff00
Chocolate   	 #d2691e
Coral   	 #ff7f50
CornflowerBlue 	 #6495ed
Cornsilk   	 #fff8dc
Crimson   	 #dc143c
Cyan    	 #00ffff
DarkBlue   	 #00008b
DarkCyan   	 #008b8b
DarkGoldenrod  	 #b8860b
DarkGray   	 #a9a9a9
DarkGreen   	 #006400
DarkKhaki   	 #bdb76b
DarkMagenta   	 #8b008b
DarkOliveGreen 	 #556b2f
DarkOrange   	 #ff8c00
DarkOrchid   	 #9932cc
DarkRed   	 #8b0000
DarkSalmon   	 #e9967a
DarkSeaGreen   	 #8fbc8f
DarkSlateBlue  	 #483d8b
DarkSlateGray  	 #2f4f4f
DarkTurquoise  	 #00ced1
DarkViolet   	 #9400d3
DeepPink   	 #ff1493
DeepSkyBlue   	 #00bfff
DimGray   	 #696969
DodgerBlue   	 #1e90ff
FireBrick   	 #b22222
FloralWhite   	 #fffaf0
ForestGreen   	 #228b22
Fuchsia   	 #ff00ff
Gainsboro   	 #dcdcdc
GhostWhite   	 #f8f8ff
Gold    	 #ffd700
Goldenrod   	 #daa520
Gray    	 #808080
Green   	 #008000
GreenYellow   	 #adff2f
Honeydew   	 #f0fff0
HotPink   	 #ff69b4
IndianRed   	 #cd5c5c
Indigo   	 #4b0082
Ivory   	 #fffff0
Khaki   	 #f0e68c
Lavender   	 #e6e6fa
LavenderBlush  	 #fff0f5
LawnGreen   	 #7cfc00
LemonChiffon   	 #fffacd
LightBlue   	 #add8e6
LightCoral   	 #f08080
LightCyan   	 #e0ffff
LightGoldenrodYellow	#fafad2
LightGreen   	 #90ee90
LightGrey   	 #d3d3d3
LightPink   	 #ffb6c1
LightSalmon   	 #ffa07a
LightSeaGreen  	 #20b2aa
LightSkyBlue   	 #87cefa
LightSlateGray 	 #778899
LightSteelBlue 	 #b0c4de
LightYellow   	 #ffffe0
Lime    	 #00ff00
LimeGreen   	 #32cd32
Linen   	 #faf0e6
Magenta   	 #ff00ff
Maroon   	 #800000
MediumAquamarine #66cdaa
MediumBlue   	 #0000cd
MediumOrchid   	 #ba55d3
MediumPurple   	 #9370db
MediumSeaGreen 	 #3cb371
MediumSlateBlue	 #7b68ee
MediumSpringGreen	#00fa9a
MediumTurquoise	 #48d1cc
MediumVioletRed	 #c71585
MidnightBlue   	 #191970
MintCream   	 #f5fffa
MistyRose   	 #ffe4e1
Moccasin   	 #ffe4b5
NavajoWhite   	 #ffdead
Navy    	 #000080
OldLace   	 #fdf5e6
Olive   	 #808000
OliveDrab   	 #6b8e23
Orange   	 #ffa500
OrangeRed   	 #ff4500
Orchid   	 #da70d6
PaleGoldenrod  	 #eee8aa
PaleGreen   	 #98fb98
PaleTurquoise  	 #afeeee
PaleVioletRed  	 #db7093
PapayaWhip   	 #ffefd5
PeachPuff   	 #ffdab9
Peru    	 #cd853f
Pink    	 #ffc0cb
Plum    	 #dda0dd
PowderBlue   	 #b0e0e6
Purple   	 #800080
Red     	 #ff0000
RosyBrown   	 #bc8f8f
RoyalBlue   	 #4169e1
SaddleBrown   	 #8b4513
Salmon   	 #fa8072
SandyBrown   	 #f4a460
SeaGreen   	 #2e8b57
Seashell   	 #fff5ee
Sienna   	 #a0522d
Silver   	 #c0c0c0
SkyBlue   	 #87ceeb
SlateBlue   	 #6a5acd
SlateGray   	 #708090
Snow    	 #fffafa
SpringGreen   	 #00ff7f
SteelBlue   	 #4682b4
Tan     	 #d2b48c
Teal    	 #008080
Thistle   	 #d8bfd8
Tomato   	 #ff6347
Turquoise   	 #40e0d0
Violet   	 #ee82ee
Wheat   	 #f5deb3
White   	 #ffffff
WhiteSmoke   	 #f5f5f5
Yellow   	 #ffff00
YellowGreen   	 #9acd32"""


websafe = """# Websafe RGB values
#000000
#000033
#000066
#000099
#0000cc
#0000ff
#003300
#003333
#003366
#003399
#0033cc
#0033ff
#006600
#006633
#006666
#006699
#0066cc
#0066ff
#009900
#009933
#009966
#009999
#0099cc
#0099ff
#00cc00
#00cc33
#00cc66
#00cc99
#00cccc
#00ccff
#00ff00
#00ff33
#00ff66
#00ff99
#00ffcc
#00ffff
#330000
#330033
#330066
#330099
#3300cc
#3300ff
#333300
#333333
#333366
#333399
#3333cc
#3333ff
#336600
#336633
#336666
#336699
#3366cc
#3366ff
#339900
#339933
#339966
#339999
#3399cc
#3399ff
#33cc00
#33cc33
#33cc66
#33cc99
#33cccc
#33ccff
#33ff00
#33ff33
#33ff66
#33ff99
#33ffcc
#33ffff
#660000
#660033
#660066
#660099
#6600cc
#6600ff
#663300
#663333
#663366
#663399
#6633cc
#6633ff
#666600
#666633
#666666
#666699
#6666cc
#6666ff
#669900
#669933
#669966
#669999
#6699cc
#6699ff
#66cc00
#66cc33
#66cc66
#66cc99
#66cccc
#66ccff
#66ff00
#66ff33
#66ff66
#66ff99
#66ffcc
#66ffff
#990000
#990033
#990066
#990099
#9900cc
#9900ff
#993300
#993333
#993366
#993399
#9933cc
#9933ff
#996600
#996633
#996666
#996699
#9966cc
#9966ff
#999900
#999933
#999966
#999999
#9999cc
#9999ff
#99cc00
#99cc33
#99cc66
#99cc99
#99cccc
#99ccff
#99ff00
#99ff33
#99ff66
#99ff99
#99ffcc
#99ffff
#cc0000
#cc0033
#cc0066
#cc0099
#cc00cc
#cc00ff
#cc3300
#cc3333
#cc3366
#cc3399
#cc33cc
#cc33ff
#cc6600
#cc6633
#cc6666
#cc6699
#cc66cc
#cc66ff
#cc9900
#cc9933
#cc9966
#cc9999
#cc99cc
#cc99ff
#cccc00
#cccc33
#cccc66
#cccc99
#cccccc
#ccccff
#ccff00
#ccff33
#ccff66
#ccff99
#ccffcc
#ccffff
#ff0000
#ff0033
#ff0066
#ff0099
#ff00cc
#ff00ff
#ff3300
#ff3333
#ff3366
#ff3399
#ff33cc
#ff33ff
#ff6600
#ff6633
#ff6666
#ff6699
#ff66cc
#ff66ff
#ff9900
#ff9933
#ff9966
#ff9999
#ff99cc
#ff99ff
#ffcc00
#ffcc33
#ffcc66
#ffcc99
#ffcccc
#ffccff
#ffff00
#ffff33
#ffff66
#ffff99
#ffffcc
#ffffff"""


#The string below is from X Windowsystem which is subject to the following
#terms:
#
#    Copyright (C) 1994 X Consortium
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to
#    deal in the Software without restriction, including without limitation the
#    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#    sell copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
#    X CONSORTIUM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
#    AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNEC-
#    TION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#    Except as contained in this notice, the name of the X Consortium shall not
#    be used in advertising or otherwise to promote the sale, use or other deal-
#    ings in this Software without prior written authorization from the X Consor-
#    tium.
#
#    X Window System is a trademark of X Consortium, Inc.
#
#Actually, nowadays
#
#    X Window System is a trademark of The Open Group
#
xrgb = """! $XConsortium: rgb.txt,v 10.41 94/02/20 18:39:36 rws Exp $
255 250 250		snow
248 248 255		ghost white
248 248 255		GhostWhite
245 245 245		white smoke
245 245 245		WhiteSmoke
220 220 220		gainsboro
255 250 240		floral white
255 250 240		FloralWhite
253 245 230		old lace
253 245 230		OldLace
250 240 230		linen
250 235 215		antique white
250 235 215		AntiqueWhite
255 239 213		papaya whip
255 239 213		PapayaWhip
255 235 205		blanched almond
255 235 205		BlanchedAlmond
255 228 196		bisque
255 218 185		peach puff
255 218 185		PeachPuff
255 222 173		navajo white
255 222 173		NavajoWhite
255 228 181		moccasin
255 248 220		cornsilk
255 255 240		ivory
255 250 205		lemon chiffon
255 250 205		LemonChiffon
255 245 238		seashell
240 255 240		honeydew
245 255 250		mint cream
245 255 250		MintCream
240 255 255		azure
240 248 255		alice blue
240 248 255		AliceBlue
230 230 250		lavender
255 240 245		lavender blush
255 240 245		LavenderBlush
255 228 225		misty rose
255 228 225		MistyRose
255 255 255		white
  0   0   0		black
 47  79  79		dark slate gray
 47  79  79		DarkSlateGray
 47  79  79		dark slate grey
 47  79  79		DarkSlateGrey
105 105 105		dim gray
105 105 105		DimGray
105 105 105		dim grey
105 105 105		DimGrey
112 128 144		slate gray
112 128 144		SlateGray
112 128 144		slate grey
112 128 144		SlateGrey
119 136 153		light slate gray
119 136 153		LightSlateGray
119 136 153		light slate grey
119 136 153		LightSlateGrey
190 190 190		gray
190 190 190		grey
211 211 211		light grey
211 211 211		LightGrey
211 211 211		light gray
211 211 211		LightGray
 25  25 112		midnight blue
 25  25 112		MidnightBlue
  0   0 128		navy
  0   0 128		navy blue
  0   0 128		NavyBlue
100 149 237		cornflower blue
100 149 237		CornflowerBlue
 72  61 139		dark slate blue
 72  61 139		DarkSlateBlue
106  90 205		slate blue
106  90 205		SlateBlue
123 104 238		medium slate blue
123 104 238		MediumSlateBlue
132 112 255		light slate blue
132 112 255		LightSlateBlue
  0   0 205		medium blue
  0   0 205		MediumBlue
 65 105 225		royal blue
 65 105 225		RoyalBlue
  0   0 255		blue
 30 144 255		dodger blue
 30 144 255		DodgerBlue
  0 191 255		deep sky blue
  0 191 255		DeepSkyBlue
135 206 235		sky blue
135 206 235		SkyBlue
135 206 250		light sky blue
135 206 250		LightSkyBlue
 70 130 180		steel blue
 70 130 180		SteelBlue
176 196 222		light steel blue
176 196 222		LightSteelBlue
173 216 230		light blue
173 216 230		LightBlue
176 224 230		powder blue
176 224 230		PowderBlue
175 238 238		pale turquoise
175 238 238		PaleTurquoise
  0 206 209		dark turquoise
  0 206 209		DarkTurquoise
 72 209 204		medium turquoise
 72 209 204		MediumTurquoise
 64 224 208		turquoise
  0 255 255		cyan
224 255 255		light cyan
224 255 255		LightCyan
 95 158 160		cadet blue
 95 158 160		CadetBlue
102 205 170		medium aquamarine
102 205 170		MediumAquamarine
127 255 212		aquamarine
  0 100   0		dark green
  0 100   0		DarkGreen
 85 107  47		dark olive green
 85 107  47		DarkOliveGreen
143 188 143		dark sea green
143 188 143		DarkSeaGreen
 46 139  87		sea green
 46 139  87		SeaGreen
 60 179 113		medium sea green
 60 179 113		MediumSeaGreen
 32 178 170		light sea green
 32 178 170		LightSeaGreen
152 251 152		pale green
152 251 152		PaleGreen
  0 255 127		spring green
  0 255 127		SpringGreen
124 252   0		lawn green
124 252   0		LawnGreen
  0 255   0		green
127 255   0		chartreuse
  0 250 154		medium spring green
  0 250 154		MediumSpringGreen
173 255  47		green yellow
173 255  47		GreenYellow
 50 205  50		lime green
 50 205  50		LimeGreen
154 205  50		yellow green
154 205  50		YellowGreen
 34 139  34		forest green
 34 139  34		ForestGreen
107 142  35		olive drab
107 142  35		OliveDrab
189 183 107		dark khaki
189 183 107		DarkKhaki
240 230 140		khaki
238 232 170		pale goldenrod
238 232 170		PaleGoldenrod
250 250 210		light goldenrod yellow
250 250 210		LightGoldenrodYellow
255 255 224		light yellow
255 255 224		LightYellow
255 255   0		yellow
255 215   0 		gold
238 221 130		light goldenrod
238 221 130		LightGoldenrod
218 165  32		goldenrod
184 134  11		dark goldenrod
184 134  11		DarkGoldenrod
188 143 143		rosy brown
188 143 143		RosyBrown
205  92  92		indian red
205  92  92		IndianRed
139  69  19		saddle brown
139  69  19		SaddleBrown
160  82  45		sienna
205 133  63		peru
222 184 135		burlywood
245 245 220		beige
245 222 179		wheat
244 164  96		sandy brown
244 164  96		SandyBrown
210 180 140		tan
210 105  30		chocolate
178  34  34		firebrick
165  42  42		brown
233 150 122		dark salmon
233 150 122		DarkSalmon
250 128 114		salmon
255 160 122		light salmon
255 160 122		LightSalmon
255 165   0		orange
255 140   0		dark orange
255 140   0		DarkOrange
255 127  80		coral
240 128 128		light coral
240 128 128		LightCoral
255  99  71		tomato
255  69   0		orange red
255  69   0		OrangeRed
255   0   0		red
255 105 180		hot pink
255 105 180		HotPink
255  20 147		deep pink
255  20 147		DeepPink
255 192 203		pink
255 182 193		light pink
255 182 193		LightPink
219 112 147		pale violet red
219 112 147		PaleVioletRed
176  48  96		maroon
199  21 133		medium violet red
199  21 133		MediumVioletRed
208  32 144		violet red
208  32 144		VioletRed
255   0 255		magenta
238 130 238		violet
221 160 221		plum
218 112 214		orchid
186  85 211		medium orchid
186  85 211		MediumOrchid
153  50 204		dark orchid
153  50 204		DarkOrchid
148   0 211		dark violet
148   0 211		DarkViolet
138  43 226		blue violet
138  43 226		BlueViolet
160  32 240		purple
147 112 219		medium purple
147 112 219		MediumPurple
216 191 216		thistle
255 250 250		snow1
238 233 233		snow2
205 201 201		snow3
139 137 137		snow4
255 245 238		seashell1
238 229 222		seashell2
205 197 191		seashell3
139 134 130		seashell4
255 239 219		AntiqueWhite1
238 223 204		AntiqueWhite2
205 192 176		AntiqueWhite3
139 131 120		AntiqueWhite4
255 228 196		bisque1
238 213 183		bisque2
205 183 158		bisque3
139 125 107		bisque4
255 218 185		PeachPuff1
238 203 173		PeachPuff2
205 175 149		PeachPuff3
139 119 101		PeachPuff4
255 222 173		NavajoWhite1
238 207 161		NavajoWhite2
205 179 139		NavajoWhite3
139 121  94		NavajoWhite4
255 250 205		LemonChiffon1
238 233 191		LemonChiffon2
205 201 165		LemonChiffon3
139 137 112		LemonChiffon4
255 248 220		cornsilk1
238 232 205		cornsilk2
205 200 177		cornsilk3
139 136 120		cornsilk4
255 255 240		ivory1
238 238 224		ivory2
205 205 193		ivory3
139 139 131		ivory4
240 255 240		honeydew1
224 238 224		honeydew2
193 205 193		honeydew3
131 139 131		honeydew4
255 240 245		LavenderBlush1
238 224 229		LavenderBlush2
205 193 197		LavenderBlush3
139 131 134		LavenderBlush4
255 228 225		MistyRose1
238 213 210		MistyRose2
205 183 181		MistyRose3
139 125 123		MistyRose4
240 255 255		azure1
224 238 238		azure2
193 205 205		azure3
131 139 139		azure4
131 111 255		SlateBlue1
122 103 238		SlateBlue2
105  89 205		SlateBlue3
 71  60 139		SlateBlue4
 72 118 255		RoyalBlue1
 67 110 238		RoyalBlue2
 58  95 205		RoyalBlue3
 39  64 139		RoyalBlue4
  0   0 255		blue1
  0   0 238		blue2
  0   0 205		blue3
  0   0 139		blue4
 30 144 255		DodgerBlue1
 28 134 238		DodgerBlue2
 24 116 205		DodgerBlue3
 16  78 139		DodgerBlue4
 99 184 255		SteelBlue1
 92 172 238		SteelBlue2
 79 148 205		SteelBlue3
 54 100 139		SteelBlue4
  0 191 255		DeepSkyBlue1
  0 178 238		DeepSkyBlue2
  0 154 205		DeepSkyBlue3
  0 104 139		DeepSkyBlue4
135 206 255		SkyBlue1
126 192 238		SkyBlue2
108 166 205		SkyBlue3
 74 112 139		SkyBlue4
176 226 255		LightSkyBlue1
164 211 238		LightSkyBlue2
141 182 205		LightSkyBlue3
 96 123 139		LightSkyBlue4
198 226 255		SlateGray1
185 211 238		SlateGray2
159 182 205		SlateGray3
108 123 139		SlateGray4
202 225 255		LightSteelBlue1
188 210 238		LightSteelBlue2
162 181 205		LightSteelBlue3
110 123 139		LightSteelBlue4
191 239 255		LightBlue1
178 223 238		LightBlue2
154 192 205		LightBlue3
104 131 139		LightBlue4
224 255 255		LightCyan1
209 238 238		LightCyan2
180 205 205		LightCyan3
122 139 139		LightCyan4
187 255 255		PaleTurquoise1
174 238 238		PaleTurquoise2
150 205 205		PaleTurquoise3
102 139 139		PaleTurquoise4
152 245 255		CadetBlue1
142 229 238		CadetBlue2
122 197 205		CadetBlue3
 83 134 139		CadetBlue4
  0 245 255		turquoise1
  0 229 238		turquoise2
  0 197 205		turquoise3
  0 134 139		turquoise4
  0 255 255		cyan1
  0 238 238		cyan2
  0 205 205		cyan3
  0 139 139		cyan4
151 255 255		DarkSlateGray1
141 238 238		DarkSlateGray2
121 205 205		DarkSlateGray3
 82 139 139		DarkSlateGray4
127 255 212		aquamarine1
118 238 198		aquamarine2
102 205 170		aquamarine3
 69 139 116		aquamarine4
193 255 193		DarkSeaGreen1
180 238 180		DarkSeaGreen2
155 205 155		DarkSeaGreen3
105 139 105		DarkSeaGreen4
 84 255 159		SeaGreen1
 78 238 148		SeaGreen2
 67 205 128		SeaGreen3
 46 139	 87		SeaGreen4
154 255 154		PaleGreen1
144 238 144		PaleGreen2
124 205 124		PaleGreen3
 84 139	 84		PaleGreen4
  0 255 127		SpringGreen1
  0 238 118		SpringGreen2
  0 205 102		SpringGreen3
  0 139	 69		SpringGreen4
  0 255	  0		green1
  0 238	  0		green2
  0 205	  0		green3
  0 139	  0		green4
127 255	  0		chartreuse1
118 238	  0		chartreuse2
102 205	  0		chartreuse3
 69 139	  0		chartreuse4
192 255	 62		OliveDrab1
179 238	 58		OliveDrab2
154 205	 50		OliveDrab3
105 139	 34		OliveDrab4
202 255 112		DarkOliveGreen1
188 238 104		DarkOliveGreen2
162 205	 90		DarkOliveGreen3
110 139	 61		DarkOliveGreen4
255 246 143		khaki1
238 230 133		khaki2
205 198 115		khaki3
139 134	 78		khaki4
255 236 139		LightGoldenrod1
238 220 130		LightGoldenrod2
205 190 112		LightGoldenrod3
139 129	 76		LightGoldenrod4
255 255 224		LightYellow1
238 238 209		LightYellow2
205 205 180		LightYellow3
139 139 122		LightYellow4
255 255	  0		yellow1
238 238	  0		yellow2
205 205	  0		yellow3
139 139	  0		yellow4
255 215	  0		gold1
238 201	  0		gold2
205 173	  0		gold3
139 117	  0		gold4
255 193	 37		goldenrod1
238 180	 34		goldenrod2
205 155	 29		goldenrod3
139 105	 20		goldenrod4
255 185	 15		DarkGoldenrod1
238 173	 14		DarkGoldenrod2
205 149	 12		DarkGoldenrod3
139 101	  8		DarkGoldenrod4
255 193 193		RosyBrown1
238 180 180		RosyBrown2
205 155 155		RosyBrown3
139 105 105		RosyBrown4
255 106 106		IndianRed1
238  99	 99		IndianRed2
205  85	 85		IndianRed3
139  58	 58		IndianRed4
255 130	 71		sienna1
238 121	 66		sienna2
205 104	 57		sienna3
139  71	 38		sienna4
255 211 155		burlywood1
238 197 145		burlywood2
205 170 125		burlywood3
139 115	 85		burlywood4
255 231 186		wheat1
238 216 174		wheat2
205 186 150		wheat3
139 126 102		wheat4
255 165	 79		tan1
238 154	 73		tan2
205 133	 63		tan3
139  90	 43		tan4
255 127	 36		chocolate1
238 118	 33		chocolate2
205 102	 29		chocolate3
139  69	 19		chocolate4
255  48	 48		firebrick1
238  44	 44		firebrick2
205  38	 38		firebrick3
139  26	 26		firebrick4
255  64	 64		brown1
238  59	 59		brown2
205  51	 51		brown3
139  35	 35		brown4
255 140 105		salmon1
238 130	 98		salmon2
205 112	 84		salmon3
139  76	 57		salmon4
255 160 122		LightSalmon1
238 149 114		LightSalmon2
205 129	 98		LightSalmon3
139  87	 66		LightSalmon4
255 165	  0		orange1
238 154	  0		orange2
205 133	  0		orange3
139  90	  0		orange4
255 127	  0		DarkOrange1
238 118	  0		DarkOrange2
205 102	  0		DarkOrange3
139  69	  0		DarkOrange4
255 114	 86		coral1
238 106	 80		coral2
205  91	 69		coral3
139  62	 47		coral4
255  99	 71		tomato1
238  92	 66		tomato2
205  79	 57		tomato3
139  54	 38		tomato4
255  69	  0		OrangeRed1
238  64	  0		OrangeRed2
205  55	  0		OrangeRed3
139  37	  0		OrangeRed4
255   0	  0		red1
238   0	  0		red2
205   0	  0		red3
139   0	  0		red4
255  20 147		DeepPink1
238  18 137		DeepPink2
205  16 118		DeepPink3
139  10	 80		DeepPink4
255 110 180		HotPink1
238 106 167		HotPink2
205  96 144		HotPink3
139  58  98		HotPink4
255 181 197		pink1
238 169 184		pink2
205 145 158		pink3
139  99 108		pink4
255 174 185		LightPink1
238 162 173		LightPink2
205 140 149		LightPink3
139  95 101		LightPink4
255 130 171		PaleVioletRed1
238 121 159		PaleVioletRed2
205 104 137		PaleVioletRed3
139  71	 93		PaleVioletRed4
255  52 179		maroon1
238  48 167		maroon2
205  41 144		maroon3
139  28	 98		maroon4
255  62 150		VioletRed1
238  58 140		VioletRed2
205  50 120		VioletRed3
139  34	 82		VioletRed4
255   0 255		magenta1
238   0 238		magenta2
205   0 205		magenta3
139   0 139		magenta4
255 131 250		orchid1
238 122 233		orchid2
205 105 201		orchid3
139  71 137		orchid4
255 187 255		plum1
238 174 238		plum2
205 150 205		plum3
139 102 139		plum4
224 102 255		MediumOrchid1
209  95 238		MediumOrchid2
180  82 205		MediumOrchid3
122  55 139		MediumOrchid4
191  62 255		DarkOrchid1
178  58 238		DarkOrchid2
154  50 205		DarkOrchid3
104  34 139		DarkOrchid4
155  48 255		purple1
145  44 238		purple2
125  38 205		purple3
 85  26 139		purple4
171 130 255		MediumPurple1
159 121 238		MediumPurple2
137 104 205		MediumPurple3
 93  71 139		MediumPurple4
255 225 255		thistle1
238 210 238		thistle2
205 181 205		thistle3
139 123 139		thistle4
  0   0   0		gray0
  0   0   0		grey0
  3   3   3		gray1
  3   3   3		grey1
  5   5   5		gray2
  5   5   5		grey2
  8   8   8		gray3
  8   8   8		grey3
 10  10  10 		gray4
 10  10  10 		grey4
 13  13  13 		gray5
 13  13  13 		grey5
 15  15  15 		gray6
 15  15  15 		grey6
 18  18  18 		gray7
 18  18  18 		grey7
 20  20  20 		gray8
 20  20  20 		grey8
 23  23  23 		gray9
 23  23  23 		grey9
 26  26  26 		gray10
 26  26  26 		grey10
 28  28  28 		gray11
 28  28  28 		grey11
 31  31  31 		gray12
 31  31  31 		grey12
 33  33  33 		gray13
 33  33  33 		grey13
 36  36  36 		gray14
 36  36  36 		grey14
 38  38  38 		gray15
 38  38  38 		grey15
 41  41  41 		gray16
 41  41  41 		grey16
 43  43  43 		gray17
 43  43  43 		grey17
 46  46  46 		gray18
 46  46  46 		grey18
 48  48  48 		gray19
 48  48  48 		grey19
 51  51  51 		gray20
 51  51  51 		grey20
 54  54  54 		gray21
 54  54  54 		grey21
 56  56  56 		gray22
 56  56  56 		grey22
 59  59  59 		gray23
 59  59  59 		grey23
 61  61  61 		gray24
 61  61  61 		grey24
 64  64  64 		gray25
 64  64  64 		grey25
 66  66  66 		gray26
 66  66  66 		grey26
 69  69  69 		gray27
 69  69  69 		grey27
 71  71  71 		gray28
 71  71  71 		grey28
 74  74  74 		gray29
 74  74  74 		grey29
 77  77  77 		gray30
 77  77  77 		grey30
 79  79  79 		gray31
 79  79  79 		grey31
 82  82  82 		gray32
 82  82  82 		grey32
 84  84  84 		gray33
 84  84  84 		grey33
 87  87  87 		gray34
 87  87  87 		grey34
 89  89  89 		gray35
 89  89  89 		grey35
 92  92  92 		gray36
 92  92  92 		grey36
 94  94  94 		gray37
 94  94  94 		grey37
 97  97  97 		gray38
 97  97  97 		grey38
 99  99  99 		gray39
 99  99  99 		grey39
102 102 102 		gray40
102 102 102 		grey40
105 105 105 		gray41
105 105 105 		grey41
107 107 107 		gray42
107 107 107 		grey42
110 110 110 		gray43
110 110 110 		grey43
112 112 112 		gray44
112 112 112 		grey44
115 115 115 		gray45
115 115 115 		grey45
117 117 117 		gray46
117 117 117 		grey46
120 120 120 		gray47
120 120 120 		grey47
122 122 122 		gray48
122 122 122 		grey48
125 125 125 		gray49
125 125 125 		grey49
127 127 127 		gray50
127 127 127 		grey50
130 130 130 		gray51
130 130 130 		grey51
133 133 133 		gray52
133 133 133 		grey52
135 135 135 		gray53
135 135 135 		grey53
138 138 138 		gray54
138 138 138 		grey54
140 140 140 		gray55
140 140 140 		grey55
143 143 143 		gray56
143 143 143 		grey56
145 145 145 		gray57
145 145 145 		grey57
148 148 148 		gray58
148 148 148 		grey58
150 150 150 		gray59
150 150 150 		grey59
153 153 153 		gray60
153 153 153 		grey60
156 156 156 		gray61
156 156 156 		grey61
158 158 158 		gray62
158 158 158 		grey62
161 161 161 		gray63
161 161 161 		grey63
163 163 163 		gray64
163 163 163 		grey64
166 166 166 		gray65
166 166 166 		grey65
168 168 168 		gray66
168 168 168 		grey66
171 171 171 		gray67
171 171 171 		grey67
173 173 173 		gray68
173 173 173 		grey68
176 176 176 		gray69
176 176 176 		grey69
179 179 179 		gray70
179 179 179 		grey70
181 181 181 		gray71
181 181 181 		grey71
184 184 184 		gray72
184 184 184 		grey72
186 186 186 		gray73
186 186 186 		grey73
189 189 189 		gray74
189 189 189 		grey74
191 191 191 		gray75
191 191 191 		grey75
194 194 194 		gray76
194 194 194 		grey76
196 196 196 		gray77
196 196 196 		grey77
199 199 199 		gray78
199 199 199 		grey78
201 201 201 		gray79
201 201 201 		grey79
204 204 204 		gray80
204 204 204 		grey80
207 207 207 		gray81
207 207 207 		grey81
209 209 209 		gray82
209 209 209 		grey82
212 212 212 		gray83
212 212 212 		grey83
214 214 214 		gray84
214 214 214 		grey84
217 217 217 		gray85
217 217 217 		grey85
219 219 219 		gray86
219 219 219 		grey86
222 222 222 		gray87
222 222 222 		grey87
224 224 224 		gray88
224 224 224 		grey88
227 227 227 		gray89
227 227 227 		grey89
229 229 229 		gray90
229 229 229 		grey90
232 232 232 		gray91
232 232 232 		grey91
235 235 235 		gray92
235 235 235 		grey92
237 237 237 		gray93
237 237 237 		grey93
240 240 240 		gray94
240 240 240 		grey94
242 242 242 		gray95
242 242 242 		grey95
245 245 245 		gray96
245 245 245 		grey96
247 247 247 		gray97
247 247 247 		grey97
250 250 250 		gray98
250 250 250 		grey98
252 252 252 		gray99
252 252 252 		grey99
255 255 255 		gray100
255 255 255 		grey100
169 169 169		dark grey
169 169 169		DarkGrey
169 169 169		dark gray
169 169 169		DarkGray
0     0 139		dark blue
0     0 139		DarkBlue
0   139 139		dark cyan
0   139 139		DarkCyan
139   0 139		dark magenta
139   0 139		DarkMagenta
139   0   0		dark red
139   0   0		DarkRed
144 238 144		light green
144 238 144		LightGreen"""

try:
    cryolacrayon_f=open("palettes/crayolacrayon.txt","rU")
except EnvironmentError:
    cryolacrayon=None
else:
    cryolacrayon=cryolacrayon_f.read()
    cryolacrayon_f.close()

try:
    cryolametalfx_f=open("palettes/crayolametalicfx.txt","rU")
except EnvironmentError:
    cryolametalfx=None
else:
    cryolametalfx=cryolametalfx_f.read()
    cryolametalfx_f.close()

try:
    cryolasilver_f=open("palettes/crayolasilver.txt","rU")
except EnvironmentError:
    cryolasilver=None
else:
    cryolasilver=cryolasilver_f.read()
    cryolasilver_f.close()

try:
    cryolagems_f=open("palettes/crayolagems.txt","rU")
except EnvironmentError:
    cryolagems=None
else:
    cryolagems=cryolagems_f.read()
    cryolagems_f.close()

try:
    cryolamscent_f=open("palettes/crayolamagicscent.txt","rU")
except EnvironmentError:
    cryolamscent=None
else:
    cryolamscent=cryolamscent_f.read()
    cryolamscent_f.close()

try:
    isccnbsdict_f=open("palettes/isccnbs.txt","rU")
except EnvironmentError:
    isccnbsdict=None
else:
    isccnbsdict=isccnbsdict_f.read()
    isccnbsdict_f.close()

try:
    xona_db_f=open("palettes/Xona.txt","rU")
except EnvironmentError:
    xona_db=None
else:
    xona_db=xona_db_f.read()
    xona_db_f.close()

from ColourDB import get_colourdb_string,ColourDB

xrgb=get_colourdb_string("xrgb",xrgb)
if isccnbsdict: isccnbsdict=get_colourdb_string("isccnbsdict",isccnbsdict)
if cryolacrayon: cryolacrayon=get_colourdb_string("cryolacrayon",cryolacrayon)
if cryolamscent: cryolamscent=get_colourdb_string("cryolamscent",cryolamscent)
if cryolametalfx: cryolametalfx=get_colourdb_string("cryolametalfx",cryolametalfx)
if cryolasilver: cryolasilver=get_colourdb_string("cryolasilver",cryolasilver)
if cryolagems: cryolagems=get_colourdb_string("cryolagems",cryolagems)
if namedcolours: namedcolours=get_colourdb_string("namedcolours",namedcolours)
html40colours=get_colourdb_string("html",html40colours)
webcolours=get_colourdb_string("web",webcolours)
websafe=get_colourdb_string("safe",websafe)
if xona_db: xona_db=get_colourdb_string("xona_db",xona_db)

def special_update(out,in_):
    for key in in_.keys():
        if key in out.keys():
            r1,g1,b1=in_[key]
            r2,g2,b2=out[key]
            out[key]=((r1+r2)//2,(g1+g2)//2,(b1+b2)//2) #i.e. approximate mean.
        else:
            out[key]=in_[key]

unicolour={}
if isccnbsdict: special_update(unicolour,isccnbsdict._ColourDB__byname.copy())  #Base
if cryolametalfx: special_update(unicolour,cryolametalfx._ColourDB__byname.copy())#Very Extra
if cryolasilver: special_update(unicolour,cryolasilver._ColourDB__byname.copy()) #Very Extra
if cryolagems: special_update(unicolour,cryolagems._ColourDB__byname.copy())   #Very Extra
if cryolamscent: special_update(unicolour,cryolamscent._ColourDB__byname.copy()) #Very Extra
if namedcolours: special_update(unicolour,namedcolours._ColourDB__byname.copy()) #Extra
if cryolacrayon: special_update(unicolour,cryolacrayon._ColourDB__byname.copy()) #Extra
if xona_db: special_update(unicolour,xona_db._ColourDB__byname.copy()) #Extra
special_update(unicolour,xrgb._ColourDB__byname.copy())         #Canonical
special_update(unicolour,webcolours._ColourDB__byname.copy())   #Common
#websafe irrelevant
special_update(unicolour,html40colours._ColourDB__byname.copy())#Standard

unicolour["rich maroon"]=unicolour["richmaroon"]=unicolour["maroon x11"]=unicolour["maroonx11"]=xrgb.find_byname("maroon")
unicolour["maroon5"]=unicolour["maroon"]
unicolour["purple x11"]=unicolour["purplex11"]=xrgb.find_byname("purple")
unicolour["gray x11"]=unicolour["grayx11"]=unicolour["grey x11"]=unicolour["greyx11"]=xrgb.find_byname("gray")
unicolour["light gray x11"]=unicolour["lightgrayx11"]=unicolour["light grey x11"]=unicolour["lightgreyx11"]=xrgb.find_byname("lightgray")
# Comes up as BronzeIi (capital then lowercase I), looks like "Bronzeli"
# Inconsistant with other naming convention (X11) and only "2" in LL-Xine compared to many numbers in X11
unicolour["bronze2"]=unicolour["bronze ii"]
del unicolour["bronze ii"]

#Additions for humorous or cultural effect
unicolour["pygmie puffskn"]=unicolour["pygmiepuffskn"]=unicolour["deeppink2"]

#Add camel names
CamelHelper={}
for i in unicolour.keys():
	if " " in i:
		CamelHelper[i.replace(" ","").lower()]=i
def cptlz(s):
	return s[0].upper()+s[1:].lower()
for i in unicolour.keys():
	#Add spaces to numbered names
	nonumber=i.rstrip("0123456789")
	number=i[len(nonumber):]
	if number and (nonumber in CamelHelper):
		i2=CamelHelper[nonumber.lower()]+" "+number
		unicolour[i2]=unicolour[i]
		i=i2
	#Camelize
	j=i.replace("-"," ").split()
	j=map(lambda s:cptlz(s),j)
	j="".join(j)
	unicolour[j]=unicolour[i]
	if j.lower()!=i:
		unicolour[j.lower()]=unicolour[j] #Just In Case
for j in unicolour.keys():
	if "'" in j:
		unicolour[j.replace("'","")]=unicolour[j]

#class alertah(dict):
#	def __getitem__(self,n):
#		if n in self.keys():
#			return dict.__getitem__(self,n)
#		else:
#			print "KLAXON!!!!",n
#			return (0,0,0)
#unicolour=alertah(unicolour)

def count_caps_and_apostrophes(str):
	caps=0
	for cap in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'":
		caps+=str.count(cap)
	return caps

def filter_aliases(truename,aliases):
	"""Remove overdefinitions (in a case insensitive world) from aliases"""
	done_lowercase=[]
	got={}
	for j in aliases:
		if j.lower() in done_lowercase:
			got[j.lower()].append(j)
		elif j.lower()==truename.lower():
			pass
		else:
			done_lowercase.append(j.lower())
			got[j.lower()]=[j]
	aliases2=[]
	for nameset in got.values():
		mostcaps=0
		mostcapsname=nameset[0] #Default to an arbitary one
		for i in nameset:
			i_caps=count_caps_and_apostrophes(i)
			if i_caps>mostcaps:
				mostcaps=i_caps
				mostcapsname=i
		aliases2.append(mostcapsname)
	return truename,aliases2

def get_priority(name):
	#Would this be described as bayesian?
	priority=0
	priority-=len(name)
	priority-=count_caps_and_apostrophes(name)
	if "dark" in name.lower():
		priority-=100
	if "medium" in name.lower():
		priority-=100
	if "light" in name.lower():
		priority-=100
	if "ultra" in name.lower():
		priority-=100
	if "gray" in name.lower():
		priority-=5
	if "grey" in name.lower():
		priority-=210
	if name[-1] in "0123456789 ":
		priority-=200
	return priority

class DictColourDB(ColourDB):
	def __init__(self,byname):
		#In DictColourDB not ColourDB so names must be premangled
		self._ColourDB__byname=byname
		byrgb1={}
		for i in byname.keys():
			if byname[i] in byrgb1.keys():
				byrgb1[byname[i]].append(i)
			else:
				byrgb1[byname[i]] = [i]
		byrgb={}
		for i in byrgb1.keys():
			aliases=byrgb1[i]
			truename=None
			abort=False
			for j in aliases:
				if j in html40colours._ColourDB__byname.keys():
					if j.title() in aliases:
						aliases.remove(j.title())
					truename=j.title()
					abort=True
					break
			if abort: #Meaning a W3C standard name is present
				byrgb[i]=filter_aliases(truename,aliases)
			else:
				aliases=filter_aliases("",aliases)[1]
				shortlist=[]
				for j in aliases:
					if j[0].isupper():
						shortlist.append(j)
				if not shortlist:
					#print aliases
					shortlist=list(aliases)
				shortlist.sort(key=get_priority,reverse=True)
				truename=shortlist[0]
				#print truename,aliases,shortlist
				aliases.remove(truename)
				byrgb[i]=(truename,aliases)
		self._ColourDB__byrgb=byrgb
		self._ColourDB__allnames=None
		self._ColourDB__name="palettes/(Internal)"

unicolour=DictColourDB(unicolour)
