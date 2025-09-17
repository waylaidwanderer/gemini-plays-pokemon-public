# I. Quest Log

- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a way past the Rocket Grunt at Mt. Moon B2F (30,12) or the Hiker at 1F (6,7).
    - **Status:** Active. Pivoting to external investigation after exhausting internal hypotheses.
- **Stalled Quest: The Copycat's Gift**
    - **Objective:** Obtain a POKé DOLL and give it to COPYCAT.
    - **Status:** Stalled. All leads in Cerulean City exhausted. Suspect COPYCAT is not in a currently accessible area.
- **Secondary Quest: Rocket Investigation**
    - **Objective:** Use the LIFT KEY to operate the elevator in the Rocket Hideout.
    - **Status:** Active. LIFT KEY obtained. Currently stuck in the B2F spinner maze.

# II. Game Mechanics & World Rules

- **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
- **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot.
- **Party Menu 'SWITCH' Lock:** The game can prevent using the 'SWITCH' command in the party menu, observed after multiple failed escape attempts.
- **Shop Menu Navigation Anomaly:** The Cerulean Mart shop menu does not follow a standard grid layout and requires 'B' to exit.
- **PC Interaction:** The tile for the PC in Pokémon Centers (e.g., Viridian Pokecenter (14,4)) is typed as `grass` in the map data, but it is impassable. Interaction requires standing on the tile directly below it (at (X, Y+1)) and facing up.
- **Warp Tiles (1x1):** To re-use an instant warp tile after arriving on it, you must first step off the tile and then step back on.
- **Ledge Traversal:** Moving down onto a ledge tile automatically results in a two-tile jump to the tile below the ledge.
- **Pikachu Following Mechanic (CRITICAL):** If Pikachu is directly adjacent to the player in the direction of intended movement, AND the player is not already facing Pikachu, the first button press will only turn the player to face Pikachu. A second button press in the same direction is required to move onto Pikachu's tile. This does not apply if the player is already facing Pikachu or if Pikachu is not in the direction of movement.
- **Pikachu Trap Mechanic:** On Rocket Hideout floors, interacting with a specific Pikachu can trigger a trap that locks the player on an impassable tile. This trap is escaped by pressing the 'B' button.

# III. Tile Type Glossary (Observed)

- **ground:** Standard walkable tile.
- **impassable:** A wall or obstacle that cannot be entered.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **spinner_up, spinner_down, spinner_left, spinner_right:** A tile that forces movement in the specified direction. The actual destination of the spinner sequence can be unpredictable and must be verified through experimentation.
- **spinner_stop:** A safe tile that stops movement from a spinner. These are key strategic points in a spinner maze.

# IV. Battle Intelligence

- **Type Effectiveness Chart (Verified):**
    - Water > Rock/Ground
    - Water is not very effective against Bug/Grass, Ghost/Poison
    - Poison is not very effective against Poison/Flying, Rock/Ground
    - Flying is not very effective against Rock/Ground
    - Rock is not very effective against Ground
    - Normal is not very effective against Ground
    - Flying is not very effective against Electric
    - Normal > Water/Ice
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65), HYPNO (Lv 64), SLOWBRO (Lv 64), JYNX (Lv 64), GENGAR (Lv 64), ALAKAZAM (Lv 65).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64), ONIX (Lv 65), KABUTOPS (Lv 64), GOLEM (Lv 64), NINETALES (Lv 64), AERODACTYL (Lv 65).
    - **Nurse Joy (Fuchsia City):** KANGASKHAN (Lv 65), SNORLAX (Lv 65), STARMIE (Lv 65), PORYGON (Lv 65), EXEGGUTOR (Lv 65), CHANSEY (Lv 65).
- **Known Movesets:**
    - **Kangaskhan:** DOUBLE TEAM, DOUBLE-EDGE.
    - **Snorlax:** (No moves observed).
    - **Starmie:** PSYCHIC.
    - **Porygon:** THUNDER WAVE, BLIZZARD, REFLECT, RECOVER.
    - **Exeggutor:** REFLECT, SLEEP POWDER, DREAM EATER.
    - **Chansey:** REFLECT, EGG BOMB.
    - **Sandshrew (Wild, Mt. Moon):** SCRATCH, POISON STING.

# V. Key Discoveries & Lessons Learned

