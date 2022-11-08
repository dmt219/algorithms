class Node:
  def __init__(self, item, _next):
    self.item = item
    self.next = _next

class LinkedList:
  def __init__(self, head):
    self.head = head

  def search(self, val):
    curr = self.head
    while (curr != None):
      if (curr.item == val):
        return curr
      curr = curr.next
    return None

  def insert(self, val):
    # insert to the end of list
    curr = self.head

    # Empty list
    if (curr == None):
      self.head = Node(val, None)
      return

    while (curr.next != None):
      curr = curr.next
    curr.next = Node(val, None)

  def delete(self, val):
    curr = self.head
    # delete head
    if (curr.item == val):
      self.head = curr.next
      return
    # delete non-head
    while (curr != None):
      if (curr.next and curr.next.item == val):
        break
      curr = curr.next
    if curr.next == None:
      return

    curr.next = curr.next.next

  def print_list_to_array(self):
    curr = self.head
    arr = []
    while (curr != None):
      arr.append(curr.item)
      curr = curr.next
    return arr

if __name__ == '__main__':
  head = Node(4, None)
  linked_list = LinkedList(head)
  linked_list.delete(4)
  assert(linked_list.head == None)
  linked_list.insert(10)
  assert(linked_list.print_list_to_array() == [10])
  linked_list.insert(1)
  linked_list.insert('a')
  linked_list.insert(100)
  linked_list.insert((1, 2))
  assert(linked_list.print_list_to_array() == [10, 1, 'a', 100, (1, 2)])
  linked_list.delete(10)
  linked_list.delete(100)
  assert(linked_list.print_list_to_array() == [1, 'a', (1, 2)])
  assert(linked_list.search(10) == None)
  assert(type(linked_list.search(1)).__name__ == 'Node')
