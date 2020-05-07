password = 'a123456'
i = 3
while i > 0 :
	i = i - 1
	pwd = input ('請輸入密碼:')
	if pwd == password:
		print ('登入成功')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print ('您還剩餘', i,'次機會')
		if i == 0:
			print ('密碼嘗試錯誤已達上限,帳戶將被鎖定')
			



