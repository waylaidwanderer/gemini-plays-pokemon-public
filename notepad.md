# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25928 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** React to Espeon's move vs Kunai.
- **Battle Plan:**
    1. **Pikachu:** Defeated.
    2. **Espeon (Lv73):** Kunai is active. Immune to Psychic.
    3. **Scenario A:** Espeon uses Psychic (0 dmg). Kunai uses Shadow Ball (Ghost, Physical, Super Effective).
    4. **Scenario B:** Espeon uses Swift/Mud-Slap. Kunai takes damage. Attack if alive, Switch to Muscle if fainted.
    5. **Next:** Muscle sweeps with Strength/Cross Chop.
- **Resources:** Muscle (280/280, Healthy). Kunai (70/70, Active).

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.