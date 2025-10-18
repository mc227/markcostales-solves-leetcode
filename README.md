This is my attempt to doing 100 code challenge problems as outlined by Raymond Gan on how to be competitive for software jobs.


"""
In IEEE 754 32-bit floating-point format, the number is stored with bit 31 as the sign (0=positive, 1=negative), bits 30-23 as the exponent (interpreted as standard binary then bias-adjusted by subtracting 127), and bits 22-0 as the fraction (interpreted as fractional powers of 2: 0.5, 0.25, 0.125, etc.), with the final value calculated as ±1.fraction × 2^(exponent-127).
"""