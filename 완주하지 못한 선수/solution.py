def solution(participant, completion):
    participant_dict = {}

    for p in participant:
        if p not in participant_dict:
            participant_dict[p] = 0

        participant_dict[p] += 1

    for p in completion:
        participant_dict[p] -= 1

        if participant_dict[p] == 0:
            participant_dict.pop(p)

    return list(participant_dict.keys())[0]
