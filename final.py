import wikipediaapi as wiki
import requests,webbrowser
from tkinter import *

def generate_random_wiki():
    request = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "1",
        "rnnamespace": 0
    }

    try:
        response = request.get(url=url, params=params)
        data = response.json()
        return data["query"]["random"]
    except requests.RequestException as e:
        print(f"Error fetching random wiki: {e}")
        return []

def update_topic():
    global RANDOMS
    RANDOMS = generate_random_wiki()
    random_title = RANDOMS[0]["title"]
    random_link = "https://en.wikipedia.org/wiki/" + random_title.replace(" ", "_")
    button_link.config(command=lambda: webbrowser.open(random_link))
    my_page = my_wiki.page(f"{random_title}")
    title_label.config(text=f"Today's topic: {my_page.title}")
    main_label.config(text=f"{my_page.summary}")

def initialize_gui():
    main_window = Tk()
    main_window.minsize(width=500, height=500)
    main_window.title("Random Wiki Article a day keeps numbness away")

    title_label = Label(text="")
    title_label.config(wraplength=900, padx=20, pady=20, font=("Times New Roman", 24, "bold"))
    title_label.grid(column=0, row=0)

    main_label = Label(text="")
    main_label.config(wraplength=1000, padx=20, pady=20, font=("Times New Roman", 11))
    main_label.grid(column=0, row=1)

    button_link = Button(text="To this wiki", command=lambda: webbrowser.open(random_link))
    button_link.config(wraplength=200, padx=20, pady=20, font=("Times New Roman", 15, "bold"))
    button_link.grid(column=0, row=2)

    button_again = Button(text="New Topic", command=update_topic)
    button_again.config(wraplength=200, padx=20, pady=20, font=("Times New Roman", 15, "bold"))
    button_again.grid(column=0, row=3)

    return main_window, title_label, main_label, button_link

# Main window initialization
my_wiki = wiki.Wikipedia("MyRandomArticle (henriquealexandremelo@hotmail.com)", "en")
main_window, title_label, main_label, button_link = initialize_gui()

# Generating Main topic
update_topic()

# UI main loop
main_window.mainloop()
