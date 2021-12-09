from diaries.DiarySample import DiarySample
from diaries.OnzawaDiary import OnzawaDiary
from diaries.WatanabeDiary import WatanabeDiary
from diaries.K20014Diary import K20014Diary
from diaries.K20054Diary import K20054Diary
from diaries.aonoDiary import AonoDiary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
    K20054Diary(),
    AonoDiary(),
    WatanabeDiary()
]


for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

