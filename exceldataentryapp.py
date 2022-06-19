import pandas as pd
#import openpyxl
import PySimpleGUI as sg 

sg.theme('DarkTeal9')


EXCEL_FILE = 'c:/Users/bucke/Desktop/Data_3400/Final Project _TigerWoods/PGATourEventDatabase.xlsx'

df = pd.read_excel(EXCEL_FILE)


layout = [
    
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('EventName', size = (15,2)), sg.InputText(key = 'EventName')],
    [sg.Text('Winner', size = (15,2)), sg.InputText(key = 'Winner')],
    [sg.Text('TourSeason', size = (15,2)), sg.InputText(key = 'TourSeason')],
    [sg.Text('VictoryMargin', size = (15,2)), sg.InputText(key = 'VictoryMargin')],
    [sg.Text('>5CareerWins', size = (15,2)), sg.InputText(key = '>5CareerWins')],
    [sg.Text('Playoff', size = (15,2)), sg.InputText(key = 'Playoff')],
    [sg.Submit(), sg.Exit()]
    
    ]
    
window = sg.Window('PGA Tour Data Entry', layout) 

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index = False)
        sg.popup('Saved.')
        clear_input()
        
window.close()
    

