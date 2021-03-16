import PySimpleGUIQt as sg
import pickle
#Create a layout to the add values stuff
layout = [[ sg.Text('Stuff to do                                                                          '),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(" ")],
          [sg.Text('DATA MAX')],
          [sg.Input()],
          [sg.Text("")],
          [sg.Button('Lista'),sg.Button("Add")]]

#create a shortcut do call the tables
win1 = sg.Window('Add', layout)
#keep the win2 closed
win2_active=False


while True:
    #take the values and open a file called data.dat
    ev1, vals1 = win1.read(timeout=100)
    v1=vals1[0]
    v2=vals1[1]
    stuff=pickle.load(open("data.dat", "rb"))
    
    #when the button ADD is press take the data and do suff
    #save on data.dat
    if ev1 == "Add":
        if stuff[1] == '':
            stuff[1]=(v1+' '+v2)
            pickle.dump(stuff, open("data.dat","wb"))
        elif stuff[2] == '':
            stuff[2]=(v1+' '+v2)
            pickle.dump(stuff, open("data.dat","wb"))
        elif stuff[3] == '':
            stuff[3]=(v1+' '+v2)
            pickle.dump(stuff, open("data.dat","wb"))
        elif stuff[4] == '':
            stuff[4]=(v1+' '+v2)
            pickle.dump(stuff, open("data.dat","wb"))
        elif stuff[5] == '':
            stuff[5]=(v1+' '+v2)
            pickle.dump(stuff, open("data.dat","wb"))

    #cloase the tab if you click on quit cross
    if ev1 == sg.WIN_CLOSED:
        break

    #when lista is clicked opens the second tab
    if ev1 == 'Lista'  and not win2_active:
        win2_active = True
        #hide the first tab
        win1.Hide()
        #load o treco
        layout2 = [[sg.Text('                                                        Lista                                                       ')],     
                   [sg.Text('  1'),sg.Text(stuff[1]),sg.Button('Del-1')],
                   [sg.Text()],
                   [sg.Text('  2'),sg.Text(stuff[2]),sg.Button('Del-2')],
                   [sg.Text()],
                   [sg.Text('  3'),sg.Text(stuff[3]),sg.Button('Del-3')],
                   [sg.Text()],
                   [sg.Text('  4'),sg.Text(stuff[4]),sg.Button('Del-4')],
                   [sg.Text()],
                   [sg.Text('  5'),sg.Text(stuff[5]),sg.Button('Del-5')],
                   [sg.Text()],
                   [sg.Button('Exit')]]
        #take data
        win2 = sg.Window('Tabela ', layout2)

        #delet the values when the del bottuns are press
        while True:
            ev2, vals2 = win2.read()
            if ev2 == "Del-1":
                stuff[1]=('')
                pickle.dump(stuff, open("data.dat","wb"))

            if ev2 == "Del-2":
                stuff[2]=('')
                pickle.dump(stuff, open("data.dat","wb"))

            if ev2 == "Del-3":
                stuff[3]=('')
                pickle.dump(stuff, open("data.dat","wb"))

            if ev2 == "Del-4":
                stuff[4]=('')
                pickle.dump(stuff, open("data.dat","wb"))

            if ev2 == "Del-5":
                stuff[5]=('')
                pickle.dump(stuff, open("data.dat","wb"))

            #cloase tab
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break