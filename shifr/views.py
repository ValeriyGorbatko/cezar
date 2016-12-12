from django.shortcuts import render


# def index(request):
#     if request.POST: # проверяешь что пришел ПОСТ, тогда берез из него данные
#         orig = request.POST['original']
#         ste = request.POST['step']
#     for letter in orig:
#         global orig
#         orig+="".join(chr(ord(letter)+ste))
#         ste+=letter + "->" + orig + ""
def index(request):
    empty = ''
    enty = ''

    if request.POST:
        orig = request.POST.get('original')
        step = request.POST.get('step')

        shifr = request.POST.get('shifr')

        if step:
            step=int(step)
            if shifr == 'deshifr':
                step = -step
            for let in orig:
                # empty += chr(ord(let) + step)
                empty = ord(let)

                if let.isalpha():
                    empty = empty + step
                    offset = 65
                    if let.islower():
                        offset = 97
                        while empty < offset:
                            empty += 26
                        while empty > offset + 25:
                            empty -= 26
                        enty += chr(empty)






    # letter = ord('a')
    # letter2 = ord('z')
    # letter3 = ord('A')
    # letter4 = ord('Z')
    # for letter in range(97, 123):
    #     print(chr(letter))
    # for letter in range(65, 91):
    #     print(chr(letter))





    # ord()
    # chr()

    # orig = request.POST['original']
    # alphabet = list('abcdefghijklmnopqrstuvwxyz')
    # ste = request.POST['step']
    # cipher = ''
    # for c in orig:
    #     cipher += alphabet[(alphabet.index(c) + ste)]

    return render(request, 'shifr/index.html', {'shifr': enty, 'deshifr':  })
