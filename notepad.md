# Ice Path Strategy (B2F Recovery)

## Current Status
- **Position:** Player at (16, 16).
- **Goal:** Retrieve Item (8, 9) & Return to B1F.
- **Puzzle State:**
  - **B2:** Dropped to (3, 12).
  - **Hypothesis:** Can I push B2 while standing on Ice at (3, 13)?

## Immediate Plan
1.  **Navigate to B2:**
    - Slide Left to (3, 16).
    - Slide Up to (3, 13) (Stop at Boulder).
2.  **Test Pushing:**
    - Try to push Boulder Up.
    - **If Success:** Push to (3, 10). Slide Right to Item.
    - **If Fail:** Slide Down/Escape. Return to B1F to Reset.
3.  **Retrieve Item:**
    - Get Item at (8, 9).
    - Exit via Ladder (9, 11).