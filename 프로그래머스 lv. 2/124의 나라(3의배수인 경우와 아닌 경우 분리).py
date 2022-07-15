def solution(n):
    answer = ''
    li = list() #answer를 만들기 위해 값을 받는 임시 배열

    while(n != 0):
        if(n % 3 == 0):
            share = n // 3 - 1 #3의 배수에서 몇번째인지 0부터 count했을때의 그 번호 값
            remain = n % 3 #나머지를 구하여 answer에 추가

            if(remain == 0):
                li.append(str(4))
            elif(remain == 1):
                li.append(str(1))
            elif(remain == 2):
                li.append(str(2))
            else:
                break

            n = share #사실상 3진법에 해당하므로 3으로 나눈 값이 n이 될 수 있도록 진행
        else:
            share = n // 3
            remain = n % 3

            if(remain == 0):
                li.append(str(4))
            elif(remain == 1):
                li.append(str(1))
            elif(remain == 2):
                li.append(str(2))
            else:
                break

            n = share

    for i in range(len(li)-1, -1, -1):
        answer = answer + li[i]

    return answer
