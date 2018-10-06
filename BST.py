#_*_coding:utf-8_*_
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    # 추가
    def insert(self,data):
        if self.data:# 데이터가 있을 경우
            if data < self.data:#insert data 현재 노드의 데이터보다 작을 경우
                if self.left is None:# 왼쪽 노드 데이터가 없을 경우
                    self.left = Node(data)
                else:#왼쪽 노드 데이터가 있을 경우 재귀 호출
                    self.left.insert(data)
            elif data > self.data:#insert data 현재 노드의 데이터보다 클 경우
                if self.right is None:#오른쪽 노드 데이터가 없을 경우
                    self.right = Node(data)
                else:#오른쪽 노드 데이터가 없을 경우 재귀 호출
                    self.right.insert(data)
        else:# 데이터가 없을 경우
            self.data = data
    # 검색
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+' Not found'
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+' Not found'
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+' is found')

    # 출력
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
