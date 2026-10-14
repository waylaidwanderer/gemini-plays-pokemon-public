# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko (Level 7, Male), Nickname: SAGE
- Status: In Birch's Lab receiving the Pokédex and Poké Balls!

## Party
1. SAGE (Treecko ♂, Level 7) - Moves: Pound, Leer, Absorb. HP: 16/24.

## Bag Highlights
- Potion x1 (1 promo Potion used to heal Sage to full HP)
- Poké Ball x5 (gift from Brendan)
- Money: ¥3300 (won ¥300 from Brendan)
- Key Items: Pokédex

## Littleroot Town & Route 101 Summary
- Player's House (East): 1F, 2F (Clock set 10:00 AM, Potion in PC).
- Rival's House (West): 1F, 2F (Met Brendan).
- Birch's Lab (South-West): Rescued Birch on Route 101, received Treecko, nicknamed SAGE.
- Route 101: Connects Littleroot Town to Oldale Town (east side is open northbound path).

## Oldale Town Layout
- Pokémon Center: West side of town (red roof, door at 6, 16). Checkpoint set!
- Poké Mart: East side of town (blue roof).
- Route 103: North exit of town (where Brendan was).
- Route 102: West exit of town (blocked by footprint NPC until rival is defeated).

## Progression History - Phase 1 (Completed)
- Completed Littleroot Town intro, clock, PC Potion, rival meeting, Birch rescue, and received Treecko (SAGE).

## Progression Checklist - Phase 2 (Active)
1. [x] Exit Birch's Lab into Littleroot Town.
2. [x] Travel north through Route 101 to Oldale Town.
3. [x] Visit Oldale Town Pokémon Center (healed Sage to 22/22 HP, checkpoint set).
4. [x] Obtain free Potion from Mart clerk outside (promo sample received outside Mart).
5. [x] Head north to Route 103 to find Brendan.
6. [x] Defeat Brendan in Rival Battle 1 (Torchic Level 5).
7. [x] Return to Birch's Lab with Brendan to receive Pokédex and Poké Balls.
8. [ ] Receive Running Shoes from Mom outside player's house.

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