 摘自维基百科

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5


 具体代码 
#!/bin/bash
-*-coding:utf-8-*-
#author:zwb
# python
def insert_sort(GivenList):
	length=len(GivenList)
	if length<2:
		return GivenList
	for i in range(1,length):
		j=i-1
		wordtobeinsert=GivenList[i]
		while j>0:
			if GivenList[j]>wordtobeinsert:
				GivenList[j],wordtobeinsert=wordtobeinsert,GivenList[j]
			j-=1
	return GivenList
		
