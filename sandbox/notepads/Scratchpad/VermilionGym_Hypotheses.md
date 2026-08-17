# Vermilion Gym - Empirical Switch Trial & Mechanics Log

## Empirical Trial Results & Refutations
- **Refuted Hypothesis:** "Switch 1 is strictly restricted to even can indices (0, 2, 4, 6, 8, 10, 12, 14)."
  - *Testing Evidence (Turns 2793-2808):* All even-indexed cans (1,7), (5,7), (9,7), (3,9), (7,9), (9,11), (5,11), (1,11) were systematically checked with visual confirmation and all returned "Nope".
  - *Conclusion:* Theoretical assembly deduction is refuted by direct in-game empirical evidence. All 15 cans must be treated as potential Switch 1 candidates.
- **Refuted Hypothesis:** "Stationary alternation at (2, 7) will rapidly trigger Switch 1."
  - *Testing Evidence (Turns 2809-2820):* 12+ consecutive toggles between (1, 7) and (3, 7) produced zero switch triggers.
  - *Conclusion:* Stationary loops do not cycle the switch state effectively within a single stagnant session.

## Current Verified Protocol: Clean Map Reload + 15-Can Sweep
1. **Map Reload:** Walk to (5, 17) to exit to Vermilion City (12, 20), then step Up to (12, 19) to re-enter Vermilion Gym (4, 17). This guarantees a clean re-initialization of the gym script.
2. **Complete 15-Can Sweep Protocol:**
   - Row 7: (1, 7) -> (3, 7) -> (5, 7) -> (7, 7) -> (9, 7)
   - Row 9: (9, 9) -> (7, 9) -> (5, 9) -> (3, 9) -> (1, 9)
   - Can (14, 7,11): NOPE [Verified Turn 2857]
- Can (15, 9,11): Checking now [Turn 2858]
3. **Switch 2 Trigger Protocol:**
   - As soon as "Hey! There's a switch under the trash!" appears on can `(sx, sy)`:
   - Dismiss dialogue and immediately inspect adjacent cans: `(sx, sy-2)`, `(sx, sy+2)`, `(sx-2, sy)`, `(sx+2, sy)` and index 0 fallback `(1, 7)`.
4. **Door Open & Surge Battle:**
   - Once "The 2nd electric lock opened! The motorized door opened!" triggers:
   - Walk through (4, 4) / (5, 4) to (5, 2).
   - Engage Lt. Surge and sweep with TERRA's Dig!