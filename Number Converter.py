import tkinter as tk
import math
import string

window = tk.Tk()
window.title('Number Converter')
window.iconbitmap(r'E:\Programming\Python\Python GUI\Number Converter\converter.ico')

window.geometry(f'{600}x{650}+{400}+{30}')
window.resizable(False , False)
window.configure(bg = '#FFFFCD')

def dec_window():
    for widget in window.winfo_children():
        widget.destroy()

    def all_dec():
        numbers = string.digits
        n = entry.get()
        answer.set(f'{n}')
        if all(char in numbers for char in n):
            answer1.set(f'{'{0:b}'.format(int(n))}')
            answer2.set(f'{'{0:o}'.format(int(n))}')
            answer3.set(f'{'{0:X}'.format(int(n))}')
        
        else:
            answer.set(f'Invalid Decimal Number')

    def clear_entries():
        entry.delete(0 , tk.END)
        answer.set('')
        answer1.set('')
        answer2.set('')
        answer3.set('')

    answer = tk.StringVar()
    answer1 = tk.StringVar()
    answer2 = tk.StringVar()
    answer3 = tk.StringVar()

    label = tk.Label(
        text='Decimal Number Converter', font=('Arial' , 30), bg='#FFFFCD'
    )
    label.pack()

    entry_label = tk.Label(
        text = 'Enter decimal number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    entry_label.place(x=50 , y=100)

    entry = tk.Entry(
        font=('Arial' , 25) , width=25
    )
    entry.place(x=50 , y=150)

    button = tk.Button(
        text='= Convert', width=10, height=1, bg='#66FF2E',font=('Times New Roman", Times, serif' , 15 ),
        command=all_dec
    )
    button.place(x=50 , y=200)

    button = tk.Button(
        text='X Clear' ,  width=7, height=1, bg='#E5E5E5',font=('"Times New Roman", Times, serif' , 15),
        command=clear_entries
    )
    button.place(x=180 , y=200)

    label = tk.Label(
        text='Binary Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=270)

    bin_entry = tk.Entry(
        textvariable=answer1 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    bin_entry.place(x=50 , y=310)

    label = tk.Label(
        text='Octal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=370)

    oct_entry = tk.Entry(
        textvariable=answer2 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    oct_entry.place(x=50 , y=410)

    label = tk.Label(
        text='Hexadecimal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=470)
    
    hex_entry = tk.Entry(
        textvariable=answer3 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    hex_entry.place(x=50 , y=510)

    output_label = tk.Label(
        textvariable=answer , font=('Arial' , 25 , 'bold') , fg='red' , bg='#FFFFCD'
    )
    output_label.place(x=50 , y=560)

    back_button = tk.Button(
        text='Back' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command = main_window
    )
    back_button.place(x=10 , y=600)

    close_button = tk.Button(
        text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command =  window.destroy
    )
    close_button.place(x=500 , y=600)

def bin_window():
    for widget in window.winfo_children():
        widget.destroy()

    def all_bin():
        n = entry.get()
        answer.set(f'{n}')
        if not all(char in '01' for char in n):
            answer.set("Invalid binary number")
            return
        
        integer_sum = 0 
        for i in range(1 , len(n)+1):
            integer_sum += int(n[i-1]) * math.pow(2 , len(n)-i)                        
        answer1.set(f'{int(integer_sum)}')

        dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
        s = ''
        if len(n)%4 == 0:
            p = n
        else:
            t = 4-len(n)%4
            p = n.zfill(len(n)+t)

        for i in range((len(p)-4), -1 , -4):
            l = (p[i:i+4])
            sum = 0
            for x in range(1 , len(l)+1):
                t = int(l[len(l)-x]) * math.pow(2 , (x-1))
                sum += t
            if int(sum) in dic:
                d = (dic.get(int(sum)))
                s = str(d) + s
            else:
                s = str(int(sum)) + s
        answer2.set(f'{s}')
                
        s = ''
        if len(n)%3 == 0:
            p = n
        else:
            t = 3-len(n)%3
            p = n.zfill(len(n)+t)
                    
        for i in range((len(p)-3), -1 , -3):
            l = (p[i:i+3])
            sum = 0
            for x in range(1 , len(l)+1):
                t = int(l[len(l)-x]) * math.pow(2 , (x-1))
                sum += t
            s = str(int(sum)) + s
        answer3.set(f'{s}')

    def clear_entries():
        entry.delete(0, tk.END)
        answer1.set("")
        answer2.set("")
        answer3.set("")
        answer.set("")

    answer = tk.StringVar()
    answer1 = tk.StringVar()
    answer2 = tk.StringVar()
    answer3 = tk.StringVar()

    label = tk.Label(
        text='Binary number converter', font=('"Times New Roman", Times, serif' , 35), bg='#FFFFCD'
    )
    label.pack()

    label = tk.Label(
        text='Enter binary number', font=('Times New Roman' , 20), bg='#FFFFCD'
    )
    label.place(x=50 , y=100)

    entry = tk.Entry(
        font=('Arial', 25), width=25,
    )
    entry.place(x=50 , y=150)

    button = tk.Button(
        text='= Convert', width=10, height=1, bg='#66FF2E',font=('Times New Roman", Times, serif' , 15 , 'bold'),
        command=all_bin
    )
    button.place(x=50, y=200)

    button = tk.Button(
        text='X Clear', width=7, height=1, bg='#E5E5E5',font=('"Times New Roman", Times, serif' , 15 , 'bold'),
        command=clear_entries
    )
    button.place(x=210, y=200)

    label = tk.Label(
        text='Decimal number', font=('Times New Roman' , 20), bg='#FFFFCD'
    )
    label.place(x=50 , y=270)

    dec_entry = tk.Entry(
        textvariable=answer1, font=('Arial', 25), width=25, state='disabled'
    )
    dec_entry.place(x=50 , y=310)

    label = tk.Label(
        text='Octal number', font=('Times New Roman' , 20), bg='#FFFFCD'
    )
    label.place(x=50 , y=370)

    oct_entry = tk.Entry(
        textvariable=answer3 , font=('Arial', 25), width=25, state='disabled'
    )
    oct_entry.place(x=50 , y=410)

    label = tk.Label(
        text='Hexadecimal number', font=('Times New Roman' , 20), bg='#FFFFCD'
    )
    label.place(x=50 , y=470)

    hex_entry = tk.Entry(
        textvariable=answer2 , font=('Arial', 25), width=25, state='disabled'
    )
    hex_entry.place(x=50 , y=510)

    output_label = tk.Label(
        textvariable=answer, font=('"Times New Roman", Times, serif' , 25 , 'bold'), bg='#FFFFCD', fg='red',
    )
    output_label.place(x=50 , y=560)

    back_button = tk.Button(
        text='Back' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command = main_window
    )
    back_button.place(x=10 , y=600)

    close_button = tk.Button(
        text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command =  window.destroy
    )
    close_button.place(x=500 , y=600)

def oct_window():
    for widget in window.winfo_children():
        widget.destroy()

    def all_oct():
        n = entry.get()
        answer.set(f'{n}')
        if all(char in '01234567' for char in n):
            s = ''
            for i in n:
                t = '{0:b}'.format(int(i)).zfill(3)
                s = s + str(t)
            answer1.set(f'{s}')
        
            sum = 0
            s = ''
            for i in n:
                t = '{0:b}'.format(int(i)).zfill(3)
                s = s + str(t)
            for x in range(1, len(s)+1):
                t = int(s[len(s)-x])
                sum += t * math.pow(2 , (x-1))
            answer2.set(f'{int(sum)}')

            s = ''
            s1 = ''
            dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
            for i in n:
                t = '{0:b}'.format(int(i)).zfill(3)
                s = s + str(t)

            if len(s)%4 == 0:
                p = s
            else:
                t = 4 - len(s)%4
                s = s.zfill(len(s) + t)

            for x in range(0 , (len(s)) , 4):
                sum = 0
                p = (s[(x):(x+4)])
                for i in range(1 , len(p)+1):
                    t = int(p[i-1]) * math.pow(2 , len(p)-i)
                    sum += t
                if int(sum) in dic:
                    d = dic.get(int(sum))
                    s1 = s1 + str(d)
                else:
                    s1 = s1 + str(int(sum))
            answer3.set(f'{s1}')
        
        else:
            answer.set(f'Invalid Octal Number')

    def clear_entries():
        entry.delete(0 , tk.END)
        answer.set('')
        answer1.set('')
        answer2.set('')
        answer3.set('')

    answer = tk.StringVar()
    answer1 = tk.StringVar()
    answer2 = tk.StringVar()
    answer3 = tk.StringVar()

    label = tk.Label(
        text='Octal Number Converter', font=('Arial' , 30), bg='#FFFFCD'
    )
    label.pack()

    entry_label = tk.Label(
        text = 'Enter octal number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    entry_label.place(x=50 , y=100)

    entry = tk.Entry(
        font=('Arial' , 25) , width=25
    )
    entry.place(x=50 , y=150)

    button = tk.Button(
        text='= Convert', width=10, height=1, bg='#66FF2E',font=('Times New Roman", Times, serif' , 15 ),
        command=all_oct
    )
    button.place(x=50 , y=200)

    button = tk.Button(
        text='X Clear' ,  width=7, height=1, bg='#E5E5E5',font=('"Times New Roman", Times, serif' , 15),
        command=clear_entries
    )
    button.place(x=180 , y=200)

    label = tk.Label(
        text='Binary Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=270)

    bin_entry = tk.Entry(
        textvariable=answer1 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    bin_entry.place(x=50 , y=310)

    label = tk.Label(
        text='Decimal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=370)

    oct_entry = tk.Entry(
        textvariable=answer2 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    oct_entry.place(x=50 , y=410)

    label = tk.Label(
        text='Hexadecimal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=470)

    hex_entry = tk.Entry(
        textvariable=answer3 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    hex_entry.place(x=50 , y=510)

    output_label = tk.Label(
        textvariable=answer, font=('"Times New Roman", Times, serif' , 25 , 'bold'), bg='#FFFFCD', fg='red',
    )
    output_label.place(x=50 , y=560)

    back_button = tk.Button(
        text='Back' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command = main_window
    )
    back_button.place(x=10 , y=600)

    close_button = tk.Button(
        text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command =  window.destroy
    )
    close_button.place(x=500 , y=600)

def hex_window():
    for widget in window.winfo_children():
        widget.destroy()
    
    def all_hex():
        n = entry.get()
        n = n.upper()
        answer.set(f'{n}')
        dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        if all(char in '0123456789ABCDEF' for char in n):
            binary_part = ''
            int_part = []
            for i in (n):
                if i in dic:
                    int_part.append(dic.get(i))
                else:
                    int_part.append(i)
            for i in int_part:
                binary_part += '{0:b}'.format(int(i)).zfill(4)
            answer1.set(f'{binary_part}')

            binary_part = ''
            int_part = []
            integer_sum = 0
            for i in (n):
                if i in dic:
                    int_part.append(dic.get(i))
                else:
                    int_part.append(i)

            for i in int_part:
                binary_part += '{0:b}'.format(int(i)).zfill(4)
            l = binary_part

            for i in range(1 , len(l)+1):
                integer_sum += int(l[i-1]) * math.pow(2 , len(l)-i)
            answer2.set(f'{int(integer_sum)}')

            bin_part = ''
            int_part = []
            for i in (n):
                if i in dic:
                    int_part.append(dic.get(i))
                else:
                    int_part.append(i)

            for i in int_part:
                l = '{0:b}'.format(int(i)).zfill(4)
                bin_part = bin_part + str(l)

            if len(bin_part)%3 == 0:
                p = bin_part
            else:
                t = 3 - len(bin_part)%3
                p = bin_part.zfill(len(bin_part) + t)

            s = ''
            for x in range(0 , len(p) , 3):
                sum = 0
                y = (p[x:x+3])
                for i in range(1 , len(y)+1):
                    d = int(y[i-1]) * math.pow(2 , len(y)-i)
                    sum += int(d)
                s += str(sum)
            answer3.set(f'{s}')

        else:
            answer.set(f'Invalid Hexadecimal Number')

    def clear_entries():
        entry.delete(0 , tk.END)
        answer.set('')
        answer1.set('')
        answer2.set('')
        answer3.set('')

    answer = tk.StringVar()
    answer1 = tk.StringVar()
    answer2 = tk.StringVar()
    answer3 = tk.StringVar()

    label = tk.Label(
        text='Hexadecimal Number Converter', font=('Arial' , 30), bg='#FFFFCD'
    )
    label.pack()

    entry_label = tk.Label(
        text = 'Enter hexadecimal number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    entry_label.place(x=50 , y=100)
    entry = tk.Entry(
        font=('Arial' , 25) , width=25
    )
    entry.place(x=50 , y=150)

    button = tk.Button(
        text='= Convert', width=10, height=1, bg='#66FF2E',font=('Times New Roman", Times, serif' , 15 ),
        command=all_hex
    )
    button.place(x=50 , y=200)

    button = tk.Button(
        text='X Clear' ,  width=7, height=1, bg='#E5E5E5',font=('"Times New Roman", Times, serif' , 15),
        command=clear_entries
    )
    button.place(x=180 , y=200)

    label = tk.Label(
        text='Binary Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=270)
    bin_entry = tk.Entry(
        textvariable=answer1 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    bin_entry.place(x=50 , y=310)

    label = tk.Label(
        text='Decimal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=370)
    oct_entry = tk.Entry(
        textvariable=answer2 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    oct_entry.place(x=50 , y=410)

    label = tk.Label(
        text='Octal Number' , font=('Times New Roman' , 20) , bg='#FFFFCD'
    )
    label.place(x=50 , y=470)
    hex_entry = tk.Entry(
        textvariable=answer3 , font=('Arial' , 25) , width=25 , state='disabled'
    )
    hex_entry.place(x=50 , y=510)

    output_label = tk.Label(
        textvariable=answer, font=('"Times New Roman", Times, serif' , 25 , 'bold'), bg='#FFFFCD', fg='red',
    )
    output_label.place(x=50 , y=560)

    back_button = tk.Button(
        text='Back' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command = main_window
    )
    back_button.place(x=10 , y=600)

    close_button = tk.Button(
        text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command =  window.destroy
    )
    close_button.place(x=500 , y=600)
    
def main_window():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(
    text='Number Converter', font=('"Times New Roman", Times, serif' , 35 , 'bold'), bg='#FFFFCD'
    )
    label.pack()

    label = tk.Label(
        text='Select the desired conversion operation', font=('"Times New Roman", Times, serif' , 20), bg='#FFFFCD' , fg='#002EFF'
    )
    label.pack(pady=20)

    dec_button = tk.Button(
        text='Decimal Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
        command=dec_window
    )
    dec_button.pack(pady=20)

    bin_button = tk.Button(
        text='Binary Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
        command=bin_window
    )
    bin_button.pack(pady=20)

    oct_button = tk.Button(
        text='Octal Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
        command=oct_window
    )
    oct_button.pack(pady=20)

    hex_button = tk.Button(
        text='Hexadecimal Number Converter' , width=27 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
        command=hex_window
    )
    hex_button.pack(pady=20)

    close_button = tk.Button(
        text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
        command =  window.destroy
    )
    close_button.pack(pady=20)

#Main window
label = tk.Label(
    text='Number Converter', font=('"Times New Roman", Times, serif' , 35 , 'bold'), bg='#FFFFCD'
)
label.pack()

label = tk.Label(
    text='Select the desired conversion operation', font=('Calibri' , 20), bg='#FFFFCD' , fg='#002EFF'
)
label.pack(pady=20)

dec_button = tk.Button(
    text='Decimal Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
    command=dec_window
)
dec_button.pack(pady=20)

bin_button = tk.Button(
    text='Binary Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
    command=bin_window
)
bin_button.pack(pady=20)

oct_button = tk.Button(
    text='Octal Number Converter' , width=25 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
    command=oct_window
)
oct_button.pack(pady=20)

hex_button = tk.Button(
    text='Hexadecimal Number Converter' , width=27 , height=2 , bg='light blue' , font=('Candara Light' , 15 , 'bold'),
    command=hex_window
)
hex_button.pack(pady=20)

close_button = tk.Button(
    text='Close' , width=7 , height=1 , bg='#FF4444' , font=('Candara Light' , 15 , 'bold'),
    command =  window.destroy
)
close_button.pack(pady=20)

window.mainloop()