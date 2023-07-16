def latin_kril(text, lang="kril-latin"):
    """ converts Latin letters to Krill and Krill letters to Latin """
    latin_kril = {
        'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е',
        'F': 'Ф', 'f': 'ф', 'G': 'Г', 'g': 'г', 'H': 'Ҳ', 'h': 'ҳ', 'I': 'И', 'i': 'и',
        'J': 'Ж', 'j': 'ж', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м',
        'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'Q': 'Қ', 'q': 'қ',
        'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у',
        'V': 'В', 'v': 'в', 'X': 'Х', 'x': 'х', 'Y': 'Й', 'y': 'й', 'Z': 'З', 'z': 'з',
        'O‘': 'Ў', "O'": "ў", "G'": 'Ғ', "g'": 'ғ', 'Sh': 'Ш', 'sh': 'ш', 'Ch': 'Ч', 'ch': 'ч',
        'C': 'Ц', 'c': 'ц', 'Ng': 'Ң', 'ng': 'ң', "Yo'": "Ё", "yo'": 'ё', "o'":"ў",
    }

    if lang == "latin-kril":
        letters = latin_kril
    elif lang == "kril-latin":
        letters = {v: k for k, v in latin_kril.items()}
    else:
        raise ValueError("Noto'g'ri turi: lotin yoki kril qilib kiriting.")

    natija = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i + 2] in letters:
            natija.append(letters[text[i:i + 2]])
            i += 2
        else:
            natija.append(letters.get(text[i], text[i]))
            i += 1

    return "".join(natija)



def latin_arabic(text, lang="latin-arabic"):
    """ converts Latin letters to Arabic letters and Arabic letters to Latin letters """
    initial_letters = {
        "o'":"او",
        "o":"آ",
        "e":"اي",
        "u":"او",
        "i":"اي",
        "y":"ي",
        "u":"او",
        "e":"اي",
    }
    middle_letters = {
        # "e":"ي",
        "i":"ي"
    }
    double_letters = {
        "sh":"ش" ,
        "ch":"چه",
        "o'":"و",
        "ng":"نك"
    }
    last_letters = {
        "e":"ى",
        "y":"ى",
        "i":"ى"
    }
    tashdid = "\u0651"
    arabic_to_latin = {"A": "ا", "a": "ا", "B": "ب", "b": "ب", "C": "ج", "c": "ج", "D": "د", "d": "د", "E": "إ", "e": "إ", "F": "ف", "f": "ف", "G": "غ", "g": "غ", "H": "ه", "h": "ه", "I": "ئ", "i": "ي", "J": "ج", "j": "ج", "K": "ك", "k": "ك", "L": "ل", "l": "ل", "M": "م", "m": "م", "N": "ن", "n": "ن", "O": "ا", "o": "ا", "P": "پ", "p": "پ" , "Q": "ق", "q": "ق", "R": "ر", "r": "ر", "S": "س", "s": "س", "T": "ت", "t": "ت", "U": "و", "u": "و", "V": "و", "v": "و", "X": "خ", "x": "خ", "Y": "ي", "y": "ي", "Z": "ز", "z": "ز",'C':'چ','c':'چ',"'":"ع"}
    if lang == "arabic-latin":
        initial_letters = {v: k for k, v in initial_letters.items()}
        middle_letters = {v: k for k, v in middle_letters.items()}
        last_letters = {v: k for k, v in last_letters.items()}
        double_letters = {v: k for k, v in double_letters.items()}
        arabic_to_latin = {v: k for k, v in arabic_to_latin.items()}
        
    words = text.split()
    arabic_words = []
    for word in words:
        for letter in double_letters.keys():
            fnd = word.find(letter)

            if fnd != -1:
                for count in range(word.count(letter)):
                    fnd = word.find(letter)

                    if word[fnd:fnd+2] in double_letters:
                        word = word[0:fnd] + double_letters[word[fnd:fnd+2]] + word[fnd+2:] 

        arabic_word = ""
        for i in range(len(word)):
            try:
                if word[i] == word[i-1]:
                    arabic_word += tashdid
                elif i == 0 and word[i].lower() in initial_letters:
                    arabic_word += initial_letters.get(word[i].lower(), word[i].lower())
                elif i == len(word) - 1 and word[i].lower() in last_letters:
                    arabic_word += last_letters.get(word[i].lower(), word[i].lower())
                elif word[i].lower() in middle_letters:
                    arabic_word += middle_letters.get(word[i].lower(), word[i].lower())
                else:
                    arabic_word += arabic_to_latin.get(word[i], word[i])
                    # if word in arabic_to_latin:
                    #   arabic_word += arabic_to_latin.get(word[i], word[i])
            except IndexError as ie:
                pass

        arabic_words.append(arabic_word)
    return ' '.join(arabic_words)