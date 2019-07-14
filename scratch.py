from typing import Union

def foo(x: Union[int, None]) -> str: 
    return f"{x}" if x else "bar"
