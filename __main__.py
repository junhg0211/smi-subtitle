import time

subtitles = []

print('대사를 입력해주세요. 타이밍은 개행 문자를 기준으로 나눕니다.')
print('더 이상 입력할 대사가 없다면 "[[END]]"이라는 문자열을 입력해주세요.')

while True:
    if (line := input()) != '[[END]]':
        subtitles.append(line)
    else:
        break

first_subtitle = int(input('처음 자막이 시작하는 시간을 ms로 입력해주세요: '))

print('Enter를 누를때마다 시간을 기록합니다. 콘솔의 마지막 줄에는 다음 대사가 나타납니다.')
input('다음: ' + subtitles[0])

start_time = int(time.time() * 1000)

subtitle_file = open('output.smi', 'w', encoding='utf-8')

subtitle_file.write('<sami>\n')
subtitle_file.write('<body>\n')

subtitle_file.write(f'<SYNC Start={first_subtitle}><p Class=KRCC>{subtitles[0]}</p>\n')

for i in range(1, len(subtitles)):
    if not subtitles[i]:
        subtitles[i] = '&nbsp;'
    input('다음: ' + subtitles[i])
    subtitle_file.write(f'<SYNC Start={int(time.time() * 1000) - start_time + first_subtitle}><P Class=KRCC>{subtitles[i]}</P>\n')
    print()

subtitle_file.write('</body></sami>')
subtitle_file.close()

print('완료되었습니다.')

