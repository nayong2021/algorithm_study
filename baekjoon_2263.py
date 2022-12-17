#https://www.acmicpc.net/problem/2263
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_position = [-1] * (n+1)
for i, val in enumerate(inorder):
    inorder_position[val] = i

tree = [-1] * (n+1)

stack = [(0, len(postorder)-1)]

while stack:
    start, end = stack.pop()
    root = postorder[end]
    root_position = inorder_position[root]
    i = start
    while i < end and inorder_position[postorder[i]] < root_position:
        i += 1
    if i > start:
        stack.append((start, i-1))
    if i < end:
        stack.append((i, end-1))
    tree[root] = (postorder[i-1] if i > start else None, postorder[end-1] if i < end else None)

def preorder_traversal(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        left_child, right_child = tree[cur]
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)

root = postorder[-1]
preorder_traversal(root)