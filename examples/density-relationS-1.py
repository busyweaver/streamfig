from streamfig import *

sg = StreamFig(alpha=0, omega=3)
sg.addNode("a", [(0,1)])
sg.addNode("b")
sg.addNode("c", [(0,1), (2,3)])

sg.addLink("a", "b", 0, 1)
sg.addLink("b", "c", 0, 1)
sg.addLink("b", "c", 2, 3)

sg.addTimeLine(ticks=1)

sg.save("density-relationS-1.fig")
