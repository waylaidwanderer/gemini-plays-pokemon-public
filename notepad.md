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
- **Battle Status:** Whitney Defeated. Plain Badge and TM45 obtained.
- **Squirtbottle Quest:** Started Turn 4268.
- **Squirtbottle Quest:**
  - Talk to the Lass next to the "wiggly tree" (Sudowoodo) on Route 36 first.
  - Path: Goldenrod -> Route 35 (via Cut tree at 17, 6) -> Route 36.
  - After talking to the Lass, return to the Teacher in the Flower Shop (Goldenrod) to get the SQUIRTBOTTLE.
- **Delivery:** Deliver KENYA (Spearow) to Route 31.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Area Knowledge
- Goldenrod City: NPC ID 4 (Cooltrainer F) patrols (19, 26) to (21, 28). Can block vertical movement on X=19.
- Flower Shop: Located north of the Gym in Goldenrod City. Teacher NPC at (2, 4).

# Psychic Mark Battle Log (Turn 4308+)
- Opponent 1: Abra (Lv 13). Defeated by GNEISS (Magnitude 5 Crit).
- Opponent 2: Abra (Lv 13). Defeated by GNEISS (Magnitude 8).
- Opponent 3: Kadabra (Lv 15).
- My Lead: GNEISS (Geodude) Lv 23. (Accuracy -1 from Flash).
- Plan: Stay in with GNEISS, use MAGNITUDE.

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block before making assertions or reports.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (the Lass on Route 36) has been spoken to, even after defeating Whitney.
- GNEISS (Geodude) grew to Lv 23 during this battle.
- Turn 3 (Turn 4318): Psychic Mark is about to use Kadabra. GEM chose not to switch.