<h1><code>Main</code></h1>

# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko (Level 7, Male), Nickname: SAGE
- Status: In Littleroot Town concluding Running Shoes dialogue with Mom outside.

## Party
1. SAGE (Treecko ♂, Level 7) - Moves: Pound, Leer, Absorb. HP: 16/24.

## Bag Highlights
- Potion x1 (1 promo Potion used to heal Sage to full HP)
- Poké Ball x5 (gift from Brendan)
- Money: ¥3300 (won ¥300 from Brendan)
- Key Items: Pokédex, Running Shoes (Hold B to run outdoors)

## Littleroot Town & Route 101 Summary
- Player's House (East): 1F, 2F (Clock set 10:00 AM, Potion in PC).
- Rival's House (West): 1F, 2F (Met Brendan).
- Birch's Lab (South-West): Received Treecko (SAGE), Pokédex, and 5 Poké Balls.
- Route 101: Connects Littleroot Town to Oldale Town (east side is open northbound path).

## Oldale Town Layout
- Pokémon Center: West side of town (red roof, door at 6, 16). Checkpoint set!
- Poké Mart: East side of town (blue roof).
- Route 103: North exit of town (where Brendan was defeated).
- Route 102: West exit of town (footprint NPC now unblocked!).

## Progression History - Phase 1 & 2 (Completed)
- Phase 1: Intro, clock set, PC Potion, rival meeting, Birch rescue, and Treecko (SAGE).
- Phase 2: Oldale Center visit, promo Potion from clerk, Brendan Rival Battle 1 won on Route 103 (Sage Lv 7), Pokédex + 5 Poké Balls from Birch/Brendan. Concluding Running Shoes cutscene with Mom.

## Progression Checklist - Phase 3 (Active)
1. [ ] Conclude Running Shoes cutscene with Mom outside player's house.
2. [ ] Travel north through Route 101 to Oldale Town.
3. [ ] Head west from Oldale Town onto Route 102 (footprint sketcher path now unblocked).
4. [ ] Catch wild Pokémon on Route 102 with Poké Balls.
5. [ ] Battle Route 102 trainers for EXP and prize money.
6. [ ] Arrive in Petalburg City and visit Petalburg Gym to speak with Dad (Norman).
7. [ ] Help Wally catch a Ralts.

## Route 103 Topology & Layout
- South connects to Oldale Town.
- Lower Ledge: Horizontal jump ledge at row 12 spans x=3 to x=14. Bypass on east side (column 15).
- Middle Level: Signpost at (11, 8). Upper jump ledge at row 5 spans middle/east section.
- Upper Bluff Path: Bypass upper ledge on the west side to reach Brendan overlooking the water at (8, 3) / (10, 3).

## Engine / Harness Mechanics Verified
- Map transitions/warps automatically abort pending movement sequences.
- Button sequences must place `sleep` strictly between button taps (no leading/trailing sleeps).
- In PC menu, Home PC directly opens player's item storage.
- Birch bag starter order: Left = Treecko, Middle = Torchic (default), Right = Mudkip.
- Poké Mart interior: Customer counter is at (1, 4), talk to shopkeeper from (1, 5) facing Up.
- Oldale Town Mart does not stock Poké Balls prior to receiving the Pokédex.
- Outdoor Mart clerk (with free promotional Potion sample) stands in the south-central area of Oldale Town near (14, 14).
- In Gen 3, all Grass-type moves (such as Absorb) are Special, so their damage is unaffected by physical Attack drops (Growl).
- Medicine use outside battle: Start -> BAG -> select item -> USE -> select Pokémon.

<hr>