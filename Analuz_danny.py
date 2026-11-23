import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_text = """Cannon Cart
1
Cannon Cart
58
Rating
5%
Usage
-0.3 %
54%
Win
-1.2 %
54%
CWR
Rascals
2
Rascals
58
Rating
5%
Usage
-0.2 %
53%
Win
-1.0 %
53%
CWR
Heal Spirit
3
Heal Spirit
57
Rating
7%
Usage
+1.0 %
53%
Win
-1.1 %
53%
CWR
Battle Ram Evolution
4
Battle Ram Evolution
57
Rating
9%
Usage
-0.0 %
53%
Win
-0.1 %
53%
CWR
Bandit
5
Bandit
57
Rating
10%
Usage
+1.1 %
53%
Win
-1.0 %
53%
CWR
Mortar Evolution
6
Mortar Evolution
57
Rating
5%
Usage
-1.2 %
53%
Win
+1.1 %
53%
CWR
Giant Skeleton
7
Giant Skeleton
56
Rating
8%
Usage
+0.9 %
53%
Win
-0.6 %
53%
CWR
Furnace
8
Furnace
56
Rating
8%
Usage
+1.4 %
52%
Win
-1.0 %
52%
CWR
Lumberjack Evolution
9
Lumberjack Evolution
55
Rating
7%
Usage
+0.9 %
52%
Win
-0.9 %
52%
CWR
Barbarian Barrel
10
Barbarian Barrel
55
Rating
24%
Usage
+2.1 %
52%
Win
-1.0 %
52%
CWR
Zap Evolution
11
Zap Evolution
55
Rating
7%
Usage
+0.1 %
52%
Win
-0.9 %
52%
CWR
Zappies
12
Zappies
55
Rating
5%
Usage
+0.3 %
52%
Win
-0.8 %
52%
CWR
Hero Goblins
13
Hero Goblins
55
Rating
2%
Usage
+0.1 %
52%
Win
-0.6 %
52%
CWR
Lava Hound
14
Lava Hound
55
Rating
2%
Usage
+0.3 %
52%
Win
-1.4 %
52%
CWR
Hero Electro Wizard
15
Hero Electro Wizard
55
Rating
10%
Usage
+1.2 %
52%
Win
-0.5 %
52%
CWR
Bowler
16
Bowler
54
Rating
2%
Usage
+0.2 %
52%
Win
-0.3 %
52%
CWR
Mother Witch
17
Mother Witch
54
Rating
6%
Usage
+1.2 %
52%
Win
-0.5 %
52%
CWR
Skeleton Barrel Evolution
18
Skeleton Barrel Evolution
54
Rating
7%
Usage
-0.4 %
52%
Win
-0.6 %
52%
CWR
Goblin Cage Evolution
19
Goblin Cage Evolution
54
Rating
2%
Usage
-0.0 %
52%
Win
-0.8 %
52%
CWR
Hero Ice Wizard
20
Hero Ice Wizard
54
Rating
12%
Usage
+0.6 %
52%
Win
-0.4 %
52%
CWR
Baby Dragon Evolution
21
Baby Dragon Evolution
54
Rating
6%
Usage
+0.6 %
52%
Win
-1.0 %
52%
CWR
Royal Ghost Evolution
22
Royal Ghost Evolution
54
Rating
6%
Usage
+1.0 %
52%
Win
-1.5 %
52%
CWR
Graveyard
23
Graveyard
54
Rating
7%
Usage
+1.1 %
52%
Win
-0.9 %
52%
CWR
Suspicious Bush
24
Suspicious Bush
54
Rating
2%
Usage
+0.0 %
52%
Win
-0.1 %
52%
CWR
Skeleton Dragons
25
Skeleton Dragons
54
Rating
3%
Usage
+0.3 %
52%
Win
-0.8 %
52%
CWR
Golem
26
Golem
53
Rating
7%
Usage
+0.4 %
51%
Win
-0.9 %
52%
CWR
Hero Bowler
27
Hero Bowler
53
Rating
7%
Usage
+0.6 %
51%
Win
-0.6 %
51%
CWR
Elite Barbarians Evolution
28
Elite Barbarians Evolution
53
Rating
7%
Usage
+0.2 %
51%
Win
-0.5 %
51%
CWR
Royal Recruits Evolution
29
Royal Recruits Evolution
53
Rating
3%
Usage
+0.0 %
51%
Win
-0.4 %
51%
CWR
Flying Machine
30
Flying Machine
53
Rating
3%
Usage
+0.1 %
51%
Win
-0.6 %
51%
CWR
Goblin Giant Evolution
31
Goblin Giant Evolution
53
Rating
1%
Usage
+0.0 %
52%
Win
-1.1 %
52%
CWR
Goblinstein
32
Goblinstein
53
Rating
1%
Usage
+0.0 %
52%
Win
-1.1 %
52%
CWR
Hero Mega Minion
33
Hero Mega Minion
53
Rating
3%
Usage
+0.0 %
51%
Win
-0.5 %
51%
CWR
Knight Evolution
34
Knight Evolution
52
Rating
4%
Usage
+1.0 %
51%
Win
-0.5 %
51%
CWR
Phoenix
35
Phoenix
52
Rating
2%
Usage
-0.2 %
51%
Win
-1.0 %
51%
CWR
Night Witch
36
Night Witch
52
Rating
5%
Usage
+0.0 %
51%
Win
-0.6 %
51%
CWR
Hero Barbarian Barrel
37
Hero Barbarian Barrel
52
Rating
3%
Usage
+0.1 %
51%
Win
-1.3 %
51%
CWR
Minion Horde Evolution
38
Minion Horde Evolution
52
Rating
3%
Usage
-0.0 %
51%
Win
-0.8 %
51%
CWR
Goblin Hut
39
Goblin Hut
52
Rating
8%
Usage
+1.8 %
51%
Win
-1.0 %
51%
CWR
Skeleton Army Evolution
40
Skeleton Army Evolution
52
Rating
6%
Usage
+0.2 %
51%
Win
-0.1 %
51%
CWR
Sparky
41
Sparky
52
Rating
4%
Usage
-0.4 %
51%
Win
+0.3 %
51%
CWR
Royal Ghost
42
Royal Ghost
52
Rating
4%
Usage
+0.2 %
51%
Win
-0.8 %
51%
CWR
Tornado
43
Tornado
52
Rating
11%
Usage
+0.2 %
51%
Win
-0.5 %
51%
CWR
Dark Prince
44
Dark Prince
52
Rating
3%
Usage
-0.1 %
51%
Win
-0.5 %
51%
CWR
Barbarians
45
Barbarians
52
Rating
1%
Usage
+0.1 %
51%
Win
-0.4 %
51%
CWR
Spirit Empress
46
Spirit Empress
52
Rating
1%
Usage
+0.0 %
51%
Win
-0.7 %
51%
CWR
Barbarians Evolution
47
Barbarians Evolution
52
Rating
1%
Usage
+0.1 %
51%
Win
-0.4 %
51%
CWR
Inferno Dragon Evolution
48
Inferno Dragon Evolution
52
Rating
4%
Usage
+0.2 %
51%
Win
-0.4 %
51%
CWR
Goblin Cage
49
Goblin Cage
52
Rating
2%
Usage
-0.1 %
51%
Win
-0.8 %
51%
CWR
Skeleton King
50
Skeleton King
52
Rating
2%
Usage
+0.2 %
51%
Win
-0.2 %
51%
CWR
X-Bow
51
X-Bow
52
Rating
2%
Usage
+0.1 %
51%
Win
+0.1 %
51%
CWR
Electro Giant Evolution
52
Electro Giant Evolution
52
Rating
3%
Usage
+0.2 %
51%
Win
-0.5 %
51%
CWR
Lightning
53
Lightning
52
Rating
12%
Usage
+0.1 %
51%
Win
-0.3 %
51%
CWR
Tombstone
54
Tombstone
51
Rating
3%
Usage
+0.1 %
51%
Win
-0.6 %
51%
CWR
Elixir Collector
55
Elixir Collector
51
Rating
4%
Usage
+0.4 %
51%
Win
-1.3 %
51%
CWR
Hero Giant
56
Hero Giant
51
Rating
3%
Usage
-0.3 %
51%
Win
+2.2 %
51%
CWR
Furnace Evolution
57
Furnace Evolution
51
Rating
6%
Usage
+1.1 %
51%
Win
-0.4 %
51%
CWR
P.E.K.K.A
58
P.E.K.K.A
51
Rating
3%
Usage
0.0 %
51%
Win
+0.0 %
51%
CWR
Bats Evolution
59
Bats Evolution
51
Rating
4%
Usage
-0.2 %
51%
Win
-0.2 %
51%
CWR
Archers Evolution
60
Archers Evolution
51
Rating
3%
Usage
-0.1 %
51%
Win
-0.0 %
51%
CWR
Vines
61
Vines
51
Rating
3%
Usage
-0.1 %
51%
Win
-0.4 %
51%
CWR
Bomber
62
Bomber
51
Rating
3%
Usage
0.0 %
51%
Win
-0.4 %
51%
CWR
Giant Snowball Evolution
63
Giant Snowball Evolution
50
Rating
5%
Usage
+0.2 %
50%
Win
-0.4 %
50%
CWR
Goblin Curse
64
Goblin Curse
50
Rating
2%
Usage
+0.2 %
51%
Win
+0.1 %
51%
CWR
Fireball
65
Fireball
50
Rating
22%
Usage
-0.9 %
50%
Win
+0.0 %
50%
CWR
Knight
66
Knight
50
Rating
6%
Usage
-0.4 %
50%
Win
-0.2 %
50%
CWR
Giant
67
Giant
50
Rating
3%
Usage
-1.0 %
50%
Win
+3.5 %
50%
CWR
Tower Princess
68
Tower Princess
50
Rating
93%
Usage
+0.4 %
50%
Win
-0.1 %
51%
CWR
Royal Chef
69
Royal Chef
50
Rating
3%
Usage
+0.1 %
50%
Win
+0.1 %
50%
CWR
Archer Queen
70
Archer Queen
50
Rating
3%
Usage
+0.2 %
50%
Win
-0.8 %
50%
CWR
Goblin Gang
71
Goblin Gang
50
Rating
10%
Usage
-0.6 %
50%
Win
-0.3 %
50%
CWR
Minions
72
Minions
50
Rating
5%
Usage
-0.6 %
50%
Win
-0.4 %
50%
CWR
Bomb Tower
73
Bomb Tower
50
Rating
2%
Usage
+0.2 %
50%
Win
-0.5 %
50%
CWR
Electro Wizard
74
Electro Wizard
50
Rating
5%
Usage
-1.0 %
50%
Win
-0.4 %
50%
CWR
Hero Dark Prince
75
Hero Dark Prince
50
Rating
3%
Usage
-0.2 %
50%
Win
-0.1 %
50%
CWR
Goblin Demolisher
76
Goblin Demolisher
50
Rating
2%
Usage
-0.1 %
50%
Win
-0.6 %
50%
CWR
Goblin Barrel Evolution
77
Goblin Barrel Evolution
50
Rating
6%
Usage
-0.5 %
50%
Win
+0.8 %
50%
CWR
Rage
78
Rage
50
Rating
5%
Usage
+0.2 %
50%
Win
-0.0 %
50%
CWR
Arrows
79
Arrows
50
Rating
26%
Usage
-0.5 %
50%
Win
+0.2 %
50%
CWR
Cannon Evolution
80
Cannon Evolution
50
Rating
8%
Usage
-0.3 %
50%
Win
+0.2 %
50%
CWR
Electro Dragon Evolution
81
Electro Dragon Evolution
50
Rating
3%
Usage
-0.1 %
50%
Win
-0.4 %
50%
CWR
Freeze
82
Freeze
49
Rating
3%
Usage
+0.1 %
50%
Win
-0.2 %
50%
CWR
Giant Evolution
83
Giant Evolution
49
Rating
1%
Usage
-0.5 %
50%
Win
+1.3 %
50%
CWR
Hero Balloon
84
Hero Balloon
49
Rating
4%
Usage
+0.6 %
50%
Win
-1.0 %
50%
CWR
Fisherman
85
Fisherman
49
Rating
2%
Usage
+0.6 %
50%
Win
-1.2 %
50%
CWR
Mighty Miner
86
Mighty Miner
49
Rating
3%
Usage
-0.1 %
50%
Win
-0.3 %
50%
CWR
Skeletons
87
Skeletons
49
Rating
20%
Usage
+0.8 %
50%
Win
-0.0 %
50%
CWR
Minion Giant
88
Minion Giant
49
Rating
3%
Usage
-2.9 %
50%
Win
+3.8 %
50%
CWR
Earthquake
89
Earthquake
49
Rating
5%
Usage
+0.1 %
50%
Win
-0.4 %
50%
CWR
Prince
90
Prince
49
Rating
3%
Usage
-0.2 %
50%
Win
+0.1 %
50%
CWR
Poison
91
Poison
49
Rating
10%
Usage
+1.1 %
50%
Win
-0.3 %
50%
CWR
Zap
92
Zap
49
Rating
12%
Usage
-0.3 %
50%
Win
+0.1 %
50%
CWR
Guards
93
Guards
49
Rating
4%
Usage
-0.2 %
50%
Win
+0.0 %
50%
CWR
Electro Spirit
94
Electro Spirit
49
Rating
10%
Usage
+0.3 %
50%
Win
-0.4 %
50%
CWR
Royal Hogs Evolution
95
Royal Hogs Evolution
49
Rating
6%
Usage
+1.4 %
50%
Win
-1.2 %
50%
CWR
Berserker
96
Berserker
49
Rating
1%
Usage
-0.0 %
50%
Win
-1.0 %
50%
CWR
Hero Mini P.E.K.K.A
97
Hero Mini P.E.K.K.A
48
Rating
8%
Usage
-0.4 %
50%
Win
+0.2 %
50%
CWR
Princess
98
Princess
48
Rating
6%
Usage
-0.2 %
50%
Win
+0.5 %
50%
CWR
Ice Golem
99
Ice Golem
48
Rating
3%
Usage
+0.1 %
50%
Win
+0.4 %
50%
CWR
Hunter
100
Hunter
48
Rating
2%
Usage
+0.4 %
50%
Win
-1.2 %
50%
CWR
Mega Minion
101
Mega Minion
48
Rating
1%
Usage
-0.0 %
50%
Win
-0.4 %
50%
CWR
Goblins
102
Goblins
48
Rating
1%
Usage
-0.0 %
50%
Win
-0.2 %
50%
CWR
Miner
103
Miner
48
Rating
4%
Usage
+0.4 %
49%
Win
-0.4 %
49%
CWR
Lumberjack
104
Lumberjack
48
Rating
2%
Usage
+0.0 %
49%
Win
+0.1 %
49%
CWR
Princess Evolution
105
Princess Evolution
47
Rating
3%
Usage
+0.0 %
49%
Win
-0.6 %
49%
CWR
Hero Berserker
106
Hero Berserker
47
Rating
2%
Usage
-0.0 %
49%
Win
-0.6 %
49%
CWR
Wizard Evolution
107
Wizard Evolution
47
Rating
3%
Usage
-0.3 %
49%
Win
+0.5 %
49%
CWR
P.E.K.K.A Evolution
108
P.E.K.K.A Evolution
47
Rating
2%
Usage
-0.1 %
49%
Win
-0.1 %
49%
CWR
Musketeer Evolution
109
Musketeer Evolution
47
Rating
4%
Usage
-0.3 %
49%
Win
-0.1 %
49%
CWR
Ice Spirit
110
Ice Spirit
47
Rating
12%
Usage
-0.5 %
49%
Win
+0.4 %
49%
CWR
Hero Knight
111
Hero Knight
47
Rating
8%
Usage
-0.5 %
49%
Win
+0.4 %
49%
CWR
The Log
112
The Log
47
Rating
23%
Usage
-1.5 %
49%
Win
+0.3 %
49%
CWR
Battle Healer
113
Battle Healer
47
Rating
1%
Usage
-0.0 %
49%
Win
-0.1 %
49%
CWR
Mini P.E.K.K.A
114
Mini P.E.K.K.A
47
Rating
5%
Usage
-0.3 %
49%
Win
+0.3 %
49%
CWR
Bomber Evolution
115
Bomber Evolution
46
Rating
1%
Usage
-0.0 %
49%
Win
-0.4 %
49%
CWR
Executioner Evolution
116
Executioner Evolution
46
Rating
2%
Usage
-0.2 %
49%
Win
+0.6 %
49%
CWR
Inferno Tower
117
Inferno Tower
46
Rating
4%
Usage
-0.3 %
49%
Win
+0.5 %
49%
CWR
Rocket
118
Rocket
46
Rating
5%
Usage
-0.2 %
49%
Win
+0.5 %
49%
CWR
Skeletons Evolution
119
Skeletons Evolution
46
Rating
4%
Usage
+0.0 %
49%
Win
+0.1 %
49%
CWR
Royal Recruits
120
Royal Recruits
46
Rating
1%
Usage
-0.0 %
49%
Win
-0.7 %
49%
CWR
Dart Goblin
121
Dart Goblin
46
Rating
8%
Usage
-0.6 %
49%
Win
+0.3 %
49%
CWR
Hero Tombstone
122
Hero Tombstone
46
Rating
2%
Usage
-0.2 %
49%
Win
-0.5 %
49%
CWR
Golden Knight
123
Golden Knight
46
Rating
3%
Usage
-0.2 %
49%
Win
-0.3 %
49%
CWR
Magic Archer
124
Magic Archer
46
Rating
1%
Usage
-0.1 %
49%
Win
-0.8 %
49%
CWR
Monk
125
Monk
46
Rating
2%
Usage
+0.2 %
49%
Win
-0.5 %
49%
CWR
Goblin Drill Evolution
126
Goblin Drill Evolution
46
Rating
3%
Usage
+0.3 %
49%
Win
-0.5 %
49%
CWR
Elixir Golem
127
Elixir Golem
46
Rating
3%
Usage
+0.1 %
49%
Win
+0.7 %
49%
CWR
Ice Wizard
128
Ice Wizard
46
Rating
1%
Usage
-0.2 %
49%
Win
+0.3 %
49%
CWR
Witch Evolution
129
Witch Evolution
45
Rating
10%
Usage
-0.6 %
49%
Win
+0.7 %
48%
CWR
Hero Ice Golem
130
Hero Ice Golem
45
Rating
2%
Usage
-0.1 %
49%
Win
+0.6 %
49%
CWR
Giant Snowball
131
Giant Snowball
45
Rating
2%
Usage
+0.1 %
49%
Win
-0.2 %
49%
CWR
Void
132
Void
45
Rating
1%
Usage
0.0 %
49%
Win
+0.0 %
49%
CWR
Baby Dragon
133
Baby Dragon
45
Rating
2%
Usage
-0.2 %
49%
Win
+0.4 %
49%
CWR
Tesla Evolution
134
Tesla Evolution
45
Rating
5%
Usage
-0.6 %
48%
Win
+0.4 %
48%
CWR
Balloon
135
Balloon
45
Rating
3%
Usage
+1.0 %
48%
Win
-2.6 %
48%
CWR
Cannon
136
Cannon
44
Rating
7%
Usage
+0.2 %
48%
Win
+0.4 %
48%
CWR
Fire Spirit
137
Fire Spirit
44
Rating
3%
Usage
-0.0 %
48%
Win
-0.3 %
48%
CWR
Cannoneer
138
Cannoneer
44
Rating
1%
Usage
-0.0 %
48%
Win
+1.2 %
48%
CWR
Hog Rider
139
Hog Rider
44
Rating
13%
Usage
-3.2 %
48%
Win
+1.3 %
48%
CWR
Mega Knight Evolution
140
Mega Knight Evolution
44
Rating
8%
Usage
-0.8 %
48%
Win
+0.7 %
48%
CWR
Royal Delivery
141
Royal Delivery
44
Rating
3%
Usage
+0.1 %
48%
Win
-0.1 %
48%
CWR
Spear Goblins
142
Spear Goblins
44
Rating
1%
Usage
-0.1 %
48%
Win
+0.2 %
48%
CWR
Boss Bandit
143
Boss Bandit
44
Rating
1%
Usage
-0.2 %
48%
Win
+0.9 %
48%
CWR
Dart Goblin Evolution
144
Dart Goblin Evolution
44
Rating
2%
Usage
-0.2 %
48%
Win
+1.2 %
48%
CWR
Hero Musketeer
145
Hero Musketeer
44
Rating
3%
Usage
-0.5 %
48%
Win
+0.9 %
48%
CWR
Mega Knight
146
Mega Knight
44
Rating
2%
Usage
-0.2 %
48%
Win
+1.0 %
48%
CWR
Barbarian Hut
147
Barbarian Hut
43
Rating
0%
Usage
0.0 %
49%
Win
+4.5 %
49%
CWR
Hero Valkyrie
148
Hero Valkyrie
43
Rating
11%
Usage
-0.3 %
48%
Win
+0.7 %
48%
CWR
Wall Breakers Evolution
149
Wall Breakers Evolution
43
Rating
2%
Usage
+0.5 %
48%
Win
-1.4 %
48%
CWR
Inferno Dragon
150
Inferno Dragon
43
Rating
1%
Usage
-0.2 %
48%
Win
+0.1 %
48%
CWR
Goblin Drill
151
Goblin Drill
43
Rating
1%
Usage
-0.1 %
48%
Win
+1.2 %
48%
CWR
Firecracker Evolution
152
Firecracker Evolution
43
Rating
6%
Usage
-0.8 %
47%
Win
+0.6 %
47%
CWR
Ronin
153
Ronin
42
Rating
4%
Usage
-0.4 %
47%
Win
+0.8 %
47%
CWR
Hunter Evolution
154
Hunter Evolution
42
Rating
1%
Usage
+0.1 %
48%
Win
-1.3 %
48%
CWR
Little Prince
155
Little Prince
42
Rating
1%
Usage
-0.2 %
47%
Win
+0.3 %
47%
CWR
Executioner
156
Executioner
42
Rating
1%
Usage
-0.1 %
47%
Win
+0.3 %
47%
CWR
Electro Giant
157
Electro Giant
42
Rating
1%
Usage
-0.1 %
48%
Win
+0.2 %
48%
CWR
Ram Rider
158
Ram Rider
42
Rating
4%
Usage
+1.8 %
47%
Win
-2.3 %
47%
CWR
Dagger Duchess
159
Dagger Duchess
41
Rating
3%
Usage
-0.4 %
47%
Win
+1.0 %
47%
CWR
Wall Breakers
160
Wall Breakers
41
Rating
4%
Usage
+1.3 %
47%
Win
-2.7 %
47%
CWR
Musketeer
161
Musketeer
41
Rating
1%
Usage
-0.2 %
47%
Win
+0.7 %
47%
CWR
Royal Hogs
162
Royal Hogs
41
Rating
2%
Usage
+0.7 %
47%
Win
-2.9 %
47%
CWR
Valkyrie Evolution
163
Valkyrie Evolution
41
Rating
3%
Usage
-0.5 %
47%
Win
+0.6 %
47%
CWR
Battle Ram
164
Battle Ram
41
Rating
1%
Usage
-1.1 %
47%
Win
+4.3 %
47%
CWR
Bats
165
Bats
41
Rating
5%
Usage
-0.7 %
47%
Win
+0.1 %
47%
CWR
Skeleton Army
166
Skeleton Army
41
Rating
4%
Usage
-0.7 %
47%
Win
+0.2 %
47%
CWR
Archers
167
Archers
40
Rating
1%
Usage
0.0 %
47%
Win
+0.8 %
47%
CWR
Three Musketeers
168
Three Musketeers
40
Rating
3%
Usage
+1.5 %
47%
Win
-5.5 %
46%
CWR
Skeleton Barrel
169
Skeleton Barrel
40
Rating
2%
Usage
-0.3 %
47%
Win
+0.6 %
46%
CWR
Royal Giant Evolution
170
Royal Giant Evolution
40
Rating
3%
Usage
+0.8 %
46%
Win
-3.7 %
46%
CWR
Tesla
171
Tesla
40
Rating
4%
Usage
-0.4 %
46%
Win
+0.9 %
46%
CWR
Clone
172
Clone
40
Rating
1%
Usage
-0.1 %
46%
Win
+0.4 %
46%
CWR
Goblin Barrel
173
Goblin Barrel
39
Rating
4%
Usage
-1.8 %
46%
Win
+1.9 %
46%
CWR
Hero Wizard
174
Hero Wizard
39
Rating
3%
Usage
-0.5 %
46%
Win
+0.6 %
46%
CWR
Hero Magic Archer
175
Hero Magic Archer
39
Rating
1%
Usage
-0.1 %
46%
Win
-0.2 %
46%
CWR
Goblin Giant
176
Goblin Giant
38
Rating
0%
Usage
+0.0 %
47%
Win
-1.1 %
47%
CWR
Rune Giant
177
Rune Giant
38
Rating
0%
Usage
-0.2 %
46%
Win
-0.3 %
46%
CWR
Elite Barbarians
178
Elite Barbarians
38
Rating
1%
Usage
-0.1 %
46%
Win
+1.2 %
46%
CWR
Goblin Machine
179
Goblin Machine
38
Rating
0%
Usage
+0.0 %
47%
Win
+0.3 %
47%
CWR
Ice Spirit Evolution
180
Ice Spirit Evolution
38
Rating
0%
Usage
-0.1 %
46%
Win
+0.4 %
46%
CWR
Minion Horde
181
Minion Horde
37
Rating
1%
Usage
-0.1 %
46%
Win
+1.0 %
46%
CWR
Mirror Evolution
182
Mirror Evolution
37
Rating
2%
Usage
+0.2 %
45%
Win
+1.4 %
45%
CWR
Firecracker
183
Firecracker
36
Rating
3%
Usage
-0.5 %
45%
Win
+1.1 %
45%
CWR
Valkyrie
184
Valkyrie
36
Rating
1%
Usage
-0.3 %
45%
Win
+0.4 %
45%
CWR
Electro Dragon
185
Electro Dragon
33
Rating
0%
Usage
-0.0 %
45%
Win
+3.3 %
45%
CWR
Mortar
186
Mortar
33
Rating
0%
Usage
-0.8 %
44%
Win
+6.3 %
44%
CWR
Witch
187
Witch
32
Rating
1%
Usage
-0.3 %
43%
Win
+1.4 %
43%
CWR
Wizard
188
Wizard
31
Rating
1%
Usage
-0.2 %
43%
Win
+1.0 %
43%
CWR
Mirror
189
Mirror
31
Rating
2%
Usage
-0.5 %
43%
Win
+0.9 %
43%
CWR
Royal Giant
190
Royal Giant
25
Rating
1%
Usage
+0.5 %
40%
Win
-6.6 %
40%
CWR"""

