# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZFtk1nFoe6BmWX_5rk4hRoO8lO40IZ-M
"""

import pandas as pd
guruh= pd.DataFrame({
                  'Ism': ['Dilyorbek','Zikirillo','Behruzbek','SHohruxbek','Bekzodbek','Bekmurod'   ],
                  'Familya': [  'Yusupov','Mahsudov','Yunusaliyev','G`ofurjonov','Murodjonov','Mahmudov'  ],
                  'Yashash manzili':[  "Yaypan","Qo`qon","Beshariq","Namangan","Beshariq","Andijon"  ],
                  'Telefon raqam':['+998940334805','+998956651255','+998901562323','+998950225653','+998946458512','+998934561239'],

})
print(guruh)

guruh.to_excel('guruh.xlsx')