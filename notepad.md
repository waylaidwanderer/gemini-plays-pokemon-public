# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Preparing for Radio Tower.
- **Status:** Accessing PC (Cherrygrove).
- **Reason:** Swapping Togepi for Gyarados.
- **Plan:**
    1. Turn ON PC (Up, A).
    2. Select Bill's PC.
    3. Deposit Togepi.
    4. Withdraw Gyarados.
    5. Fly to Goldenrod.

# Reflection (Turn 11689)
- **Execution:** Fly attempt failed (landed back in New Bark Town). Likely map navigation error or input drop.
- **Lesson:** Verify Fly destination text BEFORE pressing A. Do not batch navigation and confirmation in one turn.
- **Hygiene:** Map markers for PC types (Storage vs Research) helped avoid confusion at Elm's Lab.
- **Strategy:** Pivot to step-by-step Fly navigation.

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Flying to Goldenrod City.
- **Status:** Hard Reset (Syncing State).
- **Reason:** Screen Text ("Fly Map Open") contradicts Screen Image (Overworld). Suspect text is stale/stuck. Forcing a full menu closure to resync bot state with game state.
- **Plan:**
    1. Press B x4 to close all potential menus.
    2. Verify Overworld (No text).
    3. Next Turn: Open Menu and Fly (Start -> Pokemon -> Mistral -> Fly).