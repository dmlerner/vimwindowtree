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
        # NOTE: adding a window decreases total width availbale by 1, cause vim...
        # vary by settings re: visible white bar between windows?
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

    def get_siblings(self):
        return list(filter(lambda x: x is not self, self.parent.children))

    def window_size(self, orientation):
        # TODO does this work with mutating?
        assert not self.is_container()
        return { HORIZONTAL: self.window.width, VERTICAL: self.window.height }[orientation]

    def set_size(self, orientation):
        assert not self.is_container()

    def total_size(self, orientation):
        if self.is_container():
            return sum(child.total_size(orientation) for child in self.children)
        return self.window_size(orientation)

    def resize_relative(self, delta, orientation):
        self.resize_absolute(delta * self.size(orientation), orientation)

    def resize_absolute(self, delta, orientation):
        ''' Increase the size of this window, or the total size of all its children, by delta, by decreasing the size of its siblings. '''

        total_sibling_size_before = sum(wn.total_size() for wn in self.get_siblings())
        assert not self.is_container() # TODO
        for child in self.parent.children:
            # TODO: do I need to do siblings before me, then me, then those after me?
            # re: vim handling temporary excess size...
            # just go left to right and it should be fine
            sibling.resize_absolute(sibling.total_size()/total_sibling_size_before * delta, orientation)

