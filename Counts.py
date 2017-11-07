"""
Author: Andrew Li
"""
import jieba
import xlwt


def replacePunctuations(str_content , str_to = '#'): #注意，是英文的逗号
	#标点符号转化为str_to=‘#’
	char_1 = " …《》，、。？！；：“”‘’'\n\r-=—()（）.【】" 
	'''
	出错：replace(old , new)函数返回一个处理后的新字符串，原字符串不变
	for ch in str_content:
		if ch in char_2:
			str_content.replace(ch , '')
	for ch in str_content:
		if ch in char_1:
			str_content.replace(ch , str_to)
	print(str_content)
	'''
	for char in char_1:
		str_content = str_to.join(str_content.split(char))
	
	while '##' in str_content:
		str_content = str_content.replace('##' , '#')
	#print(str_content[:1000])	
	return str_content


def cutWords(str_content , word_lst):
	word_lst = jieba.lcut(str_content)
	#print(word_lst[:100])
	return word_lst


def countWords(word_lst , word_dict):
	'''
	出错：你是要遍历一个列表的所有元素，而不是遍历列表的长度
	for word in range(len(word_lst)):
	'''
	for word in word_lst:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	#print(word_dict)
	del word_dict['#']
	pairs = list(word_dict.items())
	items = [[x,y] for (y,x) in pairs]
	items.sort(reverse = True)
	return items

def main():
	infile = open('D:/python36/py/123.txt' , 'r')
	str_content = infile.read()
	word_dict = {}
	word_lst = []
	key_lst = []
	str_content_processed = replacePunctuations(str_content)
	word_lst = cutWords(str_content_processed , word_lst)
	#word_dict = countWords(word_lst , word_dict)
	items = countWords(word_lst , word_dict)

	with open('D:/python36/py/conuntWord.txt' , 'w') as outfile:
		for item in items:
			outfile.write(str(item[0]) + '\t'+str(item[1]) + '\n' )

	wkb = xlwt.Workbook(encoding = 'ascii')
	sheet = wkb.add_sheet('wordCount')
	sheet.write(0 , 0 , label = '词频')
	sheet.write(0 , 1 , label = '词语')
	for i in range(len(items)):
		sheet.write(i+1 , 0 , label = items[i][0])
		sheet.write(i+1 , 1 , label = items[i][1])
	#如果存储文件的扩展名为xlsx,excel2010打不开，提示文件格式或文件扩展名无效
	wkb.save('123.xls')

if __name__ == "__main__":
	main()
