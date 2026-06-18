import math

def power(a, b):
    """
    Tính lũy thừa a^b.
    
    Args:
        a: Cơ số
        b: Số mũ (số nguyên hoặc thực)
    
    Returns:
        a^b
    
    Raises:
        ZeroDivisionError: Khi a=0 và b<0
    """
    if b < 0:
        if a == 0:
            raise ZeroDivisionError("Cannot raise 0 to a negative power")
        return 1 / power(a, -b)
    return a ** b
