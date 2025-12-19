# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable. Includes FENCE and Gym Planters.
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable. Can be shaken with Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- TALL_GRASS: Traversable. Wild encounters.
- DOOR: Traversable. Map transition.
- WARP_CARPET_DOWN/RIGHT/LEFT: Traversable. Map transition.
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
- **Battle Status:** Whitney Defeated. Plain Badge and TM45 obtained. Psychic Mark defeated. Schoolboy Alan defeated.
- **Squirtbottle Quest:** Started Turn 4268. (Ongoing)
  - 1. Talk to the Lass (Floria) next to the "wiggly tree" (Sudowoodo) on Route 36. (COMPLETED Turn 4347)
  - 2. Return to the Flower Shop Teacher in Goldenrod (Map 11_2, building at 29, 6) for the SQUIRTBOTTLE.
  - 3. Use SQUIRTBOTTLE on the tree on Route 36.
- **Delivery:** Deliver KENYA (Spearow) to Route 31.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Strategy: Route 35 & National Park Navigation
- Route 35 has high trainer density. Use paths to avoid grass or use Repels.
- Bug Catcher Arnie is a contact for Ditto sightings.
- The gatehouse at Route 36 (18, 9) leads to the National Park (Map 10_17).

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (Floria) has been spoken to.
- Floria at (33, 12) on Route 36 confirms the wiggly tree is a Pokemon. (Turn 4347)