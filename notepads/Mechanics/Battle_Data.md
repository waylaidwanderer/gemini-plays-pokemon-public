Battle Data & Mechanics:
- Professor Oak automatically heals the party after major story events (verified after first rival battle on Turn 52, and delivering parcel/receiving Pokédex on Turn 166).
- Catching Mechanics: Poké Balls can fail even on full HP, very low-level Pokémon (e.g., Lv 3 Pidgey broke out at full HP, Turn 235). Weaken them first if possible, or expect to use multiple balls. Full HP catches fail frequently even on Lv 2s. Weakening to red HP allowed immediate catch (Turn 311).
- Catching Mechanics: Poké Balls can fail even when the target is in the yellow HP zone (Turn 770).
- Switch-Training: Swapping a Pokémon out shares the EXP among all participants. Odd EXP values are truncated (e.g., 23 EXP total gave 11 EXP each to two Pokémon, Turn 437).
- Free Switch-In: When an enemy faints and the game asks "Will [Player] change POKEMON?", selecting YES allows sending out a new Pokémon without taking a hit that turn. Ideal for sharing EXP with weak Pokémon.
- Stat Stages: Stat-boosting moves like Harden display 'Nothing happened!' once the stat has reached its maximum level (verified Turn 648).
- Stat Mechanics: Stat-lowering moves display "failed!" once the target's stat reaches its minimum level. String Shot failed on 3rd use (Turn 1045) and Leer failed on 2nd use (Turn 1084).
- Speed Mechanics: Stat drops significantly impact turn order. A Lv 7 Pidgey outspeeds a Lv 10 Caterpie but is outsped after one String Shot (Speed -1 stage) (Turn 1038).
(Note: Early game specific damage and EXP scaling logs have been archived to Archive/Early_Game_Battle_Data)
- Accuracy Mechanics: Tackle has 95% accuracy in Gen 1, which explains occasional misses without evasion modifiers (e.g., missed twice in a row on Turn 1218/1219). It is not just the 1/256 miss bug.
- Overworld Mechanics: Defeated trainers reset to their original spawn positions when you leave and re-enter a map. For example, a Lass ran to (20, 4) to challenge me, but reset to her original location at (23, 4) after I traveled to Pewter City and back (Turn 1208).
- Status (Sleep): Waking up consumes the entire turn. The opponent can immediately act afterwards. If they use a sleep move (like Sing), they can put the Pokémon right back to sleep before it can attack, creating a stunlock loop.
- Move Cursor Memory: Confirmed that the battle move cursor remembers its position from the last time a move was selected during the current battle (Turn 2095).
- Status (Sleep): Sing has a chance to miss. Verified Turn 2103 when Clefairy used Sing on AERO's switch-in and AERO did not gain the SLP status.
- Type Effectiveness: Bug is Super Effective against Poison in Gen 1 (verified Turn 2351: Leech Life vs Zubat).
- Turn 2763: In battle with Super Nerd, switching to FANG (Rattata, Lv 12) against Voltorb to share EXP.
- Status (Disable): In Gen 1, if a move is disabled, the game still allows you to select it in the battle menu. If you do, the turn is wasted and the text "[MOVE] was disabled!" appears (Verified Turn 5929/5930).
- Wrap Mechanics: Wrap is a multi-turn trapping move. While wrapped, the text 'Enemy [PKMN]'s attack continues!' appears each turn. The player's turn is skipped entirely and the battle menu does not appear until the move ends (Verified Turns 6296-6299 against Ekans).
- Ghost types are immune to Normal-type moves (e.g. Mega Punch, Tackle). (Verified Turn 17558 against a Gastly).