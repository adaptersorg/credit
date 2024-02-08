import sys
import time

class Credit():
    def run(self, code, boolean):
        start_time = time.time()
        if len(code) == 0: return self.error("자고로 학생들은 계속 말하는 연습을 해야해요. 자기가 혹시 지금 말을 잘한다 있습니까? 손 한번 들어보세요. 보십시오 없지않습니까? 하지만 우리가 일상을 살아가면서 가장 중요한게 말이에요 말. 말 한 마디에 천냥 빚을 갚는다라는 말이 있듯이, 말이라는게 정말로 중요합니다. 이런 말을 어떻게 잘할 수 있냐? 일단 뱉어야 해요. 일단 뭐라도 말을 해야 어떤 점이 부족하고~ 어떤 점이 좋고~ 어떤 점은 이렇고를 알 수 있는데, 지금 여러분처럼 아무 말도 하지 않으면 발전하는 것이 없습니다. 잘 기억하고 항상 명심해야됩니", "다")

        if code[0] != "예 여러분 반갑습니다":
            return self.error('요즘 저를 두 눈 똑바로 보고도 인사를 안하고 지나치는 학생들이 너무 많습니다. 짧게만 이야기하자면, 학생은 다른 거 다 안해도 돼요. 기본적으로 어른들께 인사만 잘해도 "아~ 저 친구는 참하고 좋은 친구구나~" 이래 어른들이 생각합니다. 학생으로써 도리 중 가장 기본적인게 인사에요. 옛날에는 선생님 뒷모습을 봐도 인사하라는 그런 말이 있었어요. 내가 고등학생 때는 선생님 그림자도 피해다녔었거든. 요즘 시대 학생들 잘 압니다. 시대가 많이 바뀌었죠 그죠. 하지만 그래도 인사만큼 자신을 어필하는 좋은 수단은 없다고 생각합니', "다")
        
        if code[-1] != "예 이까지 하도록 하겠습니다": return self.error("항상 말을 하고나서는 끝맺음을 해야해요. 학생들 중에서 제일 많이 못하는 경우가 이겁니다. 말을 했어요 말을 했는데, 뒤에 끝맺음이 우물쭈물하면서 갑자기 소리가 작아지거나 말을 다 안 끝내는 경우가 있어요. 그런 걸 보다보면은 생각보다 좋게 생각이 들지는 않습니다. 혹시라도 이런 습관이 있다~ 하는 사람은 고치려고 한번 노력을 해보는 게 좋을 것 같습니", "다")
        codes = []
        for cod in code: codes.append(cod.split(" "))
        del codes[0]

        if len(codes) == 0: return self.error("자고로 학생들은 계속 말하는 연습을 해야해요. 자기가 혹시 지금 말을 잘한다 있습니까? 손 한번 들어보세요. 보십시오 없지않습니까? 하지만 우리가 일상을 살아가면서 가장 중요한게 말이에요 말. 말 한 마디에 천냥 빚을 갚는다라는 말이 있듯이, 말이라는게 정말로 중요합니다. 이런 말을 어떻게 잘할 수 있냐? 일단 뱉어야 해요. 일단 뭐라도 말을 해야 어떤 점이 부족하고~ 어떤 점이 좋고~ 어떤 점은 이렇고를 알 수 있는데, 지금 여러분처럼 아무 말도 하지 않으면 발전하는 것이 없습니다. 잘 기억하고 항상 명심해야됩니", "다")

        # 모든 코드의 마지막이 "맞지요~~?"로 끝나는지 확인
        for i in range(len(codes)):
            if codes[i][-1] != "맞지요~~?" and codes[i][-1] != "반갑습니다" and codes[i][-1] != "하겠습니다" and codes[i][0] != '':
                return self.error("항상 맞는지 아닌지 확인을 해보는게 중요해요. 옛말에 돌다리도 두들겨 보고 건너라~ 라는 말이 있습니다. 그런 말처럼 '맞지요~~?' 이렇게 확인을 하지 않으면 나중에 어떤 위험이 도사릴지 알 도리가 없다 이거에요. 우리 부산 소마고 학생 여러분들은 자나깨나 확인하는 습관을 들여야 합니", "다")
            del codes[i][-1]
        

        end_time = time.time()
        print(f"\n예 성공적으로 실행을 했습니다. 실행을 하는데... {end_time - start_time}초가 걸렸어요. 맞지요~~?")
 
    def compile(self, code):
        try:
            with open(code, encoding='utf-8-sig') as mte_file:
                code = mte_file.read().splitlines()
                self.run(code, False)
        except FileNotFoundError: self.error("파일이 없는 것 같습니", "다")
        except UnicodeDecodeError: self.error("무슨 말인지 잘 모르겠다 이겁니", "다")

    def error(self, error_content, error_postfix):
        error_last_content = '. 알겠지요~~?'
        print(error_content + error_postfix + error_last_content)

# Credit().compile("./test.sin")
if __name__ == "__main__":
    Credit().compile(sys.argv[1])
    # try: 
        # filename = sys.argv[1]
        # Credit().compile(filename)
    # except: 
        # print("credit 뒤에는 파일 이름을 입력하면 컴파일할 수 있습니다. 알겠지요~~?")