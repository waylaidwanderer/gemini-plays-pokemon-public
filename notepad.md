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
*   **TV:** Impassable object.
*   **TOWN_MAP:** Impassable object.
*   **RADIO:** Impassable object. Can be interacted with for text.
*   **INCENSE_BURNER:** Impassable object. (Confirmed by attempting to walk into it).

### Impassable with Interaction:
*   **COUNTER:** Impassable. To interact with an NPC behind a counter, stand on the tile directly in front of them and press A.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.
*   **FLOOR_UP_WALL:** Confirmed one-way traversal. Can only be entered from below. Impassable from all other directions.

## B. Map Marker Mechanics
*   **Dynamic Nature:** Markers linked to an `object_id` WILL move with the object. This is useful for tracking moving NPCs.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type moves have NO EFFECT on Normal-type Pokémon.
*   Normal-type moves have NO EFFECT on Ghost-type Pokémon.
*   Unown's Hidden Power can be super-effective against Fire-type Pokémon (observed against Vulcan). The specific type is unknown, but could be Water, Rock, or Ground.

## B. Gym Leader Teams
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9). Primarily Normal/Flying type.

# III. Badges & Items
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **Hive Badge:** Acquired from Bugsy. Allows use of HM01 (Cut) outside of battle and makes traded Pokémon up to Lv30 obey.
*   **TM31 (Mud-Slap):** Received from Falkner.
*   **TM39:** Found in Union Cave B1F.
*   **TM49 (Fury Cutter):** Received from Bugsy.
*   **EVERSTONE:** Received from Professor Elm. Prevents a Pokémon holding it from evolving.
*   **PSNCUREBERRY:** Found on Route 33.

# IV. Story Progression

## A. Current Quest
*   **Rescue the Apprentice:** The Charcoal Man's apprentice is lost in Ilex Forest. Finding him is the primary lead to obtaining HM01 (Cut).

## B. Past Clues & Hints
*   **Strange Tree:** Gramps in the Route 36 Gatehouse mentioned a 'strange tree' blocking a road, which might be why fewer people are visiting the Ruins of Alph. This could be the path forward.

# V. Critical Failures & Lessons Learned
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks (like marking warps or updating my notepad) instead of performing them immediately. This is a violation of core directives and must be corrected. I must act immediately on new information.
*   **Tool Distrust:** I have repeatedly failed to trust my `find_path_to_target` tool's output, assuming it was broken when it correctly identified blocked paths (e.g., by NPCs). I must trust my tool's output and analyze the map more carefully before assuming a bug.
*   **HM moves can be used even if the Pokémon is fainted.** This is a key mechanic learned from the Gentleman in the Charcoal Kiln.
*   **stun_npc Tool Correction:** I previously believed `stun_npc` was a hallucination. This was a critical failure to consult my available tools list. `stun_npc` is a real tool and can be used to freeze NPCs.
*   **select_battle_option Tool Correction:** I previously believed `select_battle_option` was a hallucination. This was a critical failure to consult my available tools list. `select_battle_option` is a real tool and must be used for battle menu selections.

# VI. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces.

# VII. Exploration Notes
*   **Route 32 Pier:** This area is a dead end. The southern part of the route is unreachable from the northern section.
*   **Union Cave B1F:** This area is a dead end, accessible from a ladder on 1F. The path is blocked by one-way walls.
*   **Azalea Pokecenter 2F:** This entire floor is a dead end for now. All warps are blocked by NPCs or walls.

# VIII. High-Priority Tasks
*   Verify if the Team Rocket markers in Azalea Town are still relevant or if the NPCs have disappeared.
*   Test seemingly impassable objects like bookshelves and radios to confirm they are not interactable in a meaningful way.