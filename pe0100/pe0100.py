# Project Euler
# Problem 100
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu


# 21 15 		    = 1.4
# 120 85		    = 1.411
# 697 493		    = 1.4137
# 4060 2871	        = 1.4141414141
# 23661 16731	    = 1.4142011834
# 137904 97513	    = 1.4142114384
# 803761 568345	    = 1.4142131979
# 4684660 3312555   = 1.4142134
# 27304197 19306983 = 1.41421355

for b in range(1, 100000000):
    for t in range(int(b * 1.414213), int(b * 1.414214)):
        if b * (b-1) * 2 == t * (t - 1):
            print(t, b)