import itertools

class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        # Step 1: Create the smallest box
        top_trees = [trees[0]]
        bot_trees = [trees[0]]
        right_trees = [trees[0]]
        left_trees = [trees[0]]

        for tree in trees[1:]:

            if (tree[1] >= top_trees[0][1]):
                if (tree[1] == top_trees[0][1]):
                    # Add to list
                    top_trees.append(tree)
                else:
                    top_trees = [tree]
            
            if (tree[1] <= bot_trees[0][1]):
                if (tree[1] == bot_trees[0][1]):
                    # Add to list
                    bot_trees.append(tree)
                else:
                    bot_trees = [tree]

            if (tree[0] >= right_trees[0][0]):
                if (tree[0] == right_trees[0][0]):
                    # Add to list
                    right_trees.append(tree)
                else:
                    right_trees = [tree]

            if (tree[0] <= left_trees[0][0]):
                if (tree[0] == left_trees[0][0]):
                    # Add to list
                    left_trees.append(tree)
                else:
                    left_trees = [tree]
        
        # Step 2: Identity all trees at each side of the box.
        #print(f"Left Trees: {left_trees}, Right Trees: {right_trees}, Top Trees: {top_trees}, Bot Trees: {bot_trees}")
        left_trees = sorted(left_trees)
        right_trees = sorted(right_trees)
        top_trees = sorted(top_trees)
        bot_trees = sorted(bot_trees)

        # Step 3: Draw 4 lines.

        #top_right
        pt1 = top_trees[-1]
        pt2 = right_trees[-1]
        a1 = pt2[1] - pt1[1]
        b1 = pt1[0] - pt2[0]
        c1 = a1*pt1[0] + b1*pt1[1]
        top_right_diag = lambda x: (a1*x[0]+b1*x[1]==c1)

        #right_bot
        pt1 = right_trees[0]
        pt2 = bot_trees[-1]
        a2 = pt2[1] - pt1[1]
        b2 = pt1[0] - pt2[0]
        c2 = a2*pt1[0] + b2*pt1[1]
        right_bot_diag = lambda x: (a2*x[0]+b2*x[1]==c2)

        #bot_left
        pt1 = bot_trees[0]
        pt2 = left_trees[0]
        a3 = pt2[1] - pt1[1]
        b3 = pt1[0] - pt2[0]
        c3 = a3*pt1[0] + b3*pt1[1]
        bot_left_diag = lambda x: (a3*x[0]+b3*x[1]==c3)

        #left_top
        pt1 = left_trees[-1]
        pt2 = top_trees[0]
        a4 = pt2[1] - pt1[1]
        b4 = pt1[0] - pt2[0]
        c4 = a4*pt1[0] + b4*pt1[1]
        left_top_diag = lambda x: (a4*x[0]+b4*x[1]==c4)

        # Step 4: Check if any other points lies on the 8 lines
        boundary = top_trees + bot_trees + left_trees + right_trees
        rest = [x for x in trees if x not in boundary]
        boundary_test = lambda x: top_right_diag(x) or right_bot_diag(x) or bot_left_diag(x) or left_top_diag(x)
        for tree in rest:
            if boundary_test(tree):
                boundary.append(tree)
        
        boundary.sort()
        return list(boundary for boundary,_ in itertools.groupby(boundary))

points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(Solution().outerTrees(points))
