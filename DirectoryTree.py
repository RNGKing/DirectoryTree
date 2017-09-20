import sys
import os

class _Element:
    """This is the fundamental piece of the tree. An element is, for this application,
    a directory. It contains attitributes, the files it contains, and children elements."""

    def __init__(self, new_path):
        self.name = new_path.split('\\')[-1]
        self.path = new_path
        self.children = {}
        self.attributes = []
        self._make_branch(new_path)

    def _add_attribute(self, attr_to_add):
        self.attributes.append(attr_to_add)
    
    def _add_children(self, child_name,child_to_add):
        temp_dict = {child_name : child_to_add}
        self.children.update(temp_dict)
    
    def _make_branch(self, dir_path):
        for path in os.listdir(dir_path):
            temp_path = os.path.join(dir_path, path)
            if os.path.isdir(temp_path):
                temp_element = _Element(temp_path)
                self._add_children(temp_element.name,temp_element)
            else:
                temp_attr = Attribute(temp_path)
                self._add_attribute(temp_attr)  


class Attribute:
    def __init__(self, path):
        self.name = path.split('\\')[-1]
        self.path = path 
    
    

def BuildTree(dir_name):
    """Constructs a tree from a given filepath"""
    main_path = os.path.realpath(os.path.join(os.getcwd(), dir_name))
    temp = _Element(main_path)
    return temp



            


    
    
    
