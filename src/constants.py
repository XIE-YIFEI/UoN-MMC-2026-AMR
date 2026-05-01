# Constants and Parameters for the AMR Model
# Ward 1: ICU | Ward 2: General Medicine

# Ward Capacities and Length of Stay
BEDS = [15, 60]
STAY = [12, 5]  # Days
DELTA = [1/s for s in STAY]  # Discharge rates

# Admission Rates (Lambda = BEDS / STAY to keep population constant)
LAMBDA = [BEDS[i] / STAY[i] for i in range(2)]

# Antibiotic & Transmission Parameters
TAU = [0.8, 0.4]    # Antibiotic pressure (80% vs 40%)
BETA = [0.15, 0.1]   # Transmission rate per HCW contact
ETA = [0.4, 0.4]     # Initial hand hygiene compliance (40%)
GAMMA = 1/45         # Natural clearance rate (approx 1.5 months)

# Boundary Conditions (From prompt)
M_R = 0.05           # 5% of new admissions already carry AMR
TRANSFER_RATE = 0.1  # 10% transfer from ICU to GenMed