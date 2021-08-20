import schemdraw
import schemdraw.elements as elm
import numpy as np
import matplotlib.pyplot as plt



d = schemdraw.Drawing()
resistorTopLeft = d.add(elm.Resistor().left().label("4Ω"))
d.add(elm.CurrentLabelInline(direction = "out").at(resistorTopLeft).label("i"))
vLeft = d.add(elm.SourceV().down().label("10V"))
wireDownLeft = d.add(elm.Line().right())
iMiddle = d.add(elm.SourceControlledI().up().label("2i"))
wireMiddleTop = d.add(elm.Line().right())
resistorMiddle = d.add(elm.Resistor().down().label("1Ω"))
wireRightDown = d.add(elm.Line().right())
iRight = d.add(elm.SourceI().up().label("4A"))
wireRightTop = d.add(elm.Line().left())
wireMiddle = d.add(elm.Line().right().at(wireDownLeft.end))

d.draw()
d.save("firstCircuitSchematic.png")



A = np.array([[4 , 1] , [-3 , 1]])
Y = np.array([-14 , 0])

answers = np.linalg.solve(A, Y)

plt.title("First Circuit Results")
plt.text(0.1 , 0.6 , "i = " + str(answers[0]) + "A", fontsize = "xx-large")
plt.text(0.1 , 0.4 , "CW current in middle loop = " + str(answers[1]) + "A", fontsize = "xx-large")
plt.xticks([])
plt.yticks([])
plt.show()





d = schemdraw.Drawing()
vLeft = d.add(elm.SourceV().up().label("8V"))
wireTopLeft = d.add(elm.Line().right())
d.add(elm.CurrentLabelInline(direction = "in").at(wireTopLeft).label("$i_x$"))
resistorTopLeft = d.add(elm.Resistor().down().label("1Ω"))
resistorBottomLeft = d.add(elm.Resistor().down().label("2Ω"))
wireBottomRight = d.add(elm.Line().right())
vRight = d.add(elm.SourceControlledV().up().label("3$i_x$"))
resistorTopRight = d.add(elm.Resistor().up().label("4Ω"))
wireTopRight = d.add(elm.Line().left())
iMiddle = d.add(elm.SourceI().endpoints(resistorTopLeft.end, resistorTopRight.start).label("3A"))
wireBottomLeft = d.add(elm.Line().left().at(wireBottomRight.start))
d.add(elm.Line().up().at(wireBottomLeft.end))

d.draw()
d.save("secondCircuitSchematic.png")



A = np.array([[0 , -1 , 1] , [0 , 5 , 2] , [3 , -1 , -2]])
Y = np.array([3 , 0 , 8])

answers = np.linalg.solve(A, Y)

plt.title("Second Circuit Results")
plt.text(0.07 , 0.65 , "$i_x$ = " + str(round(answers[0] , 4)) + "A", fontsize = "xx-large")
plt.text(0.07 , 0.45 , "CW current in topRight loop = " + str(round(answers[1] , 4)) + "A", fontsize = "x-large")
plt.text(0.07 , 0.25 , "CW current in bottomRight loop = " + str(round(answers[2] , 4)) + "A", fontsize = "x-large")
plt.xticks([])
plt.yticks([])
plt.show()





d = schemdraw.Drawing()
vLeft = d.add(elm.SourceV().up().label("12V"))
resistorTopLeft = d.add(elm.Resistor().right().label("4Ω"))
d.add(elm.CurrentLabelInline(direction = "in").at(resistorTopLeft).label("i"))
wireTopMiddle = d.add(elm.Line().right())
iTopRight = d.add(elm.SourceControlledI().right().label("4i"))
resistorRight = d.add(elm.Resistor().down().label("4Ω"))
wireBottomRight = d.add(elm.Line().left())
wireBottomMiddle = d.add(elm.Line().left())
wireBottomleft = d.add(elm.Line().left())
resistorMiddle = d.add(elm.Resistor().endpoints(wireBottomRight.end, iTopRight.start).label("3Ω"))
iMiddle = d.add(elm.SourceI().endpoints(wireBottomMiddle.end, wireTopMiddle.start).label("5A"))

d.draw()
d.save("thirdCircuitSchematic.png")



A = np.array([[4 , 3 , -3] , [-1 , 1 , 0] , [-4 , 0 , 1]])
Y = np.array([12 , 5 , 0])

answers = np.linalg.solve(A, Y)

plt.title("Third Circuit Results")
plt.text(0.07 , 0.65 , "i = " + str(round(answers[0] , 2)) + "A", fontsize = "xx-large")
plt.text(0.07 , 0.45 , "CW current in middle loop = " + str(round(answers[1] , 2)) + "A", fontsize = "xx-large")
plt.text(0.07 , 0.25 , "CW current in right loop = " + str(round(answers[2] , 2)) + "A", fontsize = "xx-large")
plt.xticks([])
plt.yticks([])
plt.show()