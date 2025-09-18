# I. Active Quests

- **Current Quest: Retrieve the Old Amber**
    - **Objective:** Retrieve the Old Amber and present it to the Rocket Grunt on Mt. Moon B2F.
    - **Status:** Actively testing hypotheses suggested by the `npc_behavior_strategist` agent within the Pewter Museum.
- **Stalled Quest: The Copycat's Gift**
    - **Objective:** Obtain a POKé DOLL and give it to COPYCAT.
    - **Status:** Active. All leads in Cerulean City exhausted for now.

# II. Game Mechanics & World Rules

- **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
- **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot.
- **Party Menu 'SWITCH' Lock:** The game can prevent using the 'SWITCH' command in the party menu, observed after multiple failed escape attempts.
- **Shop Menu Navigation Anomaly:** The Cerulean Mart shop menu does not follow a standard grid layout and requires 'B' to exit.
- **Pikachu Trap Mechanic:** On Rocket Hideout floors and in the Pewter Museum, interacting with specific objects can trigger a trap that locks the player on an impassable tile. This trap is escaped by pressing the 'B' button.

# III. Tile Mechanics & Traversal Rules

- **`ground`**: Walkable.
- **`grass`**: Walkable, triggers wild encounters.
- **`impassable`**: Walls, cannot be entered.
- **`ledge`**: One-way traversal downwards.
- **`cuttable`**: Requires HM Cut to pass. Respawns on map change.
- **`ladder_down`**: Warp to a lower floor.
- **`elevated_ground`**: Walkable ground at a different elevation. Requires `steps` to access from `ground`.
- **`steps`**: Allows movement between `ground` and `elevated_ground`.

# IV. Battle Intelligence

- **Type Effectiveness Chart (Verified):**
    - Water > Rock/Ground
    - Water is not very effective against Bug/Grass, Ghost/Poison
    - Poison is not very effective against Poison/Flying, Rock/Ground
    - Flying is not very effective against Rock/Ground, Electric
    - Rock is not very effective against Ground
    - Normal > Ground, Water/Ice
    - Normal is not very effective against Rock/Flying
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
    - **Brock's OMASTAR (Lv 64):** HYDRO PUMP
    - **Brock's ONIX (Lv 65):** EARTHQUAKE
    - **Brock's KABUTOPS (Lv 64):** SLASH
    - **Brock's GOLEM (Lv 64):** EXPLOSION
    - **Brock's NINETALES (Lv 64):** SOLARBEAM (charge)

# V. Key Discoveries & Lessons Learned

- **Tool Deferral Failure (CRITICAL):** Repeatedly deferred the creation of necessary tools instead of building them immediately. **Lesson Reinforced:** If a repetitive manual task can be automated, or a complex reasoning task can be delegated, building a tool or agent for it is the highest priority.
- **PC Mechanics (CRITICAL):** The PC is **stateful**. Any automation tool MUST account for this by having a reset sequence to return to a known state.
- **Route 4 Access (CRITICAL):** There are two distinct maps named 'Route 4'. The eastern section is a one-way path *from* Mt. Moon.
- **Confirmation Bias & Over-Correction (CRITICAL):** My handling of the Rocket Hideout B2F maze was a cascade of cognitive errors. **Lesson:** Do not swing from one bias to another. Trust verifiable data and tool outputs over intuition.
- **Hypothesis Testing Failure (Preparation):** Arrived at a location to test a hypothesis without the required Pokémon/items/moves. **Lesson:** Always verify party composition and necessary items/moves *before* traveling.
- **Pikachu Following Mechanic (CRITICAL CLARIFICATION):** A button press in Pikachu's direction will only cause a turn *if the player is not already facing that direction*. Pathfinding tools must account for this.
- **Rocket Hideout Spinner Physics:** All known spinner data for the Rocket Hideout B2F floor has been collected.

# VI. Strategic Notes

- **Agent Utilization:** For complex puzzles, I must use `multi_stage_navigator` and `npc_behavior_strategist` instead of manual trial-and-error.
- **Tool Maintenance Protocol:** Critical tool flaws must be fixed *immediately* upon discovery.
- **`autopress_buttons` Flag (CRITICAL):** Certain automation tools require the `autopress_buttons: true` flag to be set when called to function correctly.

# VII. Cognitive Bias & Self-Correction Log

- **Fossil Quest Confirmation Bias:** I may be too focused on the Hiker at 1F (6,7) being the direct solution. I must remain open to testing hypotheses that are not directly related to interacting with the Hiker himself.
- **Game Corner Entry Failure (CRITICAL):** Became stuck in a loop for over 20 turns attempting to enter the Celadon Game Corner while Pikachu blocked one of the warp tiles. **Lesson:** If a specific path or objective is repeatedly blocked, do not persist with the same failed approach. Re-evaluate, check for alternate routes, or pivot to a different high-priority goal.

# VIII. Verified Observations

- **Game Corner Clerk Dialogue:** The clerk at (6, 7) will say "You don't have a COIN CASE!" if the player attempts to buy coins without one.
- Spoke to Super Nerd at Rock Tunnel B1F (21, 22). Dialogue: 'Costume players dress up as POKéMON for fun.' This was not related to the Mt. Moon fossil quest.
- Spoke to Super Nerd at Rock Tunnel 1F (24, 9). Dialogue: 'Oh well, I'll get a ZUBAT as I go!'. This was post-battle dialogue and not relevant to the quest. This confirms the Rock Tunnel hypothesis is a dead end.

# X. Investigation Logs & Archives

## Solved Puzzles & Completed Quests

- **Quest: Rocket Investigation (Completed)**
    - **Objective:** Use the LIFT KEY to operate the elevator in the Rocket Hideout.
    - **Solution:** Defeated Giovanni and dismantled the operation.
- **Quest: The Coin Case**
    - **Objective:** Obtain a COIN CASE to play games at the Celadon Game Corner.
    - **Status:** Completed.
    - **Solution:** The Gym Guide NPC at (1, 2) in the Celadon Diner gives the player the COIN CASE. He mentions he is giving up gambling after losing everything at the slots, a fact corroborated by the Fisher NPC in the same room.
- **Puzzle: Pewter Museum 2F Exit**
    - **Objective:** Get the Youngster NPC to move from blocking the exit warp.
    - **Status:** Solved.
    - **Solution:** The solution is a multi-step process. First, lead with a revived fossil Pokémon (e.g., Kabutops) and speak to the Youngster. His dialogue will change. Second, speak to the Scientist in the same room. Even though the Scientist's dialogue does not change, this action will cause the Youngster to move away from the exit warp.

# XI. Reflection & Maintenance Log

- **(Turn 222912):** Added `ladder_down` to my documentation. It functions as a warp to a lower floor. Added an entry about misdiagnosing the `automated_path_navigator` failure. The tool was correct; my *assumption* about the destination's reachability was wrong. **Lesson Reinforced:** I must trust my tools and verify my own assumptions about the game state before attempting to debug code. Spoke to the Rocket Grunt at B2F (30, 12). His dialogue remains: "If you find a fossil, give it to me and scram!". This confirms the fossil is the required item.
- **(Turn 223220):** Performed mandatory self-assessment. Identified and corrected a critical failure to immediately fix the `item_menu_navigator` tool. Also created the `npc_behavior_strategist` agent, which was previously deferred. This reinforces the core directive of immediate action. Added `grass` to my documentation.
- **(Turn 223454):** Received Overwatch critique. The `pc_navigator` tool is unreliable and needs to be fixed. My notepad has duplicate sections and needs to be cleaned up. I will address these data management issues immediately.