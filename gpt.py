import tkinter as tk

def callback(event):
    # Open the hyperlink
    webbrowser.open_new(event.widget.tag_names(tk.CURRENT)[0])

root = tk.Tk()
text = tk.Text(root, width=30, height=5)
text.pack()

# Set the hyperlink using the "hyperlink" tag
text.insert(tk.END, "Click here to go to Google", "hyperlink")
text.tag_config("hyperlink", foreground="blue", underline=True)

# Bind the callback function to the "hyperlink" tag
text.tag_bind("hyperlink", "<Button-1>", callback)

root.mainloop()