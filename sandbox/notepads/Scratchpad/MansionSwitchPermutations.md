# Pok�mon Mansion Switch & Barrier Permutations

## Global Switch Permutations
- **State A (Default / Untoggled)**:
  - Initial configuration upon entering the dungeon.
  - Reset to State A whenever exiting the dungeon (via door, Dig, or Teleport).
  - Hypothesis: 1F Shutter at (24..25, 13) is OPEN in State A, allowing direct access from 3F Balcony Drop (16, 14) -> (24, 13) into the northern chamber containing B1F stairs.
- **State B (Toggled)**:
  - Activated by pressing any Mewtwo statue switch (e.g. 3F (10, 5) on Turn 18484).
  - 1F Shutter at (24..25, 13) is confirmed CLOSED (Turn 18520).

## Empirical Testing Protocol
1. Use Dig to exit Mansion -> resets to State A.
2. Re-enter 1F -> ascend 2F -> ascend 3F (6, 1).
3. Do NOT press 3F switch at (10, 5).
4. Jump off balcony at (16, 13..14) to land at 1F (16, 14).
5. Walk directly to (24, 13) to verify before/after whether the shutter is OPEN.
6. If OPEN, proceed through to northern chamber and B1F stairs.
