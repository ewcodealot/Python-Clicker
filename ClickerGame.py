
#Made By Emmett Wilson
#Feel free to use this code in your projects, just give me credit! Enjoy!

from guizero import App, Text, PushButton, TextBox, Combo, Window, Picture, info
import time
app = App(title="Clicker Game With Python v1.0")

#Variables
clicks = 0
multiplier = 1
clickspersecond = 0
#Functions

def setFocus():
    click_button.focus()

def click():
    global clicks, multiplier
    clicks += 1*multiplier
    click_text.value = clicks
    if clicks == 1:
        setFocus()

def showStore():
    store.show(wait=True)

def storeError():
    app.info("Error", "Not enough clicks")

def buyItem1():
    global clicks, multiplier
    if clicks >= 10:
        clicks -= 10
        multiplier += 1
        click_text.value = clicks
        multiplierText.value = "Multiplier: "+str(multiplier)
    else:
        store.hide()
        storeError()

def buyItem2():
    global clicks, multiplier
    if clicks >= 50:
        clicks -= 50
        multiplier += 5
        click_text.value = clicks
        multiplierText.value = "Multiplier: "+str(multiplier)
    else:
        store.hide()
        storeError()

def buyItem3():
    global clicks, multiplier
    if clicks >= 500:
        clicks -= 500
        multiplier += 50
        click_text.value = clicks
        multiplierText.value = "Multiplier: "+str(multiplier)
    else:
        store.hide()
        storeError()

def buyItem4(): 
    global clicks, multiplier
    if clicks >= 10000:
        clicks -= 10000
        multiplier += 1000
        click_text.value = clicks
        multiplierText.value = "Multiplier: "+str(multiplier)
    else:
        store.hide()
        storeError()

#Widget Code
click_text = Text(app, text=clicks, height="fill", width="fill", size=70, font="roboto")
click_button = PushButton(app, text="Click me", command=click, align="top", height="fill", width="fill")
store_button = PushButton(app, text="Store", command=showStore, align="bottom", height="1", width="fill")
#Store Widgets
store = Window(app, title="Store", width=400, height=400)
store.hide()
storeTitle=Text(store, text="Store", size=20, font="roboto", align="top")
multiplierText = Text(store, text="Multiplier: "+str(multiplier), align="top")
item1 = PushButton(store, text="+1 Per Click, Cost: 10", width="fill", height="fill", command=buyItem1)
item2 = PushButton(store, text="+5 Per Click, Cost: 50", width="fill", height="fill", command=buyItem2)
item3 = PushButton(store, text="+50 Per Click, Cost: 500", width="fill", height="fill", command=buyItem3)
item4 = PushButton(store, text="+1000 Per Click, Cost: 10000", width="fill", height="fill", command=buyItem4)
#Run the app
app.display()