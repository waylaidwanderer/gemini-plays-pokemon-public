# I. Core Principles & Meta-Strategy
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **Proactive Automation:** Before any complex or repetitive task, consider automating it. If a tool is suboptimal, refine it immediately.
3.  **Trust, But Verify:** Trust agent/system outputs. If a tool contradicts game state, the tool is wrong and must be debugged.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. Systematically test one variable at a time.
5.  **Confirmation Bias Awareness:** If a hypothesis repeatedly fails, pivot to a new one. Use the `puzzle_solver_agent` to generate new lines of reasoning when stuck.

# II. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a way past the Rocket Grunt at Mt. Moon B2F (30,12) or the Hiker at 1F (6,7).
    - **Status:** Active. The isolated eastern partition of B2F is a confirmed dead end. Current focus is testing new hypotheses on the Rocket Grunt.
- **Stalled Quest: The Copycat's Gift**
    - **Objective:** Obtain a POKé DOLL and give it to COPYCAT.
    - **Status:** Stalled. All leads in Cerulean City have been exhausted. Suspect COPYCAT is not in a currently accessible area.

# III. Battle Intelligence
- **Type Effectiveness Chart (Verified):**
    - Water > Rock/Ground
    - Water is not very effective against Bug/Grass, Ghost/Poison
    - Poison is not very effective against Poison/Flying, Rock/Ground
    - Flying is not very effective against Rock/Ground
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65), HYPNO (Lv 64), SLOWBRO (Lv 64), JYNX (Lv 64), GENGAR (Lv 64), ALAKAZAM (Lv 65).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64), ONIX (Lv 65), KABUTOPS (Lv 64), GOLEM (Lv 64), NINETALES (Lv 64), AERODACTYL (Lv 65).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62), SANDSLASH (Lv 63), GOLEM (Lv 64), LICKITUNG (Lv 61), CHANSEY (Lv 63), RAICHU (Lv 64).

# IV. Fossil Quest - Hypotheses Log
- **Active Hypotheses (Ranked by Agent):**
    1.  **Fainted Fossil:** The Grunt wants a revived fossil Pokémon that has fainted. (Untestable due to low encounter rate in current area).
    2.  **Silph Scope Ghost:** The Silph Scope will reveal a ghost in Mt. Moon, or the Grunt himself is a ghost. (Current Test)
    3.  **Moon Stone Evolution:** Evolving a Clefairy with a Moon Stone in front of the Grunt will trigger an event.
    4.  **Hiker Disguise:** The Hiker on 1F will move if a 'Hiker' Pokémon (like Geodude) is in the party lead.
    5.  **Poké Doll for Hiker:** The Hiker on 1F will accept the POKé DOLL.
- **Failed Hypotheses:**
    - The Rocket Grunt on B2F will accept the POKé DOLL as the 'fossil'. (Result: Failed. Prof. Oak prevents the item's use.)
    - Giving the POKé DOLL to the Grunt will make the Hiker on 1F move. (Result: Dependent on failed hypothesis, invalidated.)
    - The Hiker will only move for an 'adult', a status temporarily gained by interacting with the 'Old Man' in Viridian City. (Result: Failed. Hiker's dialogue was unchanged.)
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
    - The Hiker on Mt. Moon 1F at (6,7) will trade you for your revived fossil Pokémon.
    - A ladder's destination can be changed by entering and exiting it multiple times.
    - There is a hidden, one-way passage concealed in the western wall on 1F.
    - The Escape Rope item functions differently within Mt. Moon.
    - A rock is a disguised ladder that requires a Clefairy in the party.
    - The Hiker is thirsty and needs a drink item.
    - An un-revived fossil can be acquired by fishing inside Mt. Moon.
    - The Rocket Grunt will accept a thematically 'fossil' Pokémon like Marowak.
    - The Pokémon Tower is a red herring for the fossil quest.
    - Interacting with the second Rocket Grunt on B2F at (30, 18) will open a new path or provide a clue. (Result: Failed. Dialogue was generic and unchanged.)

# V. ROM Hack Specific Mechanics
- **Pewter Museum Trap Tile:** On Pewter Museum 2F, the tile at (3,5) is a trap that warps the player to an isolated room. Escape requires interacting with a follower Pikachu.
- **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot. Strategy: For low-stakes wild battles, running is the most efficient option.
- **Party Menu 'SWITCH' Lock:** The game appears to intentionally prevent the use of the 'SWITCH' command in the party menu under certain, currently unknown, conditions. This was observed after multiple failed escape attempts in Mt. Moon.
- **Pokemon Tower 6F Healer Change:** The friendly Channeler at (13,11) is no longer a healer. Her dialogue has changed to 'I feel anemic and weak...'.
- **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
- **Shop Menu Navigation Anomaly:** The shop menu in the Cerulean Mart does not follow a standard grid layout. Manual testing showed 'Down' moves from 'BUY' to 'SELL', but 'Right' does nothing from either position. The menu must be exited with the 'B' button.