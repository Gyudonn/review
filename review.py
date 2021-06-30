data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('There is ', len(data), ' data')

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1

for word in wc:
		if wc[word] > 100:
			print(word, wc[word])

print(len(wc))