path = '/home/aditya/Downloads/spark/'
with open (path+'trainLabels.csv','r') as labelfile:
	print 'hi'
	with open (path+'trainLabelsCopy.csv','w+') as out:
		for line in labelfile:
			out.write(line.zfill(10))