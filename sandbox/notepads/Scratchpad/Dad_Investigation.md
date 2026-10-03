# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22).
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Active Hypotheses for Progression
### Hypothesis H50: Dark Sector Northeast Staircase & Perimeter Audit
- **Premise**: Testing if the spotlight-illuminated Dark Sector (entered via 30, 4) contains any unmapped tiles or interactive triggers.
- **Falsifiable Test**:
  1. Enter staircase at (30, 4) to arrive at Dark Sector (31, 9).
  2. Audit eastern boundary at column 31 and northern corridor along row 9.
  3. Falsified if all perimeter tiles match documented solid stone walls and rugged rock at (22, 10).

### Hypothesis H51: Central Park Pond Edge Ground Graphic Audit
- **Premise**: In Turn 18855, visual crop 'pond_grass_item.png' revealed a distinct blue ground graphic on the grass strip at the northeast edge of Central Park pond (approx cols 41-43, rows 18-19).
- **Falsifiable Test**:
  1. Return to Sovio City Central Park.
  2. Navigate to the northeast pond grass border.
  3. Inspect the graphic coordinates directly and test interaction with 'A' to verify if it represents an item, tracks, or decorative flora.
