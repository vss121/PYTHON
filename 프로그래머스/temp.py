def solution(record):
    answer=[]
    name={}
    printer={'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:    #이름 update
            name[rr[1]] = rr[2]
    
    for r in record:
        rr = r.split(' ')
        if rr[0] != 'Change':
            answer.append(name[rr[1]]+printer[rr[0]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))