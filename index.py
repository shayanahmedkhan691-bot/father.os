import time
import sys

# Simulation of a "Robotic System" booting up for a Legend
def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def celebrate():
    # 1. Robotic Boot Sequence
    print("[ SYSTEM CHECK: INITIATING FATHER_OS ]")
    time.sleep(0.5)
    typing_effect("> Loading Wisdom Modules... [100%]")
    typing_effect("> Calibrating Patience Sensors... [100%]")
    typing_effect("> Initializing GOAT_Protocol... [100%]")
    print("-" * 40)

    # 2. Robotics/AI Illustrative Art
    print("""
          _____
         |     |    [ HAPPY BIRTHDAY DAD! ]
    _____|_____|_____

    // \\
    || () () || <-- Your AI Son's
    || --- || Creation
    \_______//
     ---------
    |||
    //\\
    """)

    # 3. The "Coding Logic" Heart of the Message
    print("-" * 40)
    typing_effect(">>> EXECUTING BIRTHDAY_LOGIC.py")

    message = """
if father == "The Best":
    status = "Legendary"
    celebration = "Required"
    love = float('inf')  # Infinite Love

print(f"Happy Birthday to the man who built my foundation!")
    """
    print(f"\033[1;32m{message}\033[0m") # Prints in Green like a terminal

    # 4. The Personal Touch
    print("-" * 40)
    typing_effect("Dear Dad,", 0.05)
    typing_effect("On your special day (Feb 16), I wanted to show you", 0.04)
    typing_effect("that all the hard work I put into my 52+ achievements,", 0.04)
    typing_effect("my 1560 SAT, and my Rank 126 coding today...", 0.04)
    typing_effect("is all inspired by YOU. You are the real MVP.", 0.06)

    print("\n [ ERROR: HEART OVERFLOW ] ")
    print(" [ STATUS: BEST DAD IN THE WORLD ] ")
    print("-" * 40)

if __name__ == "__main__":
    celebrate()
