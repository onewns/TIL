def solution(genres, plays):
    answer = []
    total = list(zip(range(len(plays)), genres, plays))
    total.sort(key=lambda x: -x[2])
    music_dict = {}
    for music_id, genre, play in total:
        if genre not in music_dict:
            music_dict[genre] = [0]
        music_dict[genre][0] += play
        music_dict[genre].append((play, music_id))
    total = list(sorted(music_dict.values()))
    total.sort(reverse=True)
    for g in total:
        for play, music_id in g[1:3]:
            answer.append(music_id)
    return answer