# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (23, 0) on Victory Road 3F East (Map 0_198)

## BREAKTHROUGH DISCOVERY (Turn 108628)
- We spent several turns trying to find the exit of Victory Road on 3F East. Specifically:
  - We hypothesized that (23, 1) on 3F East was the exit warp (Turn 108538).
  - We navigated to (23, 0) on 3F East on Turn 108587.
  - We tested stepping Down to (23, 1), turning Up, and stepping Up to (23, 0) on Turn 108622.
  - **Result**: No warp occurred! Standing on (23, 1) and (23, 0) did not trigger any map transition.
  - **Analysis**: Map 0_198 (Victory Road 3F East) has ONLY 3 warps in the standard Gen 1 pokered engine:
    1. (23, 15) -> Hole (down to 2F, Map 194, Warp 4)
    2. (23, 7) -> Ladder to 2F (Map 194, Warp 3)
    3. (27, 15) -> Ladder to 2F East (Map 194, Warp 1)
  - This means there is NO exit warp on 3F East! The exit of Victory Road in Pokémon Red/Blue is on **2F East (Map 0_194)** at coordinates **(27, 1)**!
  - **The Missing Link**: On Turn 108483-108505, we explored 2F East. We walked along Column 28 to (28, 1) and (28, 0). (28, 0) is a solid wall (collision bump), and (28, 1) is not a warp. We completely bypassed Column 27 where the actual exit door is at **(27, 1)**!
  - **Active Plan**: Walk back to the ladder at (23, 7) on 3F East, go down to 2F East, and walk to (27, 1) to exit Victory Road!

## Step-by-Step Backtracking to 2F East & Exit:
- Current: (23, 0) on 3F East.
- Step 1: Walk Down 7 steps along Column 23 to reach the ladder at (23, 7): (23, 0) -> (23, 1) -> (23, 2) -> (23, 3) -> (23, 4) -> (23, 5) -> (23, 6) -> (23, 7).
- Step 2: Interact with the ladder at (23, 7) to descend to 2F East (Map 0_194).
- Step 3: On 2F East, walk to the exit warp at (27, 1):
  - From (23, 7), walk Up 2 steps to (23, 5)
  - Walk Left 6 steps to (17, 5) (bypassing the (23, 4) wall partition)
  - Walk Up 2 steps to (17, 3)
  - Walk Right 10 steps along Row 3 to (27, 3)
  - Walk Up 2 steps along Column 27 to the exit warp at (27, 1)! (27, 2) -> (27, 1).