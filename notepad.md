# Goldenrod Radio Tower Takeover (Started Turn 8588)
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Use switches 1, 2, and 3 to clear paths.
- Rescue real Director in Warehouse; obtain Card Key.
- Use Card Key on 3F Shutter in Radio Tower.

## Tower Intel
- **Card Key Slot**: 3F (14, 2).
- **Shutters**: 3F (14, 2), 4F (11, 4), 5F (14, 3).
- **Directory**: 1F Reception, 2F Sales, 3F Personnel, 4F Production, 5F Director's Office.

# Global Knowledge
## Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **COUNTER**: Impassable. Interact from front.
- **WARP_CARPET**: Map transition.
- **STAIRCASE/LADDER**: Warp points.
- **POKEBALL TILE**: Decoration.
- **BOOKSHELF**: Impassable.

## Completed Badges
- Zephyr, Hive, Plain, Fog, Storm, Mineral, Glacier.

## Navigation & PC
- **Counter Interaction**: Face the counter.
- **Fly Map (Goldenrod)**: 4 Ups, 6 Lefts from New Bark Town.
- **PC Storage**: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).

## Battle Mechanics
- **Menu Transitions**: Use 1000ms sleep for sub-menus.
- **Move Menu**: The menu WRAPS (Up at 0 -> 3). It REMEMBERS its position for the active Pokemon. Switching in a new Pokemon resets its cursor to 0.
- **Curse Status**: Deals 1/4 max HP damage every turn. Switching out CLEARS the Curse.
- **Tool Conflict**: Avoid calling `select_battle_option` and a custom tool with `autopress_buttons=True` in the same turn.

# Switch Room Puzzle (Map 3_54)
- Path: 3_53 (18, 6) -> 3_53 (21, 31) -> 3_53 (22, 27) -> 3_54 (23, 3).
- Goal: Find switches 1, 2, and 3 to clear the path.

## Hypotheses
- **Card Key**: The real Director likely has the Card Key needed for the Radio Tower shutters.
- Strategy for Muk: Calcifer (Lv43) uses Flame Wheel (Index 0).