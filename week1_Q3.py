score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score:list) -> None:
    for idx, i in enumerate(score):
        mid_term, final_term = i
        avg = (mid_term + final_term) / len(i)
        print(f'{idx+1}번, 평균: {avg}')

get_avg(score)
