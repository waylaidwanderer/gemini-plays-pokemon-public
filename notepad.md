# Roamer Hunt Strategy
- **Goal:** Catch Raikou & Entei.
- **Current Plan:** Shuffle Roamers at Ecruteak/Rt 37 Border.
- **Status:** On Route 37. Opening Map to check positions.
- **Action:** Open Pokegear -> Check Map.
- **Target:** Route 37.
- **Resources:** 16 Repels.
- **Session Start:** Turn 36369. Current: 36838.

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

# Fly Map Connections
- **New Bark Town** -> Left -> **Cherrygrove City**
- **Cherrygrove City** -> Up -> **Violet City**
- **Cherrygrove City** -> Left -> **Azalea Town**
- **Azalea Town** -> Up -> **Goldenrod City**
- **Goldenrod City** -> Up -> **Olivine City**
- **Olivine City** -> Down -> **Ecruteak City** [Confirmed]
- **Violet City** -> Left -> [Invalid]

# Game Mechanics
- **Fly Map:** Cursor remembers last destination. Always verify starting position.
- **Observation (Turn 36816):** Roamers detected at approx (25, 25) [Route 42?] and (22, 27) [Route 31?]. None immediately on Route 37.
- **Strategy:** Move to Route 37 boundary (South) to shuffle roamers efficiently.
- **Action:** Entered Route 37. Opening Pokegear Map to check Roamer positions.
- **Action:** Pressing 'A' to open full region map from Pokegear Map Card.
- **Observation:** 'A' press in Turn 36830 didn't open the map. Retrying with a delay to ensure input registration.
- **Action:** Pressing 'A' again to open full region map. Previous attempts failed.
- **Action:** Pressing 'A' again (Retry 4). If this fails, will move to a different tile to reset menu state.
- **Observation:** 'A' press failed multiple times to open full map.
- **Action:** Closing menu and moving to (9, 2) to clear 'stuck on tile' warning and reset menu state.
- **Fix:** Moving to (9, 2) to clear tile warning.
- **Tool:** Defining `safe_open_map` to handle menu cursor memory reliably.
- **Action:** Closing Start Menu (was left open) and moving to (9, 2).
- **Next:** Test `safe_open_map` tool.
- **Tool Failure:** `safe_open_map` failed because the Start Menu wraps, causing the 'reset to top' logic to select 'Exit' or 'Pokemon'.
- **Recovery:** Currently in Party Menu with Fly selected. Executing Fly to Ecruteak to shuffle roamers.
- **Action:** Select Fly -> Verify Destination (should be Ecruteak) -> Confirm.
- **Navigation:** Executing Fly path: New Bark -> Left (Cherrygrove) -> Left (Azalea) -> Up (Goldenrod) -> Up (Olivine) -> Down (Ecruteak).
- **Navigation:** Retrying Fly path from Cherrygrove with longer delays: Left (Azalea) -> Up (Goldenrod) -> Up (Olivine) -> Down (Ecruteak).
- **Navigation:** From Violet City: Down (Cherrygrove) -> Left (Azalea) -> Up (Goldenrod) -> Up (Olivine) -> Down (Ecruteak).
- **Observation:** Fly attempt failed (landed in Violet City). Suspect input timing or grid misalignment.
- **Strategy Change:** Abandoning Fly for now. Walking to Ecruteak via Route 36 -> Route 37.
- **Immediate Goal:** Navigate to Violet City West Exit (0, 8).