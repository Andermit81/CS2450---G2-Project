from tkinter import ttk
from .colors import (  
    TASK_AREA_BG,
    TASK_TEXT_COLOR,
    BG_COLOR,
    HEADER_COLOR
)

def configure_treeview_styles():
    """Configures all Treeview-related styling"""
    style = ttk.Style()
    style.theme_use("default")
    
    # Treeview main style
    style.configure("Treeview",
                    background=TASK_AREA_BG,
                    foreground=TASK_TEXT_COLOR,
                    fieldbackground=BG_COLOR,
                    rowheight=25,
                    font=('Arial', 15))
    
    # Treeview heading style
    style.configure("Treeview.Heading",
                    background=HEADER_COLOR,
                    foreground="black",
                    font=('Arial', 15, 'bold'))
    
    # Treeview tags configuration (if used elsewhere)
    # Note: Tag configurations need to stay with Treeview creation
