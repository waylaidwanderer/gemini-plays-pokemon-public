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

# Battle Strategy & Type Effectiveness
- Super Effective (x2 or x4):
    - Rock moves -> Bug, Flying, Fire, Ice.
    - Ground moves -> Poison, Fire, Electric, Rock, Steel.
    - Fire moves -> Grass, Bug, Steel, Ice.
- Not Very Effective (x0.5 or x0.25):
    - Normal moves -> Rock, Steel.
    - Ground moves -> Bug, Grass (Note: Flying is immune).
    - Rock moves -> Fighting, Ground, Steel.
- Immune (x0):
    - Ground moves -> Flying.
    - Ghost moves -> Normal.
    - Normal/Fighting moves -> Ghost.

# Gym Leader Whitney (Goldenrod City)
- **Roster:**
  - Clefairy (Lv 18): Metronome, DoubleSlap, Encore.
  - Miltank (Lv 20): Stomp, Rollout, Milk Drink, Attract.
- **Observations:**
  - Miltank's Rollout doubles in power each turn.
  - Attract fails against female Pokémon (GNEISS is female).
- **Strategy:**
  - Lead with GNEISS (Geodude). Rock/Ground resists Normal and Rock moves.
  - If Rollout chain reaches Turn 4 or 5, switch to fodder Pokémon (FRITTATA, KIMCHI) to tank the hit and force a reset.
  - Use Magnitude to burst through Milk Drink.
- **Battle Status:** Whitney defeated. Plain Badge and TM45 obtained.
- **Next Step:** Heal at Pokémon Center, then find the Squirtbottle to clear the weird tree on Route 36.

# NPCs & Trainers
- Juggler Irwin (Super Nerd sprite) at (5, 10) on Route 35: Voltorb x4. Defeated.
- Bug Catcher Arnie at (16, 8) on Route 35: Venonat. Defeated.
- Bird Keeper Bryan at (14, 28) on Route 35: Pidgey, Pidgeotto. Defeated.
- Firebreather Walt at (3, 10) on Route 35: Magmar x2. Defeated.
- Officer at (5, 6) in Goldenrod City: Requests delivery to Route 31.
- Gym Guide (ID 6) at (5, 15) in Goldenrod Gym.
- Beauty Victoria (ID 4) at (0, 4) in Goldenrod Gym: Sentret x2. Defeated.
- Lass Carrie (ID 2) at (12, 13) in Goldenrod Gym. Defeated.
- Lass Bridget (ID 3) at (9, 6) in Goldenrod Gym. Defeated.
- Beauty Samantha (ID 5) at (19, 6) in Goldenrod Gym: Meowth x2. Defeated.

# Inventory & Key Items
- Coin Case: Found in Goldenrod Underground.
- TM04 (Rollout): Found on Route 35.
- HARD STONE: Held by GNEISS.

# Area Knowledge
- Goldenrod City: NPC ID 4 (Cooltrainer F) patrols (19, 26) to (21, 28). Can block vertical movement on X=19.
- Goldenrod Gym: Maze layout. Whitney (8, 3) uses Normal types. Gym Guide recommends Fighting-types. GNEISS (Rock/Ground) resists Normal. Strategy: Lead with GNEISS, use Magnitude/Rollout. Carry HARD STONE.