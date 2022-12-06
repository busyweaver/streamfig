import streamfig
s = streamfig.StreamFig(alpha=0.0, omega=10.0, directed = True)
s.addNode("A",[ (0.0, 10.0)]) 
s.addNode("B",[ (0.0, 10.0)]) 
s.addNode("C",[ (0.0, 10.0)]) 
s.addNode("D",[ (0.0, 10.0)]) 
s.addNode("E",[ (0.0, 10.0)]) 
s.addLink("A", "B", 1.0,1.0)

s.addLink("B", "C", 2.0,2.0)
s.addLink("B", "C", 3.0,3.0)

s.addLink("C", "D", 6.0,6.0)

s.addLink("D", "E", 7.0,7.0)

s.addTimeLine(ticks=2) 
s.save_make_figure("eps",0) 
