# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Current status & Progression
- We are currently on Cerulean Cave 2F (0_226) exploring the corridors to find the ladder that descends into the isolated northwest section of 1F (where the B1F stairs are located).
- Turn 112111: Reached (18, 11) on 2F.

## 2F Exploration Discoveries & Pathing Notes
- Row 11 forms a completely open, unblocked horizontal corridor from Column 18 to Column 24, allowing horizontal travel.
- Row 16 is a solid horizontal rock wall from Column 14 to Column 20, which completely blocks direct downward access from Row 15 to Row 17 in the central section.
- Row 9 is blocked at (22, 9) and (24, 9) by rock walls, so it is not a continuous horizontal passage.
- Our goal is to explore the western corridors of 2F. To do this, we should follow the open corridors west from our current position (18, 11).

## Pathing Plans
- From (18, 11), let's explore further west. Row 11 goes west through:
  - (18, 11) -> (17, 11) -> (16, 11) -> (15, 11) -> (14, 11).
  - From (14, 11), we can go down to (14, 12) -> (14, 13).
  - Wait, can we go further west on Row 11? (13, 11) is a wall.
  - Let's look at (12, 11): it is TYPE_3fe2 (passable).
  - How do we reach Column 12?
  - Column 12 has a vertical passage from Row 9 to Row 15:
    - (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15) are all passable.
    - So if we can get to Column 12, we can travel vertically!
    - How do we get to Column 12?
    - Let's check Row 9: (12, 9), (13, 9) are passable. Is there any way to go from the east of Column 14 to the west on Row 9?
    - (14, 9) is TYPE_2889 (wall).
    - Wait, is (14, 8) passable? (14, 8) is TYPE_3fe2 (passable)! And (15, 8) is TYPE_3fe2 (passable)!
    - Let's look at Row 8:
      - (14, 8) TYPE_3fe2
      - (15, 8) TYPE_3fe2
      - (16, 8) TYPE_2889 (wall)
      - (17, 8) TYPE_2889 (wall)
      - (18, 8) TYPE_2889 (wall)
    - So Row 8 is blocked on the east.
    - Let's look at Row 7:
      - (16, 7) is TYPE_3fe2.
      - (18, 7) is TYPE_3fe2.
      - (19, 7) is TYPE_3fe2 (Ladder 3).
      - (22, 7) is TYPE_3fe2.
      - (23, 7) is TYPE_3fe2.
      - Wait, is Row 7 connected?
      - Let's explore the western corridors systematically!