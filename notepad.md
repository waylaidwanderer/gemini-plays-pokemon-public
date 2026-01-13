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
- **Action:** Transitioned to Route 36.
- **Strategy:** Opening menu to check Pokegear Map. If Roamers are present, hunt. If not, continue to Route 37/Ecruteak.
- **Action:** Pressing 'A' twice to force Full Map view from Pokegear menu.
- **Observation:** Full map failed to open with previous 'A, A' sequence. UI might be unresponsive or requiring single, distinct inputs.
- **Action:** Pressing 'A' once with a long wait to confirm map opening.
- **Observation:** Map is visible in background. No Roamers seen on current screen.
- **Action:** Exiting Pokegear and performing Violet Shuffle (Right -> Violet, Left -> Route 36).
- **Reasoning:** UI interaction is sticky, but visual confirmation "No Roamers Here" is sufficient. Faster to shuffle than to debug UI.
- **Action:** Pressing 'A' to open the full map view (Map Card is already selected).
- **Action:** Filtering Pokedex for Fire Types to find Entei.
- **Hypothesis:** Entei is "Seen" (from Burned Tower event) and will appear in the filtered list.
- **Sequence:** Right (Select Fire) -> Down x3 (Select Begin Search) -> A.
- **Action:** Retrying Search Filter.
- **Sequence:** Up x2 (Safety to top) -> Right (Select Fire) -> Down x2 (Select Begin Search) -> A.
- **Reasoning:** Previous attempt failed to change type or execute search. Adding safety presses.
- **Observation:** Currently viewing Furret (National Dex #162). Need to back out to list to search.
- **Action:** Pressing 'B' to exit entry, then 'Start' to open Search menu.
- **Correction:** Previous search attempts failed because I was still viewing the Furret entry.
- **Action:** Pressing 'B' to return to Pokedex List, then 'Start' to open Search Menu.
- **Plan:** Verify Search Menu is open before inputting search parameters.
- **Action:** Configuring Pokedex Search for 'FIRE' type.
- **Sequence:** Up x2 (Force top/Type 1), Right (Normal -> Fire), Down x3 (Navigate to 'Search'), A (Execute).
- **Correction:** Was stuck in 'Entry View' (Kakuna). Previous inputs likely navigated entries instead of menus.
- **Action:** Pressing 'B' to return to List View.
- **Action:** Pressing 'Select' to open the Search/Mode menu (Standard Gen 2 control).
- **Action:** Selecting 'TYPE MODE' from Pokedex Option Menu.
- **Sequence:** Down x3 (Navigate to bottom option), A (Select).
- **Expectation:** This will open a list of Types to choose from.
- **Action:** Closing Option Menu ('B'), then opening Search Menu ('Start').
- **Reasoning:** Screen confirms Option Menu is open. Search is accessed via 'Start' from the main list.
- **Action:** Navigating from 'GEAR' to 'POKEDEX' (Up x3) -> Open (A) -> Open Mode Menu (Select).
- **Correction:** Cursor was on GEAR, not POKEDEX. Adjusted input sequence.
- **Correction:** 'Option Menu' (Select) is for Sorting (New, Old, A-Z, Unown). It does NOT have 'Type Mode'.
- **Action:** Closing Option Menu ('B').
- **Action:** Opening Search Menu via 'Start'.
- **Goal:** Filter by 'FIRE' Type to find Entei.
- **Action:** Opening Start Menu -> Pokedex -> Search Menu.
- **Sequence:** Start -> Up x3 (Force Pokedex) -> A -> Wait -> Start.
- **Reasoning:** Resetting from Overworld to ensure clean navigation.
- **Observation:** Menu wraps. Up from Pokedex goes to Exit -> Option -> Save.
- **Correction:** Canceling Save (B), Navigating to Pokedex (Down x3), Opening (A), Opening Search (Start).
- **Action:** Closing Save Dialog ('B') -> Wait -> Navigating to Pokedex (Down x3) -> Open (A) -> Search (Start).
- **Reasoning:** 'Up' moves cursor Up (wrapping to bottom). 'Down' moves cursor Down (wrapping to top). From Save (pos 6), Down x3 wraps to Pokedex (pos 1).
- **Adjustment:** Added longer sleep after 'B' to ensure inputs aren't eaten.