import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count += 1
		bar.update(count)
		# if count % 1000 == 0:
		# 	print(len(data))

print('There is ', len(data), ' data')

#word_count
start_time = time.time()
wc = {} 
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1
end_time = time.time()
print('Spends ', end_time - start_time, 'seconds to count word.')

while True:
	search = input('Please what word do you want to search: ')
	if search == 'q':
		print('Exit')
		break
	if search in wc:
		print('Found ', search, ' in ', wc[word], ' times')
	else:
		print('Can not find this word: ', search)

# for word in wc:
# 		if wc[word] > 100:
# 			print(word, wc[word])

# print(len(wc))