while True:
    path1 = ["D:\\music\\music2\\AD张宸硕 - Feeling Good（钢琴版）.mp3",
             "D:\\music\\music2\\CelloNaduo - 一步之遥 Por Una Cabeza（《闻香识女人》插曲）.mp3",
             "D:\\music\\music2\\Circadian Eyes - Rain.mp3",
             "D:\\music\\music2\\Mike Zhou - The Dawn (亡灵序曲完整钢琴版).mp3",
             "D:\\music\\music2\\only苏坤杰 - Are You Lost（治愈版）.mp3",
             "D:\\music\\music2\\PianoPanda - 加勒比海盗（钢琴版）（翻自 Klaus Badelt）.mp3",
             "D:\\music\\music2\\安林 - 周末有空吗.mp3",
             "D:\\music\\music2\\白茶 - 未闻花名（钢琴版）.mp3",
             "D:\\music\\music2\\琥珀琴师Louis - 克罗地亚狂想曲 钢琴独奏版（Croatian Rhapsody）.mp3",
             "D:\\music\\music2\\克林SU - Flower Dance 花之舞 (钢琴独奏)（翻自 DJ Okawari）.mp3",
             "D:\\music\\music2\\路灰气球 - Komorebi【钢琴】.mp3",
             "D:\\music\\music2\\孙昊天 - 我心永恒(钢琴独奏).mp3",
             "D:\\music\\music2\\孙敬博 - 一步之遥-小提琴版.mp3",
             "D:\\music\\music2\\薛定谔的加菲猫 - 被时光移动的城市（cover 石进）（Cover 石进）.mp3",
             "D:\\music\\music2\\薛定谔的加菲猫 - 雨中的巴赫.mp3",
             "D:\\music\\music2\\张珂 - 一步之遥-钢琴版.mp3"]

    path2 = ['[Feeling Good]',
             '[一步之遥]',
             '[Rain]',
             '[亡灵序曲]',
             '[Are You Lost]',
             '[加勒比海盗]',
             '[周末有空吗]',
             '[未闻花名]',
             '[克罗地亚狂想曲]',
             '[Flower Dance 花之舞]',
             '[Komorebi]',
             '[我心永恒]',
             '[一步之遥]',
             '[被时光移动的城市]',
             '[雨中的巴赫]',
             '[一步之遥]']

    import random

    i = random.randint(0, 15)
    print(path2[i], '\n')
    import pygame

    pygame.mixer.init()
    pygame.mixer.music.load(path1[i])
    pygame.mixer.music.set_volume(0.5)  # 声音大小[0<j<1]  J = float(input("调节音量：J="))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
