import re

f_in = open('text.txt', 'r')

f_out = open('result.txt', 'w')

i = 0
q = 0
m = 0
for line in f_in:
	if '.mp3' in line:
		m += 1
		f_out.write('''
<audio preload="auto" class='pause' id="Player_{}" onended="audioend();">
    <source src="../../audio/{}"/>
</audio>
'''.format(m, line.rstrip()))
	elif '(' in line:
		q += 1
		f_out.write('''
<div id="popup_{}" style="display: none;">
    <div id="okno_{}">
        <p class="okno">{}</p>
        <input type="submit" class='send{}' name="send{}" value ="Kyllä" onclick='instruction();nextstep();'>
        <input type="submit" class='send{}' name="send{}" value ="Ei" onclick='instruction();nextstep();'>
    </form>
    </div>
</div>
'''.format(q, q, line.split('(')[0], q, q, q, q))
	elif not '.mp3' in line and not re.match(r'^\s*$', line):
		i += 1
		words = line.split()
		f_out.write('''
<div id="practice_{}" style="display: none;">
<a href="#" onclick="togglePlay();handler(this);">Tauko</a>
    <span class='text' id='text_{}' style="display: block;">
    <form method="post"  class="post-form" id='post-form-{}'>{{% csrf_token %}}
'''.format(i, i, i))
		for n in range(len(words)):
			if n == len(words)-1:
				f_out.write('\t<span>{}</span>'.format(words[n]))
			else:
				f_out.write('\t<span>{}<input id="{}checkbox{}" class="checkbox{}" type="checkbox" name="check" value="{}"><label class="checkbox_label" for="{}checkbox{}"><span>~</span><span>|</span></label></span>\n'.format(words[n], i, n, i, n, i, n))
		f_out.write('''
    </span>
</div>
''')


f_in.close()
f_out.close()




print('''
<div id="practice_{}" style="display: none;">
<a href="#" onclick="togglePlay();handler(this);">Tauko</a>
    <span class='text' id='text_{}' style="display: block;">
    <form method="post"  class="post-form" id='post-form-{}'>{{% csrf_token %}}
'''.format(i, i, i))