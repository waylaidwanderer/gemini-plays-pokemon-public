# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable. Includes FENCE and Gym Planters.
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable. Can be shaken with Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- TALL_GRASS: Traversable. Wild encounters.
- LONG_GRASS: Traversable. Wild encounters.
- DOOR: Traversable. Map transition.
- WARP_CARPET_UP/DOWN/LEFT/RIGHT: Traversable. Map transition.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way traversal.
- COUNTER: Impassable. Interaction point for NPCs behind it.
- PC: Impassable. Interacted with by standing below and facing up.

# Battle Strategy & Type Effectiveness (Verified)
- Super Effective (x2 or x4):
    - Ground moves -> Electric (Voltorb), Fire (Magmar).
    - Rock moves -> Fire (Magmar).
    - Flying moves -> Grass/Poison (Bellsprout).
    - Fire moves -> Bug/Poison (Venonat, Tangela).
- Not Very Effective (x0.5 or x0.25):
    - Normal moves -> Rock/Ground (Geodude).
    - Rock moves -> Rock/Ground (Geodude).
    - Grass moves -> Fire (Quilava).
- Immune (x0):
    - Ground moves -> Flying (Pidgey).

# Progress & Objectives
- **Battle Status:** Whitney Defeated. Plain Badge and TM45 obtained.
- **Squirtbottle Quest:** Started Turn 4268. (Ongoing)
  - 1. Talk to the Lass (Floria) next to the "wiggly tree" (Sudowoodo) on Route 36. (COMPLETED Turn 4347)
  - 2. Return to the Flower Shop Teacher in Goldenrod (Map 11_2, building at 29, 6) for the SQUIRTBOTTLE.
  - 3. Use SQUIRTBOTTLE on the tree on Route 36.
- **Delivery:** Deliver KENYA (Spearow) to Route 31.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Strategy: National Park & Goldenrod Return
- National Park Layout: The park is a large rectangle with a perimeter path behind the fence.
- Current Goal: Exit National Park south to Route 35.
- Exit: The southern gatehouse (Map 10_16) is the exit to Route 35.
- Battle Policy: Use the battle_strategist agent for all trainer and significant wild encounters to optimize move choice and party management.
- Note: Item ball at (35, 12) collected (Parlyz Heal).

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (Floria) has been spoken to.