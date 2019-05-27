import sqlite3

def draw_html_table(player_list):
    print(player_list)
    s = "<table style='border:1px solid red'>"  
    for row in player_list:  
        s = s + "<tr>"  
        for x in row:  
            s = s + "<td>" + str(x) + "</td>"  
    s = s + "</tr>"  
    return s

def 