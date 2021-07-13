line_counter = 0
data_header = []
customer_list = []

with open ("customers.csv") as customer_data:

    while True:
        data = customer_data.readline()
        if not data: break
        if line_counter==0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))

        line_counter += 1


print("Header:\t", data_header) #데이터필드값출력
for  i in range(0,10): #데이터출력(샘플10개만)
    print("Data",i,":\t\t",customer_list[i])
print(len(customer_list)) #전체데이터크기출력