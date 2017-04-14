def make_album(name, title, number_tracks=0):
	album = {}
	album['name'] = name
	album['title'] = title
	if number_tracks != 0:
		album['number_tracks'] = number_tracks
	return album

# print(make_album('test','this is a test'))
# print(make_album('ABBA', 'Dancing Queen',12))

albums = []

while True:
	flag = input("Add an album? (Y/N) ")
	if flag == 'N' or flag == 'n':
		break
	name = input("Album name: ")
	title = input("Album title: ")
	number_tracks = input("Number of tracks (or skip): ")
	if number_tracks == '':
		number_tracks = 0
	else:
		number_tracks = int(number_tracks)
	albums.append(make_album(name,title,number_tracks))

print("- Albums saved -")
for album in albums:
	print("Name: " + str(album['name']))
	print("Title: " + str(album['title']))
	if 'number_tracks' in album:
		print("Number of tracks: " + str(album['number_tracks']))