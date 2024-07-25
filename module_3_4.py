#Пункты задачи:
#Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):
    #Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []
    #При помощи цикла for переберите предполагаемо подходящие слова.
    for word_ in other_words:
        #При проверке наличия одного слова в составе другого стоит учесть, что регистр символов не должен влиять ни на
        #что. ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
        if str.upper(word_) == str.upper(root_word) or str.upper(root_word) in str.upper(word_) or str.upper(word_) in str.upper(root_word):
            same_words.append(word_)
    return same_words


#Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
#После цикла верните образованный функцией список same_words.
#Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
root_one = 'Rich'
list_words1 = ['ricHiest', 'orIchalcum', 'cheers', 'richies']
result1 = single_root_words(root_one, *list_words1)
root_two = 'Disablement'
list_words2 = ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel']
result2 = single_root_words(root_two, *list_words2)
print(f'Слова, однокоренные слову {root_one} из списка {list_words1}:')
print(result1)
print(f'Слова, однокоренные слову {root_two} из списка {list_words2}:')
print(result2)