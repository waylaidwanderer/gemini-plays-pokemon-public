# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko (Level 10, Male), Nickname: SAGE
- Status: Navigating Route 102; Calvin, Rick & Allen defeated, heading west to berry trees, Lass Tiana, and Petalburg City.

## Party
1. SAGE (Treecko ♂, Level 10) - Moves: Pound, Leer, Absorb. HP: 20/30.
2. LILZ (Lotad ♀, Level 4) - Newly caught on Route 102! Moves: Astonish, Growl.

## Bag Highlights
- Potion x1 (1 promo Potion used to heal Sage to full HP)
- Poké Ball x2 (gift from Brendan, 3 used on Lotad)
- Berries: Oran Berry x2, Pecha Berry x2 (harvested from Route 102 trees at 24..25, 1..2)
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

## Route 102
- Overview: See Locations/Route102.md for detailed map topography, trainer locations, and verified landmarks.
- Active Objective: Cleared Row 6 ledge gap at (18, 6)! Collect Pecha & Oran berries at (24..25, 1..2), defeat Lass Tiana, and enter Petalburg City.

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
- Text speed set to FAST in game Options menu (verified turn 417).