# Cinnabar Island & Pokémon Mansion - Layout & Exploration Guide

## Cinnabar Island Overworld Layout
- **Pokémon Center:** Located in the southeast corner.
- **Cinnabar Poké Mart:** Located in the south-center.
- **Cinnabar Gym:** Located in the northeast corner at `(18, 3)`. Door is at `(18, 3)` facing south (Verified Turn 46287). It is locked by default and requires the **Secret Key** to enter.
- **Cinnabar Lab (Pokémon Lab):** Located in the southwest corner. Contains three research rooms where you can trade and resurrect fossils (Fossil Pokémon resurrect at Level 30!).
- **Pokémon Mansion:** Large building located in the northwest quadrant of the island. The Secret Key is found deep inside this building on B1F.

## Pokémon Mansion Switches & Keys Puzzle
- **Switches:** Located on various Mewtwo statues throughout the building. Interacting with a statue toggles the state of the electronic gates (opening some doors and closing others).
- **Goal:** Navigate the switches, escalators, and collapsed floors to reach B1F and retrieve the **Secret Key** to unlock the Cinnabar Gym!

## Pokmon Mansion - Empirical Layout & Coordinates (Verified Turns 46039-46125)
- **1F Entrance Warp:** Warp from Cinnabar Island front door at `(6, 3)` leads directly to Pokémon Mansion 1F at `(5, 27)`.
- **Cinnabar Lab Entrance:** Warp from Cinnabar Island at `(6, 9)` leads directly to Pokémon Mansion 1F Foyer at `(2, 7)` (an isolated room).
- **1F-to-2F Stairs:** Located at `(7, 10)` on 1F, leading to 2F at `(7, 11)`.
- **2F-to-1F Stairs:** Located at `(7, 10)` on 2F, leading DOWN to 1F at `(7, 11)`. (Empirically verified on Turn 46619)

- **3F-to-2F Pit (Fall):** Falling through the open pit on columns 16, 17, or 18 on row 12 on 3F lands on 2F.

- **1F-to-B1F Stairs:** Located in the fenced-in room at `(22, 2)` on 1F, leading to B1F at `(18, 4)`.
- **Secret Key Location (B1F):** Located on the ground at `(1, 4)` on B1F. (NOT YET RETRIEVED - BAG WAS FULL!).
- **Mansion Diary (2F):** Found on a table at `(5, 12)` on 2F, reads: "Diary: Feb. 6. MEW gave birth to MEWTWO. We named the newborn MEWTWO."
- **Calcium Location (2F):** Located on the ground at `(2, 16)` on 2F.
- **Burgled Trainer:** Defeated a Burglar trainer at `(5, 11)` on 2F.
## Empirical Wall/Collision Testing & Mechanics (Verified Turns 46674-46726)
- **2F Pit West Wall Borders:** Attempted to step Right into the pits at `(23, 7)` on Turn 46674 and `(23, 6)` on Turn 46676 from `(22, 7)` and `(22, 6)`. The player bumped and did not fall, proving that the western edges of the 2F pits act as solid walls. You cannot jump off 2F into these pits; falling to 1F's fenced room must be done by jumping from 3F.
- **2F-to-3F Staircase Warp:** Stepping onto the stairs at `(5, 10)` on 2F (previously misidentified in some notes as `(5, 1)`) warps the player directly to 3F at `(5, 11)`.

## 3F Empirical Ledge & Collision Log (Verified Turns 46838-46887)
- **Railing Collisions (Solid Barriers):**
  - **(23, 6) & (23, 7)** - Bumped on Turn 46838 from `(22, 6)` & `(22, 7)`. Western railing of eastern pit is solid.
  - **(22, 5)** - Bumped on Turn 46839 from `(22, 6)`. Northern railing of western balcony is solid.
  - **(22, 8)** - Bumped on Turn 46841 from `(22, 7)`. Southern railing of western balcony is solid.
  - **(24, 4)** - Bumped on Turn 46859 from `(24, 3)`. Northern railing of central pit is solid.
  - **(28, 3)** - Bumped on Turn 46868 from `(27, 3)`. Eastern railing of central pit is solid.
  - **(28, 7)** - Bumped on Turn 46870 from `(28, 6)`. Southern railing is solid.
  - **(14, 12)** - Bumped on Turn 46887 from `(13, 12)`. Eastern railing of western pit is solid.
  - **(21, 5)** - Bumped on Turn 46949 from `(21, 6)`. Shutter gate is CLOSED in State B, blocking access to the northern section of 3F.
- **Walkable Open Ledge Entrance:**
  - The open pit entrance is on row 11 at columns 16, 17, and 18. This section has no horizontal railing, enabling the player to walk south from row 11 onto row 12 rubble and safely fall to 2F.
