<h1><code>Locations/Route102</code></h1>

# Location: Route 102

## Connection Points
- East Exit: Connects to Oldale Town at (48, 10) / (49, 10).
- West Exit: Connects to Petalburg City at roughly (0, 10).

## Trainers
1. Youngster Calvin: [DEFEATED]
   - Location: (33, 16), facing North.
   - Team: Poochyena Lv 5 (defeated by Sage's Absorb).
   - Reward: ¥80, EXP.

2. Bug Catcher Rick: [DEFEATED]
   - Location: (25, 15), facing North against tree at (25, 14).
   - Team: Wurmple Lv 4, Wurmple Lv 4 (defeated by Sage's Pound).
   - Reward: ¥64, EXP.

3. Youngster Allen: [DEFEATED]
   - Location: (19, 3), facing South at north edge of clearing.
   - Team: Zigzagoon Lv 4, Taillow Lv 3 (defeated by Sage's Pound).
   - Reward: ~¥64, EXP.

4. Lass Tiana (upcoming):
   - Team: Zigzagoon Lv 4, Shroomish Lv 4.

## Key Terrain & Landmarks
- Route 102 Signpost: at (40, 10).
- Tree Cluster: (34..35, 12..13) blocks westbound path at row 12 & 13.
- Southern Bypass: Row 14 is open flat path at (36, 14), (35, 14), (34, 14) leading into column 33.
- Short Boy NPC: at (18, 11) in tall grass (non-trainer dialogue).
- Central 3x3 Tree Block: (13..17, 10..17) divides the east and west halves of the route.
- Dead-End Grass Clearing: (16..18, 10..13) with sneezing boy NPC at (18, 11). Blocked by trees on west (col 14-15) and south (row 14+). Must exit NORTH back toward row 3-4 to proceed west!
- Northern Path (Main Route West): Extends west from Youngster Allen at (19, 3) around the north side of the pond, then turns south toward Lass Tiana and the Petalburg City entrance.
- Ledge & Potion: Accessible from the northern/western path above the ledge. Jumping down the ledge lands at the Potion item ball, leading into Petalburg.
- Berries: Pecha and Oran berry trees located in the north-east clearing at (24..25, 1..2) - still need to harvest!

## Target Encounters
- Ralts (Psychic, 4%): Prime team addition.
- Lotad (Water/Grass, 20%): [CAUGHT!] Level 4 ♀, nicknamed LILZ!
- Zigzagoon (Normal, 15%): Pickup ability for passive free items.

<hr>

<h1><code>Main</code></h1>

# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko (Level 10, Male), Nickname: SAGE
- Status: Navigating Route 102; Calvin, Rick & Allen defeated, heading west to berry trees, Lass Tiana, and Petalburg City.

## Party
1. SAGE (Treecko ♂, Level 10) - Moves: Pound, Leer, Absorb. HP: 15/30.
2. LILZ (Lotad ♀, Level 4) - Newly caught on Route 102! Moves: Astonish, Growl.

## Bag Highlights
- Potion x1 (1 promo Potion used to heal Sage to full HP)
- Poké Ball x2 (gift from Brendan, 3 used on Lotad)
- Money: ¥3492 (won ¥300 from Brendan, ¥80 from Calvin, ¥64 from Rick, ¥48 from Allen)
- Key Items: Pokédex, Running Shoes (Hold B to run outdoors)

## Littleroot Town & Route 101 Summary
- Player's House (East): 1F, 2F (Clock set 10:00 AM, Potion in PC).
- Rival's House (West): 1F, 2F (Met Brendan).
- Birch's Lab (South-West): Received Treecko (SAGE), Pokédex, and 5 Poké Balls.
- Route 101: Connects Littleroot Town to Oldale Town. South ledge at row 13 (x=7..11) is bypassed on west side via col 6 past signpost at (5, 9). Northbound path continues around central ledge.

## Oldale Town Layout
- Pokémon Center: West side of town (red roof, door at 6, 16). Checkpoint set!
- Poké Mart: East side of town (blue roof).
- Route 103: North exit of town (where Brendan was defeated).
- Route 102: West exit of town (footprint NPC now unblocked!).

## Progression History - Phase 1 & 2 (Completed)
- Phase 1: Intro, clock set, PC Potion, rival meeting, Birch rescue, and Treecko (SAGE).
- Phase 2: Oldale Center visit, promo Potion from clerk, Brendan Rival Battle 1 won on Route 103 (Sage Lv 7), Pokédex + 5 Poké Balls from Birch/Brendan, Running Shoes received from Mom.

## Progression Checklist - Phase 3 (Active)
1. [x] Receive Running Shoes from Mom outside player's house.
2. [x] Travel north through Route 101 to Oldale Town.
3. [x] Head west from Oldale Town onto Route 102 (footprint sketcher path now unblocked).
4. [x] Catch wild Pokémon on Route 102 with Poké Balls (caught Lotad ♀ Lv 4, nicknamed LILZ!).
5. [ ] Battle Route 102 trainers for EXP and prize money. (Calvin, Rick, Allen defeated; Tiana remaining).
6. [ ] Arrive in Petalburg City and visit Petalburg Gym to speak with Dad (Norman).
7. [ ] Help Wally catch a Ralts.

## Route 102 Overview
- East entrance: Connected to Oldale Town at (48, 10).
- West exit: Leads directly into Petalburg City.
- Key Wild Pokémon: Ralts, Lotad, Seedot, Zigzagoon (Pickup), Wurmple, Poochyena.
- Trainers: Youngster Calvin, Bug Catcher Rick, Youngster Allen, Lass Tiana.
- Items: Oran/Pecha berry trees, Potion.

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