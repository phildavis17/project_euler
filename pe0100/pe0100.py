# Project Euler
# Problem 100
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu


known_vals = [
    (21, 15),
    (120, 85),
    (697, 493),
    (4060, 2871),
    (23661, 16731),
    (137904, 97513),
    (803761, 568345),
    (4684660, 3312555),
    (27304197, 19306983),
]



def refine_range(vals: list) -> tuple:
    prev_guess = 0.0
    for h, l in vals:
        latest_guess = h / l
        if not prev_guess:
            prev_guess = latest_guess    
        prev_str = str(prev_guess)
        latest_str = str(latest_guess)
        new_str = ""
        for i, _ in enumerate(latest_str):
            if latest_str[:i] == prev_str[:i]:
                new_str = latest_str[:i]
        low = float(new_str + "0")
        high = float(new_str + "9")
        prev_guess = latest_guess
    return (low, high)

# 21 15 		    = 1.4
# 120 85		    = 1.411
# 697 493		    = 1.4137
# 4060 2871	        = 1.4141414141
# 23661 16731	    = 1.4142011834
# 137904 97513	    = 1.4142114384
# 803761 568345	    = 1.4142131979
# 4684660 3312555   = 1.4142134
# 27304197 19306983 = 1.41421355

low, high = 1.0, 2.0
found_vals = []

for b in range(1, 100_000_000):
    target = b * (b - 1) * 2
    for t in range(int(b * low), int(b * high) + 1):
        if t * (t - 1) == target:
            found_vals.append((t, b))
            low, high = refine_range(found_vals)
            for v in found_vals:
                print(v)
            print(f"REFINED: {low} - {high}")
            break

#for b in range(1_000_000, 100_000_000):
#    if b % 1_000_000 == 0:
#        print(f"checking {b}...")
#    for t in range(int(b * 1.414213), int(b * 1.414214)):
#        if b * (b-1) * 2 == t * (t - 1):
#            print(f"FOUND: {t}, {b}")