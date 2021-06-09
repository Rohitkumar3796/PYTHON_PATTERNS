# DIFFERENT TYPES OF PATTERNS
# print('PATTERN 1')
# n=5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         n=n-1
#         print(' ' * n,end='')
#         print('* ' *i)
# ==============================================
# print('PATTERN 2')
#     *
#    **
#   ***
#  ****
# *****
# n=5
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         n=n-1
#         print(' ' * n,i * '*' )
# =================================================
# print('PATTERN 3')
# n=5
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         n=n-1
#         print('* ' * i , end='')
#         print('' * n)
# =======================================
# print('PATTERN 4')
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         print('* ' * n)
#         n=n-1
# ==========================================
n=5
# print('PATTERN 5')
# *****
#  ****
#   ***
#    **
#     *
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         print(' ' * i,end='')
#         print('*' * n )
#         n = n - 1
# ==============================================
# print('PATTERN 6')
# *****
# ****
# ***
# **
# *
# for i in range(1,n+1):
#     for j in range(i-1,i):
#         print('*' * n )
#         n = n - 1

# print('PATTERN 7')
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         print('* '*n)
# ============================================
# print('PATTERN 8')
# * * * * *
#  * * * * *
# * * * * *
#  * * * * *
# * * * * *
#  * * * * *
# * * * * *
#  * * * * *
# * * * * *
#  * * * * *
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         print('* '*n)
#         print(' *'*n)
# =============================================
# print('PATTERN 9')
# *********
#  *******
#   *****
#    ***
#     *
# space=0
# rows=int(input('enter the number of rows:'))
# for i in range(rows+1,1,-1):
#     a=rows-1
#     for j in range(i,rows,-1):
#         print(space*' ',a*"*"+"*"*rows)
#
#     space=space+1
#     rows=rows-1

# UNDERSTAND THE CONCEPTS
# OF ROW AND COLUMN TO PRINT STAR

# ===========================================