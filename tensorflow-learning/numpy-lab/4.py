import numpy as np

# CRUD ( 추가 수정 삭제 검색 정렬 )
data = np.array([1, 2, 3, 4, 5, 6])
print(data)

# 추가
data = np.append(data, [7, 8])
print(data)

# 중간추가
data = np.insert(data, 1, [9, 10])
print(data)

# 수정
data[0] = 100
print(data)

# Slicing 수정
data[1:3] = (22, 33)
print(data)

data[3:5] = data[5:6]
print(data)

index = data > 4
data[index] = data[index] + 2

# 삭제
data = np.delete(data, 1)
print(data)

# 범위를 지정하여 삭제시 np.s_를 사용하여 삭제가능
# Index Slicing 으로 [2:]를 줄경우 에러발생
data = np.delete(data, np.s_[2:])
# data = np.delete(data, slice(2, len(data)))
print(data)

# 검색
data1 = np.array([10, 20, 30, 40, 50])
search_result_index = np.where(data1 >= 40)
print(search_result_index)
print(data1[search_result_index])

# 30보다 작은 수를 삭제하시오
data1 = np.array([10, 20, 30, 40, 50])
search_result_index = np.where(data1 < 30)
data1 = np.delete(data1, search_result_index)
print(data1)

# 정렬
# 오름차순
data2 = np.array([10, 200, 30, 40, 50])
print(np.sort(data2))

# 내림차순
data2 = np.sort(data2)
print(data2[-1::-1])
print(np.sort(data2)[-1::-1])

# 증감이 마이너스 값이면 시작 인덱스가 -1
print(np.sort(data2)[::-1])

# 정렬시 인덱스 추출
# np.argsort 후에는 정렬 전 인덱스값이 정렬 후 어떻게 변경되는지 추출
data2 = np.array([10, 200, 30, 40, 50])

# 결과값 : [ 0 2 3 4 1 ]
print(np.argsort(data2))
