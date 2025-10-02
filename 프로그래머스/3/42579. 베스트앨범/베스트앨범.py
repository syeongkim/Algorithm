def solution(genres, plays):
    answer = []
    musicList = []
    genreDictionary = {}
    
    for i in range(len(genres)):
        temp = [i, genres[i], plays[i]] # 인덱스, 장르, 재생 횟수
        musicList.append(temp)
        if genres[i] in genreDictionary:
            genreDictionary[genres[i]] += plays[i]
        else:
            genreDictionary[genres[i]] = plays[i]
        
    sortedGenreDictionary = sorted(genreDictionary.items(), key = lambda x: -x[1])
    sortedMusicList = sorted(musicList, key = lambda x: (x[1], -x[2], x[0]))
    
    for genre in sortedGenreDictionary:
        cnt = 0
        for music in sortedMusicList:
            if cnt == 2:
                break
            else:
                if music[1] == genre[0]:
                    answer.append(music[0])
                    cnt += 1
    return answer