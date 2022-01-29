money=int(input())

fiveh=money//500
money=money%500

oneh=money//100
money=money%100

fivet=money//50
money=money%50

ten=money//10

least=fiveh+oneh+fivet+ten
print(least)


