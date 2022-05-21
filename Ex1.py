# Yêu cầu:
# 1. Cài đặt python
# 2. Cài đặt thư viện trong python: scikit-lean, [scikit-image], pandas
# 3. Nắm được cú pháp python:
# - Làm việc với biến
# - Kiểu dữ liệu cơ bản
# - Kiểu dữ liệu nâng cao (List, Tuple, Dictionary)
# - Toán tử
# - Cấu trúc điều kiện
# - Cấu trúc lặp
# - Sử dụng hàm trong python
# - Sử dụng class
# 4. Trên ngôn ngữ python, thực hiện yêu cầu sau:
# Bài 1: In ra màn hình câu chào: “Hello world”
# Bài 2: Nhập 3 số a, b, c, tính tổng, hiệu, tích, thương của chúng, hiển thị ra màn hình
# Bài 3: Nhập 1 số nguyên n, kiểm tra xem nó là số chẵn hay số lẻ, hiển thị kết quả ra màn hình.
# Bài 4: Nhập 3 số nguyên a, b, c. Hiển thị ra màn hình số lớn nhất và số bé nhất trong 3 số ra màn
# hình.
# Bài 5: Tạo 1 list gồm n phần tử dữ liệu, hiển thị list đã tạo ra màn hình, sắp xếp list và hiển thị
# list sau khi sắp ra màn hình.
# Bài 6: Tạo 1 tuple gồm n phần tử dữ liệu. Hiển thị tuple vừa tạo ra màn hình.
# Bài 7: Tạo 2 biến dictionary tương ứng lưu thông tin của 2 sinh viên. Biết rằng thông tin về mỗi
# sinh viên bao gồm: Mã sv, tên sv, lớp. Hiển thị thông tin của 2 biến dictionary đã tạo ra màn
# hình.

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import sklearn
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import  train_test_split
# from sklearn import metrics as sq
# from sklearn import linear_model
# clf = linear_model.LinearRegression()

#1 
print('Send Hello ')
#2
a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))
c = int(input("Nhap vao c: "))

print("a +b + c =" + str(a + b + c))
print("a - b - c=" + str(a-b-c))
print("a* b * c =" + str(a*b*c))
print("a/b/c="+ str(a/b/c))
#3
n = int(input("Nhap vao so nguyen n: "))
if (n%2==0):
    {
    print("n la so chan")
    }
print("n la so le")
#4
d = int(input("Nhap vao d: "))
e = int(input("Nhap vao e: "))
f = int(input("Nhap vao f: "))

l = [d,e,f]
print('so lon nhat: ',max(l))
print('so be nhat: ',min(l))

#5
list = ['vanchien', 'vandoanh', 'nhat trung','tuan dat']
print(list)
liststt =[6,5,7,2,4,2,8,9]
print(liststt)
liststt.sort()
print(liststt)
#6
tuple = [2,5,5,6,7,80,91,73,56]
print(tuple[4:6])
#7
dict1 = {'msv':'19810340637', 'name':'Chien', 'class':'D14CNPM8'}
dict2 = {'msv':'19810340638', 'name':'Doanh', 'class':'D14CNPM8'}
print(dict1)