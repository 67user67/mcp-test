def power(a, b):
    """
    Tính lũy thừa a^b bằng vòng lặp.
    
    Args:
        a: Cơ số
        b: Số mũ (số nguyên dương)
    
    Returns:
        a^b
    """
    result = 1
    for _ in range(b):
        result *= a
    return result
