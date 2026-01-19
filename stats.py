def get_word_count(book_text):
        word_list = book_text.split()
        num_words = len(word_list)
        return num_words

def char_count(book_text):
	lowered = book_text.lower()
	chars = {}
	for char in lowered:
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	return chars


def sort_on(item):
    return item["num"]


def sort_list(chars):
    sortd_list = []
    for char in chars:
        order_dic = {"char": char, "num": chars[char]}
        sortd_list.append(order_dic)

    sortd_list.sort(reverse=True, key=sort_on)
    return sortd_list



