from pyechonest import song
import time

fin =open('Country.txt','r')
#print 'Got Country'

#time.sleep(10)

fout = open('CountrySongs.dat','w')
countrysongtitles = open('CountrySongTitles.dat','w')

for line in fin:

	try:
		a = line.split('-')
		#print a
		#print a
		mytitle = a[0].strip()[1:-1]
		myartist = a[1].strip()
		#print myartist+'\t'+mytitle
		s = song.search(artist=myartist,title=mytitle)
		#time.sleep(10)
		#print 'Got song!'
		mysummary = s[0].audio_summary
		mysongtype = s[0].song_type
		
		titleinfo = []
		titleinfo.append(mytitle)
		titleinfo.append(myartist)

		countrysongtitles.write(','.join(titleinfo))
		countrysongtitles.write('\n')


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
	except Exception,e:
		print 'Some jhol'
		print e


fin.close()
fout.close()
countrysongtitles.close()