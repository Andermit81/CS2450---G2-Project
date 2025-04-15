'''    
def filter_button():
    filter_window = tk.Toplevel(root)
    filter_window.title("Filter by:")
    filter_window.geometry("300x400")
    
    filter_options = ["Priority", "Tag", "Non-Complete", "Completed", "All"]
    
    user_option = tk.StringVar()
    user_option.set(filter_options[4])
    
    dropdown = OptionMenu(filter_window, user_option, *filter_options)
    dropdown.pack()
    
    
    def press_filter():
        option = user_option.get()
        if option == filter_options[0]:
            filterer = PriorityFilterer()
            filter_subwindow = tk.Toplevel(filter_window)
            filter_subwindow.title("Pick priority")
            filter_subwindow.geometry("150x200")
            subfilter_options = ["High", "Medium", "Low"]
            sub_option = tk.StringVar()
            sub_option.set(subfilter_options[0])
            subdropdown = OptionMenu(filter_subwindow, sub_option, *subfilter_options)
            subdropdown.pack()
            def press_priority():
                option = sub_option.get()
                task_man.tasks = filterer.filter(task_man.tasks, option)
                display_tasks()
                filter_subwindow.destroy()
            subfilter_button = Button(filter_subwindow, text = "Submit", command = press_priority)
            subfilter_button.pack()
            
            
        elif option == filter_options[1]:
            filterer = TagFilterer()
            filter_subwindow = tk.Toplevel(filter_window)
            filter_subwindow.title("Pick tag:")
            filter_subwindow.geometry("150x200")
            tag_choice = tk.Entry(filter_subwindow, width=30)
            tag_choice.pack()            
            def press_tags():
                option = tag_choice.get()
                task_man.tasks = filterer.filter(task_man.tasks, option)
                display_tasks()
                filter_subwindow.destroy()
            subfilter_button = Button(filter_subwindow, text ="Submit", command = press_tags)
            subfilter_button.pack()
            
            
        elif option == filter_options[2]:
            filterer = ShowAllFilterer()
            task_man.tasks = filterer.filter(task_man.tasks)
        elif option == filter_options[3]:
            filterer = DefaultFilterer()
            task_man.tasks = filterer.filter(task_man.tasks)
        else:
            filterer = CompleteFilterer()
            task_man.tasks = filterer.filter(task_man.tasks)
        display_tasks()
        filter_window.destroy()
        return
        
    sub_button = Button(filter_window, text = "Filter", command = press_filter)
    sub_button.pack(padx=20, pady=20)
    '''
