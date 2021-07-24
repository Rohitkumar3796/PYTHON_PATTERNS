# DIFFERENT TYPES OF PATTERNS
# print('PATTERN 1')
# n=5
# for i in range(1,n+1):
#     for j in range(i,i+1):
#         n=n-1
#         print(' ' * n,end='')
#         print('* ' *i)
# ===============================
# n=5
# for i in range(1, n+1 ):
#     print(' ' * (n-i), i * '* ')
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# ==============================================
# print('PATTERN 2')
# n=5
# for i in range(1,n+1):
#     for j in range(i,n):
#         print('_' * 1, end=' ')
#     print('* ' * i)

# METHOD 2
# for j in range(1,n+1):
#     print('  ' * (n-j), '* ' * j)

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
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
# n=5
# for i in range(1, n+1 ):
#     print( i * '* ')
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
# n=5
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
# n=5
# for i in range(1,n+1):
#     for j in range(i,i+1):
#             print(' ' * (i-1), '*' * ((n-i)*2+1),' ' * i)

# 2nd METHOD
# n=5
# for i in range(n, 0, -1):
#     for j in range(0,n - i): #1st turn it print  0,2nd turn (0,1),3rd(0,2)
#
#         print(' ', end='')  # printing space and staying in same line
#
#     for j in range(0,2*i-1):
#         print('*',end='')  # printing * and staying in same line
#      # printing new line
#     print()
# 3rd Method
# n=int(input("enter the number"))
# for i in range(1,n):
#     for j in range(1,(n*2)-i):
#         if (j-1)>=i and j < ((n*2)-1):
#             print('*',end='')
#         else:
#             print(' ',end='')
# 
#     print()
# ===========================================
