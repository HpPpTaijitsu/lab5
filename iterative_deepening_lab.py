import sys


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, depth):
    """
    Поиск с ограничением глубины.
    """
    if node is None:
        return False

    if node.value == goal:
        return True

    if depth == 0:
        return "cutoff"

    cutoff_occurred = False

    if node.left:
        result = depth_limited_search(node.left, goal, depth - 1)
        if result is True:
            return True
        if result == "cutoff":
            cutoff_occurred = True

    if node.right:
        result = depth_limited_search(node.right, goal, depth - 1)
        if result is True:
            return True
        if result == "cutoff":
            cutoff_occurred = True

    return "cutoff" if cutoff_occurred else False


def iterative_deepening_search_tree(root, goal):
    """
    Поиск с итеративным углублением.
    """
    if root is None:
        return False

    for depth in range(sys.maxsize):
        result = depth_limited_search(root, goal, depth)

        if result is True:
            return True
        elif result is False:
            return False

    return False


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    goal = 6

    print(
        f"Поиск с итеративным углублением для проверки существования "
        f"пользователя с goal = {goal}"
    )

    result = iterative_deepening_search_tree(root, goal)
    print(result)
