def count_developers(lst):
    # Your code here
    def is_ok(n):
        if n['continent']=='Europe' and n['language']=='JavaScript':
            return n
    list1=list(filter(is_ok,lst))
    return len(list1)