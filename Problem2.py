def tower_of_hanoi(n, source, target, auxiliary):
    """Recursive function to solve Tower of Hanoi puzzle."""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Main program
while True:
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            print("Error: Number of disks must be a positive integer.")
            continue

        print(f"\nSolution for {n} disks:")
        tower_of_hanoi(n, 'A', 'C', 'B')
        break

    except ValueError:
        print("Invalid input. Please enter an integer.")