# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support.
- **SPROUT (Gloom):** Grass/Poison Utility. Good for status effects.
- **THISTLE (Nidoran♀):** Physical Attacker.
- **PIP (Pidgeotto):** Flying Attacker.
- **PARCH (Sandshrew):** Ground Type Wall. Critically injured (14 HP) and needs healing.
- **SHELLSHOCK (Squirtle):** Water Type. Gift Pokémon, in PC.
- **LUMIN (Clefairy):** Normal Type. In PC.

# 2. Agent Development Log
- **NOTE:** I am underutilizing my agents. I must make better use of `heal_priority_agent` before exploring with injured Pokémon and `party_manager_agent` to select leads for new areas.

# 3. Current Objective: Heal Party & Train for Vermilion Gym
- **Goal:** Defeat Lt. Surge and earn the Thunder Badge.
- **Strategy:** Finish exploring Route 11 for EXP, then return to a Pokémon Center to heal. Then, challenge Lt. Surge.

# 4. Trainer Battle Logs
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).
- **Rival BLAZe (@ Cerulean City):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).
- **Rival BLAZe (@ S.S. Anne):** Krabby (Lv 19), Raticate (Lv 20), Weepinbell (Lv 22), Sandshrew (Lv 21), Eevee (Lv 24).
- **S.S. Anne:** All trainers defeated, kitchen puzzle solved, Captain event triggered, HM01 CUT obtained.
- **Vermilion Gym Puzzle:** Solved.
- **Diglett's Cave:** Traversed from Route 11 entrance to Route 2 exit.

# 5. Game Mechanics & Insights
- Poison deals 1 HP damage every 4 steps.
- Level-capped Pokémon show a fake EXP gain message, but their EXP value does not actually change.
- Non-volatile status conditions are cured after trainer battles.
- PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
- The S.S. Anne has left.
- Defeated trainers remain as impassable obstacles.
- Diglett's Cave connects the Vermilion City area (via Route 11) to the Pewter City area (via Route 2).
- An NPC in the Diglett's Cave exit house (Route 2 side) mentioned Rock Tunnel is dark and needs the move FLASH to light it up.
- **EXP Sharing:** EXP is shared among all Pokémon that participated in the battle against a single opponent's Pokémon, even if they were just switched in and out.

# 6. Type Matchup Discoveries
- **Magnemite:** Resists Flying-type moves. Hypothesis: It has a Steel type in this ROM hack.
- **Ground-types:** Appear to be immune to Paralysis from moves like Stun Spore.
- **Poison vs. Ground:** Poison-type moves (like Acid) are not very effective against Ground-types.

# 7. Critical Lessons & Unverified Assumptions
- **CRITICAL LESSON (Risk Management):** Avoid exploring with critically injured Pokémon or making reckless gambles in battle, like relying on a confused Pokémon with low HP.
- **CRITICAL LESSON (Reading):** I must read screen text verbatim and not let my expectations create hallucinations.
- **CRITICAL LESSON (Tool Usage):** Double-check arguments and notepad content to avoid repeated failures and duplicate entries.
- **CRITICAL LESSON (Battle Efficiency):** I need to be more deliberate and try to combine menu navigation and selection into single, shorter command chains.
- **Assumption:** The only way forward is through the eastern part of Route 11.