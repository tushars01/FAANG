def height_of_tree(root):
    if root == None:
        return 0
    lh = height_of_tree(root.left)
    rh = height_of_tree(root.right)
    return 1 + max(lh, rh)


class Tree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
