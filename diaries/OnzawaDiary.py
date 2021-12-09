from diaries.AbstractDiary import AbstractDiary

class OnzawaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return"""今日は英語とプログラミングの授業があった。"""

    def get_author(self):
        return "Onzawa"