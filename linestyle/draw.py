# encoding:utf-8
import time
import itertools
import numpy as np
import cv2
import imageio
from PIL import Image,ImageDraw,ImageFont

def rc(c, t=True):
	return tuple(c)[::-1] if t else tuple(c)

def new(w=340, h=480, c=(255,255,255)):
	im = np.ones((h, w, 3), dtype=np.uint8)
	im[:,:,:]=rc(c)
	return im

def show(iml, s=0):
	s = 0 if s < 0 else s
	if not isinstance(iml, list):
		cv2.imshow('img', iml)
		cv2.waitKey()
	else:
		items = itertools.cycle(iml)
		key = 0
		while key & 0xFF != 27:
			cv2.imshow('imgs', next(items))
			key = cv2.waitKey(42)
			time.sleep(s)
	cv2.destroyAllWindows()

def line(im, p1, p2, c=(0,0,0), l=1):
	cv2.line(im, tuple(p1), tuple(p2), rc(c), l)

def rect(im, p1, p2, c=(0,0,0), l=1):
	cv2.rectangle(im, tuple(p1), tuple(p2), rc(c), l)

def circle(im, p, r, c=(0,0,0), l=1):
	cv2.circle(im, tuple(p), r, rc(c), l)

def elli(im, p, r0, r1, c=(0,0,0), l=1, rotateAngle=0, startAngle=0, endAngle=360):
    cv2.ellipse(im, tuple(p), (r0, r1), rotateAngle, startAngle, endAngle, color=rc(c), thickness=l)

def text(im, p1, txt, c=(0,0,0), l=1, font=None, size=20):
    # cv2.putText(im, txt, tuple(p1), font, size, color=tuple(c), thickness=l)
    iim = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    oim = Image.fromarray(iim)
    dro = ImageDraw.Draw(oim)
    font = font or 'simsun.ttc'
    font = ImageFont.truetype(font, size, encoding='utf-8')
    dro.text(tuple(p1), txt, rc(c), font=font)
    im1 = cv2.cvtColor(np.array(oim), cv2.COLOR_RGB2BGR)
    im[:,:,:] = im1[:,:,:]

def mp4(f, im, d):
	fps=16
	size=im[0].shape[:2]
	avi = cv2.VideoWriter_fourcc(*'MJPG')
	videowriter = cv2.VideoWriter(f,avi,fps,size)
	for i in im:
		videowriter.write(i)

def gif(f, im, d=0.3):
	imageio.mimsave(f, im, 'gif', duration = d)

if __name__ == '__main__':
	c = (1,2,3)
	print(rc(c))
	print(rc(c, 1))
	print(rc(c, 0))