lines = [line.strip() for line in raw_text.strip().splitlines() if line.strip()]
records = []
i = 0
while i + 12 < len(lines):
    name = lines[i]
    rank = int(lines[i + 1])
    rating = int(lines[i + 3])
    usage = float(lines[i + 5].replace('%', '').strip())
    win_rate = float(lines[i + 8].replace('%', '').strip())
    cwr = float(lines[i + 11].replace('%', '').strip())
    records.append({
        'rank': rank,
        'card_en': name,
        'rating': rating,
        'usage': usage,
        'win_rate': win_rate,
        'cwr': cwr,
    })
    i += 13

df = pd.DataFrame(records)

en_to_ru = {
    'Cannon Cart': 'Повозка с пушкой',
    'Rascals': 'Разбойники',
    'Heal Spirit': 'Дух исцеления',
    'Battle Ram Evolution': 'Боевой таран (эволюция)',
    'Bandit': 'Бандитка',
    'Mortar Evolution': 'Мортира (эволюция)',
    'Giant Skeleton': 'Гигантский скелет',
    'Furnace': 'Печь',
    'Lumberjack Evolution': 'Дровосек (эволюция)',
    'Barbarian Barrel': 'Бочка с варваром',
    'Zap Evolution': 'Разряд (эволюция)',
    'Zappies': 'Мини-генераторы',
    'Hero Goblins': 'Герой Гоблины',
    'Lava Hound': 'Адская гончая',
    'Hero Electro Wizard': 'Герой Громовержец',
    'Bowler': 'Вышибала',
    'Mother Witch': 'Ведьмина бабушка',
    'Skeleton Barrel Evolution': 'Бочка со скелетами (эволюция)',
    'Goblin Cage Evolution': 'Клетка с гоблином (эволюция)',
    'Hero Ice Wizard': 'Герой Ледяной колдун',
    'Baby Dragon Evolution': 'Дракончик (эволюция)',
    'Royal Ghost Evolution': 'Королевский призрак (эволюция)',
    'Graveyard': 'Кладбище',
    'Suspicious Bush': 'Подозрительный куст',
    'Skeleton Dragons': 'Костяные драконы',
    'Golem': 'Голем',
    'Hero Bowler': 'Герой Вышибала',
    'Elite Barbarians Evolution': 'Элитные варвары (эволюция)',
    'Royal Recruits Evolution': 'Королевские рекруты (эволюция)',
    'Flying Machine': 'Летучка',
    'Goblin Giant Evolution': 'Гоблин-гигант (эволюция)',
    'Goblinstein': 'Гоблинштейн',
    'Hero Mega Minion': 'Герой Мегаминьон',
    'Knight Evolution': 'Рыцарь (эволюция)',
    'Phoenix': 'Феникс',
    'Night Witch': 'Ночная ведьма',
    'Hero Barbarian Barrel': 'Герой Бочка с варваром',
    'Minion Horde Evolution': 'Орда миньонов (эволюция)',
    'Goblin Hut': 'Хижина гоблинов',
    'Skeleton Army Evolution': 'Армия скелетов (эволюция)',
    'Sparky': 'Спарки',
    'Royal Ghost': 'Королевский призрак',
    'Tornado': 'Торнадо',
    'Dark Prince': 'Тёмный принц',
    'Barbarians': 'Варвары',
    'Spirit Empress': 'Императрица духов',
    'Barbarians Evolution': 'Варвары (эволюция)',
    'Inferno Dragon Evolution': 'Пламенный дракон (эволюция)',
    'Goblin Cage': 'Клетка с гоблином',
    'Skeleton King': 'Король скелетов',
    'X-Bow': 'Арбалет',
    'Electro Giant Evolution': 'Электрогигант (эволюция)',
    'Lightning': 'Молния',
    'Tombstone': 'Надгробие',
    'Elixir Collector': 'Сборщик эликсира',
    'Hero Giant': 'Герой Гигант',
    'Furnace Evolution': 'Печь (эволюция)',
    'P.E.K.K.A': 'П.Е.К.К.А.',
    'Bats Evolution': 'Летучие мыши (эволюция)',
    'Archers Evolution': 'Лучницы (эволюция)',
    'Vines': 'Лианы',
    'Bomber': 'Подрывник',
    'Giant Snowball Evolution': 'Гигантский снежок (эволюция)',
    'Goblin Curse': 'Проклятие гоблинов',
    'Fireball': 'Огненный шар',
    'Knight': 'Рыцарь',
    'Giant': 'Гигант',
    'Tower Princess': 'Принцесса башни',
    'Royal Chef': 'Королевский повар',
    'Archer Queen': 'Королева лучниц',
    'Goblin Gang': 'Банда гоблинов',
    'Minions': 'Миньоны',
    'Bomb Tower': 'Башня-бомбёжка',
    'Electro Wizard': 'Громовержец',
    'Hero Dark Prince': 'Герой Тёмный принц',
    'Goblin Demolisher': 'Подрывник-гоблин',
    'Goblin Barrel Evolution': 'Гоблинская бочка (эволюция)',
    'Rage': 'Ярость',
    'Arrows': 'Стрелы',
    'Cannon Evolution': 'Пушка (эволюция)',
    'Electro Dragon Evolution': 'Электродракон (эволюция)',
    'Freeze': 'Заморозка',
    'Giant Evolution': 'Гигант (эволюция)',
    'Hero Balloon': 'Герой Шар',
    'Fisherman': 'Рыбак',
    'Mighty Miner': 'Шустрый шахтёр',
    'Skeletons': 'Скелеты',
    'Minion Giant': 'Гигантский миньон',
    'Earthquake': 'Землетрясение',
    'Prince': 'Принц',
    'Poison': 'Яд',
    'Zap': 'Разряд',
    'Guards': 'Стражи',
    'Electro Spirit': 'Электродух',
    'Royal Hogs Evolution': 'Королевские кабаны (эволюция)',
    'Berserker': 'Берсерк',
    'Hero Mini P.E.K.K.A': 'Герой Мини-П.Е.К.К.А.',
    'Princess': 'Принцесса',
    'Ice Golem': 'Ледяной голем',
    'Hunter': 'Охотник',
    'Mega Minion': 'Мегаминьон',
    'Goblins': 'Гоблины',
    'Miner': 'Шахтёр',
    'Lumberjack': 'Дровосек',
    'Princess Evolution': 'Принцесса (эволюция)',
    'Hero Berserker': 'Герой Берсерк',
    'Wizard Evolution': 'Колдун (эволюция)',
    'P.E.K.K.A Evolution': 'П.Е.К.К.А. (эволюция)',
    'Musketeer Evolution': 'Мушкетёр (эволюция)',
    'Ice Spirit': 'Ледяной дух',
    'Hero Knight': 'Герой Рыцарь',
    'The Log': 'Бревно',
    'Battle Healer': 'Целительница-воин',
    'Mini P.E.K.K.A': 'Мини-П.Е.К.К.А.',
    'Bomber Evolution': 'Подрывник (эволюция)',
    'Executioner Evolution': 'Палач (эволюция)',
    'Inferno Tower': 'Адская башня',
    'Rocket': 'Ракета',
    'Skeletons Evolution': 'Скелеты (эволюция)',
    'Royal Recruits': 'Королевские рекруты',
    'Dart Goblin': 'Гоблин с дротиками',
    'Hero Tombstone': 'Герой Надгробие',
    'Golden Knight': 'Золотой рыцарь',
    'Magic Archer': 'Магический лучник',
    'Monk': 'Монах',
    'Goblin Drill Evolution': 'Гоблинский бур (эволюция)',
    'Elixir Golem': 'Эликсирный голем',
    'Ice Wizard': 'Ледяной колдун',
    'Witch Evolution': 'Ведьма (эволюция)',
    'Hero Ice Golem': 'Герой Ледяной голем',
    'Giant Snowball': 'Гигантский снежок',
    'Void': 'Пустота',
    'Baby Dragon': 'Дракончик',
    'Tesla Evolution': 'Тесла (эволюция)',
    'Balloon': 'Шар',
    'Cannon': 'Пушка',
    'Fire Spirit': 'Огненный дух',
    'Cannoneer': 'Канонир',
    'Hog Rider': 'Всадник на кабане',
    'Mega Knight Evolution': 'Мегарыцарь (эволюция)',
    'Royal Delivery': 'Королевская почта',
    'Spear Goblins': 'Гоблины-копейщики',
    'Boss Bandit': 'Босс-бандитка',
    'Dart Goblin Evolution': 'Гоблин с дротиками (эволюция)',
    'Hero Musketeer': 'Герой Мушкетёр',
    'Mega Knight': 'Мегарыцарь',
    'Barbarian Hut': 'Хижина варваров',
    'Hero Valkyrie': 'Герой Валькирия',
    'Wall Breakers Evolution': 'Стенобои (эволюция)',
    'Inferno Dragon': 'Пламенный дракон',
    'Goblin Drill': 'Гоблинский бур',
    'Firecracker Evolution': 'Огненная лучница (эволюция)',
    'Ronin': 'Ронин',
    'Hunter Evolution': 'Охотник (эволюция)',
    'Little Prince': 'Маленький принц',
    'Executioner': 'Палач',
    'Electro Giant': 'Электрогигант',
    'Ram Rider': 'Всадница на баране',
    'Dagger Duchess': 'Герцогиня с кинжалами',
    'Wall Breakers': 'Стенобои',
    'Musketeer': 'Мушкетёр',
    'Royal Hogs': 'Королевские кабаны',
    'Valkyrie Evolution': 'Валькирия (эволюция)',
    'Battle Ram': 'Боевой таран',
    'Bats': 'Летучие мыши',
    'Skeleton Army': 'Армия скелетов',
    'Archers': 'Лучницы',
    'Three Musketeers': 'Три мушкетёра',
    'Skeleton Barrel': 'Бочка со скелетами',
    'Royal Giant Evolution': 'Королевский гигант (эволюция)',
    'Tesla': 'Тесла',
    'Clone': 'Клон',
    'Goblin Barrel': 'Гоблинская бочка',
    'Hero Wizard': 'Герой Колдун',
    'Hero Magic Archer': 'Герой Магический лучник',
    'Goblin Giant': 'Гоблин-гигант',
    'Rune Giant': 'Рунный гигант',
    'Elite Barbarians': 'Элитные варвары',
    'Goblin Machine': 'Гоблин-машина',
    'Ice Spirit Evolution': 'Ледяной дух (эволюция)',
    'Minion Horde': 'Орда миньонов',
    'Mirror Evolution': 'Зеркало (эволюция)',
    'Firecracker': 'Огненная лучница',
    'Valkyrie': 'Валькирия',
    'Electro Dragon': 'Электродракон',
    'Mortar': 'Мортира',
    'Witch': 'Ведьма',
    'Wizard': 'Колдун',
    'Mirror': 'Зеркало',
    'Royal Giant': 'Королевский гигант',
}

