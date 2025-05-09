from typing import Annotated, Literal

from annotated_types import Gt

from pydantic import BaseModel


class Fruit(BaseModel):
    name: str  
    color: Literal['red', 'green']  
    weight: Annotated[float, Gt(0)]  
    bazam: dict[str, list[tuple[int, bool, float]]]  


print(
    Fruit(
        name="Muskan",
        color='red',
        weight=4.2,
        bazam={'basektball': [(1, True, 0.1)]},
    )
)
print(
    Fruit(
        name=7, #this line throw error because name type is str and i give int
        color='red',
        weight=4.2,
        bazam={'fooball': [(1, True, 0.1)]},
    )
)
