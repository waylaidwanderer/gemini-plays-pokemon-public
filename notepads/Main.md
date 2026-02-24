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
[Trades]
- Route 5 Gate (Underground Path entrance): NPC wants to trade a Nidoran F for a Nidoran M.
[Vermilion City Plan]
1. Heal at Pokemon Center.
2. Train Cleo (Nidoran F) and Pebbles for Lt. Surge.
3. Explore S.S. Anne (have S.S. Ticket).
[Recovery Plan]
- Start Turn: 3415
1. Buy Potions, Awakenings, and Antidotes at Cerulean Poke Mart.
2. Train Cleo (target Lv16) and Pebbles (target Lv15) on Route 24/25 before attempting Route 6 again. Use switch training with Hydro or Audrey (for Special attacks against Harden users like Metapod/Kakuna).
- Turn 3968 Reflection: Confused Saffron Gate and Underground Path due to flawed map markers. I must rely on direct observation and systematic exploration (checking all map edges) rather than trusting unverified assumptions or old notes. Ledges (TYPE_44f6) enforce one-way downward movement, requiring me to loop back to the top of Route 5 to access the right-side lanes.
- Turn 4071 Reflection: Over the last 50 turns, I resolved a massive spatial logic loop. I incorrectly assumed the Underground Path building was the Saffron Gate and repeatedly ran away from my objective. I learned that I must verify building identities by entering them, not by visual assumption. My coordinate math for map offsets (Cerulean x=28 -> Route 5 x=18) was objectively correct and I should have trusted it. I also brainstormed 5 custom tools (like a map offset calculator or a ledge-scanner) to prevent this in the future, and noted that `walk_to_coordinate` struggles with ledges, requiring manual `move_sequence` intervention.
- Turn 4227 Reflection: Successfully navigated the Route 5 ledges and am now on Route 6. Fighting trainers. Cleo got hit by multiple Sand-Attacks, deciding to switch to Pebbles. Brainstormed 5 tools: Camera Center Calculator, Tile Scanner, Battle Switch Optimizer Agent, Pathfinding Agent, Party HP Parser. No immediate tool fixes needed. Map markers are updated. Goals are clear.