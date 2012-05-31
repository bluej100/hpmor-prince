#!/usr/bin/python
import sys, time, os, random, re, urllib

start = 1
end = 0
suffix = ""
if len(sys.argv) > 1:
	start = int(sys.argv[1])
if len(sys.argv) > 2:
	end = int(sys.argv[2])
	suffix = "-"+str(start)+"-"+str(end)
			
f = open('hpmor'+suffix+'.html', 'w')
header = open('hpmor-header.html', 'r')
f.write(header.read())

titlere = re.compile('<div id="chapter-title">Chapter \\d+: (.*?)<', re.DOTALL);
contentre = re.compile("<div class='storycontent puretext' id='storycontent'>(.*?)</div>\n<div id='content'", re.DOTALL);

i = 1
while end == 0 or i <= end:
	url = 'http://hpmor.com/chapter/'+str(i)
	print url
	response = urllib.urlopen(url)
	if response.getcode() == '404':
		break
	html = response.read()
	title = titlere.search(html).group(1)
	content = contentre.search(html).group(1)
	f.write('<div class="chapter">')
	f.write('<h2><a name="'+str(i)+'">Chapter '+str(i)+'</a></h2>')
	f.write('<h3>'+title+'</h3>')
	f.write(content)
	f.write('</div>')
	i += 1
	time.sleep(2+3*random.random())

footer = open('hpmor-footer.html', 'r')
f.write(footer.read())

print 'done'
