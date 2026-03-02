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

[Timestamps]
- Route 6 / Vermilion Grinding Start: Turn 4321
- Route 11 Exploration Start: Turn 6409
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rock Tunnel Exploration Start: Turn 7476
- Journey to Celadon City Start: Turn 9075

[Trades]
- Route 5 Gate: NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City: NPC wants Spearow for Farfetch'd.
- Route 2 House: NPC wants Abra for Mr. Mime.

[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.

[Plan]
- Find the Silph Scope to see the Ghost Pokemon in Pokemon Tower. The Silph Scope is located in the Rocket Hideout beneath the Game Corner. Do not search other buildings for it.
- Find Mr. Fuji, who is missing from his Volunteer Pokemon House.

[HMs]
- HM01 (Cut): Taught to Audrey (Bellsprout).
- HM05 (Flash): Obtained! Tested party + Diglett, Dugtrio, Meowth, Voltorb - none can learn it. Abandoned finding a Flash user; navigating via grid is faster.

[Route 10]
- Found a Pokemon Center right next to Rock Tunnel entrance! This is a great place to heal and grind if needed.

[Rocket Hideout]
- Current Focus: Explore B4F to find the Elevator Key and reach the Team Rocket Boss.
- System Note: Gen 1 move menu WRAPS. Mashing 'Up' DOES NOT guarantee index 1. Must use `current_move_index` based on visual confirmation or tracking memory.
[Rocket Hideout]
- Elevator Mechanics: The elevator is its own room. The elevator doors on B1F are at (24, 16). They must be accessed from the SOUTH side (Y=17).
- Route to B1F Elevator: B1F North and South are completely separated by a wall at Y=16. You MUST take the B1F stairs at (23, 2) to B2F, navigate the B2F spinner maze to the stairs at (21, 22), which take you up to B1F South. Then walk to the elevator doors at (24, 17).
- B1F South is NOT a dead end! The wall at X=23 was a hallucination.
- Next Steps: Reach the B1F elevator doors, take the elevator to B4F, and pick up the Silph Scope item ball that I left behind after defeating Giovanni!
[Turn 11814] 50-Turn Reflection:
- Progress: Corrected my false memories about the B1F elevator. The doors do not open from the north. I need to take the long C-shaped route through the main hallway at X=17 to reach the south side of the doors at (24, 17).