# Gem's Pokémon Crystal Notepad

## Party & Rival
### My Team
- G (TOTODILE): Lv15
- HOOTHOOT (HOOTHOOT): Lv4
- HOOTIN (HOOTHOOT): Lv4
- ROCKY (ONIX): Lv5 (Traded for Bellsprout in Violet City)

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## Game Mechanics & Systems
### PC Storage
- Pokémon: None
- Items: None

### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.
- Traded a Bellsprout for an Onix with a Youngster in Kyle's House (Violet City).

### Observed Movesets
- G (TOTODILE) learned WATER GUN at Lv13.
- Wild Poliwag (Route 30): BUBBLE
- Wild Hoothoot (Route 30): TACKLE
- Wild Zubat (Route 30): Moveset unknown (fainted before attacking).
- Wild Bellsprout (Route 31): VINE WHIP

## Area and Navigation Insights
### Tile Traversal and Movement Rules
- **Objects are impassable:** All map objects (items, trees, signs, etc.) act as walls.
- **WALL:** An impassable barrier.
- **FLOOR:** A standard traversable tile.
- **TALL_GRASS:** A traversable tile that can trigger wild Pokémon encounters.
- **LEDGE:** Impassable from the bottom edge. Can be jumped down from the top edge.
- **FLOOR_HOP_RIGHT_LEDGE:** A one-way tile that allows jumping over a ledge to the right.
- **FLOOR_HOP_LEFT_LEDGE:** A one-way tile that allows jumping over a ledge to the left.
- **FLOOR_HOP_DOWN_LEDGE:** A one-way tile that allows jumping over a ledge downwards.
- **FLOOR_HOP_DOWN_OR_RIGHT_LEDGE:** A one-way tile that allows jumping over a ledge either down or to the right.
- **FLOOR_HOP_DOWN_OR_LEFT_LEDGE:** A one-way tile that allows jumping over a ledge either down or to the left.
- **COUNTER:** An impassable barrier.
- **DOOR:** A warp tile.
- **MART_SHELF:** An impassable barrier.
- **BUOY:** An impassable tile in water.
- **TOWN_MAP:** Impassable object.
- **WINDOW:** Impassable object.
- **BOOKSHELF:** An impassable object.
- **TV:** Impassable object.
- **RADIO:** Impassable object.
- **VOID:** An impassable tile outside the map boundaries.
- **WARP_CARPET_DOWN:** A warp tile that activates when facing down.
- **WARP_CARPET_LEFT:** A warp tile that activates when facing left.
- **WARP_CARPET_RIGHT:** A warp tile that activates when facing right.
- **FRUIT_TREE:** An impassable object that can sometimes yield items.
- **WATER:** Confirmed impassable.
- **CUT_TREE:** Confirmed impassable.
- **CAVE:** A warp tile that leads to another map.
- **PC:** An impassable, interactive object. Must be interacted with from the tile below, while facing up.
- **PILLAR:** Confirmed impassable. Acts as a wall.
- **LADDER:** A warp tile.
- **PAINTING:** Impassable object.

### Untested Hypotheses
- **FLOOR_UP_WALL:** Present in Dark Cave. Appears to be a one-way wall traversable only from below. Needs to be tested.
- Are `COUNTER` tiles impassable from all directions? Must test this.

### Discovered Traps & Puzzles
- **Route 30 Noob Trap:** The western path accessible by jumping the ledge near (4, 24) is a dead end. It's blocked by Youngster Mikey, forcing a full backtrack to the southern entrance.
- **Sprout Tower Layout:** The central pillar on the first and second floors splits the area into distinct eastern and western sections. It is impossible to cross between these sections on the same floor. You must use the correct set of ladders to navigate between floors and access both sides.

## Current Plan
- Leave Sprout Tower.
- Heal Pokémon at the Violet City Pokémon Center.
- Challenge Falkner at the Violet City Gym.
### Tool Development Notes
- **unstick_me_tool Bug:** The tool currently defines 'escape' as warping to a new map ID. It needs to be updated to also recognize warps to different floors within the same dungeon (i.e., same map group ID, different map number) as a valid path forward.

## Untested Hypotheses & Future Plans
- Can Onix learn Flash (HM05)? (Priority: High)
- Are `COUNTER` tiles impassable from all directions? (Priority: Medium)
- Is `FLOOR_UP_WALL` in Dark Cave a one-way wall? (Priority: Low - requires Flash)

## Tool/Agent Development Notes
- **unstick_me_tool Bug:** The tool needs to be updated. It currently defines 'escape' as warping to a new map ID. It should be modified to also recognize warps to different floors within the same location (i.e., same map group ID, different map number) as a valid path forward.
- **New Agent Idea:** Create a 'gym_battle_strategist' agent. Input would be my party and the gym leader's known Pokémon. Output would be a suggested lead Pokémon and battle strategy.