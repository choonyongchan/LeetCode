class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # We are given a adjacency list
        # Idea: Conduct DFS until no more paths can be traversed. (ie repeated nodes and edges are accepted)
        
        paths:list[list[int]] = []
        stack:list[list[int]] = [[0]] #Store all path history

        end_node:int = len(graph)-1

        while stack:
            curr_ph:list[int] = stack.pop()
            neighbours:list[int] = graph[curr_ph[-1]]

            for neighbour in neighbours:
                if neighbour == end_node:
                    paths.append(curr_ph + [neighbour])
                else:
                    stack.append(curr_ph + [neighbour])

        return paths

graph = [[4,3,1], [], [], [], []]
print(Solution().allPathsSourceTarget(graph))


        