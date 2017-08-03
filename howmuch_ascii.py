import colorconsole.terminal

ch2 = None
root = colorconsole.terminal.get_terminal()
while 1:
	ch=root.getch()
	if root.kbhit():
		ch2=root.getch()

	s = "1:\nascii:%s   \nstring:%s   \n"%(ord(ch),ch)
	s1 = '' if ch2==None else "2:\nascii:%s   \nstring:%s   \n"%(ord(ch2),ch2)

	root.print_at(0,0,s+s1.ljust(512))

	if ord(ch) == 27:#esc 退出
		break

	ch2 = None