def tower_of_hanoi(n, source, destination, auxiliary):
    # Base Case: If there's only 1 disk, move it directly
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to auxiliary rod
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    # Step 2: Move the nth (largest) disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move the n-1 disks from auxiliary back to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# --- Execution ---
n_disks = int(input("Enter the number of disks: "))
print(f"\nSteps to solve Tower of Hanoi with {n_disks} disks:")
tower_of_hanoi(n_disks, 'A', 'C', 'B')