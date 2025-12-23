# Goldenrod Underground Switch Puzzle
**Start Turn:** 13507

## Tile Mechanics & Switch Logic
- **Switch 1 (16, 1):** ON (Default). Effect on shutters not fully tested.
- **Switch 2 (10, 1):** OFF.
    - **Effect:** Opens Horizontal Shutter at (12, 8).
- **Switch 3 (2, 1):** ON.
    - **Effect:** Opens Horizontal Shutter at (6, 8).
    - **Hypothesis:** Opens Vertical Shutter at (20, 6).
    - **Effect:** Closes Horizontal Shutter at (6, 12).

## Current Status (Turn 13507)
- **Switch 1:** ON
- **Switch 2:** OFF
- **Switch 3:** ON
- **Shutter (6, 8):** OPEN (Verified)
- **Shutter (12, 8):** OPEN (Verified)
- **Shutter (20, 6):** Expected OPEN

## Objectives & Plan
- **Primary:** Reach Emergency Switch at (20, 11).
- **Secondary:** Rescue Director (Likely via Warp at 22, 10).
- **Navigation Plan:**
    1. Travel East via Row 8 (Shutter at 6,8 and 12,8 are OPEN).
    2. Turn South at Column 20.
    3. Verify Shutter (20, 6) is OPEN.
    4. Activate Emergency Switch (20, 11).
    5. Investigate Warp at (22, 10).

## Learned Lessons
- **Switch 3:** Controls multiple shutters (Row 8, Row 12, Col 20).
- **Input Accuracy:** Verify interactions (Switch ON/OFF) with screen text, not just intent.
- **Map:** Warps and Switches are key. Use markers.