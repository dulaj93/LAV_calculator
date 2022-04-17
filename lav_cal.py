from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from decimal import Decimal


class Gui:
    formula_l = {
        "km": 1000,
        "m ": 1,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "yd": 0.914400,
        "ft": 0.3048,
        "in": 0.0254
    }
    t_length = 0
    t_width = 0
    t_height = 0

    def __init__(self, root):
        # _____________________________________________________________________________________________________________
        # main window
        self.window = root
        self.window.title("LAV Calculator and Converter")
        self.window.iconbitmap("support_files/icon.ico")
        self.window.geometry("1000x700")
        self.window.minsize(1000, 700)
        self.window.maxsize(1000, 700)
        self.window.resizable(0,0)

        # _____________________________________________________________________________________________________________
        # variables
        self.units = [
            ("kilometer", "km"),
            ("meter", "m "),
            ("centimeter", "cm"),
            ("millimeter", "mm"),
            ("mile", "mi"),
            ("yard", "yd"),
            ("foot", "ft"),
            ("inch", "in")
        ]

        self.input_units = []
        self.om = []
        self.entry_units = []
        for _ in range(9):
            self.input_units.append(StringVar())
            self.om.append(None)
            self.entry_units.append(None)

        self.inputs = []
        self.input_values = []
        for _ in range(9):
            self.inputs.append(StringVar())
            self.input_values.append(None)

        self.unit_names = []
        self.unit_symbols = []
        for i, j in self.units:
            self.unit_names.append(i)
            self.unit_symbols.append(j)

        self.units_set = IntVar()
        self.units_set.set(1)

        # _____________________________________________________________________________________________________________
        # Create canvas for background
        self.canvas = Canvas(self.window, width=1000, height=700, highlightthickness=0, bd=None)
        self.canvas.grid(row=0, column=0)

        # _____________________________________________________________________________________________________________
        # Insert logo image
        self.bg = PhotoImage(file="support_files/logo.png")

        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # _____________________________________________________________________________________________________________
        # frame for input area
        self.frame_inputs = Frame(self.window, width=450, height=350, bg="#fff", padx=9, pady=10)
        # self.frame_inputs.grid(row=0, column=1, padx=5, pady=0)
        self.canvas.create_window(150, 0, anchor=NW, window=self.frame_inputs)

        # widgets - frame_inputs
        Label(self.frame_inputs, text="Enter Dimension ", font=("MS Serif", 18, "bold"), bg="#fff", pady=10).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  columnspan=7,
                                                                                                                  sticky=W)

        # length
        Label(self.frame_inputs, text="Enter length: ", font=("MS Serif", 14, "normal"), bg="#fff").grid(row=1,
                                                                                                         column=0,
                                                                                                         columnspan=7,
                                                                                                         sticky=W)

        j = 0
        for i in range(0, 3):
            self.inputs[i] = Entry(self.frame_inputs, width=10, justify=RIGHT, font=('Courier', 12), bd=0,
                                   highlightthickness=2, highlightbackground="#00b8c4", highlightcolor="#03747b",
                                   bg="#edfbfb")
            self.inputs[i].grid(row=2, column=i + j, padx=0, pady=0)
            self.entry_units[i] = Label(self.frame_inputs, text=" mm", font=('Courier', 12), bg="#fff", anchor="w")
            self.entry_units[i].grid(row=2, column=i + 1 + j, sticky=W)
            Label(self.frame_inputs, text="   ", bg="#fff").grid(row=2, column=i + 2 + j)
            j = j + 2

        # row space
        Label(self.frame_inputs, text="     ", bg="#fff").grid(row=3, column=0)

        # width
        Label(self.frame_inputs, text="Enter width: ", font=("MS Serif", 14, "normal"), bg="#fff").grid(row=4, column=0,
                                                                                                        columnspan=7,
                                                                                                        sticky=W)

        j = 0
        for i in range(0, 3):
            self.inputs[i + 3] = Entry(self.frame_inputs, width=10, justify=RIGHT, font=('Courier', 12), bd=0,
                                       highlightthickness=2, highlightbackground="#00b8c4", highlightcolor="#03747b",
                                       bg="#edfbfb")
            self.inputs[i + 3].grid(row=5, column=i + j, padx=0, pady=0)
            self.entry_units[i + 3] = Label(self.frame_inputs, text=" mm", font=('Courier', 12), bg="#fff", anchor="w")
            self.entry_units[i + 3].grid(row=5, column=i + 1 + j, sticky=W)
            Label(self.frame_inputs, text="   ", bg="#fff").grid(row=5, column=i + 2 + j)
            j = j + 2

        # row space
        Label(self.frame_inputs, text="     ", bg="#fff").grid(row=6, column=0)

        # height
        Label(self.frame_inputs, text="Enter height: ", font=("MS Serif", 14, "normal"), bg="#fff").grid(row=7,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         sticky=W)

        j = 0
        for i in range(0, 3):
            self.inputs[i + 6] = Entry(self.frame_inputs, width=10, justify=RIGHT, font=('Courier', 12), bd=0,
                                       highlightthickness=2, highlightbackground="#00b8c4", highlightcolor="#03747b",
                                       bg="#edfbfb")
            self.inputs[i + 6].grid(row=8, column=i + j, padx=0, pady=0)
            self.entry_units[i + 6] = Label(self.frame_inputs, text=" mm", font=('Courier', 12), bg="#fff", anchor="w")
            self.entry_units[i + 6].grid(row=8, column=i + 1 + j, sticky=W)
            Label(self.frame_inputs, text="   ", bg="#fff").grid(row=8, column=i + 2 + j)
            j = j + 2

        # row space
        Label(self.frame_inputs, text="     ", bg="#fff").grid(row=9, column=0)

        # sub frame for buttons
        self.frame_buttons = Frame(self.frame_inputs, bg="#fff", padx=10, pady=10)
        self.frame_buttons.grid(row=11, column=0, columnspan=8)

        # cal button
        self.btn_cal = Button(self.frame_buttons, text="Calculate", height=1, width=10, fg="white",
                              font=("MS Serif", 12, "bold"), relief="ridge",
                              bd=5, bg="#00b8c4", activebackground="#03747b", activeforeground="#ddd",
                              command=self.cal_function)
        self.btn_cal.grid(row=0, column=0, pady=2)
        # column space
        Label(self.frame_buttons, text="   ", bg="#fff").grid(row=0, column=1)
        # rst button
        self.btn_rst = Button(self.frame_buttons, text="Reset", height=1, width=10, fg="white",
                              font=("MS Serif", 12, "bold"), relief="ridge",
                              bd=5, bg="#00b8c4", activebackground="#03747b", activeforeground="#ddd",
                              command=self.rst_function)
        self.btn_rst.grid(row=0, column=2, pady=2)

        # _____________________________________________________________________________________________________________
        # frame for background
        self.section3 = Frame(self.window, width=400, height=350, bg="#fff")
        self.canvas.create_window(603, 0, anchor=NW, window=self.section3)
        # frame for input units settings
        global frame_inputs_units_settings
        self.frame_inputs_units_settings = Frame(self.window, width=400, height=350, padx=1, pady=8, bg="#fff")
        self.canvas.create_window(603, 0, anchor=NW, window=self.frame_inputs_units_settings)
        # self.frame_inputs_units_settings.grid(row=0, column=2)

        # widgets - frame_inputs_units_settings
        # sub frame for standard units
        self.frame_inputs_units_standards = Frame(self.frame_inputs_units_settings, bg="#fff")
        self.frame_inputs_units_standards.grid(row=0, column=0, columnspan=10)

        Label(self.frame_inputs_units_standards, text="Select units for inputs: ", bg="#fff",
              font=("MS Serif", 11, "bold")) \
            .grid(row=0, column=0, columnspan=1, sticky=W)
        # radio buttons for units set method
        self.rb = Radiobutton(self.frame_inputs_units_standards, text="Units \t>> m / cm / mm", bg="#fff", fg="#00b8c4",
                              font=("", 10, "bold"),
                              variable=self.units_set, value=1, command=self.units_set_method)
        self.rb.grid(row=1, column=0, padx=100, sticky=W)
        self.rb = Radiobutton(self.frame_inputs_units_standards, text="Units \t>> yd / ft / in", bg="#fff",
                              fg="#00b8c4", font=("", 10, "bold"),
                              variable=self.units_set, value=2, command=self.units_set_method)
        self.rb.grid(row=2, column=0, padx=100, sticky=W)
        self.rb = Radiobutton(self.frame_inputs_units_standards, text="Custom\t>>", bg="#fff", fg="#00b8c4",
                              font=("", 10, "bold"),
                              variable=self.units_set, value=3, command=self.units_set_method)
        self.rb.grid(row=3, column=0, padx=100, sticky=W)

        # sub frame for custon units
        global frame_inputs_units_custom
        self.frame_inputs_units_custom = Frame(self.frame_inputs_units_settings, bg="#fff", padx=5, pady=5)
        self.frame_inputs_units_custom.grid(row=1, column=0, columnspan=100, padx=10, pady=10)

        # length
        Label(self.frame_inputs_units_custom, text="Units for length: ", bg="#fff", font=("", 8, "bold")).grid(row=10,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky=W)

        Label(self.frame_inputs_units_custom, text="Set 1: ", bg="#fff").grid(row=11, column=0, sticky=W)
        self.om[0] = OptionMenu(self.frame_inputs_units_custom, self.input_units[0], *self.unit_names,
                                command=self.pass_input_units)
        self.om[0].grid(row=11, column=1)
        self.om[0].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=11, column=2)
        Label(self.frame_inputs_units_custom, text="Set 2: ", bg="#fff").grid(row=11, column=3, sticky=W)
        self.om[1] = OptionMenu(self.frame_inputs_units_custom, self.input_units[1], *self.unit_names,
                                command=self.pass_input_units)
        self.om[1].grid(row=11, column=4)
        self.om[1].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=11, column=5)
        Label(self.frame_inputs_units_custom, text="Set 3: ", bg="#fff").grid(row=11, column=6, sticky=W)
        self.om[2] = OptionMenu(self.frame_inputs_units_custom, self.input_units[2], *self.unit_names,
                                command=self.pass_input_units)
        self.om[2].grid(row=11, column=7)
        self.om[2].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)

        # row space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=12, column=0)
        # width
        Label(self.frame_inputs_units_custom, text="Units for width: ", bg="#fff", font=("", 8, "bold")).grid(row=13,
                                                                                                              column=0,
                                                                                                              columnspan=7,
                                                                                                              sticky=W)

        Label(self.frame_inputs_units_custom, text="Set 1: ", bg="#fff").grid(row=14, column=0, sticky=W)
        self.om[3] = OptionMenu(self.frame_inputs_units_custom, self.input_units[3], *self.unit_names,
                                command=self.pass_input_units)
        self.om[3].grid(row=14, column=1)
        self.om[3].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=14, column=2)
        Label(self.frame_inputs_units_custom, text="Set 2: ", bg="#fff").grid(row=14, column=3, sticky=W)
        self.om[4] = OptionMenu(self.frame_inputs_units_custom, self.input_units[4], *self.unit_names,
                                command=self.pass_input_units)
        self.om[4].grid(row=14, column=4)
        self.om[4].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=14, column=5)
        Label(self.frame_inputs_units_custom, text="Set 3: ", bg="#fff").grid(row=14, column=6, sticky=W)
        self.om[5] = OptionMenu(self.frame_inputs_units_custom, self.input_units[5], *self.unit_names,
                                command=self.pass_input_units)
        self.om[5].grid(row=14, column=7)
        self.om[5].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)

        # row space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=15, column=0)
        # height
        Label(self.frame_inputs_units_custom, text="Units for height: ", bg="#fff", font=("", 8, "bold")).grid(row=16,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky=W)

        Label(self.frame_inputs_units_custom, text="Set 1: ", bg="#fff").grid(row=17, column=0, sticky=W)
        self.om[6] = OptionMenu(self.frame_inputs_units_custom, self.input_units[6], *self.unit_names,
                                command=self.pass_input_units)
        self.om[6].grid(row=17, column=1)
        self.om[6].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=17, column=2)
        Label(self.frame_inputs_units_custom, text="Set 2: ", bg="#fff").grid(row=17, column=3, sticky=W)
        self.om[7] = OptionMenu(self.frame_inputs_units_custom, self.input_units[7], *self.unit_names,
                                command=self.pass_input_units)
        self.om[7].grid(row=17, column=4)
        self.om[7].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)
        # column space
        Label(self.frame_inputs_units_custom, text="     ", bg="#fff").grid(row=17, column=5)
        Label(self.frame_inputs_units_custom, text="Set 3: ", bg="#fff").grid(row=17, column=6, sticky=W)
        self.om[8] = OptionMenu(self.frame_inputs_units_custom, self.input_units[8], *self.unit_names,
                                command=self.pass_input_units)
        self.om[8].grid(row=17, column=7)
        self.om[8].config(font=('Courier', 12, "bold"), fg="white", bd=5, bg="#00b8c4", height=1,
                          activebackground="#03747b", activeforeground="#ddd", pady=0)

        self.units_set_method()
        self.rst_function()

        # ______________________________________________________________________________________________________________
        #  bottom section
        self.bottom_bg = PhotoImage(file="support_files/botttom_bg.png")
        self.bottom_bg_length_l = PhotoImage(file="support_files/bottom_bg_length_l.png")
        self.bottom_bg_length_w = PhotoImage(file="support_files/bottom_bg_length_w.png")
        self.bottom_bg_length_h = PhotoImage(file="support_files/bottom_bg_length_h.png")
        self.bottom_bg_area_lw = PhotoImage(file="support_files/bottom_bg_area_lw.png")
        self.bottom_bg_area_lh = PhotoImage(file="support_files/bottom_bg_area_lh.png")
        self.bottom_bg_area_wh = PhotoImage(file="support_files/bottom_bg_area_wh.png")
        self.bottom_bg_volumn = PhotoImage(file="support_files/bottom_bg_volumn.png")
        self.canvas.create_image(0, 350, image=self.bottom_bg, anchor=NW)

        self.length_text = Text(self.window, cursor="xterm", width=20, height=14, font=("Arial", 10), bd=0)
        self.area_text = Text(self.window, cursor="xterm", width=20, height=14, font=("Arial", 10), bd=0)
        self.volumn_text = Text(self.window, cursor="xterm", width=25, height=3, font=("Arial", 12), bd=0)

    # __________________________________________________________________________________________________________________
    def pass_input_units(self, *args):
        for i in self.unit_names:
            for j in self.input_units:
                if i == j.get():
                    j.set(self.unit_symbols[self.unit_names.index(i)])
        self.units_set_method()

    def units_set_method(self):
        # # custom unit set enable/disable
        for i in range(9):
            if self.units_set.get() != 3:
                self.om[i].config(state=DISABLED)
            else:
                self.om[i].config(state=NORMAL)

        # pass unit symbols
        if self.units_set.get() == 1:
            for i in range(9):
                if i == 0 or i == 3 or i == 6:
                    self.input_units[i].set(self.unit_symbols[1])
                elif i == 1 or i == 4 or i == 7:
                    self.input_units[i].set(self.unit_symbols[2])
                else:
                    self.input_units[i].set(self.unit_symbols[3])
        elif self.units_set.get() == 2:
            for i in range(9):
                if i == 0 or i == 3 or i == 6:
                    self.input_units[i].set(self.unit_symbols[5])
                elif i == 1 or i == 4 or i == 7:
                    self.input_units[i].set(self.unit_symbols[6])
                else:
                    self.input_units[i].set(self.unit_symbols[7])
        for i in range(9):
            self.entry_units[i].config(text=self.input_units[i].get())
            # self.inputs[i].delete(len(self.inputs[i].get())-3, END)
            # self.inputs[i].insert(0, 0.0)
            # self.inputs[i].insert(100, self.input_units[i].get())

    def cal_function(self):
        if self.validation() == TRUE:
            total_l_m = str(round(self.get_totals("m ")[0], 4)) + " m\n"
            m_cm_mm = self.convert_m_cm_mm(self.get_totals("m ")[0])
            total_l_m_cm_mm = str(m_cm_mm[0]) + " m  " + str(m_cm_mm[1]) + " cm  " + str(m_cm_mm[2]) + " mm\n"

            total_l_ft = str(round(self.get_totals("ft")[0], 4)) + " ft\n"
            ft_in = self.convert_ft_in(self.get_totals("ft")[0])
            total_l_ft_in = str(ft_in[0]) + " ft  " + str(ft_in[1]) + " in\n"

            total_w_m = str(round(self.get_totals("m ")[1], 4)) + " m\n"
            m_cm_mm = self.convert_m_cm_mm(self.get_totals("m ")[1])
            total_w_m_cm_mm = str(m_cm_mm[0]) + " m  " + str(m_cm_mm[1]) + " cm  " + str(m_cm_mm[2]) + " mm\n"

            total_w_ft = str(round(self.get_totals("ft")[1], 4)) + " ft\n"
            ft_in = self.convert_ft_in(self.get_totals("ft")[1])
            total_w_ft_in = str(ft_in[0]) + " ft  " + str(ft_in[1]) + " in\n"

            total_h_m = str(round(self.get_totals("m ")[2], 4)) + " m\n"
            m_cm_mm = self.convert_m_cm_mm(self.get_totals("m ")[2])
            total_h_m_cm_mm = str(m_cm_mm[0]) + " m  " + str(m_cm_mm[1]) + " cm  " + str(m_cm_mm[2]) + " mm\n"

            total_h_ft = str(round(self.get_totals("ft")[2], 4)) + " ft\n"
            ft_in = self.convert_ft_in(self.get_totals("ft")[2])
            total_h_ft_in = str(ft_in[0]) + " ft  " + str(ft_in[1]) + " in"

            input_amount = 3
            for i in range(3):
                if self.get_totals("m ")[i] == 0:
                    input_amount -= 1

            self.length_text.config(state=NORMAL)
            self.length_text.delete(0.0, END)
            self.area_text.config(state=NORMAL)
            self.area_text.delete(0.0, END)
            self.volumn_text.config(state=NORMAL)
            self.volumn_text.delete(0.0, END)

            if input_amount == 3:
                try:
                    self.canvas.delete(self.img_length)
                except: pass
                try:
                    self.canvas.delete(self.img_area)
                except: pass
                try:
                    self.canvas.delete(self.img_volumn)
                except: pass

                # insert bg image
                self.img_volumn = self.canvas.create_image(0, 350, image=self.bottom_bg_volumn, state=NORMAL, anchor=NW)

                self.length_text.insert(INSERT, total_l_m)
                self.length_text.insert(INSERT, total_l_m_cm_mm)
                self.length_text.insert(INSERT, total_l_ft)
                self.length_text.insert(INSERT, total_l_ft_in)
                self.length_text.insert(INSERT, "\n")
                self.length_text.insert(INSERT, total_w_m)
                self.length_text.insert(INSERT, total_w_m_cm_mm)
                self.length_text.insert(INSERT, total_w_ft)
                self.length_text.insert(INSERT, total_w_ft_in)
                self.length_text.insert(INSERT, "\n")
                self.length_text.insert(INSERT, total_h_m)
                self.length_text.insert(INSERT, total_h_m_cm_mm)
                self.length_text.insert(INSERT, total_h_ft)
                self.length_text.insert(INSERT, total_h_ft_in)

                self.text_box_1 = self.canvas.create_window(140, 427, anchor=NW, window=self.length_text)

                for i in range(3):
                    sq_m = str(self.area(i)[0]) + "\tm\u00b2"
                    self.area_text.insert(INSERT, sq_m)
                    sq_ft = "\n" + str(self.area(i)[1]) + "\tft\u00b2"
                    self.area_text.insert(INSERT, sq_ft)
                    perch = "\n" + str(self.area(i)[2]) + "\tperch"
                    self.area_text.insert(INSERT, perch)
                    acre = "\n" + str(self.area(i)[3]) + "\tacre"
                    self.area_text.insert(INSERT, acre)
                    self.area_text.insert(INSERT, "\n\n") if i != 2 else None

                self.text_box_2 = self.canvas.create_window(450, 427, anchor=NW, window=self.area_text)


                cubic_m = str(self.volumn()[0]) + "\tm\u00b3"
                self.volumn_text.insert(INSERT, cubic_m)
                cubic_ft = "\n" + str(self.volumn()[1]) + "\tft\u00b3"
                self.volumn_text.insert(INSERT, cubic_ft)
                cubic_in = "\n" + str(self.volumn()[2]) + "\tin\u00b3"
                self.volumn_text.insert(INSERT, cubic_in)

                self.text_box_3 = self.canvas.create_window(720, 477, anchor=NW, window=self.volumn_text)

            elif input_amount == 2:
                # check and clear other text boxes
                try:
                    self.canvas.delete(self.img_length)
                except: pass
                try:
                    self.canvas.delete(self.img_area)
                except: pass
                try:
                    self.canvas.delete(self.img_volumn)
                except: pass
                try:
                    self.canvas.delete(self.text_box_1)
                except:pass
                try:
                    self.canvas.delete(self.text_box_2)
                except:pass
                try:
                    self.canvas.delete(self.text_box_3)
                except:pass

                if self.get_totals("m ")[0] != 0:
                    self.length_text.insert(INSERT, total_l_m)
                    self.length_text.insert(INSERT, total_l_m_cm_mm)
                    self.length_text.insert(INSERT, total_l_ft)
                    self.length_text.insert(INSERT, total_l_ft_in)
                    self.length_text.insert(INSERT, "\n")
                if self.get_totals("m ")[1] != 0:
                    self.length_text.insert(INSERT, total_w_m)
                    self.length_text.insert(INSERT, total_w_m_cm_mm)
                    self.length_text.insert(INSERT, total_w_ft)
                    self.length_text.insert(INSERT, total_w_ft_in)
                    self.length_text.insert(INSERT, "\n")
                if self.get_totals("m ")[2] != 0:
                    self.length_text.insert(INSERT, total_h_m)
                    self.length_text.insert(INSERT, total_h_m_cm_mm)
                    self.length_text.insert(INSERT, total_h_ft)
                    self.length_text.insert(INSERT, total_h_ft_in)

                self.text_box_1 = self.canvas.create_window(250, 427, anchor=NW, window=self.length_text)

                if self.get_totals("m ")[0] == 0:
                    # insert bg image
                    self.img_area = self.canvas.create_image(0, 350, image=self.bottom_bg_area_wh, state=NORMAL, anchor=NW)

                    sq_m = str(self.area(2)[0]) + "\tm\u00b2"
                    self.area_text.insert(INSERT, sq_m)
                    sq_ft = "\n" + str(self.area(2)[1]) + "\tft\u00b2"
                    self.area_text.insert(INSERT, sq_ft)
                    perch = "\n" + str(self.area(2)[2]) + "\tperch"
                    self.area_text.insert(INSERT, perch)
                    acre = "\n" + str(self.area(2)[3]) + "\tacre"
                    self.area_text.insert(INSERT, acre)

                elif self.get_totals("m ")[1] == 0:
                    # insert bg image
                    self.img_area = self.canvas.create_image(0, 350, image=self.bottom_bg_area_lh, state=NORMAL, anchor=NW)

                    sq_m = str(self.area(1)[0]) + "\tm\u00b2"
                    self.area_text.insert(INSERT, sq_m)
                    sq_ft = "\n" + str(self.area(1)[1]) + "\tft\u00b2"
                    self.area_text.insert(INSERT, sq_ft)
                    perch = "\n" + str(self.area(1)[2]) + "\tperch"
                    self.area_text.insert(INSERT, perch)
                    acre = "\n" + str(self.area(1)[3]) + "\tacre"
                    self.area_text.insert(INSERT, acre)

                elif self.get_totals("m ")[2] == 0:
                    # insert bg image
                    self.img_area = self.canvas.create_image(0, 350, image=self.bottom_bg_area_lw, state=NORMAL, anchor=NW)

                    sq_m = str(self.area(0)[0]) + "\tm\u00b2"
                    self.area_text.insert(INSERT, sq_m)
                    sq_ft = "\n" + str(self.area(0)[1]) + "\tft\u00b2"
                    self.area_text.insert(INSERT, sq_ft)
                    perch = "\n" + str(self.area(0)[2]) + "\tperch"
                    self.area_text.insert(INSERT, perch)
                    acre = "\n" + str(self.area(0)[3]) + "\tacre"
                    self.area_text.insert(INSERT, acre)

                self.text_box_2 = self.canvas.create_window(638, 427, anchor=NW, window=self.area_text)

            elif input_amount == 1:
                # check and clear other text boxes
                try:
                    self.canvas.delete(self.img_length)
                except: pass
                try:
                    self.canvas.delete(self.img_area)
                except: pass
                try:
                    self.canvas.delete(self.img_volumn)
                except: pass
                try:
                    self.canvas.delete(self.text_box_1)
                except:pass
                try:
                    self.canvas.delete(self.text_box_2)
                except:pass
                try:
                    self.canvas.delete(self.text_box_3)
                except:pass

                if self.get_totals("m ")[0] != 0:
                    # insert bg image
                    self.img_length = self.canvas.create_image(0, 350, image=self.bottom_bg_length_l, state=NORMAL, anchor=NW)

                    self.length_text.insert(INSERT, total_l_m)
                    self.length_text.insert(INSERT, total_l_m_cm_mm)
                    self.length_text.insert(INSERT, total_l_ft)
                    self.length_text.insert(INSERT, total_l_ft_in)
                    self.length_text.insert(INSERT, "\n")
                elif self.get_totals("m ")[1] != 0:
                    # insert bg image
                    self.img_length = self.canvas.create_image(0, 350, image=self.bottom_bg_length_w, state=NORMAL, anchor=NW)

                    self.length_text.insert(INSERT, total_w_m)
                    self.length_text.insert(INSERT, total_w_m_cm_mm)
                    self.length_text.insert(INSERT, total_w_ft)
                    self.length_text.insert(INSERT, total_w_ft_in)
                    self.length_text.insert(INSERT, "\n")
                else:
                    # insert bg image
                    self.img_length = self.canvas.create_image(0, 350, image=self.bottom_bg_length_h, state=NORMAL, anchor=NW)

                    self.length_text.insert(INSERT, total_h_m)
                    self.length_text.insert(INSERT, total_h_m_cm_mm)
                    self.length_text.insert(INSERT, total_h_ft)
                    self.length_text.insert(INSERT, total_h_ft_in)

                self.text_box_1 = self.canvas.create_window(450, 427, anchor=NW, window=self.length_text)

            else:
                self.rst_function()

            self.length_text.config(state=DISABLED)
            self.area_text.config(state=DISABLED)
            self.volumn_text.config(state=DISABLED)

        else:
            self.error_message()

    def rst_function(self):
        for i in range(9):
            self.inputs[i].delete(0, END)
            self.inputs[i].insert(0, 0.0)

        try:
            self.canvas.delete(self.img_length)
        except: pass
        try:
            self.canvas.delete(self.img_area)
        except: pass
        try:
            self.canvas.delete(self.img_volumn)
        except: pass
        try:
            self.canvas.delete(self.text_box_1)
        except: pass
        try:
            self.canvas.delete(self.text_box_2)
        except: pass
        try:
            self.canvas.delete(self.text_box_3)
        except: pass

    def validation(self):
        self.validity = TRUE
        for i in range(len(self.inputs)):
            try:
                if self.inputs[i].get() == "" or self.inputs[i].get() == " " or self.inputs[i].get() == "   ":
                    self.inputs[i].delete(0, END)
                    self.inputs[i].insert(0, "0.0")
                self.input_values[i] = float(self.inputs[i].get())
                self.inputs[i].config(bg="white")

            except ValueError:
                self.inputs[i].config(bg="#FFB9B9")
                self.inputs[i].select_range(0, END)
                self.inputs[i].focus()
                self.validity = 0
        if self.validity == TRUE:
            return (TRUE)
        else:
            return (FALSE)

    def error_message(self):
        messagebox.showerror("Invalid inputs!!!", "Enter only integer or decimal numbers...")

    # get total length in meters
    def get_totals(self, unit):
        self.t_length = 0
        if unit == "m ":
            for i in range(0, 3):
                self.t_length = self.t_length + self.convert_l(self.input_units[i].get(), "m ", self.input_values[i])[0]
            self.t_width = 0
            for i in range(3, 6):
                self.t_width = self.t_width + self.convert_l(self.input_units[i].get(), "m ", self.input_values[i])[0]
            self.t_height = 0
            for i in range(6, 9):
                self.t_height = self.t_height + self.convert_l(self.input_units[i].get(), "m ", self.input_values[i])[0]

            self.t_length = round(self.t_length, 12)
            self.t_width = round(self.t_width, 12)
            self.t_height = round(self.t_height, 12)
        elif unit == "ft":
            for i in range(0, 3):
                self.t_length = self.t_length + self.convert_l(self.input_units[i].get(), "ft", self.input_values[i])[0]
            self.t_width = 0
            for i in range(3, 6):
                self.t_width = self.t_width + self.convert_l(self.input_units[i].get(), "ft", self.input_values[i])[0]
            self.t_height = 0
            for i in range(6, 9):
                self.t_height = self.t_height + self.convert_l(self.input_units[i].get(), "ft", self.input_values[i])[0]

            self.t_length = round(self.t_length, 12)
            self.t_width = round(self.t_width, 12)
            self.t_height = round(self.t_height, 12)
        elif unit == "in":
            for i in range(0, 3):
                self.t_length = self.t_length + self.convert_l(self.input_units[i].get(), "in", self.input_values[i])[0]
            self.t_width = 0
            for i in range(3, 6):
                self.t_width = self.t_width + self.convert_l(self.input_units[i].get(), "in", self.input_values[i])[0]
            self.t_height = 0
            for i in range(6, 9):
                self.t_height = self.t_height + self.convert_l(self.input_units[i].get(), "in", self.input_values[i])[0]

            self.t_length = round(self.t_length, 12)
            self.t_width = round(self.t_width, 12)
            self.t_height = round(self.t_height, 12)

        return (self.t_length, self.t_width, self.t_height)

    # converts lengths
    def convert_l(self, from_unit_type, to_unit_type, value):
        from_type_units = self.formula_l[from_unit_type]
        to_type_units = self.formula_l[to_unit_type]

        new_value = value * (from_type_units / to_type_units)

        return (new_value, to_unit_type)

    # separate length to m. cm and mm
    def convert_m_cm_mm(self, total_length):
        m = int(total_length / 1)
        cm = int(round(float((Decimal(total_length) - Decimal(m * 1)) / Decimal(0.01)), 7))
        mm = round(float((Decimal(total_length) - Decimal(m * 1) - Decimal(cm * 0.01)) / Decimal(0.001)), 7)
        mm = round(mm, 2)
        if mm == int(mm):
            mm = int(mm)

        return (m, cm, mm)

    # separate length to yd. ft and in
    def convert_ft_in(self, total_length):
        ft = int(total_length / 1)
        inc = round(((Decimal(total_length) - Decimal(ft * 1)) * Decimal(12)), 7)
        # inc = round((float((Decimal(total_length) - Decimal(yd * 1) - Decimal(ft / 3)) * Decimal(36))), 7)
        inc = round(inc, 2)

        if inc == int(inc):
            inc = int(inc)

        return (ft, inc)

    def area(self, val):
        if val == 0:
            area_m = self.get_totals("m ")[0] * self.get_totals("m ")[1]
            area_ft = self.get_totals("ft")[0] * self.get_totals("ft")[1]
        elif val == 1:
            area_m = self.get_totals("m ")[0] * self.get_totals("m ")[2]
            area_ft = self.get_totals("ft")[0] * self.get_totals("ft")[2]
        elif val == 2:
            area_m = self.get_totals("m ")[1] * self.get_totals("m ")[2]
            area_ft = self.get_totals("ft")[1] * self.get_totals("ft")[2]

        perch = float((Decimal(3.9536861034746) / Decimal(100)) * Decimal(area_m))
        acre = float((Decimal(24.710538146717) / Decimal(100000)) * Decimal(area_m))

        area_m = round(area_m, 4) if area_m > 0.01 else round(area_m, 6)
        area_ft = round(area_ft, 4) if area_ft > 0.01 else round(area_ft, 6)
        perch = round(perch, 4) if perch > 0.01 else round(perch, 6)
        acre = round(acre, 4) if acre > 0.01 else round(acre, 6)

        area_m = int(area_m) if area_m == int(area_m) else area_m
        area_ft = int(area_ft) if area_ft == int(area_ft) else area_ft
        perch = int(perch) if perch == int(perch) else perch
        acre = int(acre) if acre == int(acre) else acre

        area_m = area_m if area_m > 0.01 else '{:.6f}'.format(area_m)
        area_ft = area_ft if area_ft > 0.01 else '{:.6f}'.format(area_ft)
        perch = area_m if perch > 0.01 else '{:.6f}'.format(perch)
        acre = acre if acre > 0.01 else '{:.6f}'.format(acre)

        return area_m, area_ft, perch, acre

    def volumn(self):
        volumn_m = self.get_totals("m ")[0] * self.get_totals("m ")[1] * self.get_totals("m ")[2]
        volumn_ft = self.get_totals("ft")[0] * self.get_totals("ft")[1] * self.get_totals("ft")[2]
        volumn_in = self.get_totals("in")[0] * self.get_totals("in")[1] * self.get_totals("in")[2]

        volumn_m = round(volumn_m, 4) if volumn_m > 0.01 else round(volumn_m, 8)
        volumn_ft = round(volumn_ft, 4) if volumn_ft > 0.01 else round(volumn_ft, 8)
        volumn_in = round(volumn_in, 4) if volumn_in > 0.01 else round(volumn_in, 8)

        volumn_m = int(volumn_m) if int(volumn_m) == volumn_m else volumn_m
        volumn_ft = int(volumn_ft) if int(volumn_ft) == volumn_ft else volumn_ft
        volumn_in = int(volumn_in) if int(volumn_in) == volumn_in else volumn_in

        volumn_m = volumn_m if volumn_m > 0.01 else '{:.8f}'.format(volumn_m)
        volumn_ft = volumn_ft if volumn_ft > 0.01 else '{:.8f}'.format(volumn_ft)
        volumn_in = volumn_in if volumn_in > 0.01 else '{:.8f}'.format(volumn_in)

        return volumn_m, volumn_ft, volumn_in


def main():
    window = Tk()
    app = Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
