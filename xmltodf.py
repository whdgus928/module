def xmltodf():
    import pandas as pd
    import requests
    import bs4
    
    url=f'http://223.130.129.189:9191/getWaterFlux/sujCode={319}&stDt={date}&stTm={hour}&edDt={date}&edTm={hour+1}'
    response = requests.get(url)
    content = response.text
    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('item')
    name_list = [] # 열이름값
    row_list = [] # 행값
    value_list = [] #데이터값 
    
    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        #첫째 행 데이터 수집
        for j in range(0,len(columns)):
            if i ==0:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        row_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list=[]

    #xml값 DataFrame으로 만들기
    tmp_df = pd.DataFrame(row_list, columns=name_list)
    flux_df = pd.concat([flux_df,tmp_df],ignore_index=True)
        
    #corona_df.to_csv('.csv',encoding='utf-8-sig')
    return flux_df
