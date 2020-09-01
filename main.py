class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return f"The node {self.val} has left {left} and right {right}"

def construct_tree(list):
    forest = [Tree(x) for x in list]
    root = forest[0]
    for tree in range(1, len(forest)):
        found = False
        parent = root
        while not found:
            if forest[tree].val < parent.val:
                if not parent.left:
                    parent.left = forest[tree]
                    found = True
                else:
                    parent = parent.left
            elif forest[tree].val > parent.val:
                if not parent.right:
                    parent.right = forest[tree]
                    found = True
                else:
                    parent = parent.right
    print(forest)

def main():
    construct_tree([5,4,2,9,11,1,6])


if __name__ == '__main__':
    main()
