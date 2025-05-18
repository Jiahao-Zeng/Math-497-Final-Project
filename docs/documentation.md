---
layout: article
title: Documentation
permalink: /documentation/
use_math: true
---

## Project Overview

- This final project encompasses all techniques learned in Math 497: computational analysis and special topics. We reference a traffic model summary which was a catalyst for upwind and filtered upwind.

## Implementation Details
- Real world traffic analyzation
- Fluid Dynamics/ Aerodynamics
- Environmental modeling
- Industrial and Engineering aspects

### Core Components

1. Advection and Transport Phenomena  
2. Numerical Methods for PDEs  
3. Error Analysis  
4. Time-Stepping Schemes  
5. Wave Propagation and Characteristics  
6. Mathematical Modeling  
7. Parameter Sensitivity  
8. Implementation and Visualization

### Technical Specifications

- Finite Difference Discretization: Forward, backward, and upwind schemes
- Filtered Upwind Method: Applied for enhanced stability and sharpness
- Parameters:  
  - Velocity $\( \bar{v} \)$
  - Grid size $\( \Delta x = 2^{-i} \)$  
  - Time step $\( \Delta t \)$ based on CFL condition  
  - Filtering parameter $\( \gamma \)$  
- Simulation Domain: $\( x \in [0,1] \), \( t \in [0,T] \)$
- Target Evaluation Point: $\( x = 0.5 \)$
- Programming Language: Python (NumPy, Matplotlib)

## Results

- Error vs. $\( \Delta x \)$: Demonstrates expected convergence rates
- Stability:  
  - Unfiltered schemes show oscillations at discontinuities  
  - Filtered schemes suppress nonphysical behavior
- Accuracy:  
  - Higher-order filters yield reduced numerical diffusion  
  - Sensitivity to $\( \gamma \)$ evident in solution profiles
- Log-Log Error Plots:  
  - Used to estimate empirical order of accuracy

## Future Work

**Objective:**  
To simulate and analyze airflow around a Formula-style race car body, focusing on drag reduction, downforce generation, and flow separation zones using numerical methods.

**Project Scope:**
- Model 2D and 3D flow around a simplified race car geometry (with/without rear wing and diffuser)
- Use computational fluid dynamics (CFD) tools or finite difference methods to solve Navier-Stokes or Euler equations
- Evaluate lift and drag coefficients under different configurations and angles of attack

**Technical Goals:**
- Investigate the effects of body shape on pressure distribution and vortices
- Apply upwind and filtered upwind schemes to ensure numerical stability in high-speed flow
- Analyze wake dynamics and identify regions of turbulent separation

**Tools and Techniques:**
- CFD software (OpenFOAM, Ansys Fluent) or custom Python simulations
- Structured or unstructured mesh generation
- Visualization with Matplotlib, ParaView, or Blender

**Relevance:**  
This project would enhance understanding of applied aerodynamics in motorsport engineering, aiding in the optimization of vehicle performance through better aerodynamic efficiency and stability at high speeds.
## References

Childress, Stephen. Notes on Traffic Flow. 7 Mar. 2005.
Courtney-Pahlevani, Faranak. Class Notes for MATH 497: Special Topics in Applied Mathematics. Spring 2025, Penn State University.
