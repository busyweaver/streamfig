import streamfig

s = streamfig.StreamFig(alpha=0, omega=15, directed = True)


s.addNode("a", [(0,7),(10,15)])
s.addNode("b", [(0,9),(12,15)])
s.addNode("c",[(0,8),(9,15)])
s.addNode("d", [(0,15)])
s.addNode("e",[(4,8),(9,15)])
s.addNode("f",[(0,6),(9,15)])

s.addLink("a", "b", 1, 3)
s.addLink("f", "e", 10, 12)

s.save_make_figure("png",0)
