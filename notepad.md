# I. Meta-Strategy & Core Principles
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state. Deferring these tasks is a critical failure.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. I must avoid wandering aimlessly and systematically test one variable at a time, documenting all results.
5.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.
6.  **Mandatory Self-Assessment:** Every 50 turns, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles.
7.  **Efficiency Over Fixation:** If a simple automation tool fails during a low-stakes, repetitive task (like a wild battle), it is more efficient to complete the task manually and fix the tool later, rather than getting stuck debugging mid-task.
8.  **Confirmation Bias Awareness (Self-Assessment Finding):** I must be vigilant against confirmation bias. If a hypothesis fails multiple documented tests, I must actively pivot to a new, different hypothesis rather than repeating the failed approach. I should also formulate tests designed to *disprove* my own theories, not just confirm them. To combat this, I should use the `puzzle_solver_agent` more readily when I feel stuck on a single line of reasoning.

# II. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil to give to the Rocket Grunt blocking the path at Mt. Moon B2F (30,12).
    - **Status:** Pivoting to a new hypothesis after the 'hidden wall passage' test failed.
    - **Next Step:** Exit Mt. Moon, retrieve LUNA (Clefairy) from the PC, and return to test the 'Clefairy rock ladder' hypothesis.

# III. Battle Intel
- **Type Effectiveness Chart (Verified):**
    - Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
    - Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).
    - Water is not very effective against Ghost/Poison (Observed: HELIX's SURF vs GASTLY).
    - Poison is not very effective against Poison/Flying (Confirmed: ECHO's SLUDGE vs ZUBAT) and Rock/Ground (Observed: ECHO's SLUDGE vs GEODUDE).
    - Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

# IV. Fossil Quest - Hypotheses Log
- **Failed Hypotheses:**
    - The fossil is in an interactable rock.
    - The Hiker on 1F at (6,7) will move if shown the revived HELIX fossil Pokémon.
    - The scientist in the Cinnabar Lab Fossil Room can 'un-revive' a fossil Pokémon.
    - Presenting the revived HELIX fossil Pokémon to the Rocket Grunt on B2F will trigger a new event.
    - The 'fossil' the Rocket Grunt wants is the MOON STONE.
    - A specific, non-fossil Pokémon from Mt. Moon (e.g., Geodude) will satisfy the Grunt.
    - The Hiker on Mt. Moon 1F at (6,7) is part of a chained quest.
    - The 'fossil' the Grunt wants must be stolen from the Pewter City Museum of Science.
    - The move 'Dig' must be used on a specific, unmarked tile within Mt. Moon to unearth the other fossil.
    - The Rocket Grunt will accept a Pokémon nicknamed 'fossil'.
    - The 'fossil' the Rocket Grunt wants is a bone-related item from the Pokémon Tower in Lavender Town.
    - The Hiker on Mt. Moon 1F at (6,7) will trade you for your revived fossil Pokémon.
    - One of the ladders that leads to a dead end must be entered and exited a specific number of times (e.g., three times) to change its destination. (Result: Tested on ladder at (26,16). No change in destination after 3 cycles).
    - **(FALSIFIED):** There is a hidden, one-way passage concealed in the western wall on 1F. (Result: The western wall from (2,3) to (2,18) has been systematically checked and yielded no results.)

- **Active Hypotheses:**
    - **(from Turn 209957):** The scientist in the Cinnabar Lab will provide a 'replica' fossil or the other, unchosen fossil after being shown a fully-evolved version of the fossil he revived.
    - **(from Turn 209957):** The other fossil (the one you didn't pick) has respawned at its original location, but only after a specific flag is triggered, like re-battling the Super Nerd.
    - **(from puzzle_solver_agent - Turn 210894) Hypothesis 2:** A specific, seemingly mundane rock in Mt. Moon is a disguised ladder that can only be activated by having a Clefairy in the first slot of the party.
    - **(from puzzle_solver_agent - Turn 210894) Hypothesis 3:** The Escape Rope item is scripted to function differently within Mt. Moon, acting as a warp to the central B2F area instead of the cave entrance.

# V. Game Mechanics & World State
- **Tile Types (Observed):**
    - **ground/grass:** Standard traversable terrain. Grass can trigger wild encounters.
    - **impassable:** Walls, trees, buildings, and other objects that cannot be walked on or through.
    - **cuttable:** Trees that can be removed with the HM Cut. They respawn when changing maps.
    - **ledge:** Can only be jumped down from above. Acts as a wall from all other directions.
    - **water:** Requires Surf to traverse.
    - **steps:** Allows movement between 'ground' and 'elevated_ground' tiles.
    - **elevated_ground:** Raised terrain, only accessible via 'steps' or other 'elevated_ground' tiles.
    - **ladder_up/ladder_down:** Instant warp tiles between floors.
    - **teleport/hole:** Instant warp tiles.
- **Battle Menu Anomaly (Confirmed Mechanic):** The `battle_anomaly_detector_agent` has concluded that the consistent failure to navigate the move selection menu is a **suspected game mechanic**, not a random bug. The game appears to be intentionally restricting move selection in certain battles (likely wild encounters) to the first move slot. **Strategy:** For low-stakes wild battles, running is the most efficient option.
- **Pokemon Tower 6F Healer Change:** The friendly Channeler at (13,11) is no longer a healer. Her dialogue has changed to "I feel anemic and weak...". This is a significant world state change.

# VI. Automation Strategy
- **Battle:** Use `comprehensive_battle_agent` for high-stakes battles. Use `select_move_in_battle` for standard move selection. Use `battle_anomaly_detector_agent` to investigate recurring battle issues.
- **Navigation:** Use `automated_path_navigator` for single-map pathfinding. Use `master_navigator_agent` for complex, multi-map navigation.
- **Future Development Pipeline:**
    - **`fly_to_city` tool:** Automate flying to a specific city. Requires observing the Fly map layout first.
    - **`auto_battle_wild` tool:** A tool to automate simple wild battles by repeatedly using the first move.
    - **`rock_checker` tool:** A tool to automate the process of systematically checking rock formations. It would take a list of coordinates, navigate to each, turn to face the rock, interact, and mark it as checked.

# VII. Self-Assessment Log
- **(Turn 210956):** Failed to perform mandatory self-assessment on time. Made a manual pathing error by misreading map data, reinforcing the need to rely on automated tools. Acknowledged recurring system-level input drops in battle menus and the necessity of retrying failed navigation attempts.
- **(Turn 211006):** Failed to immediately fix `select_move_in_battle` tool after its first failure, leading to getting stuck in battle loops. This was a critical lapse in adhering to the immediate maintenance directive.
- **(Turn 211057):** Failed to use `battle_anomaly_detector_agent` to investigate recurring menu bugs. Must use it at the next opportunity. Identified need to improve notepad and create new tools for efficiency.
- **(Turn 211109):** Performed mandatory self-assessment. Identified minor lapses in immediate maintenance. Overhauled notepad to improve structure and add a comprehensive tile mechanics section. Re-committed to immediate action on all maintenance and documentation tasks.