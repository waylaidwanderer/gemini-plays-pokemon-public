# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support. THUNDERPUNCH has 0 PP.
- **SPROUT (Oddish):** Grass/Poison Utility. Good for status effects.
- **THISTLE (Nidoran♀):** Physical Attacker. Double Kick is key for Rock types.
- **PIP (Pidgeotto):** Flying Attacker. Good speed and decent damage.
- **PARCH (Sandshrew):** Ground Type Wall. Has Dig and Rest for recovery.
- **SHELLSHOCK (Squirtle):** Water Type. Gift Pokémon, in PC.
- **LUMIN (Clefairy):** Normal Type. In PC.

# 2. S.S. Anne - Current Objective
- **Primary Goal:** Find the Captain to get HM CUT.
- **Secondary Goal:** Find the stairs to the Captain's quarters.
- **Key Discoveries:**
    - **Kitchen Puzzle Solved:** The 'odd ball in the trash' hint from the cook at (6,13) referred to a GREAT BALL found in the trash can at (14,10), not a switch. The kitchen is a dead end.
- **Key Discoveries:**
    - The stairs to the upper decks are NOT on the B1F. They are likely accessible via a switch in the kitchen.
    - Some cooks are path-blockers, not trainers (e.g., Cook at (2,13)).
    - HM STRENGTH: A Super Nerd on B1F mentioned his Machoke has STRENGTH. This is likely the HM.
    - Rival: A battle with BLAZe is expected before reaching the Captain.

# 3. Key Hints & NPC Dialogue
- **S.S. Anne Kitchen:** A cook at (6,13) said: "I saw an odd ball in the trash." This is a hint for a hidden switch/item.

# 4. Item & TM Usage
- **TM44 (Rest):** Taught to PARCH, replacing POISON STING. (COMPLETE)
- **TM08 (Body Slam):** Plan to teach to THISTLE, replacing Tackle.

# 5. General Gameplay Insights
- **Systematic Exploration:** Clear areas methodically. Don't assume a floor is the correct path until stairs are found.
- **NPC Interaction:** Non-battling/defeated trainers are impassable walls. Some event NPCs offer gifts or block paths.
- **Game Mechanics:**
    - Poison deals 1 HP damage every 4 steps.
    - Level-capped Pokémon show fake EXP gain.
    - Non-volatile status conditions are cured after trainer battles.
    - PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
    - HM CUT: Used by pressing 'A' on a tree, not from a menu.
- **Unverified Assumptions:**
    - The S.S. Anne might leave after I get HM Cut. I should be efficient.

# 6. Battle Intel
## Gym Leaders
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).
## Rival BLAZe
- **@ Cerulean City:** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

# 7. Agent Development Log
- **Pathfinder Agent Overhaul:** The agent's system prompt has been rewritten to explicitly treat ALL objects (including defeated trainers) as impassable, with Pikachu as the only exception. This seems to be working well.
- **Consolidation Idea:** Consider merging the `stuck_solver_agent` and `map_explorer_agent` into a single, more robust exploration agent.
- **Future Agent Ideas:**
    - **Progression Blocker Agent:** To analyze key items, map data, and NPC dialogue to identify requirements for story obstacles (e.g., the thirsty Saffron guard).
    - **Trainer Battle Predictor:** To simulate battles against known trainer teams, suggesting optimal leads and switch strategies.

# 8. Training Goals
- **S.S. Anne:** Defeat all trainers.
- **Post S.S. Anne:** PARCH (Lv 12) and THISTLE (Lv 16) need training.