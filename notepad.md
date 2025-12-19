# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable. Includes FENCE and Gym Planters.
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable. Can be shaken with Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- grass: Traversable. Wild encounters.
- long grass: Traversable. Wild encounters.
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
    - Fire moves -> Bug/Poison (Venonat, Tangela, Oddish).
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
1. Exit National Park via southern gatehouse (Map 10_16) to Route 35.
2. Travel south on Route 35 to Goldenrod City.
3. Enter the Flower Shop (Map 11_2) and speak to the Teacher to receive the SQUIRTBOTTLE.
4. Return to Route 36 and use the SQUIRTBOTTLE on the Sudowoodo.
- Battle Policy: Use the battle_strategist agent for all trainer and significant wild encounters.
- Note: Item ball at (35, 12) collected (Parlyz Heal).

# Schoolboy Jack Battle Log (Turn 4384+)
- Opponent 1: Oddish (Lv 12). Defeated by Calcifer.
- Opponent 2: Voltorb (Lv 15). Defeated by GNEISS (Magnitude 9).
- Gains: ¥480.

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (Floria) has been spoken to.
- Tile Types: Use exact strings from XML (e.g., 'grass' instead of 'TALL_GRASS').
- Battle Strategy: Magnitude is highly effective against Electric types. Immunties (Ground vs Electric) should be prioritized.