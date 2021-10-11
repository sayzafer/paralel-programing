from bc_numba import *
from threading import Thread

if __name__ == '__main__':
    find_e = FindE()
    tt = TicToc()
    tt.tic()
    n = 10000000
    thread = Thread(target=find_e.find_euler, args=(n,))
    thread.start()
    thread.join()

    print("e = ", find_e.value_of_e())
    print("TIME = ", tt.toc())