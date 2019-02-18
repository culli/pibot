from rrb3 import *
import curses
import sys

screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

curses.noecho()
curses.cbreak()

screen.keypad(True)
screen.timeout(100)

rr = RRB3(9, 6)

try:
        while True:
                dist = rr.get_distance()
                if dist < 20:
                        rr.stop()
                        screen.addstr(10, 0, 'obstacle     ', curses.color_pair(7))
                elif dist >= 20:
                        screen.addstr(10, 0, '             ')
                        screen.addstr(1, 0, str(dist) + '                       ')
                        char = screen.getch()
                if char == ord('q'):
                        break
                elif char == curses.KEY_RIGHT:
                        screen.addstr(0, 0, 'right')
                        rr.right(0.88, 1)
                elif char == curses.KEY_LEFT:
                        screen.addstr(0, 0, 'left ')
                        rr.left(0.88, 1)
                elif char == curses.KEY_UP:
                        screen.addstr(0, 0, 'up   ')
                        rr.set_motors(1, 0, 1, 0)
                elif char == curses.KEY_DOWN:
                        screen.addstr(0, 0, 'down ')
                        rr.stop()
                        dist = rr.get_distance()
                        screen.addstr(1, 0, str(dist) + '                   ')
                elif char == ord('s'):
                        screen.addstr(0, 0, 'stop  ')
                        rr.stop()
except:
        rr.stop()
        curses.endwin()
        print("Unexpected error:", sys.exc_info()[0])
finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()

