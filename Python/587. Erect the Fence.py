import math 

class Solution:

    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:

        def get_bottom_left_tree(trees:list[list[int]]) -> list[int]:
            '''
            Gives the tree located on bottom and
            if there are multiple options,
            return the leftmost bottom tree.
            '''
            coor_min:list[int] = trees[0]
            for coor in trees[1:]:
                # Accept if (< min_y) or (== min_y and < min_x)
                if (coor[1] < coor_min[1]) or (coor[1] == coor_min[1] and coor[0] < coor_min[0]):
                    coor_min = coor
            return coor_min
        
        def get_quadrants(ref_tree:list[int], trees:list[list[int]]) -> list[list[list[int]]]:
            '''
            Divide remaining trees into fourth quadrants, from the POV of the reference tree.
            '''
            trees = [coor for coor in trees if not (coor[0] == ref_tree[0] and coor[1] == ref_tree[1])] # Remove Reference Tree from all trees 
            first_quadrant:list[list[int]] = [coor for coor in trees if (coor[0] > ref_tree[0] and coor[1] >= ref_tree[1])] # To the Right (exclusive) + To the Top (inclusive)
            second_quadrant:list[list[int]] = [coor for coor in trees if (coor[0] <= ref_tree[0] and coor[1] > ref_tree[1])] # To the Left (inclusive) + To the Top (exclusive)
            third_quadrant:list[list[int]] = [coor for coor in trees if (coor[0] < ref_tree[0] and coor[1] <= ref_tree[1])] # To the Left (exclusive) + To the Bottom (inclusive)
            fourth_quadrant:list[list[int]] = [coor for coor in trees if (coor[0] >= ref_tree[0] and coor[1] < ref_tree[1])] # To the Right (inclusive) + To the Bottom (exclusive)
            return [first_quadrant, second_quadrant, third_quadrant, fourth_quadrant]

        def get_first_available_quadrant(ref_quadrant:int, quadrants:list[list[list[int]]]) -> list[list[int]]:
            '''
            From all four quadrants, returns the first quadrant with at least 1 point
            '''
            for i in range(len(quadrants)):
                i = (i+ref_quadrant-1)%4
                if quadrants[i]:
                    return i+1, quadrants[i]
        
        def get_perimeter_trees(ref_tree:list[int], selected_quadrant:list[list[int]]) -> list[int]:
            '''
            Calculate the smallest gradient from the reference point and
            return a list of all trees with that gradient.
            '''

            def divide(num:int, denom:int) -> float:
                return (num/denom if denom != 0 else -math.inf)

            gradients:list[float] = [divide(coor[1]-ref_tree[1],coor[0]-ref_tree[0]) for coor in selected_quadrant]
            gradient_min:float = min(gradients)
            gradient_min_idxs = [i for i,v in enumerate(gradients) if v == gradient_min]
            return [selected_quadrant[idx] for idx in gradient_min_idxs]

        def get_next_tree(ref_tree:list[int], perimeter_trees:list[list[int]]):
            '''
            Used for tiebreaking.
            Returns the furthest trees from the perimeter trees in focus, using Manhattan distance.
            '''
            if len(perimeter_trees) == 1:
                return perimeter_trees[0]

            distances:list[int]  = [(abs(coor[1]-ref_tree[1]) + abs(coor[0]-ref_tree[0])) for coor in perimeter_trees]
            distances_max:int = max(distances)
            distances_max_idx = distances.index(distances_max)
            return perimeter_trees[distances_max_idx]

        def add(trees, res):
            '''
            Used to remove duplicates from list of tree coordinates.
            '''
            [res.append(x) for x in trees if x not in res]         

        if len(trees) == 1:
            # Edge Case: Only 1 tree.
            return trees

        start_tree:list[int] = get_bottom_left_tree(trees)
        perimeter_trees:list[list[int]] = [start_tree]
        ref_tree:list[int] = start_tree
        ref_quadrant:int = 1
        while True: # This is the maximum number of tries to build a parameter
            quadrants:list[list[list[int]]] = get_quadrants(ref_tree, trees)
            ref_quadrant, selected_quadrant = get_first_available_quadrant(ref_quadrant, quadrants)
            curr_perimeter_trees:list[int] = get_perimeter_trees(ref_tree, selected_quadrant)
            add(curr_perimeter_trees, perimeter_trees)
            next_tree:list[int] = get_next_tree(ref_tree, curr_perimeter_trees)
            ref_tree = next_tree
            if next_tree == start_tree:
                break
        return perimeter_trees

trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(Solution().outerTrees(trees))
