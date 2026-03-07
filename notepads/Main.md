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
- Cursor memory differences: Party menu from Start->POKéMON retains it, Start->ITEM->USE resets it. PC and Battle menus retain it. Move menu retains it when switching manually, but resets on faint/new battle.
- The Party Menu and Move Menu WRAP. Mashing 'Up' does not guarantee index 1.
- HALLUCINATION CHECK: Never assume a tile ID is a solid wall without physically testing it. In the Safari Zone, TYPE_fed7 and TYPE_3fe2 are BOTH passable tall grass! Thick solid bushes look distinctly different (dark green, round leaves). Always bump to verify!
- MACRO DANGER: Do not use alternating directional macros (like L-D-L-D) near ledges when searching for gaps. It can cause accidental ledge jumps, leading to false assumptions about solid walls. Always use step-by-step inputs for precise exploration.
- In the overworld, pressing a new direction takes one discrete input just to TURN without moving. When using move_sequence, always add an extra press for turning, or overshoot into walls to guarantee alignment!
[Reflection - Turn 19659]
- Caught a major routing error: the southern path from (6,19) was a dead loop. The real path forward is ON the plateau.
- Encountered a ledge at Y=15 blocking direct North movement from the stairs. The plateau extends East, so I will follow it that way.
- Custom tools are working perfectly. I am consistently saving steps by running from battles properly.
- Map markers are cleaned up.
[Reflection - Turn 19711]
- Ran out of steps in the Safari Zone, sold items for entry fee, and am heading back.
- Confirmed again: Party Menu retains cursor memory! Visually verifying the cursor position before using tools like use_hm_field is absolutely critical to avoid misinputs.
- Strategy for Safari Zone Area 4 West: Right-hand wall-following algorithm to ensure I don't miss the Secret House by assuming ledges/water create closed dead-end loops.
[Reflection - Turn 19452]
- Successfully corrected the Pity Entry hallucination, secured funds, and returned to the Safari Zone.
- Created `use_cut` custom tool to permanently solve Start/Party menu cursor memory issues.
- Encountered pathing errors due to long movement macros being interrupted by wild Pokemon or turning delays. Rule moving forward: restrict movement sequences in grassy areas to 5-10 steps to maintain alignment.
- Must read my own routing notes carefully; I recently confused East and West, causing me to walk into a tree instead of the correct path.
- Safari Zone Area 4 Exploration Start: Turn 19479
[Reflection - Turn 19555]
- Start Menu WRAPS! Mashing Up fails. Deleting use_cut. Will use use_hm_field from within the Party menu instead.
- Area 4 West Rest House confirmed at (11, 12). Secret House is elsewhere in Area 4 West.
[Reflection - Turn 19763]
- Successfully implementing short-burst movement strategy to avoid desyncs in the Safari Zone.
- Discovered that my run_battle tool works perfectly in the Safari Zone because the 2x2 menu layout maps identically to the standard battle menu (Up+Left resets to BALL, Right+Down selects RUN).
- Currently in Area 3 North, heading to Area 4 West to resume the right-hand wall-following exploration for the Secret House.
[Reflection - Turn 19815]
- Explored the lower South pocket of Area 4 West from the stairs at (6, 19). Confirmed it is a dead end containing only a Rest House at (11, 12).
- Hallucinated an item ball that was actually a sign. Must rely strictly on Game State Info for items.
- Short burst move_sequence commands (3-6 steps) are highly effective at preventing desyncs and conserving steps in the Safari Zone.
- The path forward must be North. I am testing Northward movement directly off the plateau at X=6 to access the upper grassy area.