# Pokemon Mansion - Evidence-Based Routing
## B1F PUZZLE SOLUTION:
- The stairs at B1F (23, 22) are separated from the rest of the floor by a solid wall at x=20.
- In State B: Vertical yellow shutters at (20, 17) and (21, 17) are OPEN. We use these to enter B1F North.
- In B1F North, we found the switch at (14, 17)/(15, 17). 
- Toggling to State A CLOSES the y=17 yellow shutters, but OPENS the dark grey shutters at y=16 (e.g., at x=20).
- This allows us to walk East to x=24, South to y=22, and Left to the stairs at (23, 22) while in State A!
- State A also opens the x=11 shutters on 1F, granting us escape!

## PLAN:
1. Walk to the switch at (15, 18), face Up, and toggle to State A.
2. Explore North along x=10 to see if State A opened a path into B1F North-West (where the Secret Key is).
3. If no path, escape B1F via the State A route (across y=16 at x=20) and return to 1F.