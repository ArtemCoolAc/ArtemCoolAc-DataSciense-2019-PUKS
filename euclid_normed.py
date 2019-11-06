from sklearn.metrics.pairwise import euclidean_distances
import numpy
import csv

coeffs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # здесь менять коэффициенты, ниже по ключам они же

file = open('DS2019/DataScience-2019-PUKS/summary', 'r')
reader = csv.DictReader(file, delimiter=';')
items = list()
indices = list()
for row in reader:
    item = list([int(row['quantity']), int(row['had_meal']), int(row['premium']), int(row['forum_premium']), int(row['had_agentinfo']), int(row['had_baggage']), int(row['issue_baggage']), int(row['nullsomeinfo']), int(row['nulltraveldoc']), int(row['nullbirthdate']), int(row['maxflight']), int(row['paxdoublingdata'])])
    items.append(item)
    indices.append(row['paxid'])
matr = list()
maxes = [0 for i in range(12)]
for i in range(12):
    for j in range(len(items)):
        if abs(items[j][i]) > maxes[i]:
            maxes[i] = abs(items[j][i])
print(maxes)
for i in range(12):
    for j in range(len(items)):
        items[j][i] = items[j][i] / abs(maxes[i]) * coeffs[i]
for item in items:
    matr.append(numpy.array(item))
standard = numpy.zeros(12).reshape(1,-1)
matrix = list()
for elem in matr:
    matrix.append(euclidean_distances(standard, elem.reshape(1,-1)))
sorted_matrix = list()
i = 0
for it in indices:
    #print(matrix[i-1][0][0])
    inserted = dict()
    inserted['index'] = int(it) 
    inserted['metrics'] = matrix[i][0][0]
    i += 1
    sorted_matrix.append(inserted)
#print(sorted_matrix)
sorted_matrix = sorted(sorted_matrix, key=lambda x: x['metrics'], reverse=True)
file2 = open('sorted_matrix_normed', 'w')
for elem in sorted_matrix:
    file2.write('{},{}\n'.format(elem['index'], elem['metrics']))
file.close()
file2.close()

