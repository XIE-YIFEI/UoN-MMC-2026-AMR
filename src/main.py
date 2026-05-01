import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from constants import *
from model import amr_ode

# Setup time and initial state
t = np.linspace(0, 365, 365)
y0 = [14, 0, 1, 0, 58, 0, 2, 0]

# Create output directory
save_dir = 'results/plots'
os.makedirs(save_dir, exist_ok=True)

# Base parameters
base_params = {
    'tau1': TAU[0], 'tau2': TAU[1],
    'beta1': BETA[0], 'beta2': BETA[1],
    'eta1': ETA[0], 'eta2': ETA[1],
    'nu': TRANSFER_RATE * DELTA[0]
}

# Run baseline simulation
sol_base = odeint(amr_ode, y0, t, args=(base_params,))

# Part A1: Baseline Dynamics
plt.figure(1, figsize=(10, 5))
plt.plot(t, sol_base[:, 2], 'r-', label='AMR Patients (ICU)')
plt.plot(t, sol_base[:, 6], 'b-', label='AMR Patients (GenMed)')
plt.title('Baseline: AMR Transmission Dynamics')
plt.xlabel('Days')
plt.ylabel('Number of Patients')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(f'{save_dir}/1_baseline_dynamics.png', dpi=300)

# Part A2: Sensitivity Analysis
plt.figure(2, figsize=(10, 5))
scores = [0.2, 0.4, 0.6, 0.8]

for s in scores:
    p = base_params.copy()
    p['eta1'], p['eta2'] = s, s
    sol_wash = odeint(amr_ode, y0, t, args=(p,))
    plt.plot(t, sol_wash[:, 2], label=f'Hand Washing: {int(s*100)}%')

plt.title('Sensitivity Analysis: Hand Hygiene Compliance in ICU')
plt.xlabel('Days')
plt.ylabel('AMR Patients in ICU')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(f'{save_dir}/2_sensitivity_hand_washing.png', dpi=300)

# Part B: Combined Strategy
plt.figure(3, figsize=(10, 5))

# Baseline
plt.plot(t, sol_base[:, 2], 'r-', alpha=0.5, label='1. Baseline')

# Hand Hygiene Only
p_wash = base_params.copy()
p_wash['eta1'], p_wash['eta2'] = 0.8, 0.8
sol_wash_only = odeint(amr_ode, y0, t, args=(p_wash,))
plt.plot(t, sol_wash_only[:, 2], 'b--', label='2. Hand Hygiene (80%)')

# Abx Stewardship Only
p_abx = base_params.copy()
p_abx['tau1'] *= 0.70
p_abx['tau2'] *= 0.70  
sol_abx_only = odeint(amr_ode, y0, t, args=(p_abx,))
plt.plot(t, sol_abx_only[:, 2], 'g--', label='3. Abx Stewardship (-30%)')

# Combined Strategy
p_combo = base_params.copy()
p_combo['eta1'], p_combo['eta2'] = 0.8, 0.8
p_combo['tau1'] *= 0.70
p_combo['tau2'] *= 0.70
p_combo['beta1'] *= 0.30
p_combo['beta2'] *= 0.30
sol_combo = odeint(amr_ode, y0, t, args=(p_combo,))
plt.plot(t, sol_combo[:, 2], 'm-', linewidth=2.5, label='4. Combined Synergy (Wash+Abx+Screen)')

plt.title('Part B: Synergistic Impact of Combined Interventions')
plt.xlabel('Days')
plt.ylabel('AMR Patients in ICU')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(f'{save_dir}/3_combined_synergy.png', dpi=300)

plt.show()