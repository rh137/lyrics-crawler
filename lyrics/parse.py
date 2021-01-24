import os

if __name__ == '__main__':
	file_names = os.listdir()
	print(len(file_names))
	for name in file_names:
		if '.py' in name or os.path.isdir(name): continue
		with open(name, 'r') as f, open(f'./processed/{name}', 'w') as fout:
			for line in f:
				if  '作詞：' in line or '作曲：' in line\
					or '編曲：' in line or '詞/曲：' in line\
					or '詞曲：' in line or '製作：' in line\
					or '旁白：' in line or '編 曲：' in line\
					or '詞、曲：' in line or '曲、詞：' in line\
					or '詞：' in line or '曲：' in line\
					or '編：' in line or '鼓吹：' in line\
					or 'feat.' in line:
					pass
				else:
					fout.write(line)
