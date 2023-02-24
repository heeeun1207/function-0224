hyun = 1
print(hyun)
hyun = "바보"
print(hyun)

kdt = {
  "삼백오호" : "홀쭉",
  "공욱재"  : "냥이집사",
}
print(kdt["공욱재"])
kdt_order = ["우리는", "개발자", "입니다"]
print(kdt_order[0],kdt_order[1],kdt_order[2])

for index in kdt_order:
    print(index)

def percent_calc(real_value, total_value):
   result = (real_value/ total_value) *100 
   return result 
#   python3.10 aaa.py 라고 입력하거나  우클릭으로 터미널열어야함