class Tree(object):
    def __int__(self, key, color):
        self.key = key
        self.color = color
        self.p = None
        self.left = None
        self.right = None


def left_rotate(root, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.p = x
    y.p = x.p
    if x.p.left == x:
        x.p.left = y
    elif x.p.right == x:
        x.p.right = y
    else:
        root = y
    x.p = y
    y.left = x
    return root


def right_rotate(root, y):
    x = y.left
    x.right = y.left
    if x.right:
        x.right.p = y
    x.p = y.p
    if y.p.left == y:
        y.p.left = x
    elif y.p.right == y:
        y.p.right = x
    else:
        root = x
    x.right = y
    y.p = x
    return root


def RB_insert_fixup(root, z):
    pass


def RE_insert(root, z):
    x = root
    while x:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    z.color = "RED"
    RB_insert_fixup(root, z)
    return root


def RB_transplant(root, u, v):
    if u.p is None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p
    return root


def tree_minimum(root, x):
    return "mimnum"


def RB_delete_fixup(root, x):
    pass


def RB_delete(root, z):
    y = z
    y_original_color = y.color
    if z.left is None:
        x = z.right
        RB_transplant(root, z, z.right)
    elif z.right is None:
        x = z.left
        RB_transplant(root, z, z.left)
    else:
        y = tree_minimum(root, z.right)
        y_original_color = y.color
        x = y.right
        if y.p == z:
            x.p = y
        else:
            RB_transplant(root, y, y.right)
            y.right = z.right
            y.right.p = y
        RB_transplant(root, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == "BLACK":
        RB_delete_fixup(root, x)
