def main():
    processes = int(input("number of processes : "))
    resources = int(input("number of types of resources : "))
    max_resources = [int(i) for i in input("maximum no of resources of each type : ").split()]

    print("\n-- allocated resources for each process --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    print("\n-- maximum resources for each process --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\ntotal allocated resources : {allocated}\n")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"total available resources : {available}\n")
    process_order = []
    number = 0
    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} is executing")
                    number = i+1
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("Deadlock occurred.")
            break
        process_order.append(number)
        print(f"No Deadlock occurred.\navailable resources after executing process {i+1} : {available}\n")
    for i in range(len(process_order)):
        print('process', process_order[i], end='->'if i != len(process_order) - 1 else " ")


if __name__ == '__main__':
    main()
