import os
import argparse
parser = parser = argparse.ArgumentParser(description="paper filter")
parser.add_argument('--list', '-l', type=str, default='./paperlists/conferences.txt')
args = parser.parse_args()

def is_blank(ch):
	blank_ch = [' ', '\t', '\n']
	if ch in blank_ch:
		return True
	else:
		return False

def remove_blank_in_end(string):
	length = len(string)
	first_index = 0
	last_index = length
	first_find = False
	last_find = False
	finish = False
	counter = 0
	while not finish and counter < length:
		if not first_find:
			if not is_blank(string[counter]):
				first_find = True
				first_index = counter
		if not last_find:
			if not is_blank(string[length - 1 - counter]):
				last_find = True
				last_index = length - counter
		if first_find and last_find:
			finish = True
		counter += 1
	return string[first_index:last_index]




def parse_keywords(keyword_string):
	keywords = keyword_string.split(',')
	keywords = [remove_blank_in_end(k.lower()) for k in keywords]
	return keywords

def clean_split(string, delimiter=' '):
	sub_strs = string.split(delimiter)
	splits = []
	for sub_str in sub_strs:
		if sub_str is not '':
			splits.append(sub_str)
	return splits

def search_paper(lists, keywords):
	matched = []
	for paper in lists:
		match = True
		for keyword in keywords:
			if paper.find(keyword) == -1:
				match = False
				break
		if match:
			matched.append(paper)
	return matched

def clear_screen():
	os.system('cls')



lists = []
with open(args.list, 'r', encoding='utf-8') as f:
	titles = f.read().split('\n')
	for title in titles:
		words = clean_split(title)
		clean_title = ''
		for word in words:
			clean_title += word + ' '
		clean_title = clean_title[:-1].lower()
		lists.append(clean_title)
print('{0} papers loaded in total.'.format(len(lists)))
exit = False
exit_string = ['exit', 'quit', 'bye']
indent = '    '
while not exit:
	input_str = input('>>> ')
	if input_str in exit_string:
		exit = True
		print('Bye~')
		continue
	elif input_str == 'clear':
		clear_screen()
	else:
		keywords = parse_keywords(input_str)
		matched = search_paper(lists, keywords)
		for title in matched:
			print(indent + title)
		print('{0} papers matched in total.'.format(len(matched)))
