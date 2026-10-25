import numpy as np
import matplotlib.pyplot as plt

actual_cutting_power = 1852.9 - 346.8
kc = (actual_cutting_power / (150.0 / 60.0)) / (1.0 * 0.2)

print(f"Pc: {actual_cutting_power:.1f} W\nKc: {kc:.1f} MPa")

def calc_drill(D, f, vc, kc):
    vf = f * ((vc * 1000) / (np.pi * D))
    p = (kc * (np.pi * (D**2) / 4) * vf) / 60000 
    return p, vf

p1, vf1 = calc_drill(5.0, 0.2, 50.0, kc)
t1 = (10.0 / vf1) * 60

p2_full, vf2 = calc_drill(13.0, 0.2, 50.0, kc)
p2 = p2_full * ((13.0**2 - 5.0**2) / 13.0**2)
t2 = (20.0 / vf2) * 60

print(f"Pre-Drill: {p1:.1f} W, {t1:.2f} s\nMain Drill: {p2:.1f} W, {t2:.2f} s")

times = [0, 2, 2, 2+t1, 2+t1, 4+t1, 4+t1, 4+t1+t2, 4+t1+t2, 6+t1+t2]
powers = [0, 0, p1, p1, 0, 0, p2, p2, 0, 0]

plt.step(times, powers, where='post')
plt.show()
