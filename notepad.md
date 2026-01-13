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
- **Status:** At Silver Cave (Accidental Fly).
- **Correction:** Must Fly to Goldenrod City.
- **Reason:** Previous Fly attempt targeted Silver Cave instead of Goldenrod.
- **Plan:**
  1. Open Fly Map (Mistral).
  2. Navigate Cursor: Silver Cave -> Left (to Johto) -> Goldenrod.
  3. Buy Super Repels at Dept Store.
  4. Fly to Ecruteak -> Route 37.
- **Inventory:** 16 Ultra Balls. Cash: ¥12,294.

# Tools & Automation
- **perform_grass_scan(num_steps):** Automates walking back and forth in grass.
- **Map Navigation Note:** Standard button presses failed to move the Fly cursor from New Bark Town. Suspect input speed issue. Testing with delays.
- **Reflection (Turn 38054):** Addressed stuck Fly map state. Previous inputs ignored. Using `navigate_fly_map` with 500ms delays to ensure registration. Goal: New Bark -> Ecruteak (Left x3) -> Goldenrod.
- **Map Navigation Strategy:** Resetting cursor by closing/reopening map (B -> A). Assuming start at Ecruteak, Down -> Goldenrod.
- **Fly Navigation:** Retrying Fly from Silver Cave. Step 1: Open Map. Step 2: Navigate Left (West) to Johto.
- **Correction:** Previous attempts to move cursor from Silver Cave failed. Testing if map is responding or if Silver Cave is isolated.
- **Fly Navigation:** Dead reckoning suggests cursor is at Ecruteak (Silver Cave -> Leftx3 -> New Bark -> Leftx3 -> Ecruteak).
- **Next Step:** Press Down to select Goldenrod. Verify destination before confirming.
- **Fly Navigation:** Attempting rigorous sequence: B (Reset) -> A (Open) -> Left x4 -> Down x1. Target: Goldenrod.
- **Reason:** Previous dead reckoning was inconsistent. Hard reset ensures known starting point (Silver Cave).
- **Fly Logic Correction:** Previous failure was due to cursor being on 'STATS' in submenu.
- **Current Plan:** Up (to FLY) -> A (Open Map) -> Left x4 (to Ecruteak) -> Down (to Goldenrod) -> A (Execute).
- **Assumed Starting Point:** Silver Cave (Current Location).