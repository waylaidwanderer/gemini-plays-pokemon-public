# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 9122: Standing at (35, 12) on Map 0_61 (Mt. Moon B2F) facing Up. We have successfully proven that the eastern platform of B2F is completely isolated from the northern section where the exit ladder is located. We are now executing our multi-floor backtracking plan to reach the northern section via 1F.
- Mt. Moon Progression Start: Turn 5170.

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [ ] Explore the Museum of Science (optional, northern part of town).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [ ] Traverse Mt. Moon to reach Route 4.
- [ ] Reach Cerulean City.

## Active B2F Exploration and Exit Strategy:
- **Primary Hypothesis**: The eastern platform on B2F has stairs leading down to a lower floor containing the exit.
- **Systematic Boundary Testing**:
  - Turn 9047: Tested Column 32 Row 11/12 boundary by pressing Up. Blocked by an impassable cliff wall.
  - Turn 9069: Tested Column 31 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Turn 9078: Tested Column 33 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Turn 9087: Tested Column 34 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Plan: Test Column 35 Row 11/12 boundary. If it is also blocked, we have proven the eastern platform is completely isolated from the northern section where the exit ladder is located.
- **Multi-Floor Backtracking Backup Strategy (If Column 35 is blocked)**:
  - If Column 35 is blocked, we will:
    1. Backtrack west along the Row 16 lower floor back to the central platform stairs.
    2. Ascend to (21, 17) and take the ladder back up to B1F.
    3. From B1F (21, 17), walk west along the horizontal corridor (Row 16/17) back to the far-NW pocket ladder at (5, 5).
    4. Ascend the (5, 5) ladder to 1F.
    5. On 1F, walk east along the Row 15 corridor to the north-central ladder at (17, 11).
    6. Take the (17, 11) ladder down to B1F (25, 9).
    7. From B1F (25, 9), walk to (17, 11) and take the ladder down to B2F (25, 9) (the Northern Section).
    8. Walk east past the fossils and the Super Nerd to the exit ladder at (33, 9) leading to Route 4 East!

## Mt. Moon Team-Training Strategy & Timestamps (Turn 4801):
- Starting Turn for Pewter Restocking: Turn 4801
- Target Level-Ups:
  - **BUGGY (METAPOD)**: Lv 12 achieved! Learned Confusion!
  - **SPARKY (PIKACHU)**: Train to Level 11 to learn Quick Attack.

### SPARKY Training Session Log (Turn 6126):
- Starting Turn for SPARKY training: Turn 6126
- Starting Level: Level 6 (0/117 EXP)
- Target Level: Level 16 (to learn Quick Attack in Red/Blue)
- Timestamp: Sunday, May 24, 2026 at 3:25 PM PDT.
- Grinding Progress:
  - Turn 6149: Reached Level 7 after defeating Rocket Grunt's Level 11 Sandshrew (gained 108 EXP).
  - Turn 6168: Gained 66 EXP after defeating Rocket Grunt's Level 11 Rattata.
  - Turn 6198: Reached Level 8 after defeating Rocket Grunt's Level 11 Zubat (gained 63 EXP).
  - Turn 6263: Gained 69 EXP after defeating wild Level 9 Zubat.
  - Turn 6289: Gained 55 EXP after defeating wild Level 9 Geodude.
  - Turn 6307: Reached Level 9 and learned THUNDER WAVE! (Defeated wild Level 10 Zubat, gained 75 EXP).
  - Turn 6339: Gained 49 EXP after defeating wild Level 8 Geodude. SPARKY is now at Level 9 with 98/148 EXP.
  - Turn 6377: Gained 77 EXP after defeating wild Level 10 Zubat. SPARKY is now at Level 9 with 175/148 EXP.
  - Turn 6430: Gained 46 EXP after defeating wild Level 6 Zubat. SPARKY is now at Level 9 with 221/148 EXP.
  - Turn 6460: Defeated wild Level 8 Zubat. SPARKY gained 61 EXP (now Level 9 with 282/148 EXP).
  - Turn 6613: Defeated wild Level 10 Zubat. SPARKY gained 38 EXP and reached Level 10!
  - Turn 6825: Used RARE CANDY on SPARKY. He grew to Level 11! We discovered Pikachu learns Quick Attack at Level 16 in Red/Blue (unlike Level 11 in Yellow). Updating target to Level 16.

## Verified 1F Overworld Connections:
- **Row 15 Corridor (Turn 8382)**: Verified that Row 15 is a fully passable horizontal corridor (TYPE_3fe2) across Columns 21-25, connecting the western half of Mt. Moon 1F to the eastern half (specifically to the NE ladder at (25, 15)). This allows us to walk directly to the NE ladder from the southern/western areas without underground backtracking.
- Turn 9106: Testing Column 35 Row 11/12 boundary.
  - Hypothesis: Moving Up from (35, 12) to (35, 11) is blocked by a cliff wall (similar to Columns 31-34).
  - Method: Press Up.
  - Verification: Check if player position changes or if we collide and remain at (35, 12).
  - Result: Confirmed! We pressed Up and remained at (35, 12) on Turn 9107 (0 tiles visited), proving the eastern platform has no north-facing stairs or open pathways here. The eastern platform on B2F is completely isolated from the northern area containing the exit. We must execute our multi-floor backtracking plan.