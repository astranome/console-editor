from colorconsole.terminal import *

scr=get_terminal()
keymap={
	'backspace':(8,None),
	'enter':(13,None),
	'esc':(27,None),
	'tab':(9,None),
	'key_up':(224,72),
	'key_down':(224,80),
	'key_left':(224,75),
	'key_right':(224,77)
}

def ctrl(ch):
	int_ch=ord(ch)
	if int_ch>=97 and int_ch<=122:
		return (int_ch-96,None)
	else:
		raise Exception("wrong num: %2d"%int_ch)

def b_decode(b_char):
	return bytes.decode(b_char)

def ch_input():
	ch1=ord(scr.getch())
	ch2=None if scr.kbhit(0.01)==0 else ord(scr.getch())
	return (ch1,ch2)

while 1:
	i=ch_input()
	if i==keymap['enter']:
		scr.cprint(7,0,'helloworld')
	elif i==keymap['key_up']:
		scr.move_up()
	elif i==keymap['key_down']:
		scr.move_down()
	elif i==keymap['key_left']:
		scr.move_left()
	elif i==keymap['key_right']:
		scr.move_right()
	elif i==ctrl('q'):
		exit(0)