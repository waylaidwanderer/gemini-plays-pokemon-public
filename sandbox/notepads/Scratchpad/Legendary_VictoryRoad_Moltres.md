# Quest Log: Legendary Fire Bird Moltres & Victory Road 2F

## Active Strategic Objectives
- [x] HM04 Strength active on Victory Road 1F [Cast Turn 30364 by ROCKY]
- [x] Ride west along Route 22 to Pokémon League Reception Gate [Turn 30325]
- [x] Pass through Reception Gate and traverse Route 23 South to Victory Road 1F entrance (8, 17) [Turn 30356]
- [x] Enter Victory Road 1F, solve Boulder 1 puzzle to lower barrier (9, 12), and take Ladder (1, 1) to 2F (0, 8) [Completed Turn 30447]
- [x] Solve Switch Plate A puzzle: pushed Boulder (4, 14) south to row 16, then west onto Switch Plate A (1, 16), lowering Plateau Barrier at (7, 8)-(7, 9) [Completed Turn 30476]
- [ ] Ascend wooden staircase (5, 10) onto plateau (5, 9), walk east across lowered barrier (7, 8)-(7, 9) into eastern sector
- [ ] Traverse Column 16 Highway north to Row 1, walk west to Moltres at (11, 5)
- [ ] From 2F (0, 8), navigate north toward Northwest Chamber (4, 2) and empirically test unverified hypothesis: whether an open eastward corridor connects (4, 2) across rows 0-3 to (13, 3) and Moltres at (11, 5)
- [ ] Weaken Moltres with Swift and capture with Ultra Balls

## Party Preparation & Tactics (Audited Turn 30066)
- Wild Moltres Lv 50 Moves: Peck (Flying physical STAB, 35 power), Fire Spin (Fire special trapping, 15 power).
- Mewtwo (OMEGA Lv 70): Primary combatant & tank with 234 HP, 195 Speed, Recover (100% first-move sustain), Barrier (+2 Defense), and Swift (60 BP physical).
  - Empirical Damage Calculation vs Moltres (Lv 50, Def 100-120, HP 150-165):
    - Swift Non-Crit: Deals 44 to 62 HP (~28-38% of max HP).
    - Swift Crit: Deals 98 to 118 HP (max 118 HP leaves at least 32+ HP remaining). Zero risk of 1HKO!
  - Retail Gen 1 Capture Formula & Status Math:
    - Non-statused target: Ultra Ball generates R1 in [0, 150]. If target has no status, Step 2 requires R1 <= CatchRate (Moltres CatchRate = 3). Thus, if R1 > 3 (147/151 values), the ball misses immediately regardless of HP! The non-statused catch probability has an absolute mathematical ceiling of 4/151 (~2.65%) per Ultra Ball at red HP.
    - Statused target (PAR/BRN/PSN): Status bonus = 12. If R1 <= 12 (13/151 values = ~8.61%), the target is caught immediately in Step 1 prior to CatchRate/HP checks! Combined with the remaining checks at red HP, catch rate reaches ~11-12% per Ultra Ball.
    - Statused target (SLP): Status bonus = 25. Instant capture rate is 26/151 (~17.22%)!
  - Capture Protocol:
    - Primary: Use Mewtwo's Swift (non-crit 44-62 HP, crit max 118 HP vs Moltres Def 100-120, max HP 150-165) 1-2 times to safely weaken Moltres to yellow/red HP with 0% risk of 1HKO.
    - Sustain: Deploy Barrier (+2 Def) to tank Peck and Recover (100% first-move sustain with 195 Speed), throwing Ultra Balls each turn.
- Blastoise (SHELDON Lv 70): Emergency defensive tank (resists Fire Spin). Do NOT attack with Body Slam (crit risks lethal 1HKO on Moltres). Capture protocol relies strictly on Mewtwo Swift weakening + Ultra Ball attrition.
- Drowzee (SANDMAN Lv 9): Do NOT switch in (instantly faints to Moltres STAB).
- Ultra Ball Arsenal: 21 Ultra Balls ready in Bag.
- Geodude (ROCKY Lv 8): Active Strength user for boulder clearance.
- Diglett (DIGBY Lv 19): Dig escape if extraction needed.
