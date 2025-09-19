import sys
input = sys.stdin.readline
# dict, recur 이용해서 트리 만들기
n = int(input().strip())
tree = {} # 딕셔너리 선언

for _ in range(n):
    p, l, r = input().split()
    tree[p] = (None if l == '.' else l,
               None if r == '.' else r)
    
def preorder(node): # 루트, 왼쪽, 오른쪽
    if node is None:
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node): # 왼쪽, 루트, 오른쪽
    if node is None:
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node): # 왼쪽 오른쪽 루트
    if node is None:
        return
    postorder(tree[node][0]) 
    postorder(tree[node][1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')