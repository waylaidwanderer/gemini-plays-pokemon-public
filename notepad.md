<h1><code>Main</code></h1>

# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko (Level 5, Male), Nickname: SAGE
- Status: Sage learned Absorb! Concluding battle and walking into Oldale Town.

## Party
1. SAGE (Treecko ♂, Level 6) - Moves: Pound, Leer, Absorb. HP: 16/22.

## Bag Highlights
- Potion x1 (withdrawn from PC)

## Littleroot Town & House Layout
- Player's House (Jade's House): East house (right side of town).
  - 1F: Entrance (1..2, 8), Stairs to 2F at (2, 1).
  - 2F Bedroom: Stairs at (1, 1), Wall Clock at (3, 1), PC at (8, 1) with chair at (8, 2).
- Rival's House (Brendan's House): West house (left side of town).
  - 1F: Entrance (8, 8), Stairs to 2F at (8, 1).
  - 2F Bedroom: Stairs at (7, 1), Poké Ball at (3, 4).
- Professor Birch's Pokémon Lab: South-west building (door at 7, 17 / 6, 13).
- Route 101: North exit of town at (10..11, 0..1).

## Route 101 Topology
- Ledges face south (one-way downward shortcuts for the return trip).
- Boy NPC stands at (16, 8).
- Columns 17 and 18 form an unobstructed, grass-free open northbound path directly into Oldale Town!

## Progression Checklist - Phase 1 (Completed!)
1. [x] Step out of moving truck and listen to Mom.
2. [x] Enter player's house, go upstairs, set the wall clock (10:00 AM).
3. [x] Withdraw Potion from bedroom PC.
4. [x] Go downstairs, watch Dad (Norman) on TV with Mom.
5. [x] Visit Brendan's house (west) and meet Brendan upstairs.
6. [x] Head north to Route 101 to rescue Professor Birch from Zigzagoon.
7. [x] Choose Starter Pokémon: Treecko!
8. [x] Defeat wild Zigzagoon using Pound.
9. [x] Return to Birch's Lab, receive Treecko, and nickname it SAGE.

## Progression Checklist - Phase 2 (Active)
1. [x] Exit Birch's Lab into Littleroot Town.
2. [ ] Travel north through Route 101 to Oldale Town (entering now via column 17).
3. [ ] Visit Oldale Town Pokémon Center / obtain free Potion from clerk.
4. [ ] Head north to Route 103 to find Brendan.
5. [ ] Defeat Brendan in Rival Battle 1 (Torchic Level 5).
6. [ ] Return to Birch's Lab with Brendan to receive Pokédex and Poké Balls.
7. [ ] Receive Running Shoes from Mom outside player's house.

## Engine / Harness Mechanics Verified
- Map transitions/warps automatically abort pending movement sequences.
- Button sequences must place `sleep` strictly between button taps (no leading/trailing sleeps).
- In PC menu, Home PC directly opens player's item storage.
- Interacting with rival's Poké Ball at (3, 4) triggers rival's bedroom introduction.
- Birch bag starter order: Left = Treecko, Middle = Torchic (default), Right = Mudkip.

<hr>