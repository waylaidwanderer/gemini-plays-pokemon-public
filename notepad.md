# Roamer Hunt Strategy
- **Goal:** Catch Raikou & Entei.
- **Current Plan:** Fly to Ecruteak City (Central Hub).
- **Status:** Flying to Ecruteak City.
- **Action:** Select FLY (A) -> Navigate Map (Left x3) -> Confirm (A x2).
- **Goal:** Relocate to Ecruteak Hub.
- **Next:** Check Roamers.
- **Resources:** 16 Repels.
- **Session Start:** Turn 36369. Current: 36756.

# Reflection (Turn 36756)
- **Error Analysis:** Route 35 Gatehouse Shuffle failed to move Roamers for 15+ cycles.
- **Lesson:** Gatehouse transitions likely do not count as map transitions for Roamers. Use Route boundaries or Fly.
- **Tooling:** "cycle_roamer_hunt" tool failed due to positioning drift and warp mechanics. Manual 2-turn shuffle was safer but tedious.
- **Correction:** Abandoned Route 35. Relocating to Ecruteak.

# Tile Mechanics
- **Warp Tiles:** Must step *off* and then *back on* to trigger. Standing on them does nothing.
- **Ledge Hop:** One-way jump.
- **Headbutt Tree:** Can be shaken for Pokemon.

# Hall of Fame
- **Champion:** Turn 33314. MVP: Muscle (Machoke) Lv88.

# Completed Objectives
- **Johto Gyms:** All 8 Badges.
- **Elite Four:** Defeated.
- **Kanto Gyms:** All 8 Badges.
- **Red:** Defeated.
- **Lugia:** Caught (Maelstrom).
- **Correction:** Fly attempt 1 failed (stayed in New Bark). Retrying with 'Left, Left, Up' and slower inputs.
- **Correction:** Fly attempt 2 failed (landed in Cherrygrove). Retrying from Cherrygrove with 'Left, Up'.
- **Correction:** Fly attempt 3 failed (landed in Cherrygrove). 'Left, Up' didn't work. Trying 'Left, Left, Up' (Cherrygrove -> Violet -> Goldenrod -> Ecruteak).
- **Correction:** Fly map cursor was on New Bark Town (despite player being in Cherrygrove).
- **Navigation:** Attempting 'Left (Cherrygrove) -> Left (Violet) -> Left (Ecruteak)' from New Bark Town cursor.
- **Correction:** Fly attempt 5 failed (Left x3 from New Bark -> New Bark). Grid navigation is unclear. Switching to Step-by-Step verification to ensure correct destination selection.
- **Correction:** Attempting 'Left -> Up -> Left' for Fly path. New Bark -> Cherrygrove (Left) -> Violet (Up) -> Ecruteak (Left).
- **Observation:** Fly attempt 'Left -> Up -> Left' from New Bark cursor landed in Cherrygrove.
- **Strategy:** Opening Fly map and moving cursor 'Up' from Cherrygrove to verify destination text before confirming.
- **Strategy:** Opening Fly map and pausing to visually confirm the default cursor position before navigating.
- **Verification:** Resetting UI state with 'B, B, B' to ensure clean menu navigation.
- **Mechanic:** Fly map cursor remembers the last destination (New Bark Town), NOT the player's current location (Cherrygrove).
- **Navigation Test:** Attempting 'Left, Left, Up' from New Bark cursor and checking text to map the grid.
- **Observation:** Verified cursor starts at Cherrygrove City.
- **Navigation Test:** Attempting 'Left -> Up' from Cherrygrove to find Ecruteak.
- **Observation:** 'Left, Up' from Cherrygrove landed on Violet City.
- **Navigation:** Attempting 'Left' from Violet City to reach Ecruteak.
- **Observation:** 'Left' from Violet City did not change destination.
- **Hypothesis:** Violet City is reached via 'Left, Left, Up' from New Bark. Ecruteak is likely 'Left' or 'Up' from Violet.
- **Navigation Test:** Attempting 'Left, Left, Up, Left' from New Bark cursor.
- **Observation:** Cursor is currently at Cherrygrove City.
- **Verification:** Pressing 'Up' to verify it selects Violet City (as observed in Turn 36801).
- **Observation:** 'Left' from Violet City appears to be invalid (cursor didn't move).
- **Strategy:** Backtracking to Cherrygrove ('Down') and testing 'Left' from there to find a path to the west side of Johto (Goldenrod/Ecruteak).
- **Observation:** 'Left' from Cherrygrove appeared to fail (remained at Cherrygrove).
- **Hypothesis:** Path to Ecruteak might be Cherrygrove -> Azalea -> Goldenrod -> Ecruteak.
- **Navigation Test:** Attempting 'Left, Up, Up' from Cherrygrove.
  - If Left works: Azalea -> Goldenrod -> Ecruteak.
  - If Left fails: Cherrygrove -> Violet -> Mahogany/Ecruteak?
- **Observation:** 'Left' from Cherrygrove leads to Azalea Town.
- **Hypothesis:** Previous 'Up' inputs may have been eaten by animation. Testing 'Up' from Azalea to reach Goldenrod.