from appJar import gui
import os
# function called by pressing the buttons

pink = ''
orange = ''
def press(btn):

    if btn=="Cancel":
        app.stop()
    else:
        B=(app.getEntry('begin'))
        E=(app.getEntry('end'))
        file = open('bridge.csv','w', newline="\n")
        file.write('long,short')
        file.close()

        long_portfolio = ['long_one','long_two','long_three','long_four','long_five']
        short_portfolio = ['short_one','short_two','short_three','short_four','short_five']
        for stock in long_portfolio:
            try:
                longs = (app.getEntry(stock))
                file = open('bridge.csv','a',newline='\n')
                file.write('\n'+longs+',')
                file.close()
            except:
                pass
        for stock in short_portfolio:
            try:
                shorts = (app.getEntry(stock))
                file = open('bridge.csv','a',newline="\n")
                file.write('\n,'+shorts)
                file.close()
            except:
                pass
        os.system('pythonw -m zipline run -f Backtester.py --start '+B+' --end '+E+' -o apple.txt')

if pink=='':
    app = gui()
    app.addLabel("title", "LONG FIVE STOCKS", 0, 0, 4)  # Row 0,Column 0,Span 4
    app.addLabel("long_one", "STOCK ONE:", 1, 0)              # Row 1,Column 0
    app.addEntry("long_one", 1, 1)                           # Row 1,Column 1
    app.addLabel("long_two", "STOCK TWO:", 2, 0)              # Row 2,Column 0
    app.addEntry("long_two", 2, 1)                     # Row 2,Column 1
    app.addLabel("long_three", "STOCK THREE:", 3, 0)              # Row 3,Column 0
    app.addEntry("long_three", 3, 1)                           # Row 3,Column 1
    app.addLabel("long_four", "STOCK FOUR:", 4, 0)              # Row 4,Column 0
    app.addEntry("long_four", 4, 1)                     # Row 4,Column 1
    app.addLabel("long_five", "STOCK FIVE:", 5, 0)              # Row 5,Column 0
    app.addEntry("long_five", 5, 1)                           # Row 5,Column 1

    app.addLabel("title2", "SHORT FIVE STOCKS", 6, 0, 4)  # Row 6,Column 0,Span 24  
    app.addLabel("short_one", "STOCK ONE:", 7, 0)              # Row 7,Column 0
    app.addEntry("short_one", 7, 1)                     # Row 7,Column 1
    app.addLabel("short_two", "STOCK TWO:", 8, 0)              # Row 8,Column 0
    app.addEntry("short_two", 8, 1)                     # Row 8,Column 1
    app.addLabel("short_three", "STOCK THREE:", 9, 0)              # Row 9,Column 0
    app.addEntry("short_three", 9, 1)                     # Row 9,Column 1
    app.addLabel("short_four", "STOCK FOUR:", 10, 0)              # Row 10,Column 0
    app.addEntry("short_four", 10, 1)                     # Row 10,Column 1
    app.addLabel("short_five", "STOCK FIVE:", 11, 0)              # Row 11,Column 0
    app.addEntry("short_five", 11, 1)                     # Row 11,Column 1
    
    app.addLabel("title3", "TIME PERIOD", 12, 0, 4)  # Row 12,Column 0,Span 24  
    app.addLabel("begin", "Begin from(YYYY-M-D):", 13, 0)              # Row 13,Column 0
    app.addEntry("begin", 13, 1)
    app.addLabel("end", "End at(YYYY-M-D):", 14, 0)              # Row 14,Column 0
    app.addEntry("end", 14, 1)
    app.addButtons(["Submit", "Cancel"], press, 15, 0, 2)   # Row 15,Column 0,Span 2
    app.setEntryFocus("long_one")
    app.go()


