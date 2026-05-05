# Pokemon Mansion Navigation & Floor Testing Log
- Overwatch Agent identified a flaw: I assumed hitting a wall at (5, 27) meant I was on B1F, which caused me to constantly flip my floor hypothesis. A wall at y=27 does not prove the floor.
- Goal: Definitively prove current floor by triggering the stairs in the South-East and observing the System Map Transition message.
- Test Plan: Navigate from current position to the stairs. I will test both (23, 21) and (21, 23) to see which one triggers the warp, and record the [Previous Map] -> [New Map] coordinates permanently.