# Mechanics & State
- **Location:** Route 37.
- **Goal:** Encounter Raikou/Entei.
- **Map Transition Latency:** All map transitions (Warps, Fly, Borders) require massive delays (8s+ load) to prevent input swallowing. Critical for automation.
- **Roamer Hunt:** Scramble positions by moving between Ecruteak and Route 37.

# Hall of Fame & Progress
- **Champion:** Turn 33314.
- **Lugia:** Caught (Maelstrom).
- **All 16 Badges:** Obtained.
- **Red:** Defeated.

# Important Locations
- **Route 37:** Contains Red, Blue, and Black Apricorns.
- **Ecruteak City:** Pokemon Center, Tin Tower, Burned Tower.

# Current Task: Roamer Hunt (Raikou/Entei)
- **Start Turn:** 37586
- **Last Reset:** 37974
- **Location:** Route 37 (Grass).
- **Goal:** Register in Pokedex -> Track on Map.
- **Status:** Repel worn off. Applying last one.
- **Strategy:** Repel Shuffle (Route 37 <-> Ecruteak).
  - Gyarados (Lv 36) + Repel blocks wilds, allows Roamers (Lv 40).
  - 1 Repel remaining.
  - **Critical Issue:** Money is ¥294. Cannot buy Repels.
  - **Plan B:** Sell ~5 Ultra Balls at Ecruteak Mart to fund Super Repels.

# Tools & Automation
- **perform_grass_scan(num_steps):** Automates walking back and forth in grass.
- **reset_roamers:** Automates the Route 37 <-> Ecruteak transition with 15s delays to handle lag.