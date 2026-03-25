[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle.
- If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST.
- NEVER use dead reckoning. ALWAYS verify the Game State Player Position against the visual sprite position in the screenshot, as the Game State can sometimes be stale after a battle!
- EXHAUSTIVE EXPLORATION: NEVER declare an area a dead end until you have physically bumped into the absolute furthest boundaries of the space. Walk the entire perimeter! Stopping short leads to massive routing failures.
- Gen 1 PC menus (DEPOSIT, WITHDRAW, etc.) retain cursor memory.
- Gen 1 Battle menus retain cursor memory! Reset the main menu cursor to FIGHT by pressing Up and Left before navigating.
- Gen 1 Move menu cursor memory is ALWAYS retained between turns in the same battle, even when the opponent sends out a new Pokemon! It only resets at the start of a completely new encounter.
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
- Safari Zone True Path Run Start: Turn 31428
- Ultimate Secret Key Plan Execution Start: Turn 46422

[HMs]
- HM01 (Cut): Taught to Audrey (Bellsprout).
- HM02 (Fly): Taught to Gye (Doduo).
- HM03 (Surf): Obtained! (Safari Zone Secret House prize).
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
- Moved to Locations/FuchsiaCity.

[Gen 1 Mechanics]
- Cursor memory differences: Party menu from Start->POKéMON ALWAYS RETAINS cursor memory, even if you close the Start menu completely and return to the overworld! Start->ITEM->USE resets it. PC and Battle menus retain it. Move menu retains it when switching manually, but resets on faint/new battle. PokeMart SELL menu RESETS to the top after every sale!
- The Party Menu and Move Menu WRAP. Mashing 'Up' does not guarantee index 1.
- HALLUCINATION CHECK: In the Safari Zone, TYPE_3fe2 is regular grass/path. TYPE_fed7 is PASSABLE TALL GRASS (Proven Turn 28643 by walking through it). TYPE_2889 is a solid bush. Do not assume visual "trees" are solid without physically bumping into them! Always verify turning vs stepping when a move sequence fails.
- MACRO DANGER: Do not use alternating directional macros (like L-D-L-D) near ledges when searching for gaps. It can cause accidental ledge jumps, leading to false assumptions about solid walls. Always use step-by-step inputs for precise exploration.
- In the overworld, the harness automatically handles turning in place before walking. You ONLY need to press a direction once to turn and take a step. DO NOT add extra presses for turning.
- The Start Menu WRAPS! Mashing 'Up' does not guarantee index 1.
- run_battle tool works perfectly in the Safari Zone because the 2x2 menu layout maps identically to the standard battle menu.
- NEVER assume a building's purpose based on interior floor tiles (e.g., checkered floors). Different buildings can share tilesets. Always rely on Game State Info (like the presence of a PC or Nurse Joy) to identify it.
- NEVER delete a verified, working path from notes just because you suspect a shortcut exists. Only update navigation notes AFTER empirically proving the new route works. Hallucinating gaps in solid walls (like Y=22 in Fuchsia) wastes dozens of turns.
- HALLUCINATION CHECK: If my current visual perception (e.g., seeing an Item Ball in a building) contradicts a previously written note (e.g., "This building is a trap Rest House"), I MUST trust my eyes and investigate the anomaly, rather than blindly following the note and ignoring the item. Notes can be poisoned by past false assumptions!
- Turn Hallucinations: When mashing A or B through dialogue (like the Safari Zone entrance), the exact number of turns taken can vary based on text rendering speed and auto-advances. Always double-check the current turn number in the Game State before declaring the current turn.
- HALLUCINATION CHECK: Always verify Cut bushes exist as SPRITES in the Game State before trying to cut them. Standard tree walls look identical on the grid but will yield "There isn't anything to CUT!".
- DIRT TRENCH NORTH: The dirt trench (TYPE_2770) extends North to Y=6. The green grass at Y=5 is separated by a ledge, preventing Northward movement.
- TOOL DESIGN NOTE: A custom tool for using HM field moves cannot reliably start from the Overworld because the Start Menu retains cursor memory (it doesn't reset to POKéMON). Therefore, `use_hm_field` MUST start from the Party Menu where the `current_index` can be visually verified by the player.
- SAFARI ZONE MAP TRANSITIONS: Transitions between Safari Zone areas do NOT always preserve coordinates. For example, moving West from Area 1 Center (0, 11) deposits you at Area 4 West (29, 23) - a +12 tile Y-shift! Never assume strict spatial continuity between Safari Zone sub-maps.
- [PokeMart Mechanics] Gen 1 Mart inventories do NOT scale with badges. They are fixed to their location. Celadon Dept Store 2F is fixed to Super Potions and Great Balls. Must visit late-game cities (Saffron, Fuchsia, Cinnabar) for Hyper Potions, Ultra Balls, and Full Heals.
[Run Status]
- Post-game exploration active.
- Strategy for Unknown Dungeon: Systematically map 2F and 3F. Mark ladders to track floor connections. Use Dugtrio's Dig to escape after catching Mewtwo.
[50-Turn Reflection (Turn 55672)]
- Maze Trap Analysis: I spent roughly 40 turns tracing a massive path on Unknown Dungeon 2F from the (7, 1) ladder, only to discover it dead-ends at (24, 5). 
- Lesson: In late-game dungeons, paths that span the entire width of the map without offering new elevation changes or intersections are often massive decoys. The ladder at 1F (8, 1) is a trap designed to waste time and resources. I must return to 1F and find a different ladder UP to reach the isolated (1, 3) ladder on 2F.
- My `run_battle` tool and strict 3-step movement rules are keeping me safe from disorientation during the high encounter rate here. I will continue to strictly enforce the 3-step limit.
[Dig/Teleport Mechanics]
- Dig and Escape Ropes return you to the last Pokemon Center where you ACTUALLY HEALED your Pokemon. Simply entering and exiting a Pokemon Center does NOT set the warp point. You must speak to Nurse Joy and complete the healing dialogue. (Proved Turn 55685 when Dig warped me from Unknown Dungeon back to Pallet Town because I skipped healing in Cerulean City).
[50-Turn Reflection (Turn 55724)]
- Error Analysis: My `use_field_move` custom tool failed not because the code was wrong, but because I passed `current_index: 1` when the cursor was actually preserved at index 6 from a previous interaction. I MUST visually verify the cursor before passing arguments to blind macros.
- Goal Clarity: I am focusing on explicitly setting my Dig warp point at Cerulean City so I don't accidentally warp back to Pallet Town from the Unknown Dungeon again.
- Map Hygiene: I successfully consolidated my Unknown Dungeon 1F notes and correctly mapped the massive 2F dead-end. Next time I enter, I need to explore the water path or the other ladders.