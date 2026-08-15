import os

def main():
    print("Pruning obsolete and unused files from sandbox...")
    obsolete_files = [
        "flee_battle.py",
        "cleanup_and_verify.py",
        "get_teeth_from_18_24.py",
        "get_teeth_ultimate.py",
        "verify_teeth.py",
        "find_safari_gap.py",
        "find_safari_gap_east.py",
        "run_to_plateau_north.py",
        "run_to_safari_area3_prep.py",
        "buy_ticket_and_enter.py",
        "talk_to_clerk.py"
    ]
    
    for filename in obsolete_files:
        if os.path.exists(filename):
            print(f"Deleting obsolete script: {filename}")
            os.remove(filename)
        else:
            print(f"File already deleted or not found: {filename}")
            
    # Also delete any .pyc compiled files inside __pycache__ if they exist
    pycache_dir = "__pycache__"
    if os.path.exists(pycache_dir):
        print(f"Cleaning compile cache inside: {pycache_dir}")
        for filename in os.listdir(pycache_dir):
            file_path = os.path.join(pycache_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Compile cache cleaned.")
        
if __name__ == "__main__":
    main()
