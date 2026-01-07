# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25942 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Use Strength vs Espeon.
- **Battle Plan:**
    1. **Pikachu:** Defeated.
    2. **Espeon (Lv73):** Muscle (260/280 HP) vs Espeon.
    3. **Vs Espeon:** Use Strength (Physical, Neutral, 80 BP).
       - Cross Chop is resisted (50 BP). Punches are Special (bad vs Espeon).
       - Espeon will use Psychic. Muscle must tank it and 2HKO Espeon.
    4. **Snorlax (Lv75):** Muscle's Cross Chop.
    5. **Venusaur (Lv77):** Muscle's Ice Punch.
    6. **Charizard (Lv77):** Muscle's ThunderPunch.
    7. **Blastoise (Lv77):** Muscle's Cross Chop or ThunderPunch.
- **Resources:** Muscle (260/280). 1 Sacrifice left (Gyarados). 4 Revives, 3 Hyper Potions.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.