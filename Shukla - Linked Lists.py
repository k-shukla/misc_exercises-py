''' Here, we construct linked lists, a type of data structure useful particularly in slightly
    lower-level languages such as C.'''
   
''' First, I'm going to create nodes themselves. These will be bi-directional nodes, with references
    to both previous and subsequent nodes. The methods retr_prev, retr_next, set_prev, and set_next
    will all check '''

class Node(object):
    
    def __init__(self, data, prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
    
    def retr_data(self):
        return self.data
    
    def retr_prev(self):
        if type(self.prev_node) == Node or type(self.prev_node) == None:
            return self.prev_node
        else:
            raise TypeError("field 'prev_node' in class Node must be of type Node or None")
    
    def retr_next(self):
        if type(self.next_node) == Node or type(self.next_node) == None:
            return self.next_node
        else:
            raise TypeError("field 'next_node' in class Node must be of type Node or None")
    
    def set_new_prev(self, new_prev):
        if type(new_prev) == Node or type(new_prev) == None:
            self.prev_node = new_prev
            return
        else:
            raise TypeError("field 'prev_node' in class Node must be of type Node or None")
    
    def set_new_next(self, new_next):
        if type(new_next) == Node or type(new_next) == None:
            self.next_node = new_next
            return
        else:
            raise TypeError("field 'next_node' in class Node must be of type Node or None")

''' Now, I'll create the linked list itself. For the same reasons as with the Node class, I won't do
    type checking on this object. The methods I want are to insert a first node, insert a last node,
    insert a node before a given node, insert a node after a give node, delete the first node, delete
    the last node, delete a given node, delete a node before a given node, delete a node after a
    given node, traverse the list to find data, find the number of nodes, and convert this to a
    Python list.
   
    I won't do type-checking here to see if any references to prev_node or next_node are actually of
    the correct type (i.e. type Node or None), since that is already handled in the definition of the
    Node class. '''

class LinkedList(object):
    
    def __init__(self, first = None):
        self.first = first
    
    def set_new_first(self, new_first_data):
        new_first_node = Node(new_first_data, None, self.first)
        self.first = new_first_node
        return
    
    def set_new_last(self, new_last_data):
        now_node = self.first
        if now_node == None:
            self.set_new_first(new_last_data)
        else:
            while now_node.retr_next() != None:
                now_node = now_node.retr_next()
            new_last_node = Node(new_last_data, now_node, None)
            now_node.set_new_next(new_last_node)
            return
    
    def set_before(self, new_before_data, ref_node_data):
        pass
    
    def set_after(self, new_after_data, ref_node_data):
        pass
    
    def delete_first(self):
        pass
    
    def delete_last(self):
        pass
    
    def delete_given_node(self, data_to_remove):
        pass
    
    def delete_before(self, ref_node_data):
        pass
    
    def delete_after(self, ref_node_data):
        pass
    
    def find_data_first_instance(self, ref_data):
        pass
    
    def find_data_all_instances(self, ref_data):
        pass
    
    def check_cycle(self):
        pass
    
    def num_nodes(self):
        curr_nodes = 0
        now_node = self.first
        while now_node != None:
            curr_nodes += 1
            now_node = now_node.retr_next()
        return
    
    def py_list_convert(self):
        converted_list = []
        now_node = self.first
        if now_node == None:
            return converted_list
        else:
            while now_node != None:
                converted_list.append(now_node.retr_data())
                now_node = now_node.retr_next()
            return converted_list
