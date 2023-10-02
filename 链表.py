节点初始化，关键字为0，下一位为空
class listnode:
    del init(ori_node,key = 0,next = None):
        ori_node.key = key
        ori_node.next = next

#链表初始化，表头为空
class linklise:
    def init(ori_node):
        ori_node.head = None

#data为一整个数据表
def create(ori_node,data):
    ori_node.head = listnode(0)
    cur = ori_node.head
    for i in range(len(data)):
        node = listnode(data[i])
        cur.next = node
        cur = cur.next

#新节点作为表头
def head_insert(ori_node,key):
    node = listnode(key)
    node.next = ori_node.head
    ori_node.head = node

#新节点作为表尾
def end_insert(ori_node,key):
    node = listnode(key)
    cur = ori.head
    while cur.next:
        cur = cur.next#循环直到表尾,cur.next = None
    cur.next = node

#新节点插入在中间
def insert_between(ori_node,pos,key):
    count = 0
    cur = ori_node
    while cur and count < pos-1:
        cur = cur.next
        count = count+1

    if not cur:
        print("error:overflow")
        return

    node = listnode(key)
    node.next = cur.next
    cur.next = node#注意头尾链接的顺序

def switch(ori_node,pos,key):
    count = 0
    cur = ori_node
    while cur and count < pos-1:
        cur = cur.next
        count = count+1

    if not cur:
        print("error:overflow")
        return
    cur.key = key

def head_del(ori_node):
    if ori_node:
        ori_node.head = ori_node.head.next

def end_del(ori_node):
    cur = ori_node.head
    while cur.next:
        cur = cur.next
        cur = None

def del_between(ori_node,pos):
    count = 0
    cur = ori_node.head
    while cur and count<pos-1:
        cur = cur.next
        count = count-1
    if not cur:
        print("error:overflow")
        return

    del_node = cur.next
    cur.next = del_node.next

def search(ori_node,pos):
    count = 0
    cur = ori_node.head
    while cur and count<pos-1:
        cur = cur.next
        count = count-1
    if not cur:
        print("error:overflow")
        return

    res = cur.key
    print(f"result = {res}")

