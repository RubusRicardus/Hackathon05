import pandas as pd
import numpy as np 
from scipy.sparse import csr_matrix

def create_R_csr_matrix(df, 
                        user_col='user_id', 
                        item_col='item_id',
                        rate_col ='rating'): 
    
	user_list = df[user_col].unique().tolist()
	item_list = df[item_col].unique().tolist()

	# map users to index and vice-versa
	User2Index = {id:idx for idx, id in enumerate(user_list)} 
	Index2User = {i:j for j,i in User2Index.items()} 

	# map items to index and vice-versa 
	Item2Index = {id:idx for idx, id in enumerate(item_list)}  
	Index2Item = {i:j for j,i in Item2Index.items()} 

	data=df[rate_col].tolist()

	row_ind = [User2Index[user] for user in df[user_col]]
	col_ind = [Item2Index[item] for item in df[item_col]]
	
	m = len(user_list) 
	n = len(item_list)

	R_CSR = csr_matrix((data, (row_ind, col_ind)), shape=(m, n))
	
	return R_CSR


