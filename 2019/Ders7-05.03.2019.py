"""Matris Determinantı Bulma"""

matrix_1=[[1,2],[3,4]]
matrix_2=[[13,2,3,4],[5,6,7,8],[92,10,31,42],[13,134,15,16]]
print(matrix_1 , matrix_2)

def det_from_2_by_2(m_1):
    s_1=m_1[0][0]*m_1[1][1]
    s_2=m_1[0][1]*m_1[1][0]
    s_3=s_1-s_2
    return s_3
print(det_from_2_by_2(matrix_1))
satır_sayısı=len(matrix_1)
sutun_sayısı=len(matrix_1[0])
print((satır_sayısı , sutun_sayısı))

print("------------------------------------------")


def delete_row_col_from_matrix(m_1,m,n):
    result=[]
    size_1=(len(m_1))
    size_2=(len(m_1[0]))
    
    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)
    
    return result
print(matrix_2)
print(delete_row_col_from_matrix(matrix_2,0,0))
print("-----------------------------------------")
def det_from_3_by_3(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(m_1,0,0)
    a_3=det_from_2_by_2(a_2)
    a_4=a_1*a_3

    b_1=m_1[0][1]
    b_2=delete_row_col_from_matrix(m_1,0,1)
    b_3=det_from_2_by_2(b_2)
    b_4=b_1*b_3

    c_1=m_1[0][2]
    c_2=delete_row_col_from_matrix(m_1,0,2)
    c_3=det_from_2_by_2(c_2)
    c_4=c_1*c_3
    
    return a_4-b_4+c_4
print(matrix_2)
print(det_from_3_by_3(matrix_2))

print("---------------------------------------")

def det_from_4_by_4(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(m_1,0,0)
    a_3=det_from_3_by_3(a_2)
    a_4=a_1*a_3

    b_1=m_1[0][1]
    b_2=delete_row_col_from_matrix(m_1,0,1)
    b_3=det_from_3_by_3(b_2)
    b_4=b_1*b_3

    c_1=m_1[0][2]
    c_2=delete_row_col_from_matrix(m_1,0,2)
    c_3=det_from_3_by_3(c_2)
    c_4=c_1*c_3

    d_1=m_1[0][3]
    d_2=delete_row_col_from_matrix(m_1,0,3)
    d_3=det_from_3_by_3(d_2)
    d_4=d_1*d_3

    return a_4-b_4+c_4-d_4
print(matrix_2)
print(det_from_4_by_4(matrix_2))
