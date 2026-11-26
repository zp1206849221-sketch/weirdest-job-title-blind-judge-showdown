import os

TITLE = "Senior Specialist, Telling People They're on Mute"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
