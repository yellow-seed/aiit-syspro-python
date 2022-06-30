import time, random # 一行で複数のimportを行わない

sum = 0

before=time.clock() # イコールにスペースがない
for i in range(1000000) : # コロンに不要なスペースがある
        sum = sum + random.randint(1 , 100) # インデントが正しくない(スペース4つが正しい) # カンマの左スペースは不要
gaptime = time.clock() - before

print( "gaptime:" , gaptime , flush = True ) # カッコとカンマに不要なスペースがある # キーワード引数のイコールにスペースは不要