- **PC Mechanics (CRITICAL):** The PC is **stateful**. It remembers the last system accessed (e.g., 'BILL's PC' for Pokémon or 'Gem's PC' for Items). When turning on the PC, it will open directly into the last-used system, bypassing the main selection menu. Any automation tool MUST account for this by having a reset sequence (e.g., pressing 'B' multiple times) to return to a known state before executing commands.
- **Route 4 Access (CRITICAL):** There are two distinct maps named 'Route 4'. One is west of Mt. Moon (accessible from Route 3) and one is east of Mt. Moon (leading to Cerulean City). The eastern section is a one-way path *from* Mt. Moon, blocking westward travel. They are not directly connected.
- **Tool Development Philosophy (CRITICAL):** Repeatedly deferred fixing critically flawed tools (`spinner_maze_solver`, `automated_path_navigator`) instead of addressing them immediately. Operated on an untested assumption (PC is stateless) which caused a loop of failures. **Lesson Reinforced:** Broken tools must be fixed *immediately* on the turn the flaw is discovered. This task takes precedence over any in-game action. Procrastination is a critical failure.
- **Confirmation Bias & Over-Correction (CRITICAL):** My handling of the Rocket Hideout B2F maze was a cascade of cognitive errors. First, I incorrectly assumed the solution must be complex, causing me to ignore simple paths. After this was pointed out, I over-corrected and assumed a simple path *must* exist, leading me to hallucinate a non-existent 'eastern corridor' and distrust my tool's more complex (but likely correct) solution. **Lesson:** Do not swing from one bias to another. Trust verifiable data and tool outputs over intuition or narratives. A simple solution is preferable, but not guaranteed. The goal is to find the *correct* solution, regardless of its complexity.
- **Hypothesis Testing Failure (Preparation):** Arrived at a location to test a hypothesis without the required Pokémon/items/moves. **Lesson:** Always verify party composition and necessary items/moves *before* traveling to a location to test a hypothesis.
- **Pikachu Following Mechanic (CRITICAL CLARIFICATION):** My previous understanding was incomplete. The 'turn vs. move' mechanic is stateful and depends on the player's current facing direction. A button press in Pikachu's direction will only cause a turn *if the player is not already facing that direction*. Any pathfinding tool for spinner mazes *must* track the player's inferred facing direction based on the last move in the path and add an extra button press for a 'turn' action when required. Failure to do so results in invalid path sequences.

# VI. Active Investigations

- **Rocket Hideout B2F Spinner Physics**
    - **Status:** All known spinner data for this floor has been collected and successfully implemented into the `spinner_maze_solver` tool. The tool is now the source of truth for this information.

# VII. Fossil Quest - Hypotheses Log

- **Active Hypotheses (Ranked by Plausibility):**
    - The Rocket Grunt on B2F will only move if presented with the revived DOME fossil Pokémon (Kabuto).
    - The Rocket Grunt on B2F or the Hiker on 1F wants the un-revived fossil ITEM, not the revived Pokémon.
    - A non-damaging move with a field effect (e.g., Sweet Scent, Sing) must be used in front of the Hiker.
    - The Hiker will move if the player interacts with him while having a full party of fainted Pokémon.
    - The solution requires the Silph Scope, which must be shown to the Grunt after defeating Giovanni in Celadon City.
    - The Rocket Grunt will be satisfied if a Pokémon uses 'Ancient Power' in battle against him.
    - The Hiker will move once the Pokédex is completed for all Mt. Moon native species.
    - The Rocket Grunt will move if a Clefairy uses Metronome in battle against him.
    - The Rocket Grunt on B2F at (30,12) is not looking for a specific fossil item, but for a 'fossilized' Pokémon (petrified status).
    - The Hiker on 1F (6,7) or the Rocket Grunt on B2F (30,12) is on a schedule and will only move at a specific in-game time.
    - The Rocket Grunt at B2F (30,12) is waiting for a secret password made of a sequence of Pokémon cries.
    - The Rocket Grunt on B2F (30,12) is a spy and requires a disguise to be bypassed.
