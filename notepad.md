# Strategy for Suicune Sighting (Crystal)
1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
3. Route 42 (Central Island): Middle Apricorn grove. [Pending] -> My analyst suggests the next major trigger is in the Tin Tower 1F. I will attempt to trigger the battle there.
4. Route 36 (Sudowoodo junction): [Pending]
5. Tin Tower 1F (Final Battle): Requires all previous sightings. I have the Clear Bell and Fog Badge. [Checked on Turn 24410 - Suicune not present]

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
- Wise Trio (Wise Trio Room): Defeated (Room is empty).
- Turn 24395: Started Suicune Trigger Verification.
- Sage at (4, 6) (Gatehouse): Granted passage.
- Sages at (11, 11), (5, 9), (14, 6) (Tin Tower 1F): Lore shared.

# Strategy for Beating Suicune
- Status: Lv40 legendary. **Static encounter at Tin Tower 1F (Crystal).** Does NOT roam/run during battle.
- Moveset: Leer, Bubblebeam, Rain Dance, Roar.
- Lead: Calcifer (Lv45) or GNEISS (Lv44) to tank.
- Tactical Plan:
  1. Weaken with non-lethal moves (Typhlosion/Graveler).
  2. Switch to XENON (Gastly).
  3. Use Hypnosis (MANDATORY to prevent Roar and Bubblebeam).
  4. If Roar is used: The battle ends. I must reload the save.
  5. Throw Great Balls while Suicune is asleep.
  6. Priority: Keep Suicune asleep at all times.

# Tile Mechanics (Global)
- WARP_CARPET_LEFT/RIGHT: Warp triggered by moving in the direction the carpet faces while standing on it. [Verified]