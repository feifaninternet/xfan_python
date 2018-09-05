# Python 集合

"""
    python 中的集合是一个无序不重复元素的序列
    创建集合的方式：
        1.param = {value01,value02,...}
        2.set(value)
"""

# 集合是会自动去重的
basket = {'orange', 'apple', 'orange', 'pear', 'apple'}
print(basket)

# add() 添加元素
cusMap = {'a', 'b', 'c'}
cusMap.add('d')
print(cusMap)

# 还可以使用update()添加元素，update函数参数可以是列表，元组，字典等
testUpdate = {'xfan', 'python'}
testUpdate.update({1, 3})
print(testUpdate)
testUpdate.update((4, 5))
print(testUpdate)
testUpdate.update([6], [7])
print(testUpdate)

# remove() 移除元素 这种方式移除元素如果元素不存在会发生错误
testUpdate.remove(1)
# testUpdate.remove('hah') 会报错

# discard() 移除元素 这种方式移除元素如果元素不存在不会发生错误
# 这样就不会报错
testUpdate.discard('hah')
print(testUpdate)

# len(s) 集合中元素的个数
print(len(testUpdate))

# x in s 判断集合中是否存在该元素
print(2 in testUpdate)

# clear() 清空集合
testUpdate.clear()
print(testUpdate)
