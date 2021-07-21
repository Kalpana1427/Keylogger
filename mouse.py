from pynput.mouse import Listener


def store_in_file(x, y):
    print('Current Position of mouse:{0}'.format((x, y)))


with Listener(on_move=store_in_file) as l:
    l.join()
