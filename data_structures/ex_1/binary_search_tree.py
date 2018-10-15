class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# RECURSIVE IMPLEMENTATION
# traverse along its neighbors
# add all the visited nodes to a list
# until all the nodes are visited
# traverse until you hit a leaf and then go back
# call the callback pass in the value
# if this node has a left child we call the recursion
# same goes for the right
    # def depth_first_for_each(self, cb):
    #     cb(self.value)
    #     if self.left:
    #         self.left.depth_first_for_each(cb)
    #     if self.right:
    #         self.right.depth_first_for_each(cb)

# ITERATIVE IMPLEMENTATION
# create a stack/list that holds on to nodes we visit
# add root of tree to the stack, current node we are on
# while length of stack is true
# refer to the node we pop off of stack
# if it has a child to the right append it to our stack
# callback current node value
  # start at the root and append it to the stack
  # checkes if the root has children right and left
  # root gets popped off the stack and adds its children to stack
  # callback gets called on root and ends the roots connection
  # most recent child gets popped off the stack and gets checked for childs
  # if childs then they get added to the stack and the cb is called
  # on the the popped child
    def depth_first_for_each(self, cb):
        stack = []
        stack.append(self)

        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

# same as depth first except right left ordering is different
# and it is a different data structure
    def breadth_first_for_each(self, cb):
        queue = []
        queue.append(self)

        while len(queue):
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            cb(current_node.value)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
