# Strategy for Suicune Sighting (Crystal)
1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
3. Route 42 (Central Island): Middle Apricorn grove. [Pending] -> My analyst suggests the next major trigger is in the Tin Tower 1F. I will attempt to trigger the battle there.
4. Route 36 (Sudowoodo junction): [Pending]
5. Tin Tower 1F (Final Battle): Requires all previous sightings. I have the Clear Bell and Fog Badge.

# Tile Mechanics (Global)
- FLOOR: Walkable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Walkable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below. [Verified]
- VOID: Impassable. Map boundary. [Verified]
- WARP_CARPET_DOWN: Traversable. Triggers exit to overworld. [Verified]

# NPC & Interaction Rules
- Sage (4, 6): Passage guard. Granted access. [Verified]
- Apricorn Trees: (27, 16), (28, 16), (29, 16) on Route 42. [All empty on Turn 24380]

# Trainer Defeats
- Wise Trio (Wise Trio Room): Defeated.
- Sage at (4, 6) (Gatehouse): Granted passage.
- Sages at (11, 11), (5, 9), (14, 6) (Tin Tower 1F): Lore shared.

# Strategy for Beating Suicune
- Status: Lv40 legendary.
- Moveset: Leer, Bubblebeam, Rain Dance, Roar.
- Lead: XENON (Lv21).
- Tactical Plan:
  1. Turn 1: Mean Look (prevents fleeing, but NOT Roar).
  2. Turn 2+: Hypnosis (MANDATORY to prevent Roar and Bubblebeam).
  3. If Roar is used: The battle ends. I must reload the save.
  4. If XENON is KO'd: Switch to Calcifer or GNEISS to tank while throwing Great Balls.
  5. Night Shade: Deals exactly 21 damage. Use only if HP is high (Suicune has ~125 HP).
  6. Priority: Keep Suicune asleep at all times.

# Navigation to Tin Tower
- Path: Ecruteak City (18, 11) -> Tin Tower Gatehouse (5, 3) warp -> (17, 15) -> (17, 3) warp -> Wise Trio Room (1, 4) -> (7, 4) warp -> Ecruteak Restricted Area (20, 2) -> (37, 7) warp -> Tin Tower 1F.
- Requirements: Clear Bell, Fog Badge, and Sages' approval (all obtained).