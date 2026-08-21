import os

notepads = [
    "Locations/PalletTown_And_Route1",
    "Locations/ViridianCity",
    "Locations/PewterCity",
    "Locations/Route3",
    "Locations/Route4",
    "Locations/CeruleanCity",
    "Locations/Route24",
    "Locations/Route25",
    "Locations/Route5",
    "Locations/Route6",
    "Locations/VermilionCity",
    "Locations/SSAnne",
    "Locations/Route9",
    "Locations/Route10",
    "Locations/RockTunnel1F",
    "Locations/RockTunnelB1F",
    "Locations/LavenderTown",
    "Locations/Route8",
    "Locations/UndergroundPath_Route7_Route8",
    "Locations/Route7",
    "Locations/CeladonCity",
    "Locations/CeladonGym",
    "Locations/PokemonTower",
    "Locations/Route12",
    "Locations/Route13",
    "Locations/Route14",
    "Locations/Route15",
    "Locations/Route18",
    "Locations/CinnabarIsland",
    "Locations/Route22",
    "Locations/ViridianForest",
    "Locations/Route2",
    "Locations/DiglettsCave",
    "Mechanics/Search_Scripting_Pitfalls",
    "Mechanics/Naming_Screen_Offset",
    "Mechanics/UI_And_Border_Rendering"
]

os.makedirs("notepads/Locations", exist_ok=True)
os.makedirs("notepads/Mechanics", exist_ok=True)

for n in notepads:
    path = f"notepads/{n}.md"
    if not os.path.exists(path):
        print(f"Creating placeholder for {n}...")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {n}\n\nPlaceholder to prevent data loss.\n")

print("All remaining notepad placeholders created successfully!")
