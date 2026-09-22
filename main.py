from robot_simulation import (
    MainRobot,
    ScoutRobot,
    VerifierRobot
)

from coordination import Coordinator

from dashboard import show_dashboard


print("\n")
print("=" * 50)
print("     MULTI-ROBOT SEARCH & RESCUE SYSTEM")
print("=" * 50)


# --------------------------------
# INITIALIZE ROBOTS
# --------------------------------

main_robot = MainRobot()
scout = ScoutRobot()
verifier = VerifierRobot()

coordinator = Coordinator()


# --------------------------------
# STEP 1: MAIN ROBOT
# --------------------------------

main_robot.explore()

detection = main_robot.detect()


# --------------------------------
# STEP 2: CREATE TASK
# --------------------------------

task = coordinator.create_detection_task(
    detection
)


# --------------------------------
# STEP 3: DISPATCH SCOUT
# --------------------------------

coordinator.dispatch_scout(task)

scout_result = scout.investigate(
    detection["location"]
)


# --------------------------------
# STEP 4: DISPATCH VERIFIER
# --------------------------------

if scout_result["result"] == "POSSIBLE_HUMAN":

    coordinator.dispatch_verifier(task)

    verifier_result = verifier.verify(
        detection["location"]
    )

else:

    verifier_result = {
        "result": "NOT_REQUIRED"
    }


# --------------------------------
# STEP 5: COMPLETE TASK
# --------------------------------

if verifier_result["result"] == "VERIFIED":

    coordinator.complete_task(task)


# --------------------------------
# STEP 6: DASHBOARD
# --------------------------------

show_dashboard(
    detection,
    task,
    scout_result,
    verifier_result
)
