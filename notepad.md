# Blackthorn City - Quest for the Rising Badge
- Primary Goal: Acquire the Rising Badge (Started Turn 35145)
- Requirement: Clair refused to give the badge. Must complete "Dragon User Challenge" in Dragon's Den.
- Dragon's Den Location: "Behind the Gym".

## Strategy: Dragon User Challenge
1. Heal party at Blackthorn Pokemon Center. (DONE)
2. Navigate to the area north (behind) the Blackthorn Gym.
3. Locate entrance to Dragon's Den.
4. Reach the "small shrine" at the center of the Den.

## Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL: Impassable boundary.
- LADDER: Warp between floors.
- WARP_CARPET_DOWN: Exit from buildings.
- COUNTER: Impassable interaction point for Nurse/Clerk. Face and press A from adjacent tile.
- PC: Access Pokemon storage.
- WATER: Traversable only while Surfing.

## Blackthorn Gym Puzzle (2F) - SOLVED
- Status: Boulders pushed into pits.
- Pits: P1(8,3), P2(2,5), P3(8,7).

## Lessons Learned
- Clair's Badge: Defeating her is not sufficient; a second trial in Dragon's Den is required.
- Dragon's Den: Contains a central shrine.
- Type Effectiveness (Gen 2):
    - Dragonair (Dragon): Resists Fire, Water, Electric, Grass. Weak to Ice, Dragon.
    - Kingdra (Water/Dragon): Resists Fire, Water (0.25x), Electric, Grass (0.5x). Weak to Dragon. Ice is neutral.
    - Note: High level differences (e.g., Lv49 vs Lv40) can make resisted damage appear neutral.
- NPC Interaction: Counter tiles act as barriers; interact with NPCs across them.
- Ledge Traversal: LEDGE_HOP_DOWN tiles allow one-way movement south. They act as walls from the south.