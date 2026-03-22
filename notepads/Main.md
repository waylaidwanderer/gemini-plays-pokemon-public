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
- 2F West Exploration Start: Turn 40713
- Cinnabar Gym Challenge Start: Turn 48811
- Gym Leader Blaine Battle Start: Turn 48967
- [PokeMart Mechanics] Gen 1 Mart inventories do NOT scale with badges. They are fixed to their location. Celadon Dept Store 2F is fixed to Super Potions and Great Balls. Must visit late-game cities (Saffron, Fuchsia, Cinnabar) for Hyper Potions, Ultra Balls, and Full Heals.
- Earth Badge Obtained (Giovanni): Turn 49188
- Route 22 Exploration Start: Turn 49331
[Turn 49695 Reflection]
- 50-Turn Review: The last 50 turns were dominated by the Route 22 maze. I suffered from severe spatial hallucinations (assuming water existed where there was rock, assuming walls were infinite without testing).
- Correction: I solved it by returning to the "Exhaustive Exploration" rule—physically bumping every single tile along the perimeter of obstacles. This revealed the hidden gaps at Y=11 and Y=9.
- Going forward, I will NEVER declare a path blocked without physically bumping the tiles to verify. Visuals in Gen 1 can be highly misleading (e.g., the top of the archway at 14, 4 looked like a path but was solid; the wall at 5, 11 looked solid but had a gap).
[Turn 49747 Reflection]
- 50-Turn Review: The transition from Route 22 to Route 23 was highly successful due to finally applying the 'Exhaustive Exploration' rule to find the hidden gaps in the Route 22 maze. Currently navigating the linear sequence of Badge Checks on Route 23. My custom tools are functioning perfectly. Notepad hygiene is being maintained by consolidating step-by-step logs into permanent geographical notes once a path is verified.
[Turn 49798 Reflection]
- 50-Turn Review: The last 50 turns were spent passing the Boulderbadge, Cascadebadge, Thunderbadge, and Rainbowbadge checks on Route 23.
- My main failure mode recently was "hallucinating tool execution" — I would write down my intended button presses in the notepad log, but forget to actually output the tool call in my response, leading to turns where I did nothing and got confused. I must double-check my tool calls before completing my turn!
- I am currently at (11, 104) facing water. I need to use Surf. I am pressing Start now.
[Turn 49851 Reflection]
- 50-Turn Review: The last 50 turns were spent passing the Soulbadge (Turn 49829) and Marshbadge (Turn 49846) checks. I successfully navigated around a ledge block at Y=83 by surfing West to X=7, and I am now making landfall again at X=8, Y=71. No major errors, spatial reasoning is sound, and custom tools are working perfectly.
[Turn 49903 Reflection]
- 50-Turn Review: Successfully cleared the remaining Badge Checks on Route 23 (Soul, Marsh, Volcano, Earth) and entered Victory Road. Marked the entrance. Encountered a boulder puzzle. Activated Strength. My movement sequences to reach the boulder keep getting interrupted by wild encounters (Machop, Geodude), forcing me to run since Hydro is at 14 HP. I also identified a raised floor obstacle at X=6/X=7 that I need to path around (North, then West, then South) to get behind the boulder at (5, 14). Custom tools and notepads are working flawlessly.