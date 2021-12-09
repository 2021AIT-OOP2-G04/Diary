from diaries.AbstractDiary import AbstractDiary

class WatanabeDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return"""今日は英語とプログラミングの授業があった。
        英語のテストの点があまり良くなかった。"""

    def get_author(self):
        return super().get_author()(self)
        return "Watanabe"