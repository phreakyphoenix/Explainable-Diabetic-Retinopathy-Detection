import os
path = '/media/aditya/Data/test/'
print len(os.listdir(path))
for filename in os.listdir(path):
	num, suffix = filename[:-5].split('_')
	print num,suffix
	num = num.zfill(6)
	suffix ='a.jpeg' if suffix =='left' else 'b.jpeg'
	os.rename(path+filename, path+num+suffix)