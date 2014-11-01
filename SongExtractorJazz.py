from pyechonest import song,artist
import time

#time.sleep(10)

fout = open('JazzSongs.dat','w')
jazzsongtitles = open('JazzTitles.dat','w')




artistlist = ['BB King','Albert King','Stevie Ray Vaughan']
for tempartist in artistlist:
	a = artist.Artist(tempartist)
	songlist = a.get_songs(results=100)

	for mysong in songlist:
		try:
			mytitle = mysong.title
			myartist = tempartist
			#print myartist+'\t'+mytitle
			
			#time.sleep(10)
			#print 'Got song!'
			mysummary = mysong.audio_summary
			mysongtype = mysong.song_type
			
			titleinfo = []
			titleinfo.append(mytitle)
			titleinfo.append(myartist)

			jazzsongtitles.write('|'.join(titleinfo))
			jazzsongtitles.write('\n')


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
			print 'Success! '+ myartist
		except Exception,e:
			print 'Some jhol'
			print e


fout.close()
jazzsongtitles.close()