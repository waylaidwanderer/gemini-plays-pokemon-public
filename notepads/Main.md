[Location Encounters]
(Moved to Archive/LocationEncounters)

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

[Plan]
- Find the real Pokemon Center in Fuchsia City to heal.
- Locate the Safari Zone.
- Restock on Poke Balls and healing items.

[Reflection 14881]
- 50-Turn Check completed.
- Ledges (TYPE_3fe2) are strictly ONE-WAY. You can only jump DOWN (South) over them. Moving North against a ledge acts as a solid wall. I spent too many turns trying to navigate up through the Fuchsia Zoo ledges.
- I must stop logging POIs in my notepad BEFORE visually confirming their interiors.
- `shop_buyer` tool updated to handle target quantities and bypass cursor memory. Will test it at the Mart soon.

[HMs]
- HM01 (Cut): Taught to Audrey (Bellsprout).
- HM05 (Flash): Obtained! Tested party + Diglett, Dugtrio, Meowth, Voltorb - none can learn it. Abandoned finding a Flash user; navigating via grid is faster.

[Exploration Notes]
- System Note: Gen 1 move menu WRAPS. Mashing 'Up' DOES NOT guarantee index 1. Must use `current_move_index` based on visual confirmation or tracking memory.
- NEVER assume a path is blocked based on visual patterns (like fences). ALWAYS physically test every tile along the suspected barrier by bumping into it to confirm if there is a hidden gap.
- Encountered Lv 30 Snorlax on Route 12. Failed to catch due to running out of Poke Balls. Defeating it to clear the path. Must stock up before the next static encounter!
- Custom tools cannot read the screen mid-execution (no while loops for visual feedback).
- Skull Bash is a 2-turn move (Turn 1: lowers head, Turn 2: attacks).
- Always visually confirm the item name under the cursor before pressing A in the item menu, as the bag is not alphabetized and indices change.
[Reflection 14724]
- Must rewrite shop_buyer tool to read screen text instead of blind mashing.
- Need to locate Fuchsia City Pokemon Center immediately after curing BamBam.
- Map marker hygiene is good; placed PokeMart marker.
- Confirmed Party and Item menus retain cursor memory; visual confirmation is absolutely non-negotiable.
[Reflection 14777]
- The building at (22, 13) in Fuchsia City is NOT the Pokemon Center. It's a house with books. I need to find the real Pokemon Center.
- I need to update my `shop_buyer` tool.
- Team is in bad shape. Need to heal ASAP.
[Reflection 14932]
- 50-Turn Check completed.
- Walked into a dead end at (5, 20) in Fuchsia City. The path between the Y=19 ledge and Y=21 fence ends at X=5. I must backtrack East to find the proper path around the zoo enclosures to get back North.
- Team is 5/6 fainted. Must find the Pokemon Center ASAP. It's somewhere North of the ledges.
- Gen 1 Mechanics: Fainted Pokemon CAN use field moves (HMs). The option remains in their menu. My failure earlier was purely due to cursor memory putting me on a Pokemon without the HM!
[Reflection 14984]
- 50-Turn Check completed.
- Gen 1 Cursor Memory Nuance: Opening the party from 'Start Menu -> POKéMON' RETAINS cursor memory. Opening it from 'Start Menu -> ITEM -> USE' RESETS the cursor to index 1! This inconsistency caused me to use my last Revive on the wrong Pokemon.
- Fainted Pokemon CAN use HMs.
- The critique suggested resetting the party cursor by mashing 'Up'. However, the Gen 1 Party Menu WRAPS (Index 1 -> CANCEL -> Index 6). Mashing 'Up' will NOT guarantee hitting index 1. Visual confirmation remains the ONLY foolproof method for Party Menu navigation.