df['card_ru'] = df['card_en'].map(en_to_ru).fillna(df['card_en'])


def classify_card(name_en):
    if name_en.startswith('Hero '):
        return 'hero'
    if name_en.endswith(' Evolution'):
        return 'evolution'
    return 'normal'


df['category'] = df['card_en'].apply(classify_card)
df.to_csv('royaleapi_cards_ru.csv', index=False)

print(f"Всего карт: {len(df)}")
print(df['category'].value_counts())

df_heroes = df[df['category'] == 'hero']
df_evo = df[df['category'] == 'evolution']
df_normal = df[df['category'] == 'normal']


def prep_usage_pie(sub_df, top_n=10):
    s = sub_df.set_index('card_ru')['usage'].sort_values(ascending=False)
    if len(s) > top_n:
        top_part = s.iloc[:top_n]
        others_sum = s.iloc[top_n:].sum()
        s = pd.concat([top_part, pd.Series({'Остальные': others_sum})])
    return s


def plot_pie(ax, series, title):
    wedges, texts, autotexts = ax.pie(
        series.values,
        labels=series.index,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.76,
        textprops={'fontsize': 8.5},
    )
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(8)
        autotext.set_fontweight('bold')
    ax.set_title(title, fontsize=11, fontweight='bold', pad=12)
    ax.axis('equal')


