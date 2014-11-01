from pyechonest import song
import time

fin =open('Rock.txt','r')

fout = open('RockSongs.dat','w')
rocksongtitles = open('RockSongTitles.dat','w')

for line in fin:

	try:
		a = line.split('\t')[1].split('-')
		print a
		myartist = a[0].strip()
		mytitle = a[1].strip()
		s = song.search(artist=myartist,title=mytitle)
		#print 'Got song!'
		mysummary = s[0].audio_summary
		mysongtype = s[0].song_type
		
		titleinfo = []
		titleinfo.append(mytitle)
		titleinfo.append(myartist)

		rocksongtitles.write('\t'.join(titleinfo))
		rocksongtitles.write('\n')


		l = []
		l.append(str(mysummary['time_signature']))
		l.append(str(mysummary['energy']))
		l.append(str(mysummary['liveness']))
		l.append(str(mysummary['tempo']))
		l.append(str(mysummary['speechiness']))
		l.append(str(mysummary['acousticness']))
		l.append(str(mysummary['danceability']))
		l.append(str(mysummary['instrumentalness']))
		l.append(str(mysummary['key']))
		l.append(str(mysummary['duration']))
		l.append(str(mysummary['loudness']))

		fout.write('\t'.join(l))
		fout.write('\n')
		print 'Success!'
		#time.sleep(3)
	except Exception,e:
		print 'Some jhol'
		print e


fin.close()
fout.close()
rocksongtitles.close()