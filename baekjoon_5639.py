import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start==end:
        print(preorder[start])
        return
    root = preorder[start]
    i = start + 1
    
    while i <= end and preorder[i] < root:
        i+=1
    if i != start + 1:
        postorder(start+1, i-1)
    if i <= end:
        postorder(i, end)
    print(root)

postorder(0, len(preorder)-1)