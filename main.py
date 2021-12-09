from diaries.DiarySample import DiarySample
from diaries.k20119 import K20119diary
from diaries.OnzawaDiary import OnzawaDiary
from diaries.WatanabeDiary import WatanabeDiary
from diaries.K20014Diary import K20014Diary
from diaries.K20054Diary import K20054Diary
from diaries.AonoDiary import AonoDiary
from diaries.K20047Diary import K20047Diary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
    K20014Diary(),
    K20047Diary(),
    OnzawaDiary(),
    K20054Diary(),
    AonoDiary(),
    WatanabeDiary(),
    K20119diary()

]



for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

