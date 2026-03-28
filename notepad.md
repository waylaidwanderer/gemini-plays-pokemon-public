<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO)
Rival Team (GARY):
- Bulbasaur
[Turn 31, Mar 27 2026] Log updated.
[Turn 51, Mar 27 2026] 50-Turn Reflection:
- Progress: Starter acquired, rival defeated, heading to Route 1.
- Hygiene: Map markers for Pallet Town are clean. Notepads are organized.
- Custom Tools: Considered creating tools for battle logic or grass exploration, but manual control is safer for now.
- Error Analysis: Tracing exact tile steps prevents wall-bumping. Must continue this practice in Route 1.

<hr>

<h1><code>Locations/Pallet_Town</code></h1>

Room Layout (Player's Room):
- PC is at top-left: Monitor (0,0), Keyboard (0,1). Stand at (0,2) facing Up to use.
- SNES is in middle: TV (3,4), Console (3,5).
- Stairs down: (7,1).
Ash's House (Downstairs):
- Stairs up to room: (7,1)
- Mom: (5,4)
- Dining Table: (3,4) to (4,5)
Pallet Town Layout:
- Ash's House: (5,5)
- Gary's House: (13,5)
- Oak's Lab: (12,11)
- Route 1 (North Exit): Tall grass begins around X=10, Y=1.
Oak's Lab Layout:
- Oak: (5,2)
- Walkway to exit: X=4 and X=5.
- Table with Pokeballs: Y=3, X=6,7,8.

<hr>

<h1><code>Mechanics/PC_Storage</code></h1>

Player's PC starts with 1 Potion in item storage.

<hr>

<h1><code>Scratchpad/Route_1</code></h1>

Routing through Route 1:
- Objective: Head north from Pallet Town through Route 1 to reach Viridian City.
- Strategy: Avoid jumping over ledges (brown rocky tiles) as they are one-way. Find gaps in the ledges to proceed north.
- Current Route: At (10,30). Ledge blocks North at Y=27. Gap appears to be at X=8. Moving Left 2 to (8,30), then Up to bypass the sign at (9,27) and ledge.
- Current Route: At (12,22). Another ledge spans Y=19. Gap is located at X=9. Moving Left 3 to (9,22), then Up to pass through the gap at (9,19).
- Current Route: At (9,18). Heading straight North through the clear path and flower grass to (9,14).
- Current Route: At (9,14). Ledge and trees block North at Y=13. Moving Left to find a gap.
- Current Route: At (5,14). Path north is blocked. A gap is visible at X=2, but it is separated by a white fence at X=3. Moving South to trace the fence and find a way to its left side.
- Current Route: At (5,18). The white fence at X=3 blocks access to the western path (X=1, X=2) which leads North past Y=13. I must jump down the ledge at Y=19 and head South to find the bottom of the fence, then traverse up the left side.
- [Turn 68] Jumped down the ledge at Y=19. Now at (5,22), trapped between the ledge above (Y=19) and trees below (Y=23). Heading East to escape this horizontal strip.
- [Turn 69] Trapped in horizontal strip Y=20..22. Going East to X=16 to jump down the ledge at (16,23) and return to the Southern section. From there, I will head West to find the bottom of the white fence.
- [Turn 70] Successfully jumped down the ledge at (16,23), landing at (16,24). Currently at (14,24). Moving West along Y=25 to X=4 to find the crossover point to the western path (left of the X=3 fence).

<hr>

<h1><code>Locations/Route_1</code></h1>

Route 1 Layout:
- South exit to Pallet Town: (10,35) and (11,35).
- Path heads North through tall grass.

<hr>

<h1><code>Mechanics/Battle_Data</code></h1>

Battle Data & Mechanics:
- Oak automatically heals the party after the first rival battle (verified Turn 52).
- Wild Lv 2 Pidgey yields 15 EXP (verified Turn 58).

<hr>