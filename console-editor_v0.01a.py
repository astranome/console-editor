#version:0.01a
#write by inoit
#mail:2877712781@qq.com
from colorconsole.terminal import *
import click
import time

class editor:
	a,b=20,5
	string=['']
	cx,cy=0,0
	filename=None

def read():
	with open(e.filename,'r') as fp:
		e.string = [l for l in fp.read().split('\n')]

def save():
	with open(e.filename,'w') as fp:
		fp.write('\n'.join(e.string))

def send(msg):
	tx,ty=e.cx,e.cy
	root.print_at(0,16,msg)
	e.cx,e.cy=tx,ty

def keyprocess(ch1,ch2):
	if ord(ch1)==27:# esc退出
		exit(0)
	elif ord(ch1) == 19:# ctrl+s 保存
		save()
		send('%3d byte was save'%(len(e.string)))
	elif ord(ch1) == 13:# enter回车
		if e.cy>=0 and e.cy<=e.b:
			e.string.append('')
			e.cx,e.cy=0,e.cy+1
	elif ord(ch1) == 8:# backspace删除
		if e.cx==0 and e.cy!=0:
			e.string.pop()
			e.cx,e.cy = len(e.string[e.cy-1]),e.cy-1
		elif e.cx>0:
			e.string[e.cy]=e.string[e.cy][:-1]
			e.cx -= 1
			root.putch(b'\x08')
			root.putch(b' ')
	elif ord(ch1) == 224:# 上下左右
		if ord(ch2) == 72 and e.cy>0:
			e.cy-=1
		elif ord(ch2) == 80 and e.cy<=e.b:
			e.cy+=1
		elif ord(ch2) == 75 and e.cx>0:
			e.cx-=1
		elif ord(ch2) == 77 and e.cx<=e.a:
			e.cx+=1
	elif ord(ch1)>=32 and ord(ch1)<=126:# 普通打印
		if e.cx<len(e.string[e.cy]):
			e.string[e.cy]=e.string[e.cy][:e.cx]+bytes.decode(ch1)+e.string[e.cy][e.cx+1:]
			root.putch(ch1)
		elif e.cx>=0 and e.cx<=e.a:
			root.putch(ch1)
			e.string[e.cy] += bytes.decode(ch1)
			e.cx += 1

root=get_terminal()
e=editor()

@click.command()
@click.option('--file', default='default.txt', help='pyedit.py <filename>.')
def main(file):
	__import__('os').system('cls')
	ch1,ch2=0,0
	e.filename=file
	if file=='default.txt':
		send('default file was open to write')
	else:
		with open(file,'r') as fp:
			root.print_at(0,0,fp.read())
		e.filename=file
		read()
	root.gotoXY(0,0)
	while True:
		ch1=root.getch()
		if root.kbhit(0.01):
			ch2=root.getch()
		keyprocess(ch1,ch2)
		root.gotoXY(e.cx,e.cy)
		time.sleep(0.05)

if __name__ == '__main__':
	main()
