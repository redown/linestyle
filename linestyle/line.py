# encoding:utf-8
from .base import C, G, P
from .draw import new,line,rect,circle,elli,text,show,mp4,gif

class Line(G):
	def __init__(self, p1, p2, c=(0,0,0), sl=1, sc=(0,0,0)):
		super().__init__(p1, p2, c, sl, sc)

	def __str__(self):
		return f'Line({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1})'

	def draw(self, im, t=False):
		if t:self.c.T()
		line(im, self.p1, self.p2, self.c, self.sl)

	def copy(self):
		return Line(self.p1, self.p2, self.c, self.sl, self.sc)

class Rect(G):
	def __init__(self, p1, p2, c=(0,0,0), sl=1, sc=(0,0,0)):
		super().__init__(p1, p2, c, sl, sc)

	def __str__(self):
		return f'Rect({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1})'

	def draw(self, im, t=False):
		if t:self.c.T()
		rect(im, self.p1, self.p2, self.c, self.sl)

	def copy(self):
		return Rect(self.p1, self.p2, self.c, self.sl, self.sc)

class Circle(G):
	def __init__(self, p, r, c=(0,0,0), sl=1, sc=(0,0,0)):
		super().__init__(P(p)-r, P(p)+r, c, sl, sc)

	def __str__(self):
		return f'Circle({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1})'

	def draw(self, im, t=False):
		if t:self.c.T()
		circle(im, self.dp, self.r0, self.c, self.sl)

	def copy(self):
		return Circle(self.dp, self.r0, self.c, self.sl, self.sc)

class Elli(G):
	def __init__(self, p, r0, r1, c=(0,0,0), sl=1, sc=(0,0,0), a0=0, a1=0, a2=360):
		p1 = P(p) - (r0, r1)
		p2 = P(p) + (r0, r1)
		super().__init__(p1, p2, c, sl, sc)
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2

	def __str__(self):
		return f'Elli({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1}, {self.a0, self.a1, self.a2})'

	def draw(self, im, t=False):
		if t:self.c.T()
		elli(im, self.dp, self.r0, self.r1, self.c, self.sl, self.a0, self.a1, self.a2)

	def copy(self):
		return Elli(self.dp, self.r0, self.r1, self.c, self.sl, self.sc, self.a0, self.a1, self.a2)

class Text(G):
	def __init__(self, p, t, c=(0,0,0), sl=1, sc=(0,0,0), font=None, size=20):
		self.t = t
		self.font = font
		self.size = size
		super().__init__(p, p, c, sl, sc)

	def __str__(self):
		return f'Text({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1}, {self.t}, {self.font}, {self.size})'

	def draw(self, im, t=False):
		if not t:self.c.T()
		text(im, self.p1, self.t, self.c, self.sl, self.font, self.size)

	def copy(self):
		return Text(self.p1, self.t, self.c, self.sl, self.sc, self.font, self.size)

class I():
	def __init__(self, g, t=True):
		self.g = g
		self.t = t

class Image():
	def __init__(self, w=400, h=400):
		self.imgs = []
		self.w = w
		self.h = h

	def add(self, g, t=False):
		if isinstance(g, list):
			for i in g: self.imgs.append(I(i.copy(), t))
		else:
			self.imgs.append(I(g.copy(), t))

	def clean(self):
		r = Rect((0,0), (self.w,self.h), c=(255,255,255), sl=-1)
		self.imgs.append(I(r, False))

	def draw(self, cf=0):
		iml = []
		im = new(self.w, self.h)
		for i in self.imgs:
			i.g.draw(im, cf)
			if i.t: iml.append(im.copy())
		iml.append(im)
		return iml

	def show(self, t=0.2):
		iml = self.draw()
		show(iml, t)

	def mp4(self, f, d=0.2):
		iml = self.draw()
		mp4(f, iml, d)

	def gif(self, f, d=0.2):
		iml = self.draw(1)
		gif(f, iml, d)

if __name__ == '__main__':
	im = Image(200,200)
	l = Line((50,50), (50,50), sl=5)
	print(l)
	im.add(l)
	l.up(1)
	im.add(l)
	print(l)
	l.big(2)
	im.add(l)
	print(l)
	im.add(l)
	c = Circle((100,100), 10, sl=3)
	print(c)
	im.add(c)
	im.show()
