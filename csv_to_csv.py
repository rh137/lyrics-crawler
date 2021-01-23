import csv
from tqdm import tqdm

from utils import *

def csv_to_csv(input_='./data/raw_data.csv', output='./data/output.csv'):
	my_dict = dict()
	with open(input_, 'r') as f, open(output, 'w') as fout,\
		 open('./data/no_candidate.csv', 'w') as fno,\
		 open('./data/multiple_candidate.csv', 'w') as fmul:
		reader = csv.reader(f)
		writer = csv.writer(fout)
		w0 = csv.writer(fno)
		wm = csv.writer(fmul)

		raw_data = list(reader)
		header = raw_data[0]
		writer.writerow(header)
		w0.writerow(header)
		wm.writerow(header)

		# album_name: row[4], song_name: row[5], artist: row[6]
		cnt0, cnt1up = 0, 0
		lst0 = []
		for i in tqdm(range(1, len(raw_data))):
			row = raw_data[i]
			album_name = row[4]
			artist_name = row[6]
			
			if (album_name, artist_name) not in my_dict.keys():
				my_dict[(album_name, artist_name)] = kkbox_search(album_name, artist_name)
			candidates = my_dict[(album_name, artist_name)]	
			'''
			if len(candidates) == 0:
				print(f'{i+1}: {album_name}-{artist_name}')
				cnt0 += 1
				lst0.append((album_name, artist_name))
			'''
			if len(candidates) == 1:
				album = candidates[0]
				crawl_songs(album)
				for s in album.songs:
					row[5] = s.title()
					writer.writerow(row)
					#crawl_lyrics(s)
			else:
				row[-1] = len(candidates)
				writer.writerow(row)
				if len(candidates) > 1:
					for album in candidates:
						row[13] = album.link
						wm.writerow(row)
				else:
					w0.writerow(row)

csv_to_csv()
