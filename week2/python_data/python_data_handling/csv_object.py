import csv
seoung_nam_data= []
header= []
rownum= 0

with open("korea_floating_population_data.csv","r", encoding="cp949") as p_file:
    csv_data= csv.reader(p_file) #csv객체를이용해서csv_data읽기
    for row in csv_data: #읽어온데이터를한줄씩처리
        if rownum== 0:
            header= row #첫번째줄은데이터필드로따로저장
        location= row[7]
        #“행정구역”필드데이터추출, 한글처리로유니코드데이터를cp949로변환
        if location.find(u"성남시") != -1:
            seoung_nam_data.append(row)#”행정구역”데이터에성남시가들어가있으면seoung_nam_dataList에추가
            rownum+=1
            
with open("seoung_nam_floating_population_data.csv","w", encoding="utf8") as s_p_file:
    writer= csv.writer(s_p_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    # csv.writer를사용해서csv파일만들기delimiter필드구분자# quotechar는필드각데이터는묶는문자, quoting는묶는범위
    
    writer.writerow(header)     # 제목필드파일에쓰기
    for row in seoung_nam_data:
        writer.writerow(row) #seoung_nam_data에있는정보list에쓰기