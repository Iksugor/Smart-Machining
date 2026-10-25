pi = 3.141592653589793

actual_cutting_power = 1852.9 - 346.8
kc = (actual_cutting_power / (150.0 / 60.0)) / (1.0 * 0.2)

print("Pc:", actual_cutting_power, "W")
print("Kc:", kc, "MPa")

def calc_drill(D, f, vc, kc):
    vf = f * ((vc * 1000) / (pi * D))
    p = (kc * (pi * (D**2) / 4) * vf) / 60000 
    return p, vf

p1, vf1 = calc_drill(5.0, 0.2, 50.0, kc)
t1 = (10.0 / vf1) * 60

p2_full, vf2 = calc_drill(13.0, 0.2, 50.0, kc)
p2 = p2_full * ((13.0**2 - 5.0**2) / 13.0**2)
t2 = (20.0 / vf2) * 60

print("Pre-Drill:", p1, "W,", t1, "s")
print("Main Drill:", p2, "W,", t2, "s")
