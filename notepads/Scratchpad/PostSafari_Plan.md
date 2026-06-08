# Post-Safari Zone Route & Progression Plan (Turn 73831)

## Location Correction:
- Map 0_158 is the Fuchsia Meeting Room (Safari Zone Bureau), NOT the Warden's House!
- The NPC at (10, 1) is a staff member.
- The NPC at (0, 2) is the Warden's pet Slowpoke.
- The NPC at (4, 1) is the youngster/Slowpoke.
- The real Warden's House is Map 0_157, located in the south-eastern part of Fuchsia City.

## Plan:
1. Exit Fuchsia Meeting Room (Map 0_158) from (4, 7).
2. Walk to the south-eastern houses in Fuchsia City to find Map 0_157 (Warden's House).
3. Enter Warden's House (Map 0_157).
4. Talk to the Warden (the real Warden!) to deliver his Gold Teeth and receive HM04 Strength.
5. Teach Strength to ROCKY (GEODUDE).

## Socratic Verification Plan (Turn 73867):
- **Finding the Real Warden's House**: We will walk Down along Column 24 to find the fence opening, walk Right, and then stand at (27, 29) to read the overworld signpost. The signpost should confirm it is the Warden's House.
- **Resolving the Map 0_157 Gym vs. House Conflict**: Once we enter the Warden's House, we will immediately look at the `<Location><Map>` game state field to verify its true map ID and correct any discrepancies in our permanent regional notepads.

- Turn 73899: Signpost at (27, 29) successfully read. It says "SAFARI ZONE WARDEN'S HOME"! This empirically proves that the left building with the door at (27, 27) is indeed the real Warden's House. We will now dismiss the text box, step UP into the building, and identify its map ID to resolve our regional map conflict.