vim = None

class WindowNode:

    HORIZONTAL = 'HORIZONTAL'
    VERTICAL = 'VERTICAL'

    def __init__(self, window=None):
        self.window = window
        self.children = []

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
                    pass
            # existing nodes should have same size relative to each other before and after adding
            # new node should hav same size as average node after
            node.parent = self
            self.children.append(node)
        else:
            container = WindowNode()
            container.add(self)
            container.add(node)

    def siblings(self):
        return set(filter(lambda x: x is not self, self.parent.children))

    def window_size(self, orientation):
        # TODO does this work with mutating?
        assert not self.is_container()
        return { HORIZONTAL: self.window.width, VERTICAL: self.window.height }[orientation]

    def total_size(self, orientation):
        if self.is_container():
            return sum(child.total_size(orientation) for child in self.children)
        return self.window_size(orientation)

    def resize_relative(self, delta, orientation):
        self.resize_absolute(delta * self.size(orientation), orientation)

    def resize_absolute(self, delta, orientation):
        ''' Increase the size of this window, or the total size of all its children, by delta, by decreasing the size of its siblings. '''

        total_sibling_size_before = sum(wn.total_size() for wn in self.siblings())
        for wn in self.siblings:

