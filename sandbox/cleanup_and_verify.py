import os
import shutil

def main():
    print("Performing workspace cleanup and updating locations guide...")
    
    # Paths to delete
    redundant_paths = [
        "notepads/notepads",  # directory
        "notepads/Locations/FuchsiaGym",
        "notepads/Locations/SafariZone",
        "notepads/Scratchpad/SafariZone_Route",
        "Scratchpad/SafariZone_Route"
    ]
    
    for path in redundant_paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                print(f"Removing directory: {path}")
                shutil.rmtree(path)
            else:
                print(f"Removing file: {path}")
                os.remove(path)
        else:
            print(f"Path not found (already deleted or wrong path): {path}")
            
    # Edit Locations/SafariZone.md to document empirical proof of teeth retrieval
    safari_zone_md_path = "notepads/Locations/SafariZone.md"
    if os.path.exists(safari_zone_md_path):
        with open(safari_zone_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_text = "- **Gold Teeth:** Located at `(19, 25)` on the southern ground level. The overworld item ball is physically present and solid, and can be retrieved by standing at `(19, 24)` facing DOWN and pressing A."
        new_text = "- **Gold Teeth:** Located at `(19, 25)` on the southern ground level. Empirically proven on Turn 40356 that standing at `(19, 24)` facing DOWN and pressing A successfully retrieves the Gold Teeth, removing the overworld item ball."
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            with open(safari_zone_md_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully updated Locations/SafariZone.md with Turn 40356 proof.")
        else:
            print("Did not find target text in Locations/SafariZone.md. Appending proof to landmarks section...")
            # If target text isn't found exactly, we append/insert it safely
            content = content.replace("### 🔍 Verified Area 3 (West) Landmarks & Paths", "### 🔍 Verified Area 3 (West) Landmarks & Paths\n- **Gold Teeth:** Located at `(19, 25)` on the southern ground level. Empirically proven on Turn 40356 that standing at `(19, 24)` facing DOWN and pressing A successfully retrieves the Gold Teeth.")
            with open(safari_zone_md_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully appended proof to Locations/SafariZone.md.")
    else:
        print(f"File not found: {safari_zone_md_path}")

if __name__ == "__main__":
    main()
