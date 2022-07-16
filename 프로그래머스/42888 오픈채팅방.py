def solution(record):
    #딕셔너리에 이름 처리하기
    name={}
    for i in range(len(record)):
        if record[i][0] == 'L':
            continue
        id_name = record[i].split()
        name[id_name[1]] = id_name[2]

    #answer(리스트)에 출력 메세지 넣기
    answer = []
    for i in range(len(record)):
        if record[i][0] == 'E':
            answer.append(f"{name[record[i].split()[1]]}님이 들어왔습니다.")
        elif record[i][0] == 'L':
            answer.append(f"{name[record[i].split()[1]]}님이 나갔습니다.")

    return answer

#record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#print(solution(record))