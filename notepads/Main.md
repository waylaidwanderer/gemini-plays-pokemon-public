[Location Encounters]
(Moved to Archive/LocationEncounters)

[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.

[Timestamps]
- Start Turn: 339 (Entered Viridian Forest navigation task)
- Grinding Start: Turn 415
- Route 2 Arrival: Turn 869
- Mt. Moon Start: Turn 1385
- Cerulean City Arrival: Turn 2126
- Turn 3135: Severe spatial hallucination occurred because I ignored objective Y-coordinate data (Y=27) indicating I was at the south edge of the map, and instead trusted a flawed visual assumption. Lesson: ALWAYS trust (X, Y) coordinate math over feelings of being lost.
- Turn 3239 Reflection: Long pathing macros (walk_waypoints) are highly brittle in NPC-populated areas. Navigate step-by-step and verify 'TYPE_' collision data instead of trusting visual assumptions about fences/roofs.
- Route 24 Grinding Start: Turn 3516 (Resumed Turn 3638, Mon Feb 23 2026)
- Route 6 / Vermilion Grinding Start: Turn 4321
- Route 11 Exploration Start: Turn 6409
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rival Gary Battle Start (S.S. Anne): Turn 4855

[Trades]
- Route 5 Gate (Underground Path entrance): NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City (House next to Mart): NPC wants Spearow for Farfetch'd.

[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.

[Plan]
- Cut the tree blocking the Vermilion Gym and challenge Lt. Surge. (Lead with Pebbles or Cleo for Electric immunity!)
- Return to Cerulean City to exchange Bike Voucher for Bicycle. Route: Vermilion City -> North to Route 6 -> Underground Path -> Route 5 -> North to Cerulean City.

[Navigation Rules]
- Ledges (e.g. TYPE_44f6) enforce one-way movement. Route 5 requires looping back to the top to access the right-side lanes.
- Building identities must be verified by entering them, not by visual assumption. Saffron Gate and Underground Path are visually similar.
- Do NOT blindly trust assumed long-distance coordinate math (e.g. 'walk straight south from X'). Walk step-by-step and trace impassable tiles (water, trees) to find correct paths.
- When mapping, use exact coordinates and do not jump to conclusions about blocked paths until physically bumping into them. Use map markers to explicitly mark entrances!

[Battle Tactics]
- Switch out immediately if hit by multiple accuracy-dropping moves (like Sand-Attack) to avoid wasting turns mashing attacks that miss.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle, as fainting could invalidate the marker.
- Always consider enemy speed and damage rolls.

[Turn 4850 Reflection]
- STRICT RULE: If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST. I wasted turns trying to pick up stools. Stop interacting with furniture.
- Fixed `swap_pokemon_party` custom tool to handle Gen 1 cursor memory.

[Rival Gary - S.S. Anne]
- Pidgeotto Lv 19
- Raticate

[Boss Prep Checklist]
- Check party HP and status conditions.
- Heal at Pokemon Center BEFORE entering known hostile or boss areas.
- Verify optimal lead Pokemon.

[S.S. Anne Navigation]
- NEVER use dead reckoning. ALWAYS read the Game State Player Position before making any navigational assumptions or using walk_to_coordinate.
[Turn 5214 Reflection: Path to S.S. Anne]
- The path to the docks is NOT near the Gym. It is on the FAR EAST side of town.
- From Pokemon Center, walk East to X=30.
- Walk South down X=30 to Y=26.
- Walk West along Y=26 to X=18.
- Walk South onto the bridge at X=18.
- NEVER ask custom agents for exact map coordinates or pathfinding instructions, as they will hallucinate them. Always manually trace collision bounds.
- Missed Items due to Full Bag: TM24 (Lt. Surge in Vermilion Gym), Old Rod (Fishing Guru at Vermilion City 0_163).
[PC Item Storage]
- TM34, TM01, TM45, TM19, Rare Candy x2
[Turn 6357 Reflection]
- I got stuck looping at (20, 18) because I told my `walk_to_coordinate` tool to walk Left, straight into `TYPE_4e8c` (water). The tool doesn't do pathfinding, only L-shapes.
- CRITICAL: Always visually trace the L-shape path on the screen grid to ensure there are no ledges, water, or buildings in the way before calling `walk_to_coordinate`.
- Created `deposit_item_pc` to speed up future PC visits.
[Turn 6461 Reflection]
- Diglett's Cave exploration is underway. High-level Diglett/Dugtrio are extremely fast and can prevent running. Cleo (Lv 20 Nidoqueen) is too slow and weak to Ground moves. Swapping Hydro (Lv 31 Wartortle) to the lead for guaranteed escapes and safe damage.
- Custom tools `withdraw_item_pc` and `use_hm_field` were successfully created to reduce menu hallucination risks.
- Map marker placed at (24, 27) to track my path through the visually repetitive cave.
[Fast Travel Route]
- Vermilion City (Route 11) <-> Route 2 via Diglett's Cave. Bypasses earlier obstacles.
- Current Objective on Route 2: Retrieve HM05 Flash from Professor's Aide (requires 10+ caught Pokemon, currently have 15).