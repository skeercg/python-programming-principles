height = int(input('Enter the height of the pyramid: '))
peak = input('Which character for the top you want to use? ')

max_width = height * 2 - 1
for i in range(height):
    width = i * 2 + 1
    pyramid_part = ''
    if i == 0:
        pyramid_part = peak
    elif i == height - 1:
        pyramid_part = '/' + (width - 2) * '_' + '\\'
    else:
        pyramid_part = '/' + (width - 2) * ' ' + '\\'
    empty_space = (max_width - width) // 2
    print((empty_space * ' ') + pyramid_part + (empty_space * ' '))