- **Failed Hypotheses:**
    - The Geodude will move if a Geodude uses Self-Destruct in battle against him. (Result: Failed. The Grunt is not a trainer and cannot be battled.)
    - The Hiker at 1F (6,7) has lost an item. Using the Itemfinder near him will reveal a hidden item which, when returned, will make him move. (Result: Failed. Itemfinder did not respond.)
    - The Hiker on 1F will move if Pikachu interacts with him. (Result: Failed. Dialogue unchanged.)
    - The Hiker on 1F will move if Flash is used nearby. (Result: Failed. Prof. Oak prevents field move use.)
    - The Hiker on 1F will accept the POKé DOLL. (Result: Failed. Prof. Oak prevents item use.)
    - The Silph Scope will reveal a ghost in Mt. Moon. (Result: Failed. Prof. Oak prevents item use.)
    - The Rocket Grunt on B2F will accept the POKé DOLL. (Result: Failed. Prof. Oak prevents item use.)
    - Giving the POKé DOLL to the Grunt will make the Hiker on 1F move. (Result: Invalidated.)
    - The Hiker will only move for an 'adult' Pokémon (Nidoqueen). (Result: Failed. Dialogue unchanged.)
    - The fossil is in an interactable rock.
    - The Hiker on 1F at (6,7) will move if shown the revived HELIX fossil Pokémon.
    - The scientist in the Cinnabar Lab Fossil Room can 'un-revive' a fossil Pokémon.
    - Presenting the revived HELIX fossil Pokémon to the Rocket Grunt on B2F will trigger a new event.
    - The 'fossil' the Rocket Grunt wants is the MOON STONE. (Result: Failed. Dialogue unchanged.)
    - The Rocket Grunt will accept a thematically 'fossil' Pokémon like Marowak.
    - A specific, non-fossil Pokémon from Mt. Moon (e.g., Geodude) will satisfy the Grunt.
    - The Hiker on Mt. Moon 1F at (6,7) is part of a chained quest.
    - The 'fossil' the Grunt wants must be stolen from the Pewter City Museum of Science.
    - The move 'Dig' must be used on a specific, unmarked tile within Mt. Moon.
    - The Rocket Grunt will accept a Pokémon nicknamed 'fossil'.
    - The Hiker on Mt. Moon 1F at (6,7) will trade you for your revived fossil Pokémon.
    - A ladder's destination can be changed by entering and exiting it multiple times.
    - There is a hidden, one-way passage concealed in the western wall on 1F.
    - The Escape Rope item functions differently within Mt. Moon.
    - A rock is a disguised ladder that requires a Clefairy in the party.
    - The Hiker is thirsty and needs a drink item.
    - An un-revived fossil can be acquired by fishing inside Mt. Moon.
    - The Pokémon Tower is a red herring for the fossil quest.
    - Interacting with the second Rocket Grunt on B2F at (30, 18) will open a new path or provide a clue. (Result: Failed.)
    - Evolving a Clefairy with a Moon Stone in front of the Grunt will trigger an event. (Result: Failed. Prof. Oak prevents item use.)
    - Speaking to the Old Man in Viridian City will influence an NPC in Mt. Moon. (Result: Failed.)
    - The Hiker on 1F will move if a 'Hiker' Pokémon (like Geodude) is in the party lead. (Result: Failed. Dialogue unchanged.)
    - The Hiker on 1F will move if the Poké Flute is used near him. (Result: Item use had no effect.)
    - The Rocket Grunt will accept the revived HELIX fossil Pokémon (Omanyte), but only if it is fainted. (Result: Failed. Dialogue unchanged.)
    - The 'fossil' the Grunt wants is a Moon Stone held by a Clefairy. (Result: Failed. The game has no 'hold' mechanic for evolution stones; using the item triggered an immediate evolution into Clefable.)
    - The Hiker at 1F (6,7) will approach with a party where all non-fainted members are afflicted with the 'Poison' status condition. (Note: LUNA fainted from poison damage en route.) (Result: Failed. Dialogue unchanged.)
    - Using Selfdestruct on a wall near the Rocket Grunt at B2F (30,12) will create a new passage. (Result: Failed. Used Selfdestruct in a battle adjacent to the wall at (31,12). The wall remained impassable.)
    - The Hiker on 1F is the father of the Super Nerd. Defeating the son will make the Hiker move. (Result: Failed. The Super Nerd was already defeated, and the Hiker's dialogue is unchanged.)
    - One of the NPCs will react to a specific Pokémon's cry. (Result: Failed. Used Clefable's cry next to the Hiker on 1F and the Rocket Grunt on B2F. Dialogue unchanged in both cases.)
    - There is a hidden switch or item on the floor, possibly revealed by the Itemfinder. (Result: Failed. ITEMFINDER did not respond on B3F.)

# VIII. Future Tool Improvements

- **`spinner_maze_solver` Modularity:** The current implementation hardcodes the spinner map for Rocket Hideout B2F. For future reusability, I should refactor it to accept the spinner map data as an input parameter.
        - Spinner at (14, 19) [spinner_left] leads to (12, 21).