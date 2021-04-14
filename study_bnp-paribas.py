def kesson_table(df): 
    null_val = df.isnull().sum()
    percent = 100 * df.isnull().sum()/len(df)
    print(df.shape[1])
    cnt = []
    val = []
    pst = []
    for count in range(df.shape[1]):
        if null_val[count] != 0:
            cnt.append(count)
            val.append(null_val[count])
            pst.append(percent[count])
    cnt = pd.DataFrame(cnt)        
    val = pd.DataFrame(val)
    pst = pd.DataFrame(pst)
    kesson_table = pd.concat([cnt, val, pst], axis=1)
    kesson_table_ren_columns = kesson_table.rename(
    columns = {0 : 'Number', 1 : '欠損数', 2 : '%'})
    return kesson_table_ren_columns
kesson_table(train)
train["v1"] = train["v1"].fillna(train["v1"].median())
train["v2"] = train["v2"].fillna(train["v2"].median())
kesson_table(train)