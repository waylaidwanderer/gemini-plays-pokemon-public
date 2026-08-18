# Saffron City Gym - 3x3 Warp Room Matrix & Navigation Guide

## Overview
Saffron City Gym features a 3x3 grid of rooms separated by solid walls, connected via teleporter warp pads in the corners.
To reach Sabrina from the entrance room, the golden rule is the **TR / BL alternating opposite rule**:
- If you land on a **Top-Right (TR)** pad, take the **Bottom-Left (BL)** pad in that room.
- If you land on a **Bottom-Left (BL)** pad, take the **Top-Right (TR)** pad in that room.
- Alternating this sequence (TR -> BL -> TR -> BL) avoids loops and leads directly to Sabrina in the center room.

## Map Layout & Verified Room Warp Matrix

### 1. Entrance Room (S Room, Bottom-Center)
- **Starting Coordinates:** `(8, 17)`
- **Gym Guide:** Located in this room near the statues.
- **Accessible Warp Pad:** `(11, 15)` (BL)
- **Transition:** Stepping on `(11, 15)` warps the player to `(11, 15)` inside the SE Room.

### 2. SE Room (Bottom-Right, Room 1)
- **Warp Pads:**
  - TL: `(15, 11)`
  - TR: `(19, 11)` - **Target Warp Pad** (alternating rule step 1)
  - BL: `(15, 15)`
  - BR: `(19, 15)`
- **Trainer:** Psychic at `(17, 14)` (Defeated on Turn 45684. Had Slowpoke Lv33 and Slowbro Lv33).
- **Transition:** Stepping on TR `(19, 11)` warps the player to `(19, 13)` inside the E Room.

### 3. E Room (Middle-Right, Room 2)
- **Warp Pads:**
  - TL: `(15, 11)`
  - TR: `(19, 11)`
  - BL: `(15, 15)` - **Target Warp Pad** (alternating rule step 2)
  - BR: `(19, 15)`
- **Transition:** Stepping on BL `(15, 15)` warps the player to `(19, 3)` inside the NE Room.

### 4. NE Room (Top-Right, Room 3)
- **Arrival Position:** Landed on TR pad at `(19, 3)`.
- **Warp Pads:**
  - TL: `(15, 3)`
  - TR: `(19, 3)`
  - BL: `(15, 5)` - **Target Warp Pad** (alternating rule step 3)
  - BR: `(19, 5)`
- **Trainer:** Psychic at `(17, 2)` (Currently battling on Turn 45692. Has Kadabra Lv31).