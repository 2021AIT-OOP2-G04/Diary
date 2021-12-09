from diaries.DiarySample import DiarySample
from diaries.OnzawaDiary import OnzawaDiary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    OnzawaDiary(),
]

for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

