class calculator:
    def add(num_list):
        total = 0
        for num in num_list:
            total+=int(num)
        return total
    
    def multi(num_list):
        total = 1
        for num in num_list:
            total*=int(num)
        return total
    
    
    def subtract(a,b):
        total = a - b
        return total
    
    
    def divide(a,b):
        total = a / b
        return total