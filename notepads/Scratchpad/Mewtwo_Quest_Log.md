# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 130874
- Current Position: standing on foot at (11, 13) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Unconstrained Surfing Route**: We mathematically proved on Turn 130948 using a correct Gen 1 BFS transition model that the Northwest B1F stairs at (1, 3) on 1F are fully reachable. In Generation 1, we can enter the water from any land tile adjacent to water and dismount onto any adjacent walkable land tile. We do not need a ramp to start or end surfing. Thus, we can easily reach (1, 3) on 1F by entering the water on the east/south side and surfing to the west side, dismounting directly onto (1, 3) or adjacent land.
- **Proof of Work**: Tested via python BFS script on Turn 130948. Reaching (1, 3) was confirmed true (unconstrained reachable set of 474 tiles). Path: from 1F entrance (24, 17) -> walk to water -> SURF west -> dismount onto land near (1, 3).
- **Previous Spatial Hallucinations**:
  - The hypothesis that we had to use 2F West's northern corridor to bypass 1F's water was a complete hallucination, as 2F West's northern corridor is isolated from (1, 3) by a vertical barrier on Row 6.
  - The belief that we could only enter/exit water at ramps was a major design oversight in our custom BFS model, leading us to falsely think B1F stairs were isolated. We now know we can surf/dismount anywhere.
- **Next Step**: We will walk Down Ladder 5 from (9, 1) on 2F to arrive on 1F at (7, 1). From there, we will walk east to the water's edge, use SURF to enter the water, surf west, and dismount onto the land at (1, 3) to reach B1F!