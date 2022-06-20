import tkinter as tki

main_window=tki.Tk()

def event_tekan():
    label2=tki.Label(main_window, text='Aku ditekan AWOKWOKWOKWOWK')
    label2.pack()


label=tki.Label(main_window, text='Halo sy adalah GUI sederhana \n Good Job Boys')
tombol=tki.Button(main_window, text='TEKAN AKU CUY', command=event_tekan)


label.pack()
tombol.pack()
main_window.mainloop()