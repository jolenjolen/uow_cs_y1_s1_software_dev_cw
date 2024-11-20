
def get_filename_from_date(day,month,year): # explain this function 👇

    if month <=9: 
        if day <=9:
            return f"traffic_data0{day}0{month}{year}.csv"
        else:
            return f"traffic_data{day}0{month}{year}.csv"
    else:
        return f"traffic_data{day}{month}{year}.csv"
    
def fetch_data_from_file(filename): # explain this function 👇
    data_list=[]
    
    try:
        with open(filename, 'r') as file: 
            csv_reader = csv.reader(file) 
            header = next(csv_reader)     
            for row in csv_reader:        
                data_list.append(row)
        row_length=len(data_list)
    except FileNotFoundError:
        print("No file was found for this date")
        return "",0
    
    return data_list,row_length

main():
  # ...
  filename=get_filename_from_date(day,month,year) # 👈 explain what this does
  data_list,row_length=fetch_data_from_file(filename) # 👈 explain what this does
  if data_list=="" and row_length==0: ## 👈 explain
      continue                        ## 👈 explain
  # ...
