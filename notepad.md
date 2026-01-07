# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25919 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Sacrifice Mistral, then Muscle vs Espeon.
- **Battle Plan:**
    1. **Pikachu:** Defeated.
    2. **Espeon (Lv73):** Mistral (Lv15) uses Quick Attack (chip dmg) then faints. Switch to Muscle. Use Strength (Normal is 1x, Fighting is 0.5x vs Psychic).
    3. **Snorlax (Lv75):** Muscle's Cross Chop.
    4. **Venusaur (Lv77):** Muscle's Ice Punch.
    5. **Charizard (Lv77):** Muscle's ThunderPunch.
    6. **Blastoise (Lv77):** Muscle's Cross Chop or ThunderPunch.
- **Resources:** Muscle (201/280 HP). 5 Revives. 1 Full Restore. Mistral will die this turn.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.