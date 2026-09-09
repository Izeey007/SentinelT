# SentinelT engineering mass allocation
# This is a design estimate, NOT a measured physical mass.

LIMIT_KG = 5.000

budget = [
    ('Chassis and lower armor', 1.10),
    ('Drive motors and gearboxes', 0.75),
    ('Wheels, hubs and shafts', 0.30),
    ('Battery and power system', 0.60),
    ('RC electronics, ESCs and wiring', 0.25),
    ('Guarded active mechanism + drive/mount', 0.70),
    ('Upper structure, arms and outer shells', 0.50),
    ('Bearings, brackets and fasteners', 0.25),
    ('Contingency allowance', 0.20),
]

total = sum(mass for _, mass in budget)
margin = LIMIT_KG - total

print('SENTINELT ENGINEERING MASS BUDGET')
for name, mass in budget:
    print(f'{name:<45} {mass:>5.2f} kg')
print('-' * 56)
print(f'{"TOTAL":<45} {total:>5.2f} kg')
print(f'{"MARGIN TO 5 KG":<45} {margin:>5.2f} kg')
print('STATUS:', 'PASS' if total < LIMIT_KG else 'FAIL')
print('\nIMPORTANT: final physical mass must be verified on a calibrated scale.')
