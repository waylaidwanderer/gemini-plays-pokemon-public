# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25950 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Use Hyper Potion on Muscle.
- **Battle Plan:**
    1. **Charizard (Lv77):** Active. Muscle (51 HP).
    2. **Turn 1 (Current):** Confirm Hyper Potion Use.
       - Sequence: Select Hyper Potion (A) -> Select USE (A) -> Select Muscle (A).
       - Muscle heals to 251/280.
       - Charizard attacks.
    3. **Turn 2:** Attack with Strength.
       - Strength (Physical, 80 BP) vs ThunderPunch (Special, 75 BP * 2 = 150).
       - Machoke's Atk >> SpAtk. Strength is likely more consistent.
    4. **Snorlax:** Muscle's Cross Chop.
    5. **Venusaur:** Ice Punch or Strength.
    6. **Blastoise:** Cross Chop.
- **Resources:** Muscle (51/280). 3 Hyper Potions. 1 Max Revive. Gyarados alive.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.