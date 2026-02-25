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
- S.S. Anne Boarding: Turn 4431
[Trades]
- Route 5 Gate (Underground Path entrance): NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City (House next to Mart): NPC wants Spearow for Farfetch'd.
[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.
[Plan]
- URGENT: Inventory is FULL (20/20)! I must free up a slot (e.g. by using my HP UP or Rare Candy) before talking to the Captain, otherwise I cannot receive HM01 (Cut).
- Return to Cerulean City eventually to exchange Bike Voucher for Bicycle.
[Navigation Rules]
- Ledges (e.g. TYPE_44f6) enforce one-way movement. Route 5 requires looping back to the top to access the right-side lanes.
- Building identities must be verified by entering them, not by visual assumption. Saffron Gate and Underground Path are visually similar.
- Trust objective coordinate math (e.g. Cerulean x=28 -> Route 5 x=18) over feelings of being lost.
- When mapping, use exact coordinates and do not jump to conclusions about blocked paths until physically bumping into them.
[Battle Tactics]
- Switch out immediately if hit by multiple accuracy-dropping moves (like Sand-Attack) to avoid wasting turns mashing attacks that miss.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle, as fainting could invalidate the marker.
- Always consider enemy speed and damage rolls.