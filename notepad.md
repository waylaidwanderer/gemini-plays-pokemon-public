# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Flying to Goldenrod City.
- **Status:** Navigating to Violet City (Step 1).
- **Reason:** Map is open. Executing first half of navigation (Left -> Up) to confirm movement and reach Violet City.
- **Plan:**
    1. Send Inputs: Left, Up.
    2. Verify "Violet City" text next turn.
    3. If success, continue: Left -> Down (Goldenrod).
    4. If fail (stuck at New Bark), assume animation lag and retry.

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