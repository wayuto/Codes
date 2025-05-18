def cpp(func) -> None:
    
    '''Syntax of C++'''
    class Cout:
        def __init__(self) -> None:
            pass

        def __lshift__(self, other) -> None:
            print(other, end="")
            return self

    class Cin:
        def __init__(self) -> None:
            pass

        def __rshift__(self, other) -> None:
            other = input()
            return other
    ''''''
    def decorator(*args, **kwargs) -> None:
        result = func(cout=Cout(), endl="\n", cin=Cin(), *args, **kwargs)
        return result
        
    return decorator