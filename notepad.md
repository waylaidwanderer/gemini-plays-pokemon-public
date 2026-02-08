# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14). Requires **Voice ID**.
- **Immediate**: Unlock/Activate Switch at B1F (19, 11). Status: "Turned off" (Unresponsive despite 2 statues active).

## Key Puzzles & Blockers
1.  **The Switch (B1F 19, 11)**: CONFIRMED "Turned off" and inactive. Needs to be unlocked.
    -   **Statue 1 (6, 1)**: ACTIVE (Changed from "Shiny" to "Normal").
    -   **Statue 2 (24, 6)**: ACTIVE (Changed from "Shiny" to "Normal").
    -   **Result**: Main Switch still OFF. Missing something?
2.  **The Shutter (B1F 15, 10)**: Closed. Separates East and West wings.
3.  **The Murkrows**:
    -   **West Wing (10, 4)**: Perched on computer. Unresponsive to A-press/Bump from South/West/North.
    -   **East Wing (22, 8)**: Perched on computer. Unresponsive (Checked from North & South).
    -   *Hypothesis*: Murkrows need a trigger (Radio? Specific Grunt? Item?). Or maybe the **Switch at (19, 11)** activates them?
4.  **Boss Door (B2F 23, 14)**: Passwords entered, but needs Voice ID.

## Navigation & Map Data
-   **B1F West Wing**: Main entrance. Contains Statue Traps, "Useless Grunt" (2, 4), Murkrow (10, 4), Stairs to B2F (3, 14).
-   **B1F East Wing**: Accessed via Shop Stairs (27, 2) or Warp (5, 15) [ONE WAY]. Contains Switch (19, 11), Jed (18, 12), Murkrow (22, 8).
-   **B2F**: Accessed via West Wing Stairs (3, 14). Contains Boss Door (23, 14).
-   **Traps**:
    -   **Warp Traps**: (12, 8) [Active?], (19, 1) [Confirmed Inert/Safe].
    -   **Battle Traps**: Geodude/Voltorb/Koffing tiles on the floor.
    -   **Jed's Warning**: "Warp panel up ahead" likely refers to (19, 12).

## Current Plan
1.  **Unlock Switch at (19, 11)**:
    -   Currently "Turned off".
    -   **Loop Condition**: Switch OFF -> Warp (19, 12) Active -> Warps to (22, 11) -> Grunt blocks path.
    -   **Goal**: Turn Switch ON to disable Warp (19, 12).
    -   *Action*: Re-check Switch and adjacent Computer (19, 10).
2.  **Investigate West Wing**:
    -   If Switch fails, re-check Murkrow (10, 4) and trap field for hidden triggers.
    -   Verify if Grunt at (22, 10) can be bypassed or battled.

## Confirmed Facts
-   **Statues**: (6, 1) and (24, 6) are active switches. (Already triggered).
-   **Traps**: (19, 12) is a Warp Trap to (22, 11).
-   **Boss Door**: Needs Voice ID.