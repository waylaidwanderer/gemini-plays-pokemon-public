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
- Gen 1 Move menu cursor memory is retained even when switching Pokemon!
- The Game State Info inventory list is alphabetized, but the in-game bag is NOT. Do not rely on Game State indices to find items.

[Timestamps]
- Route 6 / Vermilion Grinding Start: Turn 4321
- Route 11 Exploration Start: Turn 6409
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rock Tunnel Exploration Start: Turn 7476
- Journey to Celadon City Start: Turn 9075
- Silph Scope Retrieval (Backtracking): Turn 11929

[Trades]
- Route 5 Gate: NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City: NPC wants Spearow for Farfetch'd.
- Route 2 House: NPC wants Abra for Mr. Mime.

[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.

[Plan]
- Return to Lavender Town with the Silph Scope to see the Ghost Pokemon in Pokemon Tower.
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
- The elevator is on B1F at (24, 12) facing DOWN.
- B1F South is a dead end.
- Pokemon Tower Top Floor Reached: Turn 13130