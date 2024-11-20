
def get_filename_from_date(day,month,year): 

    if month <=9: 
        if day <=9:
            return f"traffic_data0{day}0{month}{year}.csv"
        else:
            return f"traffic_data{day}0{month}{year}.csv"
    else:
        return f"traffic_data{day}{month}{year}.csv"
    
def fetch_data_from_file(filename): 
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
  filename=get_filename_from_date(day,month,year) 
  data_list,row_length=fetch_data_from_file(filename)
  if data_list=="" and row_length==0:
      continue                        
  # ...
