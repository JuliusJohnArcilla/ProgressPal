import tkinter as tk
import datetime
import calendar

month_names = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class ScheduleView:
    def __init__(self, root, control)->None:
        #DEFINE ROOT
        super(ScheduleView, self).__init__()
        self.control = control
        self.root = root
    
    def show(self):
        self.root.title("Calendar")
        
        #DEFINE COLORS
        self.color_background='#2D3033'
        self.color_text = '#FFFFFF'
        self.color_weekdays = '#868C96'
        self.color_days = '#404040'
        self.color_selected_day = '#6D98E7'
        self.color_today = '#E76D6D'
        self.color_toggleMenu ='#868C96'
        #DEFINE CALENDAR
        self.current_month = tk.StringVar()
        self.current_year = tk.StringVar()
        self.selected_day = tk.StringVar()
        self.today = tk.StringVar()

        #SET CURRENT MONTH AND YEAR TO THE CURRENT DATE
        now = datetime.datetime.now()
        self.current_month = now.strftime("%B")
        self.current_year.set(now.year)

        #CREATE CALENDAR
        self.calendar_frame = tk.Frame(self.root, background=self.color_background)
        self.calendar_frame.pack(expand=True, fill='both')

        #TITLE
        self.title_frame = tk.Frame(self.calendar_frame, background=self.color_background)
        self.title_frame.pack(side='top', pady=20)

        #CURRENT MONTH AND YEAR LABEL
        self.current_month_label = tk.Label(self.title_frame, text=self.current_month, font=('Montserrat',24), background=self.color_background, foreground=self.color_text)
        self.current_month_label.pack(side='left', padx=(30,0))
        self.current_year_label = tk.Label(self.title_frame, textvariable=self.current_year, font=('Montserrat',24), background=self.color_background, foreground=self.color_text)
        self.current_year_label.pack(side='left', padx=(10,0))

        #WEEKDAY NAMES
        weekday_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.weekdays_frame = tk.Frame(self.calendar_frame, background=self.color_background)
        self.weekdays_frame.pack(side='top', pady=20)
        for i in range(7):
            weekday_label = tk.Label(self.weekdays_frame, text=weekday_names[i], font=('Montserrat',14), background=self.color_background, foreground=self.color_weekdays, width=8)
            weekday_label.grid(row=0, column=i)

        #DAYS
        self.days_frame = tk.Frame(self.calendar_frame, background=self.color_background)
        self.days_frame.pack(side='top')
        self.day_buttons = [[None]*7 for i in range(6)]
        for i in range(0, 7): # change from range(6) to range(1, 7)
            for j in range(7):
                day_button = tk.Button(self.days_frame, text='', font=('Montserrat',14), background=self.color_days, foreground=self.color_text, width=8, height=4, border=0, command=lambda row=i, col=j: self.select_day(row, col), activebackground='gray')
                self.day_buttons[i-1][j] = day_button
        
        #SELECTED DAY AND TODAY LABEL
        self.selected_day_label = tk.Label(self.calendar_frame, textvariable=self.selected_day, font=('Montserrat',18), background=self.color_background, foreground=self.color_selected_day)
        self.selected_day_label.pack(side='top', pady=(10,0))

        #BUTTON IMPLEMENTATION
        self.toggleButtonOpen = tk.Button(self.root, text='>', width=4, height=2, command = self.toggleMenu, background=self.color_toggleMenu, border = 0)
        self.toggleButtonOpen.place(x=5,y=5)

        self.update_calendar()

    def update_calendar(self):
    # MONTH CALENDAR
        month_num = month_names.index(self.current_month) 
        year_num = int(self.current_year.get())
        month_calendar = calendar.monthcalendar(year_num, month_num)

    # DAY BUTTONS
        for i in range(len(month_calendar)):
            for j in range(len(month_calendar[i])):
                day_text = month_calendar[i][j] #number of days
                if day_text == 0:
                    day_button = tk.Label(
                        self.days_frame,
                        text='',
                        font=('Montserrat', 14),
                        background=self.color_days,
                        foreground=self.color_text,
                        width=7,
                        height=3,
                        border=0,
                    )
                else:
                    day_button = tk.Button(
                        self.days_frame,
                        text=day_text,
                        font=('Montserrat', 14),
                        background=self.color_days,
                        foreground=self.color_text,
                        width=7,
                        height=3,
                        border=0,
                        command=lamb    da row=i, col=j: self.select_day(row, col),
                        activebackground='gray'
                    )
                day_button.grid(row=i, column=j, padx=5, pady=5)
                self.day_buttons[i][j] = day_button
                
                
    def toggleMenu(self):
        
        #TOGGLE MENU
        self.toggleMenuFrame = tk.Frame(self.root, width = 400, height = 750, background=self.color_toggleMenu)
        
        def ToggleClose():
            self.toggleMenuFrame.destroy()
        
        def ToggleButtons(x, y, name, bcolor, cmd):
            toggleButton = tk.Button(self.toggleMenuFrame, text = name, 
                                     width = 65, height = 3, 
                                     background = bcolor, 
                                     foreground = self.color_background, 
                                     command = cmd, 
                                     border=0,
                                     font=('Montserrat',8))
            
            toggleButton.place(x=x,y=y)
        
        def placeholdercmd():
            ToggleClose()
            pass
        
        #TOGGLE BUTTON
        self.toggleButtonClose = tk.Button(self.toggleMenuFrame, text='<', width=4, height=2, command = ToggleClose, background=self.color_toggleMenu, border = 0)
        self.toggleMenu1 = ToggleButtons(0,80, name='H O M E', bcolor=self.color_toggleMenu, cmd=self.SwitchViewHome)
        self.toggleMenu2 = ToggleButtons(0,131, name='M A N A G E   T A S K', bcolor=self.color_toggleMenu, cmd=self.SwitchViewTasks)
        self.toggleMenu3 = ToggleButtons(0,182, name='S C H E D U L E', bcolor=self.color_toggleMenu, cmd=self.ToggleClose)
        self.toggleMenu4 = ToggleButtons(0,233, name='P R O F I L E', bcolor=self.color_toggleMenu, cmd=self.switchViewProfile)


        #IMPLEMENTATION
        self.toggleMenuFrame.place(x=0,y=0)
        self.toggleButtonClose.place(x=5,y=5)
       
    def ToggleClose(self):
        self.toggleMenuFrame.destroy() 
        
    def SwitchViewHome(self):
        self.calendar_frame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewHome()
    
    def SwitchViewTasks(self):
        self.calendar_frame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewTasks()        

    def switchViewProfile(self):
        self.calendar_frame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewProfile()
        
    def select_day(self, row, col):
        pass

    def display_calendar(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    calendar_gui = ScheduleView(root, None)
    root.mainloop()