# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25943 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Use Strength vs Espeon.
- **Battle Plan:**
    1. **Pikachu:** Defeated.
    2. **Espeon (Lv73):** Muscle (260/280 HP, Neutral Stats) vs Espeon.
    3. **Action:** Use Strength (80 BP, Neutral).
       - Math: Cross Chop (100 * 1.5 STAB * 0.5 Resist = 75 BP). Strength (80 BP).
       - Strength is stronger and 100% accurate.
    4. **Next:** Espeon uses Psychic. Muscle tanks it. 2HKO Espeon.
    5. **Snorlax (Lv75):** Muscle's Cross Chop.
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