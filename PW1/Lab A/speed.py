import time
import decay

N0 = 200000
lam = 0.4

# Measure pure-Python loop speed
t0 = time.perf_counter()
res_loop = decay.simulate_loop(N0, lam)
t1 = time.perf_counter()
t_loop = t1 - t0

# Measure NumPy speed
t0 = time.perf_counter()
res_numpy = decay.simulate(N0, lam)
t1 = time.perf_counter()
t_numpy = t1 - t0

speedup = t_loop / t_numpy if t_numpy > 0 else 0

print(f"loop: {t_loop:.4f} s")
print(f"numpy: {t_numpy:.4f} s")
print(f"speed-up: {speedup:.2f}x faster")