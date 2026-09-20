# Quest Log: Legendary Fire Bird Moltres & Victory Road 2F

## Strategic Roadmap & Objectives
- [x] Heal team at Cinnabar Pokémon Center (cure Mewtwo FRZ, restore HP/PP) [Turn 29983]
- [x] Sell Nugget at Cinnabar Poké Mart for ¥5,000 (Wallet: ¥25,256) [Turn 29990]
- [x] Purchase 21 Ultra Balls (¥1,200 each, total ¥25,200) [Turn 29994]
- [x] Fly to Indigo Plateau via Farfetch'd (DUX) [Turn 30006]
- [x] Enter Victory Road 2F via Route 23 North cave entrance at (14, 31) [Turn 30024]
- [ ] Infiltrate Victory Road 2F and navigate to Moltres plateau (previously sighted Turns 15533, 16069, 17798, 19831)
- [ ] Capture Legendary Bird MOLTRES using Ultra Balls

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
    - Optional Status Risk/Reward: Blastoise's Body Slam has a 30% Paralysis rate. Non-crit deals 61-86 HP (safe), but critical hit (15.2% chance) deals 138-165 HP (risks 1HKO). If attempting Body Slam for Paralysis, only use when Moltres is at 100% HP and accept crit risk; otherwise stick strictly to Mewtwo Swift weakening + Ultra Ball attrition.
- Blastoise (SHELDON Lv 70): Emergency tank (resists Fire Spin). Do NOT attack with Body Slam (crit risks 1HKO at 165 HP).
- Drowzee (SANDMAN Lv 9): Do NOT switch in (instantly faints to Moltres STAB).
- Ultra Ball Arsenal: 21 Ultra Balls ready in Bag.
- Geodude (ROCKY Lv 8): Active Strength user for boulder clearance.
- Diglett (DIGBY Lv 19): Dig escape if extraction needed.