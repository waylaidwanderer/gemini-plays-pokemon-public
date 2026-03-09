[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle.
- If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST.
- NEVER use dead reckoning. ALWAYS read the Game State Player Position before making any navigational assumptions.
- Gen 1 PC menus (DEPOSIT, WITHDRAW, etc.) retain cursor memory.
- Gen 1 Battle menus retain cursor memory! Reset the main menu cursor to FIGHT by pressing Up and Left before navigating.
- Gen 1 Move menu cursor memory is retained when switching Pokemon manually. It RESETS to index 1 when a Pokemon faints and a new one is sent out, or at the start of a NEW battle!
- The Game State Info inventory list is alphabetized, but the in-game bag is NOT. Do not rely on Game State indices to find items.
- The overworld Start Menu ALSO retains cursor memory! Always check where the cursor is before blindly executing navigation sequences.
- When menu state desyncs or cursor memory causes an error, ALWAYS back out entirely to the overworld (spam B) and start fresh. Do not try to "fix" it mid-menu blindly.

[Timestamps]
- Route 6 / Vermilion Grinding Start: Turn 4321
- Route 11 Exploration Start: Turn 6409
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rock Tunnel Exploration Start: Turn 7476
- Journey to Celadon City Start: Turn 9075
- Silph Scope Retrieval (Backtracking): Turn 11929

[HMs]
- HM01 (Cut): Taught to Audrey (Bellsprout).
- HM05 (Flash): Obtained! Tested party + Diglett, Dugtrio, Meowth, Voltorb - none can learn it. Abandoned finding a Flash user; navigating via grid is faster.

[Exploration Notes]
- NEVER assume a path is blocked based on visual patterns (like fences). ALWAYS physically test every tile along the suspected barrier by bumping into it to confirm if there is a hidden gap.
- Encountered Lv 30 Snorlax on Route 12. Failed to catch due to running out of Poke Balls. Defeating it to clear the path. Must stock up before the next static encounter!
- Custom tools cannot read the screen mid-execution (no while loops for visual feedback).
- Skull Bash is a 2-turn move (Turn 1: lowers head, Turn 2: attacks).
- Always visually confirm the item name under the cursor before pressing A in the item menu, as the bag is not alphabetized and indices change.
- The building at (22, 13) in Fuchsia City is NOT the Pokemon Center. It's a house with books.
- I must exclusively use short (1-3 step) movement sequences when navigating tight corridors with ledges and fences.
- WARNING: Cut bushes respawn if you walk too far away from them (off-screen reload)! Always re-verify if the path is actually open.

[Fuchsia City Layout]
- Ledges are strictly ONE-WAY. You can only jump DOWN (South) over them. Moving North against a ledge acts as a solid wall. Note: Not all TYPE_3fe2 tiles are ledges (many are just flat paths or grass), so rely on visual confirmation.
- The path West towards the Pokemon Center is blocked by a Cut bush at (18, 19). Y=13/14 paths are blocked by fences/buildings.
- To return North from the bottom of the city, you CANNOT go up the West side due to ledges. You must head East along the bottom (Y=27/29) to X=18, then head North and Cut the bush at (18, 19) to access the top half.
- Safari Zone Path: From the Cut bush at (18, 19), walk North. You cannot walk straight North at X=18 due to zoo fences at Y=7. Instead, walk West to X=16, walk North, use Cut on the bush at (16, 11), then continue North to Y=6, West to X=15 to dodge the sign, North to Y=4, East to X=18, and Up to enter.

[Gen 1 Mechanics]
- Cursor memory differences: Party menu from Start->POKéMON retains it, Start->ITEM->USE resets it. PC and Battle menus retain it. Move menu retains it when switching manually, but resets on faint/new battle. PokeMart SELL menu RESETS to the top after every sale!
- The Party Menu and Move Menu WRAP. Mashing 'Up' does not guarantee index 1.
- HALLUCINATION CHECK: Never assume a tile ID is a solid wall without physically testing it. In the Safari Zone, TYPE_fed7 and TYPE_3fe2 are BOTH passable tall grass! Thick solid bushes look distinctly different (dark green, round leaves). Always bump to verify!
- MACRO DANGER: Do not use alternating directional macros (like L-D-L-D) near ledges when searching for gaps. It can cause accidental ledge jumps, leading to false assumptions about solid walls. Always use step-by-step inputs for precise exploration.
- In the overworld, pressing a new direction takes one discrete input just to TURN without moving. When using move_sequence, always add an extra press for turning, or overshoot into walls to guarantee alignment!
- The Start Menu WRAPS! Mashing 'Up' does not guarantee index 1.
- run_battle tool works perfectly in the Safari Zone because the 2x2 menu layout maps identically to the standard battle menu.
- Safari Zone Attempt 4: Turn 20128
- NEVER assume a building's purpose based on interior floor tiles (e.g., checkered floors). Different buildings can share tilesets. Always rely on Game State Info (like the presence of a PC or Nurse Joy) to identify it.
- NEVER delete a verified, working path from notes just because you suspect a shortcut exists. Only update navigation notes AFTER empirically proving the new route works. Hallucinating gaps in solid walls (like Y=22 in Fuchsia) wastes dozens of turns.
- HALLUCINATION CHECK: If my current visual perception (e.g., seeing an Item Ball in a building) contradicts a previously written note (e.g., "This building is a trap Rest House"), I MUST trust my eyes and investigate the anomaly, rather than blindly following the note and ignoring the item. Notes can be poisoned by past false assumptions!
- Reflection Turn 22413: Confirmed Rest House at (11, 11) is a trap. Plateau wall blocks North/South movement between Y=15 and Y=16 near the Rest House. Getting stuck at (13, 12) was due to being trapped between the Rest House at (12, 12) and the plateau wall at X=14. Must escape via Y=13, then head West to X=6 to continue North.