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
- Super Effective: Ground -> Electric, Fire, Poison, Rock, Steel; Rock -> Bug, Fire, Flying, Ice; Flying -> Bug, Fighting, Grass; Fire -> Bug, Grass, Ice, Steel.
- Not Very Effective: Normal -> Rock/Ground; Rock -> Rock/Ground; Grass -> Fire.
- Immune: Ground -> Flying.
- Policy: Use battle_strategist for trainer fights.

# Progress & Objectives
- Whitney Defeated. Plain Badge and TM45 obtained.
- Squirtbottle Quest:
  1. Talked to Floria on Route 36 (Turn 4347).
  2. Return to Goldenrod Flower Shop (Map 11_2 at 29, 6) for SQUIRTBOTTLE.
  3. Use SQUIRTBOTTLE on Sudowoodo.
- Deliver KENYA (Spearow) to Route 31.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Strategy: Goldenrod Return
1. Exit National Park via southern gatehouse (Map 10_16) at (15, 51).
2. Travel south on Route 35 to Goldenrod City.
3. Enter Flower Shop, get SQUIRTBOTTLE.
4. Back to Route 36.
- Item at (35, 12): collected (Parlyz Heal).

# Pokefan Beverly Battle Log (Turn 4402+)
- Opponent 1: Snubbull (Lv 14).
- Turn 1: GNEISS vs Snubbull. Using Magnitude.

# Lessons Learned
- Hallucination Prevention: Always explicitly verify Map ID and object coordinates from the Game State Information block.
- Quest Logic: The Flower Shop Teacher in Goldenrod won't provide the Squirtbottle until her sister (Floria) has been spoken to.
- Tile Types: Use exact strings from XML (e.g., 'grass' instead of 'TALL_GRASS').
- Battle Strategy: Ground vs Normal is neutral, but GNEISS resists Normal. Magnitude is high damage.