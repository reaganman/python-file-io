print('opening dummy.txt')
with open('dummy.txt', 'r') as infile:
    print('opening output.txt')
    with open('output.txt', 'w') as outfile:
        for line in infile:
            line=line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                outfile.write('{0}\n'.format(word))
print('done!')
print('dummy.txt is closed?', infile.closed)
print('output.txt is closed?', outfile.closed)



