# Scratchpad: Sovio City Hypotheses & Live Routing

## Commercial District & Mart Search Checklist
- [x] Pokémon Center Interior (Columns 1-15, Rows 1-8): Verified Turn 2491. Single room, no Mart counter or item vendor.
- [x] Building Facade at (32-37, 8-12): Verified Turn 2482. Wooden shutters at (35-36, 12) are solid decorative collision.
- [x] Residential Houses Checked:
  - (48, 13) East Plaza: Nana & Little Girl (residential)
  - (39, 7) North-Central: Elderly Man with Wii (residential)
  - (28, 13) Northwest: Mother & Son (residential)
  - (14, 15) Northwest: Machop Family (residential)
  - (31, 26) South-Central: Elderly Woman (residential)
- [ ] Unsurveyed Western Avenue Block (Columns 16-27, Rows 10-17): North of main street between Rocky (24, 17) and Machop house (14, 15). Prime candidate for standalone PokéMart building.
- [ ] Southwest Perimeter (Columns 17-20, Rows 25-29): Wooden building near Bikers. Perimeter approaches from rows 25-26 and row 28 unverified.
- [ ] North Street Terminus (Columns 38-41, North of Row 7): Check if road continues to commercial area.

## Tactical Analysis: Fifth Grunt (Litwick Lv8)
- **Litwick Threat Profile**: Ghost/Fire, Lv8.
  - Immune to Normal (Quick Attack) and Fighting (Mach Punch).
  - Type Matchup vs Metal Claw (Steel): Ghost is 1.0x (neutral), Fire is 0.5x (resisted) -> **Overall 0.5x (Resisted)**!
  - Damage calculation:
    - At +0 Attack (27 Atk): Metal Claw deals ~7-8 dmg vs Litwick (~23 HP) -> 3-4 hits to KO.
    - At +1 Attack (40 Atk via 1 Work Up): Metal Claw deals ~12-14 dmg -> **Solid 2HKO**!
  - Moves observed: Minimize (+2 evasion), Ember (STAB Fire, ~7-8 dmg vs Sirius), Fire Spin (trapping + chip).
  - Ability: Flame Body (30% chance to burn attacker on contact; Metal Claw makes contact!). Burn status cuts Physical Attack by 50% and deals 1/16 max HP per turn.
- **Inventory Verified (Turn 2543)**:
  - Bag Items: Potion x 1 (restores 20 HP)
  - Bag Poké Balls: Empty (0)
- **Refined Battle Strategy**:
  - Turn 1: Use **Work Up** once (+1 Atk / +1 SpAtk). This cannot miss, makes no contact (0% Flame Body risk), and increases Metal Claw damage to a 2HKO.
  - Turn 2+: Attack with **Metal Claw** to achieve a 2HKO.
  - Contingency: If Sirius drops below 15 HP or takes heavy burn chip, use the Potion (+20 HP) immediately to sustain through any Minimize evasion checks.