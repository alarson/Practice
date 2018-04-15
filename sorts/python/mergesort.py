#python merge sort
#it's been too long since I python'ed and I start work tomorrow. Let's go
#Ari Larson
#8/5/2016

import sys

def main():

	bottom_up()

def bottom_up():
	'''
	'''
	#arr = [[int(i)] for i in sys.argv[1:]]
	arr = [int(i) for i in sys.argv[1:]]
	result = [0]*len(arr)
	print arr
	print result
	splitNmerge(arr,result,0,len(arr)-1)
	print arr

def splitNmerge(arr,result,start,stop):
	'''
	recursively split array, merge from bottom up
	'''
	if(stop-start)<2: #base case, trivially sorted
		return
	mid = (stop-start)/2 #int rounds to lower
	splitNmerge(arr,result,start,mid)
	splitNmerge(arr,result,mid,stop)
	mergeUp(arr,result,start,mid,stop)
	copyBack(arr,result,start,stop)

def mergeUp(arr,result,start,mid,stop):
	'''
	merge arr into result using runs start...mid and mid...stop
	'''
	# for i in range(mid-start):
	# 	for j in range(stop-mid):
	# 		if arr[i] < arr[j]:
	# 			result[]
	mark = start
	for i in arr[start:mid]:
		for j in arr[mid:stop]:
			if(i<j):
				result[mark]=i
				i+=1
			else:
				result[mark]=j
				j+=1
			mark+=1
	copyBack(arr,result,start,stop)

def copyBack(a,b,start,stop):
	'''
	copies b to a for indices start...stop
	'''
	for i in range(start,stop):
		a[i]=b[i]

main()	
