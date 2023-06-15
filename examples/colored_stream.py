from streamfig import *

s = streamfig.StreamFig(alpha=0, omega=4, streaming=False)

s.addColor("tPink", "#FF9896") # 255, 152,150

s.addNode("a")
s.addNode("b")
s.addNode("c")
s.addNode("d")

#s.addPath([(1,"b","a"), (4.5,"a","c"), (6, "c", "b")], 1, 5, color=11, width=6)
#s.addPath([(2,"b","d")], 1, 1, color=11, width=6)

s.addLink("a", "b", 1, 1)
s.addLink("b", "d", 2, 2)
s.addLink("a", "c", 4, 4)
s.addLink("b", "c", 3, 3)

s.addTimeNodeColor(0,"a",color=1,width=4)
s.addTimeNodeColor(1,"a",color=2,width=4)
s.addTimeNodeColor(0,"b",color=3,width=4)
s.addTimeNodeColor(1,"b",color=4,width=4)

s.addTimeLine(ticks=2)
s.save_make_figure("eps",0) 
