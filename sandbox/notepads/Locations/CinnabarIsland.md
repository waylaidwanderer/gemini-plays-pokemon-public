# Cinnabar Island - Overworld Landmarks & Map Warps

## Verified Coordinates & Warps
- **Pok&eacute;mon Center:** Entrance door is at `(11, 12)`.
- **Pok&eacute; Mart:** Entrance door is at `(15, 12)`.
- **Cinnabar Lab Lobby (Middle Door):** Entrance door is at `(12, 4)` on Cinnabar Island. Inside, the exit is at `(2, 7)` or `(3, 7)` which warps the player back outside to `(12, 5)`.
- **Cinnabar Lab Room 1 (Left Door):** Entrance door is at `(1, 4)` on Cinnabar Island. Inside, the exit is at `(2, 7)` which warps the player back outside to `(1, 5)`.
- **Cinnabar Lab Room 3 (Right Door):** Entrance door is at `(16, 4)` on Cinnabar Island. Inside, the exit is at `(2, 7)` which warps the player back outside to `(16, 5)`.
- **Pok&eacute;mon Mansion Entrance:** Stand at `(6, 4)` and step UP into the door at `(6, 3)` to enter `Pokemon Mansion 1F West` (landing at `(5, 27)`).
- **Cinnabar Gym:** Entrance door is at `(18, 4)`. Permanently locked until the Secret Key is obtained from the Mansion.

## Navigation Routes
- **Master Route to Mansion Entrance:** Walk from Cinnabar Island `(11, 12) -> (18, 12) -> (18, 4) -> (6, 4) -> (6, 3)` and step UP to enter.

## CRITICAL WARNINGS FOR NAVIGATION
- **Cinnabar Lab Room 1 (Left Door) is at (1, 4):** This is far to the left of the Mansion entrance at `(6, 3)`. Under NO circumstances should navigation scripts walk further left than Column 6 on Row 4 or 5 when heading to the Mansion. Doing so will accidentally trigger the door warp and enter the Lab, resulting in getting stuck due to the NPC blocking the vertical return path.
- **Door Warp Collision Quirk:** In Gen 1, walking horizontally onto a warp tile (like `(2, 7)` inside Lab Room 1) does NOT trigger the warp. It must be entered vertically. Since the vertical path to `(2, 7)` is permanently blocked by the Scientist at `(2, 6)`, walking into Lab Room 1 is a physical trap that requires resetting or using another method!


## Pok&eacute;mon Mansion Structural Discoveries
- **3F West Pitfall Trap at (5, 9):** Stepping on this tile immediately warps the player down to 2F West at (5, 10) (discovered on Turn 55204). Avoid walking UP to Row 9 Column 5 on 3F West in both State A and State B!
