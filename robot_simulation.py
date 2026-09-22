import time


class MainRobot:

    def __init__(self):
        self.name = "MAIN_ROBOT"

    def explore(self):
        print("\n[MAIN ROBOT] Exploring environment...")
        time.sleep(1)

    def detect(self):
        print("[MAIN ROBOT] Thermal signature detected!")

        detection = {
            "robot": self.name,
            "location": (12.4, 8.7),
            "confidence": 0.87
        }

        print(f"[MAIN ROBOT] Location: {detection['location']}")
        print(f"[MAIN ROBOT] Confidence: {detection['confidence']}")

        return detection


class ScoutRobot:

    def __init__(self):
        self.name = "SCOUT_1"

    def investigate(self, location):

        print(f"\n[SCOUT 1] Moving to {location}...")
        time.sleep(1)

        print("[SCOUT 1] Entering narrow-access area...")
        time.sleep(1)

        print("[SCOUT 1] Possible human presence detected.")

        return {
            "robot": self.name,
            "location": location,
            "result": "POSSIBLE_HUMAN"
        }


class VerifierRobot:

    def __init__(self):
        self.name = "VERIFIER_2"

    def verify(self, location):

        print(f"\n[VERIFIER 2] Moving to {location}...")
        time.sleep(1)

        print("[VERIFIER 2] Performing close-range verification...")
        time.sleep(1)

        print("[VERIFIER 2] Human presence verified.")

        return {
            "robot": self.name,
            "location": location,
            "result": "VERIFIED"
        }
