# Tile Mechanics
- `FLOOR`: Traversable.
- `WALL`: Impassable. Includes `FENCE`.
- `WATER`: Impassable. Requires Surf.
- `HEADBUTT_TREE`: Impassable.
- `CUT_TREE`: Impassable.
- `TALL_GRASS`: Traversable. Wild encounters.
- `LONG_GRASS`: Traversable. Wild encounters.
- `DOOR`: Traversable. Map transition.
- `WARP_CARPET_DOWN`: Traversable. Map transition.
- `LEDGE_HOP_DOWN`: One-way down.
- `LEDGE_HOP_LEFT`: One-way left.
- `LEDGE_HOP_RIGHT`: One-way right.
- `NPCs/Objects`: Impassable.

# Area Knowledge
## Route 35
- Mystery Warp at (3, 5) leads to National Park.
- Collected: TM04 (Rollout) at (13, 16).
- Collected: Coin Case at (7, 25).

# Trainer Roster
- Juggler Irwin: Voltorb (Lv 2, 6, 10, 14)
- Bug Catcher Arnie: Venonat (Lv 15).
- Bird Keeper Bryan: Pidgey (Lv 12), Pidgeotto (Lv 14)
- Firebreather Walt: Magmar (Lv 11, 13)

# Strategy: Whitney Prep
- **Objective**: Defeat Whitney.
- **Whitney Gym Strategy**: 
    - Lead with GNEISS (Geodude) to resist Normal moves.
    - Level GNEISS to Lv 20.
    - Use Magnitude/Rock Throw/Rollout.
- **Spearow Delivery**: Deliver KENYA to Route 31 after training.
    - **Route**: Route 35 -> Route 36 -> Violet City -> Route 31.

## GNEISS (Geodude) Info
- **Held Item**: HARD STONE (Turn 4001).
- **Moveset**: Magnitude (Lv 16), Defense Curl, Rock Throw, Rollout (Turn 3994).
- **Recent Level**: Level 18 reached at Turn 4051.

# Technical Lessons
- **Menu Cursor Persistence**: The Start menu and Pack pockets remember the last cursor position.
- **Menu Wrapping**: The Start menu wraps (Up at index 0 goes to index 7).
- **Lesson**: To reset the menu cursor reliably, use a large number of 'Up' presses (e.g., 8) to hit the wrap, but this is not a true reset to index 0. Better to track the current index.
- **Battle Strategy**: Use Rock Throw against Bug/Flying (Yanma) for 4x damage. Use Magnitude against grounded targets (Nidoran).