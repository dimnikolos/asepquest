abcd21234 = {'α':'1','β':'2','γ':'3','δ':'4'}
questionnum = 1
unit = ""
with open("quest2.txt",encoding = "utf-8") as f:
	with open("quest2.html", "w", encoding="utf-8") as wf:
		for line in f.readlines():
			#input(line)
			if line.startswith('Ενότητα'):
				unit = line;
				processedline = '';
			elif line[0].isdigit():
				processedline = '<div class="question" id="quest'+str(questionnum)+'"><div class="ekfonisi">'
				questionnum+=1
				processedline += line.replace('\n','')
				processedline += '</div>'
			elif line[0] in ['α','β','γ','δ']:
				processedline = '<div class="answer'+abcd21234[line[0]]+ '"' + (' onclick="correct(this)";' if '<red>' in line else '') + '>'
				processedline += line.replace('<red>','')
				processedline += '</div>'
				if line[0] == 'δ':
					processedline += '<div class="unit">'
					processedline += unit
					processedline += '</div></div>'
			wf.write(processedline);

