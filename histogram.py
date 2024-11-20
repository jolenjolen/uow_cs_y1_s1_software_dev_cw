# Assuming you have the graphics.py file and data already stored in var data_list and row_length
def taskD(data_list,row_length): 
    win = GraphWin("Histogram", 1000, 750)
    win.setBackground("white")
    title=Text(Point(304, 30), f"Histogram of vehicle frequency per hour ({data_list[0][1]})") 
    title.setSize(15)
    title.setStyle("bold")
    title.draw(win)

    elm_legend= Rectangle(Point(50,50), Point(70,70))
    elm_legend.setFill("pink")
    elm_legend.draw(win)
    elm_text=Text(Point(200, 62), "Traffic at Elm Avenue/Rabbit Road")
    elm_text.draw(win)
    hanley_legend= Rectangle(Point(50,75), Point(70,95))
    hanley_legend.setFill("cyan")
    hanley_legend.draw(win)
    hanley_text=Text(Point(200, 88), "Traffic at Hanley Highway/Westway")
    hanley_text.draw(win)
    
    x_axis = Line(Point(100,500), Point(900,500))
    x_axis.draw(win) 
    hour_margin=0
    for i in range(24):
        numbering=Text(Point(116.6+hour_margin, 520), f"{i}")
        hour_margin+=33.33 
        numbering.draw(win) 
    x_axis_label=Text(Point(500, 560), "Hours 00:00 to 24:00") 
    x_axis_label.setSize(10)
    x_axis_label.draw(win)
    
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    section1_height=Rectangle(Point(1,563), Point(1000,1))
    
    for row in range(row_length):
        hour = int(data_list[row][2][:2])  
        vehicle_count[hour] += 1 
    
    
    max_height = max(vehicle_count)
    if max_height == 0:
        max_height = 1
    
    window_height = 400  
    scaling_factor = window_height / max_height
    
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    

    for row in range(row_length):
        
        if data_list[row][0] == "Hanley Highway/Westway":
            
            hour = int(data_list[row][2][:2])  
            vehicle_count[hour] += 1  
    x1=114
    x2=x1+14
    y1=500 
    y2= 500
    for i in range(len(vehicle_count)):
        constt=vehicle_count[i]*scaling_factor
        bar=Rectangle(Point(x1,y1), Point(x2,y2-constt))
        vehicle_count_per_hr=Text(Point(x1+9, y2-constt-15), f"{vehicle_count[i]}")
        vehicle_count_per_hr.setSize(8)
        vehicle_count_per_hr.setTextColor("dark blue")
        vehicle_count_per_hr.draw(win)
        x1+=33.33
        x2=x1+14
        bar.setFill("cyan")
        bar.draw(win)

    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for row in range(row_length):
        if data_list[row][0] == "Elm Avenue/Rabbit Road":
            
            hour = int(data_list[row][2][:2])  
            vehicle_count[hour] += 1 
    x1=100
    x2=x1+14
    y1=500 
    y2= 500
    for i in range(len(vehicle_count)):
        constt=vehicle_count[i]*scaling_factor
        bar=Rectangle(Point(x1,y1), Point(x2,y2-constt))
        vehicle_count_per_hr=Text(Point(x1+7, y2-constt-15), f"{vehicle_count[i]}")
        vehicle_count_per_hr.setSize(8)
        vehicle_count_per_hr.setTextColor("red")
        vehicle_count_per_hr.draw(win)
        x1+=33.33
        x2=x1+14
        bar.setFill("pink")
        bar.draw(win)
    
    section2_height=Rectangle(Point(1,750), Point(1000,563)) 

    instructions = Text(Point(500, 656), "Click anywhere to close the window")
    instructions.draw(win)

    win.getMouse()
    win.close()