fig1, axes1 = plt.subplots(1, 3, figsize=(20, 6.8))
plot_pie(axes1[0], prep_usage_pie(df_heroes, top_n=10), '1. Герои: популярность (топ-10 + остальные)')
plot_pie(axes1[1], prep_usage_pie(df_evo, top_n=10), '2. Эволюции: популярность (топ-10 + остальные)')
plot_pie(axes1[2], prep_usage_pie(df_normal, top_n=10), '3. Обычные карты: популярность (топ-10 + остальные)')
fig1.suptitle('Популярность использования карт (данные RoyaleAPI, Ranked 7d)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('royaleapi_popularity_3pie.png', dpi=150)


def prep_winrate_bars(sub_df, top_n=10):
    top_df = sub_df.sort_values(['win_rate', 'rating', 'usage'], ascending=[False, False, False]).head(top_n)
    top_df = top_df.sort_values(['win_rate', 'rating'], ascending=[True, True])
    return top_df.set_index('card_ru')['win_rate']


def plot_ascending_bars(ax, series, title, color):
    x = np.arange(len(series))
    bars = ax.bar(x, series.values, color=color, edgecolor='black', linewidth=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(series.index, rotation=32, ha='right', fontsize=9)
    ax.set_ylabel('Процент побед (%)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    y_min = max(0.0, np.floor(series.min() - 2.0))
    y_max = min(100.0, np.ceil(series.max() + 1.5))
    ax.set_ylim(y_min, y_max)

    for bar, val in zip(bars, series.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.15,
            f'{val:.0f}%',
            ha='center',
            va='bottom',
            fontsize=8.5,
            fontweight='bold',
        )


fig2, axes2 = plt.subplots(1, 3, figsize=(20, 6.8))
plot_ascending_bars(
    axes2[0],
    prep_winrate_bars(df_heroes, top_n=10),
    '4. Герои: топ-10 по % побед (по возрастанию)',
    color='#4C72B0',
)
plot_ascending_bars(
    axes2[1],
    prep_winrate_bars(df_evo, top_n=10),
    '5. Эволюции: топ-10 по % побед (по возрастанию)',
    color='#DD8452',
)
plot_ascending_bars(
    axes2[2],
    prep_winrate_bars(df_normal, top_n=10),
    '6. Обычные карты: топ-10 по % побед (по возрастанию)',
    color='#55A868',
)
fig2.suptitle('Процент побед (Win Rate) по группам карт — от меньшего к большему (RoyaleAPI)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('royaleapi_winrate_bars.png', dpi=150)

plt.show()
print("Готово! Сохранены: royaleapi_cards_ru.csv, royaleapi_popularity_3pie.png, royaleapi_winrate_bars.png")
