# typing에서 가져올 건데~ ~~~를 연결할게
from typing import List, Dict, Set, Tuple, Union, Final

# Final은 변경하지 말라는 뜻
data: Final[int] = 10
# data = 20 → 변수 값 변경 노노!
print(data)

class A:
    pass

class B:
    @staticmethod
    # int랑 str 둘 다 사용이 가능하다고 알려주고 싶으면
    # Union을 써서 묶어주기
    # Union = |
    # | 은 3.0이상의 버전부터 사용 가능
    # 콜론 전에 return의 타입을 알려주기
    # data1: A → A class
    def test(data: Union[int, str], number: int | float, data1: A, datas: List[int], data_dict: Dict[str, int]) -> int:
        return 10
