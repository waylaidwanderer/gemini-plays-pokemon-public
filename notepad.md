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
*   **TV:** Impassable object. (Hypothesis)
*   **TOWN_MAP:** Impassable object. (Hypothesis)
*   **RADIO:** Impassable object. Can be interacted with for text.

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

# IV. Story Clues & Hints
*   **Strange Tree:** Gramps in the Route 36 Gatehouse mentioned a 'strange tree' blocking a road, which might be why fewer people are visiting the Ruins of Alph. This could be the path forward.
*   **Azalea Town Trouble:** Multiple NPCs have confirmed SLOWPOKE have disappeared and a Team Rocket grunt is blocking the well.
*   **Kurt the Ballmaker:** A Teacher in Azalea mentioned a man named KURT who makes special Poké Balls. This house is likely his.

# V. Critical Failures & Lessons Learned
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks (like marking warps or updating my notepad) instead of performing them immediately, especially on Azalea Pokecenter 2F. This is a violation of core directives and must be corrected. I must act immediately on new information.
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

# VIII. Untested Assumptions & Hypotheses
*   **Kurt's Location:** I assume this house (CharcoalKiln) belongs to Kurt. **Test:** Find an NPC who identifies as Kurt.
*   **Moltres Sprite:** I assume the Moltres sprite is decorative. **Alternative:** It's an interactable object/switch. **Test:** Interact with it after speaking to all human NPCs.
*   **Slowpoke Well:** I assume the well is the key to the town's problem. **Alternative:** The 'forest's protector' is the real key. **Test:** Find a way past the Rocket Grunt, likely by advancing the Kurt plotline.

# IX. High-Priority Tasks
*   Use `team_composition_advisor` before challenging the Azalea Town Gym.

### Impassable with Interaction:
*   **COUNTER:** Impassable. To interact with an NPC behind a counter, stand on the tile directly in front of them and press A.

## C. Map Marker Mechanics
*   **Static Nature:** Markers linked to an `object_id` do NOT move with the object. They are static. To track a moving object, the old marker must be deleted and a new one created at the new coordinates.