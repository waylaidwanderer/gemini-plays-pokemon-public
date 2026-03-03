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
- Silph Scope Retrieval (Backtracking): Turn 11929

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
- CRITICAL EPIPHANY 5: The B1F elevator is INACCESSIBLE from both the north entrance AND the south stairs! The enclosed room at B1F (24, 17) is a dead end.
- The TRUE ELEVATOR ENTRANCE is on B2F!
- THEORIZED PATH TO SILPH SCOPE:
  1. Enter Hideout B1F (21, 2).
  2. Take stairs at B1F (23, 2) to reach B2F (27, 8).
  3. On B2F, walk DOWN the right-side corridor to Y=17.
  4. Walk LEFT to the elevator at B2F (24, 17).
  5. Walk UP into the elevator doors at (24, 16).
  6. Take Elevator to B4F and pick up Silph Scope!
- [Turn 12126] 50-Turn Reflection:
  - Progress: Realized B1F South is a dead end. Theorizing the true elevator entrance is on B2F at (24, 17).
  - Error Analysis: Struggled with cursor memory when trying to use Dig. The overwatch system suggested I hallucinated being stuck and that I can walk right to X=24 from B2F (21, 22). However, the screen visually shows a black wall at X=23. I must test this physically.
  - Next Steps: Walk right to test the wall at X=23. If the overwatch is wrong and I am truly stuck, I will manually use Dig one button at a time to ensure I don't misclick due to cursor memory again.
- Update: I confirmed I am blocked by a wall (`TYPE_2889`) at X=23 on B2F. The overwatch system was incorrect in suggesting I could walk to the right side from (21, 22). I will manually use Dig one button at a time to ensure I don't misclick due to cursor memory.