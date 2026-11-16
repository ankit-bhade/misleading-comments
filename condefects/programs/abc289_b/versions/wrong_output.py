# Example: input '10 1\n9' prints 1 2 3 4 5 6 7 8 9 10
N, M = map(int, input().split())
p = list(map(int, input().split())) if M > 0 else []

graph = ""
for i in range(1, N+1):
    node = str(i)
    graph += node + ("v" if i in p else ",")

result = []
for subgraph in graph.split(","):
    result += sorted(subgraph.split("v"), reverse=True)

print(*result)
