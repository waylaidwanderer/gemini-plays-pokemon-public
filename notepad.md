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
- **Status:** Flying to Goldenrod City.
- **Reason:** Buying Super Repels at Dept Store.
- **Plan:**
  1. Fly to Goldenrod (Mistral).
  2. Buy Super Repels (Target: 20+).
  3. Fly back to Ecruteak.
  4. Resume hunt.
- **Inventory:** 16 Ultra Balls. Cash: ¥12,294.

# Tools & Automation
- **perform_grass_scan(num_steps):** Automates walking back and forth in grass.
- **Map Navigation Note:** Standard button presses failed to move the Fly cursor from New Bark Town. Suspect input speed issue. Testing with delays.
- **Reflection (Turn 38054):** Addressed stuck Fly map state. Previous inputs ignored. Using `navigate_fly_map` with 500ms delays to ensure registration. Goal: New Bark -> Ecruteak (Left x3) -> Goldenrod.
- **Map Navigation Strategy:** Resetting cursor by closing/reopening map (B -> A). Assuming start at Ecruteak, Down -> Goldenrod.