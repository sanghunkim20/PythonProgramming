"""
value1 = ord('A')
value2 = ord('a')

print('A =', value1, 'a =', value2)

print('97 =', chr(97))
print('65 =', chr(65))
print(len('Cambodia'))

print(' I\'m a student')

print("She said, \"It\'s easy to read when you follow the line breaks correctly.\"\nThen she added, \'Remember to escape quotes properly!\'")
"""
fp = open('bam.txt', 'r', encoding='utf-8')
bam_lyrics = ""
while 1:
    line = fp.readline()
    if not line:
        break
    bam_lyrics = bam_lyrics + line.strip() + "\n"
fp.close()

bam_count = bam_lyrics.count("밤양갱")
bam_lyrics = bam_lyrics.replace('밤양갱', '마라탕')
print(bam_lyrics)
print("밤양갱 등장횟수 : ", bam_count)