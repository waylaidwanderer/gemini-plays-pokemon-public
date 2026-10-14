# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Status: In Birch's Lab! Receiving Treecko and proceeding to nickname screen (SAGE).
- Starter: Treecko (Planned Nickname: SAGE)

## Littleroot Town & House Layout
- Player's House (Jade's House): East house (right side of town).
  - 1F: Entrance (1..2, 8), Stairs to 2F at (2, 1).
  - 2F Bedroom: Stairs at (1, 1), Wall Clock at (3, 1), PC at (8, 1) with chair at (8, 2).
- Rival's House (Brendan's House): West house (left side of town).
  - 1F: Entrance (8, 8), Stairs to 2F at (8, 1).
  - 2F Bedroom: Stairs at (7, 1), Poké Ball at (3, 4).
- Professor Birch's Pokémon Lab: South-west building.
- Route 101: North exit of town at (10, 1). Little girl at (10, 2).

## Immediate Progression Checklist
1. [x] Step out of moving truck and listen to Mom.
2. [x] Enter player's house, go upstairs, set the wall clock (10:00 AM).
3. [x] Withdraw Potion from bedroom PC.
4. [x] Go downstairs, watch Dad (Norman) on TV with Mom.
5. [x] Visit Brendan's house (west) and meet Brendan upstairs.
6. [x] Head north to Route 101 to rescue Professor Birch from Zigzagoon.
7. [x] Choose Starter Pokémon: Treecko!
8. [x] Defeat wild Zigzagoon using Pound.
9. [ ] Return to Birch's Lab, receive Treecko, and nickname it SAGE.

## Engine / Harness Mechanics Verified
- Map transitions/warps automatically abort pending movement sequences.
- Button sequences must place `sleep` strictly between button taps (no leading/trailing sleeps).
- In PC menu, Home PC directly opens player's item storage.
- Interacting with rival's Poké Ball at (3, 4) triggers rival's bedroom introduction.
- Birch bag starter order: Left = Treecko, Middle = Torchic (default), Right = Mudkip.