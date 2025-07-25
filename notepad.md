# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **LONG_GRASS:** Traversable, can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.
*   **LADDER:** Functions as a two-way warp between floors.

### Warp Tiles:
*   **WARP_CARPET_DOWN:** One-way warp. Activated by pressing 'Down'.
*   **WARP_CARPET_LEFT:** One-way warp. Activated by pressing 'Left'.
*   **WARP_CARPET_RIGHT:** One-way warp. Activated by pressing 'Right'.

### Confirmed Impassable:
*   **WALL:** Confirmed impassable. Blocks movement from all directions.
*   **WINDOW:** Impassable. Functions as a wall.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. Likely requires HM Cut.
*   **HEADBUTT_TREE:** Impassable. Likely requires HM Headbutt.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.
*   **BOOKSHELF:** Impassable. Functions as an object that can be interacted with for text.
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.
*   **MART_SHELF:** Impassable. Functions as a wall.
*   **WATER:** Confirmed impassable. Blocks movement entirely.
*   **BUOY:** Impassable. Functions as a wall in water.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.
*   **FLOOR_UP_WALL:** Confirmed one-way traversal. Can only be entered from below. Impassable from all other directions.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.
*   Unown's Hidden Power can be super-effective against Fire-type Pokémon (observed against Vulcan). The specific type is unknown, but could be Water, Rock, or Ground.

## B. Gym Leader Teams
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9). Primarily Normal/Flying type.

# III. Badges & Items
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner.
*   **TM39:** Found in Union Cave B1F.
*   **EVERSTONE:** Received from Professor Elm. Prevents a Pokémon holding it from evolving.
*   **PSNCUREBERRY:** Found on Route 33.

# IV. Phone Calls & Side Quests
*   Wade has called multiple times about the Bug-Catching Contest at the National Park, which seems to be a time-sensitive event happening today.

# V. Critical Failures & Lessons Learned
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks (like marking warps or updating my notepad) instead of performing them immediately. This is a violation of core directives and must be corrected.
*   **stun_npc Tool Correction:** I previously believed `stun_npc` was a hallucination. This was a critical failure to consult my available tools list. `stun_npc` is a real tool and can be used to freeze NPCs.
*   **select_battle_option Tool Correction:** I previously believed `select_battle_option` was a hallucination. This was a critical failure to consult my available tools list. `select_battle_option` is a real tool and must be used for battle menu selections.
*   **Tool Development Failures:** I have repeatedly failed to perform data management and tool refinement immediately. My `find_path_to_target` tool was broken for many turns. This is a severe violation of core directives and must not happen again.
*   **Diagnostic Methodology Failure:** I repeatedly concluded my pathfinding tool was broken when it was correctly identifying that my requested paths were impossible due to map layout (e.g., walls, NPCs). I must trust my tool's output and analyze the map more carefully before assuming a bug.

# VI. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   **Initial Hypotheses (Failed):** Early attempts to solve the puzzle by arranging the pieces and pressing Start, or by simply exiting with B, were unsuccessful. The puzzle is not solved by just completing the image.
*   **Hypothesis 4 (Confirmed):** The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces. This led to the inner chamber where Unown appeared.

# VII. Story Clues & Hints
*   **Strange Tree:** Gramps in the Route 36 Gatehouse mentioned a 'strange tree' blocking a road, which might be why fewer people are visiting the Ruins of Alph. This could be the path forward.
*   **Azalea Town Trouble:** Gramps in Azalea Town mentioned that SLOWPOKE have disappeared and their TAILS are being sold. A Team Rocket grunt is blocking the well, claiming it's unsafe.

# VIII. Exploration Notes
*   **Route 32 Pier:** This area is a dead end. My verified `find_path_to_target` tool confirmed that the southern part of the route is unreachable from the northern section.
*   **Route 33 Pathing:** The route is split by ledges. The eastern upper level is inaccessible from the entrance from Union Cave. The only path forward is west.
*   **Union Cave B1F:** This area is a dead end, accessible from a ladder on 1F. The path is blocked by one-way walls.

# IX. High-Priority Tasks