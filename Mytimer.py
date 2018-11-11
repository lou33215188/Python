import time


class Mytimer:
    def __init__(self):
        self.prompt = "未开始计时！"
        self.index = ["年", "月", "日", "时", "分", "秒"]
        self.start_time = 0
        self.stop_time = 0
        self.borrow = [0, 12, 31, 24, 60, 60]

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt

    def __add__(self, other):
        prompt_result = "总共运行了"
        result = []
        for each in range(6):
            result.append(self.result[each] + other.result[each])
            if result[each]:
                prompt_result += str(result[each]) + self.index[each]
        return prompt_result

    def start(self):
        if self.start_time:
            self.start_time = 0
            print("注意！！！已开始重新计时！")
            self.prompt = "请先停止计时！"
            self.start_time = time.localtime()
        else:
            print("开始计时......")
            self.start_time = time.localtime()

    def stop(self):
        if not self.start_time:
            print("请先开始计时！")
        else:
            self.stop_time = time.localtime()
            print("计时结束......")
            self._calc()

    def _calc(self):
        self.prompt = "总共运行了"
        self.result = []
        for each in range(6):
            temp = (self.stop_time[each] - self.start_time[each])
            if temp < 0:
                i = 1
                while self.result[each - i] < 1:
                    self.result[each - i] += self.borrow[each - i] - 1
                    self.result[each - i - 1] -= 1
                    i = i + 1
                self.result.append(self.borrow[each] + temp)
                self.result[each - 1] -= 1
            else:
                self.result.append(temp)
            if self.result[each]:
                self.prompt += str(self.result[each]) + self.index[each]
        self.start_time = 0
        self.stop_time = 0
        print(self.prompt)
