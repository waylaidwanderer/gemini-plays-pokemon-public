# Pokémon Mansion Switch Permutations & Route Analysis

## Verified Switch States & Mechanics
- All Mewtwo statue switches toggle the global mansion flag between State A (Default) and State B.
- Entering the mansion from outside resets the switches to State A.

## Multi-Floor Shutter State Table
| Floor | Gate / Shutter Location | State A (Default) | State B (Toggled) |
|---|---|---|---|
| 1F | (18..19, 8) Shutter Gate | CLOSED | OPEN |
| 1F | (24..25, 13) Shutter Gate | OPEN | CLOSED |
| 2F | (9, 4..5) Shutter Gate | OPEN | CLOSED |
| 3F | (15, 10..11) Shutter Gate | CLOSED | OPEN |

## Active Progression Route
1. Enter Pokémon Mansion in default State A.
2. Ascend to 2F at (5, 10), navigate to (6, 1) stairs -> ascend to 3F.
3. On 3F, activate Mewtwo statue switch at (10, 5) to toggle to State B (opens 3F (15, 10..11) gate and 1F (18..19, 8) gate).
4. On 3F (State B), pass through open (15, 10..11) gate to the Right Balcony Pit at (19, 14) and drop down to 1F (18, 14).
5. On 1F (State B), walk north through open (18..19, 8) gate into northern hallway.
6. Explore northern hallway (rows 1-7) west towards the 1F Northwest room Mewtwo statue at (2, 5) to toggle back to State A.
7. With State A active, the shutter gate at (24..25, 13) is open; walk south down eastern corridor to locate the true B1F entrance.
