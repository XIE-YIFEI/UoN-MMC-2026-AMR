import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from constants import *
from model import amr_ode

# Time span: 1 year
t = np.linspace(0, 365, 365)

# Baseline Parameters Dictionary
params = {
    'tau1': TAU[0], 'tau2': TAU[1],
    'beta1': BETA[0], 'beta2': BETA[1],
    'eta1': ETA[0], 'eta2': ETA[1],
    'nu': TRANSFER_RATE * DELTA[0]
}

# Initial State: Mostly uncolonized
# [PU1, PN1, PR1, HC1, PU2, PN2, PR2, HC2]
y0 = [14, 0, 1, 0, 58, 0, 2, 0]

# Run Simulation
sol = odeint(amr_ode, y0, t, args=(params,))

# --- Visualization ---
plt.figure(figsize=(10, 5))
plt.plot(t, sol[:, 2], 'r-', label='AMR Patients (ICU)')
plt.plot(t, sol[:, 6], 'b-', label='AMR Patients (GenMed)')
plt.title('Baseline AMR Dynamics - 12 Months')
plt.xlabel('Days')
plt.ylabel('Patient Count')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../results/plots/baseline_dynamics.png', dpi=300)
plt.show()

# --- Sanity Check (Total Population) ---
total_pop_icu = sol[-1, 0:3].sum()
print(f"Sanity Check: Total ICU Patients = {total_pop_icu:.2f} (Expected ~15)")