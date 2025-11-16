import os

project_files = [
    "main.py",
    "gmail_reader.py",
    "groq_classifier.py",
    "linear_client.py",
    "requirements.txt",
    ".env"
]

def create_structure():
    print("📁 Creating empty project structure...")

    for file in project_files:
        if not os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                pass
            print(f"   ✓ Created: {file}")
        else:
            print(f"   ⏭ Already exists, skipped: {file}")

    print("\n🎉 Project structure created successfully!")
    

if __name__ == "__main__":
    create_structure()
