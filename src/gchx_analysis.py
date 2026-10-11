"""
GCHX & Microclimate Chamber Thermal Analysis Script
Author: Ifthequar Ali Shaik
Institution: IIT Madras
Description: Calculates sensible heat load, LMTD, and heat exchanger effectiveness 
             for the GCHX-based air conditioning system.
"""

import numpy as np

def calculate_sensible_load(mass_flow_rate, specific_heat, t_ambient, t_target):
    """Calculates sensible heat load (Qs) in Watts."""
    return mass_flow_rate * specific_heat * (t_ambient - t_target)

def calculate_lmtd(t_in, t_out, t_ground):
    """Calculates Log Mean Temperature Difference (LMTD) for the GCHX loop."""
    dt1 = t_in - t_ground
    dt2 = t_out - t_ground
    if dt1 == dt2:
        return dt1
    return (dt1 - dt2) / np.log(dt1 / dt2)

def main():
    # Design Parameters
    m_dot = 0.5  # kg/s (Air mass flow rate)
    c_p = 1005   # J/kg·K (Specific heat of air)
    
    # Operational Cases
    cases = [
        {"mode": "Winter (GCHX Heating)", "t_amb": 11.2, "t_target": 18.0, "t_ground": 19.5, "t_out": 17.8},
        {"mode": "Summer (Cooling Coil)", "t_amb": 36.4, "t_target": 26.0, "t_ground": 23.1, "t_out": 25.5}
    ]
    
    print("--- GCHX System Thermal Analysis Output ---")
    for case in cases:
        qs = calculate_sensible_load(m_dot, c_p, case["t_amb"], case["t_target"])
        lmtd = calculate_lmtd(case["t_amb"], case["t_out"], case["t_ground"])
        print(f"Mode: {case['mode']}")
        print(f"  -> Sensible Heat Load (Qs): {qs:.2f} W")
        print(f"  -> LMTD: {lmtd:.2f} °C\n")

if __name__ == "__main__":
    main()
