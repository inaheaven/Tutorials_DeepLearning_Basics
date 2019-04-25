from konlpy.tag import Twitter

twitter = Twitter()
text="아름다운그녀가아버지가방에들어가신다."
malist = twitter.pos(text, norm=True, stem=True)
print('-'*40)
print( malist)

malist = twitter.pos(text, norm=False, stem=True)
print('-'*40)
print( malist)

malist = twitter.pos(text, norm=True, stem=False)
print('-'*40)
print( malist)

malist = twitter.pos(text, norm=False, stem=False)
print('-'*40)
print( malist)

print('-'*40)

for myitem in malist:
    print('단어', myitem[0])
    print('품사', myitem[1])
