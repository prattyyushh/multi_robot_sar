def show_dashboard(
    detection,
    task,
    scout_result,
    verifier_result
):

    print("\n")
    print("=" * 50)
    print("       SEARCH & RESCUE DASHBOARD")
    print("=" * 50)

    print("\nMAIN ROBOT")
    print("-------------------------")

    print("Status: ACTIVE")

    print(
        f"Detection Location: "
        f"{detection['location']}"
    )

    print(
        f"Confidence: "
        f"{detection['confidence']}"
    )

    print("\nTASK")
    print("-------------------------")

    print(f"Task ID: {task.task_id}")
    print(f"Priority: {task.priority}")
    print(f"Status: {task.status}")

    print("\nSCOUT 1")
    print("-------------------------")

    print(
        f"Result: "
        f"{scout_result['result']}"
    )

    print("\nVERIFIER 2")
    print("-------------------------")

    print(
        f"Result: "
        f"{verifier_result['result']}"
    )

    print("\nFINAL SYSTEM STATUS")
    print("-------------------------")

    if verifier_result["result"] == "VERIFIED":

        print("VICTIM DETECTION VERIFIED")
        print("RESCUE TASK COMPLETED")

    print("=" * 50)
