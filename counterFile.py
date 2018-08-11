def count(file_text, words_list):
    if file_text:
        try:
            file = open(str(file_text), 'r')
            full_text = file.readlines()
            file.close()
            count_result = dict()
            for word in words_list:
                for text in full_text:
                    if word in count_result:
                        count_result[word] = count_result[word] + text.count(word)
                    else:
                        count_result[word] = text.count(word)
            return count_result
        except:
            print('Something really bad just happened!')


print(count('mo.txt', ['Mohammad Mahjoub']))