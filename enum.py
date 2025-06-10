#enumerate questions
i=1
with open("asep.txt",encoding="utf-8") as f:
    with open("new.txt","w",encoding="utf-8") as wf:
        for line in f.readlines():
            if line=='<div class="question">\n':
                wf.write('<div class="question" id="quest'+ str(i) + '">')
                i+=1
            else:
                wf.write(line)
