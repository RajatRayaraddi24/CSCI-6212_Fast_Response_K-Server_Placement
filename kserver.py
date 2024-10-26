import sys
import time
import random
import matplotlib.pyplot as plt

def cost_with_one_server(weights, i, j):
    total_cost = 0
    for x in range(i, j + 1):
        total_cost += abs(x - (i + j) // 2) * weights[x]
    return total_cost


def optimal_server_placement(weights, n, k):

    dp = [[sys.maxsize] * (k + 1) for _ in range(n)]
    cost_table = [[0] * n for _ in range(n)]
    last_server_position = [[-1] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            cost_table[i][j] = cost_with_one_server(weights, i, j)
    
    for i in range(n):
        dp[i][1] = cost_table[0][i]
        last_server_position[i][1] = 0

    for servers in range(2, k + 1):
        for i in range(n):
            for j in range(i):
                cost = dp[j][servers - 1] + cost_table[j + 1][i]
                if cost < dp[i][servers]:
                    dp[i][servers] = cost
                    last_server_position[i][servers] = j

    locations = []
    i = n - 1
    for servers in range(k, 0, -1):
        locations.append(last_server_position[i][servers])
        i = last_server_position[i][servers]

    locations.reverse()

    return dp[n - 1][k], locations

# ns = [100]
# ks = [5]
# x = [range(1,101,1)]
# y = [[5]*100]
# z = [[5]*5]

ns = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
ks = [5, 6, 7, 8, 9, 10]
results = []

for n in ns:
    weights = [(random.uniform(0, 50)) for _ in range(n)]
    for k in ks:
        start_time = time.perf_counter_ns()
        min_cost, server_locations = optimal_server_placement(weights, n, k)
        elapsed_time = time.perf_counter_ns() - start_time
        results.append((n, k, elapsed_time))
        print(f"n = {n}, k = {k}, Time = {elapsed_time} ns")
        print("Minimum total traffic cost with {} servers and {} clients: {}".format(k, n, min_cost))
        print("Optimal server locations (client indices):", server_locations,"\n")

    # plt.figure(figsize=(14, 7))
    # plt.scatter(x, y, marker = 'x', color='blue', label='Clients in the network')
    # plt.scatter(server_locations, z, color='red', marker='o', label='Optimal server locations')
    # plt.title('Clients and Optimal Server Locations (Visualization)')
    # plt.xlabel('Clients (n)')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

n_values = sorted(list(set([res[0] for res in results])))
k_values = sorted(list(set([res[1] for res in results])))

plt.figure(figsize=(14, 7))

for k in k_values:
        times = [res[2] for res in results if res[1] == k]
        plt.plot(n_values, times, label=f'k={k}')

plt.xlabel('n (Number of Clients)')
plt.ylabel('Time (nanoseconds)')
plt.title('Execution Time vs n for varying k values')
plt.legend()
plt.grid(True)
plt.show()
