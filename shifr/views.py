from django.shortcuts import render


class Graph(object):
    letter = ''
    count = 0

def index(request):

    empty = ''
    enty = ''
    lit = ''
    zet = ''

    if request.POST:
        orig = request.POST.get('original')
        step = int(request.POST.get('step'))
        shifr = request.POST.get('shifr')
        shifr_text = request.POST.get('shifr_text')


        if step:
            if shifr == 'deshifr':
                step = -step
                orig = shifr_text
            for let in orig:
                if let.isalpha():
                    local_step = step
                    if let in ['z', 'Z']:
                        local_step -= 26
                    if let in ['a', 'A'] and step < 0:
                        local_step += 26
                    empty += chr(ord(let) + local_step)
                else:
                    empty += let
            if shifr == 'deshifr':
                orig, empty = empty, orig
        else:
            empty = orig
        answer = []

        for lit in range(97, 123):
            object = Graph()
            object.letter = chr(lit)
            object.count = empty.count(chr(lit))
            answer.append(object)

        return render(request, 'shifr/index.html', {'shifr': empty, 'deshifr': orig, 'answer' : answer})

    return render(request, 'shifr/index.html')
