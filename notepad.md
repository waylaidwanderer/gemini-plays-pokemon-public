# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25944 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Refuse Switch. Save Gyarados.
- **Battle Plan:**
    1. **Pikachu:** Defeated.
    2. **Espeon:** Defeated.
    3. **Charizard:** Incoming.
       - Refuse switch (Keep Gyarados as Revive Pivot).
       - Turn 1: Use Hyper Potion on Muscle (51 -> 251 HP).
       - Charizard attacks. Muscle tanks.
       - Turn 2: ThunderPunch (Super Effective).
    4. **Snorlax:** Muscle's Cross Chop.
    5. **Venusaur:** Ice Punch.
    6. **Blastoise:** ThunderPunch/Cross Chop.
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