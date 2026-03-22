import sys


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.children.append(child)

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, depth, path):
    """
    Поиск с ограничением глубины с сохранением пути.
    """
    if node is None:
        return None

    path.append(node.value)

    if node.value == goal:
        return path

    if depth == 0:
        path.pop()
        return "cutoff"

    cutoff_occurred = False

    for child in node.children:
        result = depth_limited_search(child, goal, depth - 1, path.copy())

        if isinstance(result, list):  # Нашли цель
            return result
        elif result == "cutoff":
            cutoff_occurred = True

    path.pop()

    return "cutoff" if cutoff_occurred else None


def iterative_deepening_search_filesystem(root, goal):
    """
    Поиск с итеративным углублением в файловой системе.
    """
    if root is None:
        return None

    for depth in range(sys.maxsize):
        result = depth_limited_search(root, goal, depth, [])

        if isinstance(result, list):
            return result
        elif result is None:
            return None

    return None


if __name__ == "__main__":
    root = TreeNode("dir1")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))

    goal = "file5"

    print(f"Поиск в файловой системе с goal = '{goal}'")

    result = iterative_deepening_search_filesystem(root, goal)

    if result:
        print(" -> ".join(result))
    else:
        print(f"Цель '{goal}' не найдена в файловой системе")
