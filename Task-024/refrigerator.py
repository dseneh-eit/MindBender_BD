#!/usr/bin/env python
# coding: utf-8

class Refrigerator():
    def __init__(self) -> None:
        self.shelf_s = []
        self.shelf_m = []
        self.shelf_l = []
        super().__init__()
    
    # Remove items from the refrigerator
    def get(self, item, shelf):
        """
        Remove items from a specified shelf.
        Shelves Numbers:
            Small  = 1
            Medium = 2
            Large  = 3
        """
        if shelf <1 or shelf >3:
            return 'You must enter a valid shelf number between 1 and 3'

        if shelf == 1:
            for i in range(len(self.shelf_s)):
                if self.shelf_s[i]['item'] == item and len(self.shelf_s) >0:
                    del self.shelf_s[i]
                    return f'{item} has been deleted from the small shelf.'
                    break
                else: 
                    return 'Item not found in this shelf.'
        elif shelf == 2:
            for i in range(len(self.shelf_m)):
                if self.shelf_s[i]['item'] == item  and len(self.shelf_m) >0:
                    del self.shelf_2[i]
                    return f'{item} has been deleted from the medium shelf.'
                    break
                else: 
                    return 'Item not found in this shelf.'
        elif shelf == 3:
            for i in range(len(self.shelf_l)):
                if self.shelf_l[i]['item'] == item and len(self.shelf_l) >0:
                    del self.shelf_l[i]
                    return f'{item} has been deleted from the large shelf.'
                    break
                else: 
                    return 'Item not found in this shelf.'
    
    
    # Put method checks severial conditions before executing.
    def put(self, item=None, size=0, shelf=None):
        """
        Add items from a specified shelf.
        Shelves Numbers:
            Small  = 1
            Medium = 2
            Large  = 3
        """
        
        if item is None:
            return 'Please specify item'
        
        if size is None or size <= 0 or size > 500:
            return 'Item size must between 1 and 500'

        if shelf is None or shelf == 0 or shelf > 3:
            return 'Please specify a valid shelf number between 1 and 3'
        
        if size <=100 and shelf == 1:
            total_size_s =sum(item['size'] for item in self.shelf_s)
            s = size + total_size_s
            if s <= 100:
                self.shelf_s.append({'item':item, 'size':size})
                return f'{item} added to small sized shelf.'
            else:
                return f'Item cannot fit in this shelf. You have {100-total_size_s}/100cm of free space.'
                
        elif size >= 101 and size <= 300 and shelf == 2:
            total_size_m =sum(item['size'] for item in self.shelf_m)
            s = size + total_size_m
            if s <= 300:
                self.shelf_m.append({'item':item, 'size':size})
                return f'{item} added to medium sized shelf.'
            else:
                print(f'Item cannot fit in this shelf. You have {300-total_size_m}/100cm of free space.')
                
        elif size >= 301 and size <= 500 and shelf == 3:
            total_size_l =sum(item['size'] for item in self.shelf_l)
            s = size + total_size_l
            if s <= 500:
                self.shelf_l.append({'item':item, 'size':size})
                print(f'{item} added to large sized shelf.')
            else:
                print(f'Item cannot fit in this shelf. You have {500-total_size_l}/100cm of free space.')
        else:
            print('Item must be placed into the right shelf size.')
            return None