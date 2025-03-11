from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    input_text = request.GET['fulltext']
    word_list = input_text.split()

    # 과제 - 단어 수 세기
    count = len(word_list)

    # 과제 - 글자 수 세기(띄어쓰기 제외)
    count_no_split = len(input_text) - len(word_list) + 1
    # count_no_split = len(input_text.replace(" ", ""))

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    # 과제 - 가장 많이 나온 단어
    max_frequency = max(word_dictionary.values())

    max_words = []
    for word, freq in word_dictionary.items():
        if freq == max_frequency:
            max_words.append(word)

    return render(request, "result.html", 
                {'alltext': input_text, 
                'dictionary': word_dictionary.items(), 
                'count': count, 
                'count_no_split' : count_no_split, 
                'max_words': max_words, 
                'max_frequency': max_frequency})


# 과제
def hello(request):
    input_text = request.GET['myname']

    return render(request, "hello.html", {'myname' : input_text})