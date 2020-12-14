class WindowNode:

    vim = None
    HORIZONTAL = 'HORIZONTAL'
    VERTICAL = 'VERTICAL'

    def __init__(self, window=None):
        self.window = window
        self.children = []

    def orientation_size(self, orientation=WindowNode.HORIZONTAL):

    def is_container(self):
        assert bool(self.window) ^ bool(self.children)
        return not bool(self.window)

    def add(self, node, orientation=WindowNode.HORIZONTAL):
        if self.is_container():
            sizes = { c: c.size() for c in self }
            total_size = sum(sizes.values())
            new_window_size = total_size / (len(self) + 1)
            old_node_size_scale_factor = (total_size - new_window_size) / total_size
            for c in self:
                if orientation == WindowNode.HORIZONTAL:
            # existing nodes should have same size relative to each other before and after adding
            # new node should hav same size as average node after
            node.parent = self
            self.children.append(node)
        else:
            container = WindowNode()
            container.add(self)
            container.add(node)

    def __iter__(self):
        return iter(self.children)

    def size(self, orientation):
        if self.is_container():
            return sum(c.size(orientation) for c in self)
        return lambda node: getattr(node, orientation){ HORIZONTAL: self.window.width, VERTICAL: self.window.height }[orientation]
