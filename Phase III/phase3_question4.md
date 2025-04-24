# Numerical Advection: Accuracy & Convergence

---

## Part 1: Convergence Study

**Quantity**  
```text
Error(Δx) = ‖rho_num(·, t=0.4) - rho_exact(·, t=0.4)‖₁
```

**Plot**  
Log–log graph of `Error` vs. `Δx` for γ=0 (upwind) and γ=1.75 (enhanced).

| Observation                              | Interpretation                             |
|------------------------------------------|--------------------------------------------|
| Data lie on a straight line of slope ≈ 1 | Global convergence is first-order: `Error = O(Δx)` |
| Halving Δx halves the L¹ error           | Discontinuities force at most first-order decay |

---

## Part 2: Temporal Profile at x = 0.5

**Exact solution**  
```text
rho_exact(t, 0.5) =
  0            for t < x/v = 1.0
  rho_l = 0.5  for t ≥ 1.0
```

**Numerical schemes**  
- γ = 0   (first-order upwind)  
- γ = 1.75 (quasi-second-order correction)  

| Feature                    | γ = 0 (Upwind)                   | γ = 1.75 (Enhanced)                      |
|----------------------------|----------------------------------|------------------------------------------|
| Front arrival time         | Exactly at t = 1.0               | Exactly at t = 1.0                       |
| Transition width (“smear”) | Very broad ramp (high diffusion) | Sharper ramp (reduced numerical viscosity) |
| Spurious oscillations      | None                             | None (γ chosen below oscillatory threshold) |

---

## Part 3: Spatial Profile at t = 0.4

**Exact step location**  
```text
x_front = v × t = 0.5 × 0.4 = 0.2
```

**Numerical snapshot (γ = 1.75)**  
- Plateau at rho ≈ 0.5 for x < 0.2  
- Plateau at rho ≈ 0   for x > 0.2  
- Transition region spans several grid cells of width ~ Δx  

> **Key point:** Even with a higher-order correction, the discontinuity remains smeared by `O(Δx)` due to intrinsic numerical viscosity.

---

## Overall Conclusions

1. **First-order global convergence.**  
   Discontinuities enforce an `O(Δx)` decay rate in the L¹ norm, regardless of any higher-order reconstruction.

2. **Tunable numerical diffusion.**  
   The parameter γ trades diffusion vs. potential oscillations. Here γ = 1.75 sharpens the front without introducing wiggles.

3. **Accurate front timing.**  
   Both schemes capture the exact arrival time `t = x/v` with negligible phase error.

4. **Grid refinement required.**  
   Only by refining `Δx` (and reducing `Δt` proportionally at fixed CFL) can the smeared transition be further narrowed.
