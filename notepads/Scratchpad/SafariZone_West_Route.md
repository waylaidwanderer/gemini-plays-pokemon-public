# Safari Zone West Exploration Scratchpad (Run 14 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 14 Start Turn**: Turn 50092.
- **Current Turn**: Turn 50115.
- **Steps Taken in Run 14**: 54 overworld steps.
- **Steps Remaining**: 446 steps remaining (from 500 starting steps).

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c) (Proven on Turn 49498 by physical bump from 2, 14 to 2, 13).
- Row 0/1/2 Columns 24-25 are blocked by solid tree walls (TYPE_2889) (Proven on Turn 49548 by physical bump).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 11-16 on the plateau are completely blocked to the North by solid cliff walls.
- Row 25 is completely blocked by a solid wall of trees across Columns 11-15 and 18-29 (proven on Turn 49102).

### RUN 13 OPTIMIZED PATH (500 STEPS BUDGET):
- [COMPLETED] **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)**
- [COMPLETED] **Phase 2: Traverse Center to East (Map 0_217)**
- [COMPLETED] **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)**
- [COMPLETED] **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)**
- [IN PROGRESS] **Phase 5: Backtrack across West Plateau to Southwest Ground Level (6, 20)**
  - Walk Down the eastern corridor to (25, 18). [COMPLETED]
  - Walk Left to (21, 18). [COMPLETED]
  - Climb the stairs at (21, 17) to (21, 16). [COMPLETED]
  - Walk Left across the plateau to (6, 16). [IN PROGRESS]
  - Walk Down to descend the western stairs at (6, 19) to (6, 20).
- **Phase 6: Re-verify Northwest Ground Passage & Retrieve Items**
  - Walk to (6, 20) and re-evaluate the southwest-northwest connection.
  - Re-verify if Column 2 Row 13 water or Column 1 Row 14/15 trees are passable.
  - Walk to the northern ground level, collect the Warden's Gold Teeth at (19, 7) or (9, 7), and visit the Secret House at (3, 3) to get HM03 Surf.

## Systematic Western Blockage Testing Protocol (Run 13) - COMPLETED & VERIFIED
- On Turns 49995-49999, we executed systematic foot-testing to investigate southwest-northwest ground-level connectivity:
  1. **Test Column 1 Row 15**: Standing at (1, 16) on Turn 49995, we attempted to walk Up into (1, 15) (TYPE_2889 tree). Result: Collision (remained at 1, 16), physically proving (1, 15) is a solid, impassable tree wall.
  2. **Test Column 2 Row 13**: Standing at (2, 14) on Turn 49998, we attempted to walk Up into (2, 13) (TYPE_4e8c water). Result: Collision (remained at 2, 14), physically proving (2, 13) is blocked by water.
  3. **Test Column 1 Row 14**: Standing at (2, 14) on Turn 49999, we attempted to walk Left into (1, 14) (TYPE_2889 tree). Result: Collision (remained at 2, 14), physically proving (1, 14) is a solid, impassable tree wall.
- **Definitive Conclusion**: There is absolutely NO ground-level passage from the Southwest to the Northwest. The elevated plateau is the only route. We must backtrack across the plateau.

## Socratic Question Answers (Turn 50081 Update)
### Socratic Question 1
- **Collision at (6, 16) -> (6, 15)**: Walking Up from (6, 16) resulted in a collision on Turn 50069. This physically proves that Column 6 Row 15 is blocked by a solid cliff wall (TYPE_2770).
- **Contradiction of Assumption**: We assumed walking to the western edge of the plateau would allow us to walk north directly to the northern ground level, but the western edge on Row 16 is completely bounded by a solid cliff face.
- **Redundant Traversal**: We walked 15 steps east from (6, 18) to (21, 16) by mistake because we confused Map 0_219 with Map 0_218. This wasted 30 steps total (15 east, 15 west). Our actual remaining overworld steps is 177 on Turn 50081.

### Socratic Question 2
- **Plateau Connection to Northern Ground Level**: Socratic Question 2 states that Column 10 (cliff/slopes) is blocked on Rows 6-9, Column 17 is blocked, and Column 6 Row 15 is blocked.
- **Systematic Test Candidates on Row 6**: The exact coordinate candidates on Row 6 of the plateau are Columns 11, 12, 13, 14, 15, and 16. We must systematically walk to (16, 6) and test each column by trying to walk north (Up) off the plateau onto Row 5 (the ground level). One of these columns must be the unblocked descent!

### Socratic Question 3
- **Step Counting & Tracking Sync**:
  - Our active tertiary objective has been synchronized to exactly 177 remaining steps on Turn 50081.
  - The 38-step tracking drift over the last 30 turns occurred because we executed a sequence of movement buttons (including collisions) during our blockage tests and backtracking without subtracting them turn-by-turn from the objectives.
  - **Discipline**: I will count every successful and unsuccessful overworld movement button pressed in every turn and subtract them immediately from our active remaining steps in both the scratchpad and objectives turn-by-turn.

### Socratic Question 4
- **Visual Verification of Gold Teeth**:
  - Yes! We visually verified the presence of the Pokéball item representing the Gold Teeth on the screen.
  - At (16, 6) on Turn 50048, we saw a Pokéball at (19, 7) (Northeast Ground Pokéball).
  - At (11, 6) on Turn 50049, we saw another Pokéball at (9, 7) (Northwest Ground Pokéball).
  - Both coordinates (19, 7) and (9, 7) correspond to actual visual Pokéball items on the ground level. We will collect both of them once we find the unblocked descent.