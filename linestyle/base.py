# encoding:utf-8
from collections import Iterable

class C():
	def __init__(self, *args):
		if len(args) == 1 and isinstance(args[0], int):
			self.r = self.g = self.b = self.__check(args[0])
		elif len(args) == 1 and isinstance(args[0], Iterable):
			self.r = self.__check(args[0][0])
			self.g = self.__check(args[0][1])
			self.b = self.__check(args[0][2])
		elif len(args) > 1:
			self.r = self.__check(args[0])
			self.g = self.__check(args[1])
			self.b = self.__check(args[2])
		else:
			self.r = self.g = self.b = 0

	def __str__(self):
		return f'C{self.r, self.g, self.b}'

	def __getitem__(self, idx):
		if idx == 0:
			return self.r
		elif idx == 1:
			return self.g
		elif idx == 2:
			return self.b
		else:
			raise StopIteration

	def __iter__(self):
		yield self.r
		yield self.g
		yield self.b

	def __check(self, d):
		if d < 0:
			return 0
		elif d > 255:
			return 255
		else:
			return d

	def T(self):
		self.r, self.b = self.b, self.r

class P():
	def __init__(self, *args):
		if len(args) == 1 and isinstance(args[0], int):
			self.x = args[0]
			self.y = args[0]
		elif len(args) == 1 and isinstance(args[0], Iterable):
			self.x = args[0][0]
			self.y = args[0][1]
		elif len(args) > 1:
			self.x = args[0]
			self.y = args[1]
		else:
			self.x = 0
			self.y = 0

	def __str__(self):
		return f'P{self.x, self.y}'

	def __len__(self):
		return 2

	def __iter__(self):
		yield self.x
		yield self.y

	def __getitem__(self, idx):
		if idx == 0:
			return self.x
		elif idx == 1:
			return self.y
		else:
			raise StopIteration

	def __add__(self, p):
		p = P(p)
		return P(self.x+p.x, self.y+p.y)

	def __sub__(self, p):
		p = P(p)
		return P(self.x-p.x, self.y-p.y)
		
	def __mul__(self, p):
		p = P(p)
		return P(self.x*p.x, self.y*p.y)

	def __truediv__(self, p):
		p = P(p)
		return P(self.x/p.x, self.y/p.y)

	def __and__(self, p):
		p = P(p)
		return P(self.x*p.x, self.y*p.y)

	def __or__(self, p):
		p = P(p)
		return P(self.x+p.x, self.y+p.y)

class G():
	def __init__(self, p1, p2, c=(0,0,0), sl=1, sc=(0,0,0)):
		self.p1 = P(p1)
		self.p2 = P(p2)
		self.c  = C(c)
		self.sl = sl
		self.sc = C(sc)
		self.__dr()

	def __dr(self):
		self.dp = self.__dp()
		self.r0 = self.__r0()
		self.r1 = self.__r1()

	def __str__(self):
		return f'L({self.p1}, {self.p2}, {self.c}, {self.sl}, {self.sc}, {self.dp}, {self.r0}, {self.r1})'

	def __dx(self):
		return self.p2.x - self.p1.x

	def __dy(self):
		return self.p2.y - self.p1.y

	def __dp(self):
		return P(self.p1.x+int(self.__dx()/2), self.p1.y+int(self.__dy()/2))

	def __r0(self):
		return abs(int(self.__dx()/2))

	def __r1(self):
		return abs(int(self.__dy()/2))

	def mv(self, p1, p2=None):
		self.p1 += p1
		self.p2 += p2 or p1
		self.__dr()
		return self

	def up(self, p1, p2=None):
		self.mv(P(p1) & (0, -1), P(p2 or p1) & (0, -1))
		return self

	def down(self, p1, p2=None):
		self.mv(P(p1) & (0, 1), P(p2 or p1) & (0, 1))
		return self

	def left(self, p1, p2=None):
		self.mv(P(p1) & (-1, 0), P(p2 or p1) & (-1, 0))
		return self

	def right(self, p1, p2=None):
		self.mv(P(p1) & (1, 0), P(p2 or p1) & (1, 0))
		return self

	def big(self, p):
		mp = lambda x:int(x*p)
		self.__dr()
		self.p1 = self.dp - (mp(self.r0), mp(self.r1))
		self.p2 = self.dp + (mp(self.r0), mp(self.r1))
		return self

	def small(self, p):
		mp = lambda x:int(x/p)
		self.__dr()
		self.p1 = self.dp - (mp(self.r0), mp(self.r1))
		self.p2 = self.dp + (mp(self.r0), mp(self.r1))
		return self

	def strong(self, p):
		p = p if p > 0 else 1
		self.sl = p
		return self

	def rotate(self, d, p=(0,0)):
		pass4
		return self

	def copy(self):
		return G(self.p1, self.p2, self.c, self.sl, self.sc)

	def range(self, p1, p2, n):
		return [self.mv(p1, p2).copy() for i in range(n)]

	def urange(self, p1, n):
		return [self.up(p1).copy() for i in range(n)]

	def drange(self, p1, n):
		return [self.down(p1).copy() for i in range(n)]

	def lrange(self, p1, n):
		return [self.left(p1).copy() for i in range(n)]

	def rrange(self, p1, n):
		return [self.right(p1).copy() for i in range(n)]

	def color(self, c=(0,0,0)):
		self.c = C(c)

if __name__ == '__main__':
	l = G(100, 200)
	print(l)
	l.big(3)
	print(l)
	l.small(3)
	print(l)
	ll = l.range((10, 10), (0,0), 3)
	for i in ll:
		print(i)
