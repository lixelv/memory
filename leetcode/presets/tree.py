class Tree:
    def __init__(self, value, roots=None):
        self.value = value
        self.roots = roots or []

    def __getitem__(*args):
        self = args[0]

        if (
            len(args) == 2
            and hasattr(args[1], "__iter__")
            and not isinstance(args[1], (str, bytes))
        ):
            iterator = iter(args[1])
        elif len(args) > 1:
            iterator = iter(args[1:])

        current = self

        for i in iterator:
            current = current.roots[i] if isinstance(current, Tree) else None

        return current

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.roots[index] = value

        current = self

        for i in iterator:
            current = current.roots[i] if isinstance(current, Tree) else None

        return current

    def __iter__(self):
        return iter(self.roots)

    def __repr__(self):
        def _build_tree_string(node, prefix, is_last, is_root=False):
            builder = ""
            if not is_root:
                builder += prefix
                builder += "└───" if is_last else "├───"
                builder += repr(node.value) + "\n"
                prefix += "    " if is_last else "│   "
            else:
                builder += repr(node.value) + "\n"

            for i, root in enumerate(node.roots):
                is_last_child = i == len(node.roots) - 1
                builder += _build_tree_string(root, prefix, is_last_child)

            return builder

        return (
            "\n" + _build_tree_string(self, "", True, is_root=True)[:-2]
            if self.roots != []
            else repr(self.value)
        )


a = Tree(
    3,
    [
        Tree(100, [Tree(10, [Tree(":s"), Tree("snake")])]),
        Tree(200, [Tree("hello world")]),
        Tree(545),
        Tree("UWU"),
        Tree("Fuck"),
    ],
)

a[0, 0, 0] = Tree("Hay, yo nigga, uga buga")

print(a)
