# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support. THUNDERPUNCH has 0 PP.
- **SPROUT (Oddish):** Grass/Poison Utility. Good for status effects. Currently paralyzed.
- **THISTLE (Nidoran♀):** Physical Attacker. Fainted.
- **PIP (Pidgeotto):** Flying Attacker. Fainted.
- **PARCH (Sandshrew):** Ground Type Wall. Fainted.
- **SHELLSHOCK (Squirtle):** Water Type. Gift Pokémon, in PC.
- **LUMIN (Clefairy):** Normal Type. In PC.

# 2. Agent Development Log
- **ACTION ITEM:** Consolidate `team_builder_agent` and `party_manager_agent` into a single, more robust `team_strategist_agent`.
- **NOTE:** Make better use of existing agents (`explorer_agent`, `progression_blocker_agent`) before creating new ones.

# 3. Completed Milestones
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).
- **Rival BLAZe (@ Cerulean City):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).
- **S.S. Anne:**
    - Defeated all trainers on the ship (except rival).
    - Solved the kitchen 'odd ball' puzzle (was a GREAT BALL).
    - Triggered the event to make the sailor blocking the Captain's quarters move.
    - Located the stairs to the Captain's Quarters.

# 4. General Gameplay Insights
- **Systematic Exploration:** Prioritize `Reachable Unseen Tiles`. Don't assume NPC dialogue is a progression trigger without exploring all physical paths first.
- **Battle Preparation:** Do not enter major battles (Gyms, Rivals) with a damaged party. Heal and restore PP beforehand.
- **Battle Tactics:** Avoid reactive switching that gives the opponent free hits. Commit to a strategy, even if it means walling with a resistant Pokémon in a neutral damage matchup.
- **Game Mechanics:**
    - Poison deals 1 HP damage every 4 steps.
    - Level-capped Pokémon show fake EXP gain.
    - Non-volatile status conditions are cured after trainer battles.
    - PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
    - The S.S. Anne might leave after I get HM Cut.