# Tile Mechanics
- FLOOR: Traversable. Individual Behavior: Can be traversed. Relational Behavior: No special interactions noted. Mechanics: Standard ground.
- WALL: Impassable. Individual Behavior: Blocks movement. Relational Behavior: Cannot be entered from any direction. Includes FENCE and Gym Planters.
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires Cut.
- TALL_GRASS: Traversable. Wild encounters. Observed on Route 35.
- DOOR: Traversable. Map transition.
- WARP_CARPET_DOWN: Traversable. Map transition.
- LEDGE_HOP_DOWN: One-way down.
- LEDGE_HOP_LEFT: One-way left.
- LEDGE_HOP_RIGHT: One-way right.
- VOID: Impassable. Map boundary.
- COUNTER: Impassable. Individual Behavior: Blocks movement. Relational Behavior: Interaction point for NPCs behind it (e.g., Nurse Joy).
- PC: Impassable. Individual Behavior: Blocks movement. Relational Behavior: Interacted with by standing below and facing up.

# Battle Strategy & Type Effectiveness (Verified)
- Super Effective (x2 or x4):
    - Ground moves -> Electric (Voltorb), Fire (Magmar).
    - Rock moves -> Fire (Magmar).
    - Flying moves -> Grass/Poison (Bellsprout).
    - Fire moves -> Bug/Poison (Venonat).
- Not Very Effective (x0.5 or x0.25):
    - Normal moves -> Rock/Ground (Geodude).
    - Rock moves -> Rock/Ground (Geodude).
- Immune (x0):
    - Ground moves -> Flying (Pidgey).
- Note: Other matchups are based on general knowledge and require in-game verification.

# Progress & Objectives
- **Battle Status:** Whitney Defeated. Plain Badge and TM45 obtained. Psychic Mark defeated. Schoolboy Alan defeated.
- **Squirtbottle Quest:** Started Turn 4268. (Ongoing)
  - 1. Talk to the Lass next to the "wiggly tree" (Sudowoodo) on Route 36.
  - 2. Return to the Flower Shop Teacher in Goldenrod (11_8) for the SQUIRTBOTTLE.
  - 3. Use SQUIRTBOTTLE on the tree on Route 36.
- **Delivery:** Deliver KENYA (Spearow) to Route 31.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block before making assertions or reports.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (the Lass on Route 36) has been spoken to, even after defeating Whitney.
- GNEISS (Geodude) grew to Lv 23 during the battle with Psychic Mark.
- Psychic Mark defeated on Turn 4331. Gains: ¥480.
- Arnie (Bug Catcher) called about rare Ditto on Route 35.
- Schoolboy Alan defeated on Turn 4343. Gains: ¥512. Calcifer used Ember to KO Tangela.