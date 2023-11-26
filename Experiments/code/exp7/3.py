# TODO: complete this class
import math
class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page=items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count()/self.items_per_page)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if (page_index+1)<self.page_count() and page_index>=0:
            return self.items_per_page
        elif (page_index+1)==self.page_count() and page_index>=0:
            last=self.item_count()%self.items_per_page
            return self.items_per_page if last==0 else last
        else:
            return -1
        
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if(item_index<self.item_count() and item_index>=0):
            return item_index//self.items_per_page
        else:
            return -1