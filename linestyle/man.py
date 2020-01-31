from .line import *

def Hair(p1, p2):
	h=Line(p1, p2, sl=2)
	return h.rrange(7, 5)

def Head(p1, p2):
	return Circle(p1, p2, sl=2)

def Eye(p1, p2):
	return Circle(p1, p2, sl=2)

def Body(p1, p2):
	return Line(p1, p2, sl=2)

def Arm(p1, p2):
	return Line(p1, p2, sl=2)

def Leg(p1, p2):
	return Line(p1, p2, sl=2)

def Mouse(p1, p2):
	a, b = p2
	return Elli(p1, a, b, sl=2)

class Man():
	def __init__(self, p=(0,0), t=10):
		self.p = P(p)
		self.t = t
		M = lambda x,y:(int(self.t*x),int(self.t*y))
		self.hair = Hair(self.p+M(1,0), self.p+M(1,1))
		self.head = Head(self.p+M(2,2), 30)
		self.leye = Eye(self.p+M(1.4,1.8), 4)
		self.reye = Eye(self.p+M(2.6,1.8), 4)
		self.mouse = Mouse(self.p+M(2,2.3), (4,2))
		self.body = Body(self.p+M(2,3), self.p+M(2,7))
		self.larm = Arm(self.p+M(2,3), self.p+M(1,7))
		self.rarm = Arm(self.p+M(2,3), self.p+M(3,7))
		self.lleg = Leg(self.p+M(2,7), self.p+M(1,11))
		self.rleg = Leg(self.p+M(2,7), self.p+M(3,11))
		self.im = Image(360,480)

	def clean(self):
		self.im.clean()

	def draw(self):
		self.im.clean()
		self.im.add(self.hair)
		self.im.add(self.head)
		self.im.add(self.leye)
		self.im.add(self.reye)
		self.im.add(self.mouse)
		self.im.add(self.body)
		self.im.add(self.larm)
		self.im.add(self.rarm)
		self.im.add(self.lleg)
		self.im.add(self.rleg, True)

	def show(self):
		self.im.show()

if __name__ == '__main__':
	m = Man()
	m.show()