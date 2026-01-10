# Strategic Notes
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Hunt Roaming Beasts (Raikou/Entei).
- **Navigation:** Return to Ecruteak City.

## Roamer Hunt
- **Target:** Raikou & Entei.
- **Method:** Route 37 Loop.
- **Note:** No trapper in party. Goal is to encounter for Dex tracking.

## Observations & Tips
- **Menu Navigation:** `navigate_menu` can register double inputs. Use `press_buttons` for precision if needed.
- **Celadon Dept Store:** 2F has Repels (Left Clerk) and TMs (3F).
- **Exploration:** Unmarked warps at (16,3) & (17,3) (Celadon Mansion back?).

# Current Strategy
## Roamer Hunt (Raikou/Entei)
- **Goal:** Encounter Raikou and Entei.
- **Location:** Ecruteak City (South Exit).
- **Setup:** Super Repel Active (Turn 32028).
- **Hunting Loop:**
  1. Move Down to Route 37 (8,0).
  2. Execute `rt37_hunt_return` (Walk in grass, return to gate).
  3. If encounter (Battle Screen): STOP. Catch/Track.
  4. If no encounter: Loop automatically returns to Ecruteak.
  5. Repeat.
- **Mechanics:** Repel filters Lvl < 36. Roamers are Lvl 40.

## Map Notes
- **Route 37:** Grass patches at (6,2)-(9,5).
- **Ecruteak City:** Connection North.