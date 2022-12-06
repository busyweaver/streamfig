import streamfig
s = streamfig.StreamFig(alpha=0.0, omega=32.0, directed = True)

s.addColor("red", "#FF0000")
s.addColor("green", "#00FF00")
s.addColor("blue", "#0000FF")
s.addColor("gold", "#cc9900")
s.addColor("black", "#000000")

s.addNode("a",[ (0.0, 4.0), (6.0, 26.0), (30.0, 32.0)]) 
s.addNode("b",[ (0.0, 17.0), (18.0, 32.0)]) 
s.addNode("c",[ (0.0, 23.0), (24.0, 32.0)]) 
s.addNode("d",[ (0.0, 32.0)]) 
s.addNode("e",[ (0.0, 2.0), (6.0, 18.0), (20.0, 32.0)]) 
s.addLink("a", "b", 1.0,2.0)
s.addLink("a", "b", 15.0,16.0)
s.addLink("a", "b", 23.0,24.0)

s.addLink("a", "c", 8.0,9.0)

s.addLink("b", "c", 3.0,5.0)
s.addLink("b", "c", 11.0,11.0)
s.addLink("b", "c", 19.0,22.0)
s.addLink("b", "c", 25.0,28.0)

s.addLink("b", "d", 12.0,14.0)

s.addLink("c", "d", 6.0,7.0)
s.addLink("c", "d", 18.0,19.0)
s.addLink("c", "d", 27.0,29.0)

s.addLink("d", "e", 9.0,11.0)
s.addLink("d", "e", 16.0,16.0)
s.addLink("d", "e", 23.0,24.0)
s.addLink("d", "e", 30.0,31.0)


# s.addPath(((2,"a","b"), (4,"b","c"), (6, "c", "d"), (9, "d", "e")), 2, 9, color="blue", width=6)
# s.addPath(((9,"a","c"), (18,"c","d"), (23, "d", "e")), 9, 23, color="green", width=6)
# s.addPath(((15,"a","b"), (19,"b","c"), (27,"c","d"), (30,"d", "e")), 15, 30, color="red", width=6)


s.addTimeNodeMark(0,"a",color="gold",width=4)
s.addTimeNodeMark(31,"e",color="gold",width=4)

# s.addTimeNodeMark(17,"b",color="black",width=4)
# s.addTimeNodeMark(17.5,"b",color="black",width=4)
# s.addTimeNodeMark(18,"b",color="black",width=4)

# s.addTimeNodeMark(23.5,"c",color="black",width=4)
# s.addTimeNodeMark(23,"c",color="black",width=4)
# s.addTimeNodeMark(24,"c",color="black",width=4)


s.addTimeLine(ticks=2) 
s.save_make_figure("eps",0) 
