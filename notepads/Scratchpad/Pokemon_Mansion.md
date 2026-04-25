Pokemon Mansion Mechanics:

- Switches at 3F (10, 4), 1F (2, 5), and 1F (18, 25) toggle ALL shutters globally.
- STATE A (Default upon entering Mansion): Yellow OPEN, Dark Grey CLOSED.
- STATE B: Yellow CLOSED, Dark Grey OPEN.

- STAIRS & WARPS:
  - 1F (5, 10) <-> 2F (5, 10) (West Wing)
  - 2F (6, 1) <-> 3F (6, 1) (North Wing)
  - 1F (23, 22) <-> 2F (21, 23) (East Wing)
  - B1F (7, 10) -> 1F (7, 10) (One-way drop)
  - 1F (23, 21) <-> B1F (23, 21) (Stairs between 1F East and B1F South)

Current Status:
- Goal: Reach 2F North via West Wing stairs at (5, 10).
- Confirmed constraints: The x=9 vertical wall is made of Dark Grey shutters. It is CLOSED in State A.
- To reach the West Wing, I must be in State B. 
- In State B, Yellow shutters at (16, 16) are CLOSED. But Dark Grey shutters at (14, 16)/(15, 16) are OPEN, allowing escape from the switch at (18, 25).
- Action Plan: Navigate to (18, 25), toggle to State B, walk North through (14, 16), walk West through x=9, reach (5, 10).