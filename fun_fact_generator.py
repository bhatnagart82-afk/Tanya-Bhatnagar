import requests#• requests: This library is used to talk to the internet. It goes to a website API, grabs data, and brings it back into Python.
from pywebio.input import *#• pywebio imports (input, output, session): This library turns your Python script into an interactive webpage without needing to write HTML, CSS, or JavaScript.
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):#• clear(): This wipes the webpage clean. It deletes the old text and old buttons so that things don't pile up on top of each other every time you click.
#• put_html(...): It redraws the title and smiley face header at the top of the freshly cleared page.

    clear()
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    # Using the exact endpoint matching the intended data format
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    try:
        response = requests.get(url)
        # Safely parse JSON directly via requests
        data = response.json() 
        useless_fact = data.get('text', 'Could not find a fact. Try clicking again!')
    except Exception as e:
        useless_fact = "Failed to retrieve a fact due to a network connection error."

    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')], 
        onclick=get_fun_fact
    )

if __name__ == '__main__':
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'#•  It draws the header layout at the top of the webpage. It displays the title "Fun Fact Generator" along with a smiley face icon image pulled from the GeeksforGeeks website.
    )
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')], 
        onclick=get_fun_fact # put_buttons(...): It places a green button labeled "Click me" on the screen. The crucial part here is onclick=get_fun_fact, which tells the program: "Keep an eye on this button. If the user clicks it, immediately run the get_fun_fact function."
    )
    hold()#• This keeps the web page open and running. Without this, the script would finish running in less than a second and instantly close the page.

