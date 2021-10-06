import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from Ma_DES import Ui_MainWindow
from HVIP import Ui_MainWindow1
from Loop import Ui_MainWindow2
from mrE import Ui_MainWindow3
from Sbox import Ui_MainWindow4
from hvP import Ui_MainWindow5
from Ket_qua import Ui_MainWindow6
import Mã_DES
import numpy as np
np.set_printoptions(linewidth=200)


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.But_cre.clicked.connect(self.cre_data)
        self.uic.But_Cre.clicked.connect(self.Cre_data)
        self.uic.But_sa.clicked.connect(self.sa_data)
        self.uic.But_Sa.clicked.connect(self.Sa_data)
        self.uic.But_in.clicked.connect(self.input_data)
        self.uic.But_In.clicked.connect(self.Input_data)
        self.uic.But_En.clicked.connect(self.open_HVIP)
        self.uic.But_in.setEnabled(False)
        self.uic.But_In.setEnabled(False)
        self.uic.But_sa.setEnabled(False)
        self.uic.But_Sa.setEnabled(False)

    def input_data(self):
        f = open('Input Data.txt', 'r')
        file_contents = f.read()
        a = []
        for i in file_contents:
            if i.isdigit():
                a.append(int(i))
        f.close()
        c = []
        for i in range(int(len(a) / 8)):
            b = []
            for j in range(8):
                b.append(a[j + i * 8])
            c.append(b)
        danh_sach = [self.uic.dl_1, self.uic.dl_2, self.uic.dl_3, self.uic.dl_4,
                     self.uic.dl_5, self.uic.dl_6, self.uic.dl_7, self.uic.dl_8]
        for i in range(len(c)):
            danh_sach[i].setText(str(np.array(c[i])))
        MainWindow.data = np.array(c)
        self.uic.But_sa.setEnabled(True)
        return MainWindow.check(self)

    def Input_data(self):
        f = open('Input Key.txt', 'r')
        file_contents = f.read()
        a = []
        for i in file_contents:
            if i.isdigit():
                a.append(int(i))
        f.close()
        c = []
        for i in range(int(len(a)/48)):
            b = []
            for j in range(48):
                b.append(a[j+i*48])
            c.append(b)
        danh_sach = [self.uic.kv_1,self.uic.kv_2,self.uic.kv_3,self.uic.kv_4,
                     self.uic.kv_5,self.uic.kv_6,self.uic.kv_7,self.uic.kv_8,
                     self.uic.kv_9,self.uic.kv_10,self.uic.kv_11,self.uic.kv_12,
                     self.uic.kv_13,self.uic.kv_14,self.uic.kv_15,self.uic.kv_16]
        for i in range(len(c)):
            danh_sach[i].setText(str(np.array(c[i])))
        MainWindow.Data = np.array(c)
        self.uic.But_Sa.setEnabled(True)
        return MainWindow.check(self)


    data = []

    def cre_data(self):
        danh_sach = [self.uic.dl_1,self.uic.dl_2,self.uic.dl_3,self.uic.dl_4,self.uic.dl_5,self.uic.dl_6,self.uic.dl_7,self.uic.dl_8]
        khoa = Mã_DES.Create_Key()
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(khoa[i]))
        MainWindow.data = khoa
        if len(MainWindow.data) != 0:
            self.uic.But_sa.setEnabled(True)



        return MainWindow.check(self)

    def sa_data(self):
        file2write = open("Input Data.txt", 'w')
        for i in range(len(MainWindow.data)):
            for j in range(len(MainWindow.data[i])):
                file2write.write(str(MainWindow.data[i][j]) + ' ')
            file2write.write(str('\n'))
        file2write.close()
        self.uic.But_in.setEnabled(True)

    def Sa_data(self):
        file2write = open("Input Key.txt", 'w')
        for i in range(len(MainWindow.Data)):
            for j in range(len(MainWindow.Data[i])):
                file2write.write(str(MainWindow.Data[i][j]) + ' ')
            file2write.write(str('\n'))
        file2write.close()
        self.uic.But_In.setEnabled(True)

    Data = []
    def Cre_data(self):
        danh_sach = [self.uic.kv_1,self.uic.kv_2,self.uic.kv_3,self.uic.kv_4,self.uic.kv_5,self.uic.kv_6,self.uic.kv_7,self.uic.kv_8,
                    self.uic.kv_9,self.uic.kv_10,self.uic.kv_11,self.uic.kv_12,self.uic.kv_13,self.uic.kv_14,self.uic.kv_15,self.uic.kv_16]
        khoa = Mã_DES.Create_Key_Loop()
        khoa = np.array(khoa)
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(khoa[i]))
        MainWindow.Data = khoa
        if len(MainWindow.Data) != 0:
            self.uic.But_Sa.setEnabled(True)

        return MainWindow.check(self)

    def check(self):
        if len(MainWindow.data) != 0 and len(MainWindow.Data) != 0:
            self.uic.But_En.setEnabled(True)


    def open_HVIP(self):
        self.HVIP_Window = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self.HVIP_Window)
        self.HVIP_Window.show()
        danh_sach_1 = [self.uic1.Dl_1, self.uic1.Dl_2, self.uic1.Dl_3, self.uic1.Dl_4, self.uic1.Dl_5, self.uic1.Dl_6,
                     self.uic1.Dl_7, self.uic1.Dl_8]
        for i in range(len(danh_sach_1)):
            danh_sach_1[i].setText(str(MainWindow.data[i]))
        danh_sach_2 = [self.uic1.Dl_9, self.uic1.Dl_10, self.uic1.Dl_11, self.uic1.Dl_12, self.uic1.Dl_13, self.uic1.Dl_14,
                     self.uic1.Dl_15, self.uic1.Dl_16]
        for i in range(len(danh_sach_2)):
            danh_sach_2[i].setText(str(Mã_DES.IP[i]))

        self.main_win.close()
        self.uic1.But_HV_IP.clicked.connect(self.Hoan_vi)
        self.uic1.But_Loop.clicked.connect(self.open_Loop)


    L0 = []
    R0 = []

    temp = []
    def Hoan_vi(self):
        data1 = Mã_DES.HV_table(MainWindow.data,Mã_DES.IP)
        data = Mã_DES.HV_table1(MainWindow.data,Mã_DES.IP)
        data1 = np.array(data1)
        l0 = data1[0:len(data1) // 2]
        MainWindow.L0  = l0
        r0 = data1[len(data1) // 2:]
        MainWindow.R0 = r0
        data = np.array(data)
        danh_sach = [self.uic1.Dla_1, self.uic1.Dla_2, self.uic1.Dla_3, self.uic1.Dla_4, self.uic1.Dla_5, self.uic1.Dla_6,
                       self.uic1.Dla_7, self.uic1.Dla_8]
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(data[i]))
        MainWindow.data = data
        self.uic1.l_0.setText(str(l0))
        self.uic1.r_0.setText(str(r0))
        self.uic1.But_HV_IP.setEnabled(False)
        self.uic1.But_Loop.setEnabled(True)

    bien_dem = 0
    l_0 = []
    r_0 = []
    def open_Loop(self):
        self.Loop_Window = QMainWindow()
        self.uic2 = Ui_MainWindow2()
        self.uic2.setupUi(self.Loop_Window)
        self.Loop_Window.show()

        self.HVIP_Window.close()
        self.uic2.But_CKV.setEnabled(False)
        self.uic2.But_TSB.setEnabled(False)
        self.uic2.But_HVP.setEnabled(False)
        self.uic2.But_MHNT_XDNCL.setEnabled(False)
        self.uic2.But_HVIP_1.setEnabled(False)
        if MainWindow.bien_dem == 15:
            MainWindow.temp = MainWindow.R0
            self.uic2.But_VKT.setEnabled(False)
        else:
            MainWindow.temp = MainWindow.L0
        MainWindow.l_0 = MainWindow.L0
        MainWindow.r_0 = MainWindow.R0
        self.uic2.lb_l0.setText("L" + str(MainWindow.bien_dem))
        self.uic2.lb_r0.setText("R" + str(MainWindow.bien_dem))
        self.uic2.lb_l1.setText("L" + str(MainWindow.bien_dem + 1))
        self.uic2.lb_r1.setText("R" + str(MainWindow.bien_dem + 1))
        self.uic2.lb_key.setText("Kr" + str(MainWindow.bien_dem + 1))
        self.uic2.L_0.setText(str(np.array(MainWindow.L0)))
        self.uic2.R_0.setText(str(np.array(MainWindow.R0)))
        # MainWindow.temp = MainWindow.R0
        self.uic2.But_MRNP.clicked.connect(self.MR_E)
        self.uic2.But_E.clicked.connect(self.MR_E)
        self.uic2.But_CKV.clicked.connect(self.C_KV)
        self.uic2.But_plus1.clicked.connect(self.C_KV)
        self.uic2.khoa_vong.setText(str(MainWindow.Data[MainWindow.bien_dem]))
        self.uic2.But_TSB.clicked.connect(self.Sbox)
        self.uic2.But_Sbox.clicked.connect(self.Sbox)
        self.uic2.But_HVP.clicked.connect(self.HV_P)
        self.uic2.But_P.clicked.connect(self.HV_P)
        self.uic2.But_MHNT_XDNCL.clicked.connect(self.C_L0)
        self.uic2.But_plus2.clicked.connect(self.C_L0)
        self.uic2.But_VKT.clicked.connect(self.VKT)
        self.uic2.But_HVIP_1.clicked.connect(self.HVIP_1)
        self.uic2.But_plus1.setEnabled(False)
        self.uic2.But_Sbox.setEnabled(False)
        self.uic2.But_plus2.setEnabled(False)
        self.uic2.But_P.setEnabled(False)
        if MainWindow.bien_dem == 15:
            self.uic2.But_plus2.setText("+ XOR L15")





    def MR_E(self):
        self.E_Window = QMainWindow()
        self.uic3 = Ui_MainWindow3()
        self.uic3.setupUi(self.E_Window)
        self.E_Window.show()
        self.uic3.kdv.setText(str(np.array(MainWindow.R0)))
        danh_sach = [self.uic3.E_1,self.uic3.E_2,self.uic3.E_3,self.uic3.E_4,self.uic3.E_5,self.uic3.E_6]
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(Mã_DES.E[i]))
        # temp = MainWindow.R0
        MainWindow.R0 = Mã_DES.HV_line(MainWindow.R0,Mã_DES.E)
        self.uic3.kdmr.setText(str(np.array(MainWindow.R0)))
        if self.E_Window.isVisible() == True:
            self.uic2.open_kq.setText(str(np.array(MainWindow.R0)))
            self.uic2.But_E.setEnabled(False)
            self.uic2.But_MRNP.setEnabled(False)
            self.uic2.But_plus1.setEnabled(True)
            self.uic2.But_CKV.setEnabled(True)

    def C_KV(self):
        MainWindow.R0 = Mã_DES.XOR(MainWindow.R0,MainWindow.Data[MainWindow.bien_dem])
        self.uic2.add_kq.setText(str(np.array(MainWindow.R0)))
        self.uic2.But_plus1.setEnabled(False)
        self.uic2.But_CKV.setEnabled(False)
        self.uic2.But_Sbox.setEnabled(True)
        self.uic2.But_TSB.setEnabled(True)

    kdr1 = []
    R_Sbox = []
    Sbox_dem = 0
    def Sbox(self):
        self.Sbox_Window = QMainWindow()
        self.uic4 = Ui_MainWindow4()
        self.uic4.setupUi(self.Sbox_Window)
        self.Sbox_Window.show()
        self.uic4.S_dv.setText(str(np.array(MainWindow.R0)))
        MainWindow.R_Sbox = MainWindow.R0
        self.uic4.But_Next.clicked.connect(self.Sbox_loop)
        if self.Sbox_Window.isVisible() == True:
            for i in range(int(len(MainWindow.R0) / 6)):
                sub_r_i2 = MainWindow.R0[i * int(len(MainWindow.R0) / 8):i * int(
                    len(MainWindow.R0) / 8) + (int(len(MainWindow.R0) / 8))]
                row1 = int(str(sub_r_i2[0]) + str(sub_r_i2[-1]), 2)
                col1 = int(str(''.join([str(i) for i in sub_r_i2[1:-1]])), 2)
                sub_r_i2 = f"{Mã_DES.S_box[i][row1][col1]:04b}"
                for j in sub_r_i2:
                    MainWindow.kdr1.append(int(j))
        self.uic2.Sbox_kq.setText(str(np.array(MainWindow.kdr1)))
        self.uic2.But_Sbox.setEnabled(False)
        self.uic2.But_TSB.setEnabled(False)
        self.uic2.But_P.setEnabled(True)
        self.uic2.But_HVP.setEnabled(True)


    kdr = []
    def Sbox_loop(self):
        danh_sach = [self.uic4.S_1, self.uic4.S_2, self.uic4.S_3, self.uic4.S_4]
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(Mã_DES.S_box[MainWindow.Sbox_dem][i]))
        self.uic4.S_label.setText("Sbox số " +str(MainWindow.Sbox_dem + 1))
        sub_r_i = MainWindow.R_Sbox[MainWindow.Sbox_dem * int(len(MainWindow.R_Sbox) / 8):MainWindow.Sbox_dem * int(len(MainWindow.R_Sbox) / 8) + (int(len(MainWindow.R_Sbox) / 8))]
        row = int(str(sub_r_i[0]) + str(sub_r_i[-1]), 2)
        col = int(str(''.join([str(i) for i in sub_r_i[1:-1]])), 2)
        sub_r_i1 = f"{Mã_DES.S_box[MainWindow.Sbox_dem][row][col]:04b}"
        for j in sub_r_i1:
            MainWindow.kdr.append(int(j))
        self.uic4.S_dr.setText(str(np.array(MainWindow.kdr)))
        MainWindow.Sbox_dem += 1
        if MainWindow.Sbox_dem == 8:
            self.uic4.But_Next.setEnabled(False)
            self.uic2.But_Sbox.setEnabled(False)
            self.uic2.But_P.setEnabled(True)
            MainWindow.R0 = MainWindow.kdr
        else:
            MainWindow.R0 = MainWindow.kdr1

    def HV_P(self):
        self.hvP_Window = QMainWindow()
        self.uic5 = Ui_MainWindow5()
        self.uic5.setupUi(self.hvP_Window)
        self.hvP_Window.show()
        danh_sach = [self.uic5.P_1,self.uic5.P_2,self.uic5.P_3,self.uic5.P_4]
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(Mã_DES.P[i]))
        self.uic5.kdvP.setText(str(np.array(MainWindow.kdr1)))
        MainWindow.R0 = Mã_DES.HV_line(MainWindow.kdr1,Mã_DES.P)
        self.uic5.kdrP.setText(str(np.array(MainWindow.R0)))
        self.uic2.hoanvi_kq.setText(str(np.array(MainWindow.R0)))
        self.uic2.But_P.setEnabled(False)
        self.uic2.But_HVP.setEnabled(False)
        self.uic2.But_MHNT_XDNCL.setEnabled(True)
        self.uic2.But_plus2.setEnabled(True)


    def C_L0(self):
        if MainWindow.bien_dem == 15:
            MainWindow.L0 = Mã_DES.XOR(MainWindow.L0, MainWindow.R0)
            self.uic2.L_1.setText(str(np.array(MainWindow.L0)))
            self.uic2.R_1.setText(str(np.array(MainWindow.temp)))
            self.uic2.But_HVIP_1.setEnabled(True)
        else:
            MainWindow.R0 = Mã_DES.XOR(MainWindow.R0,MainWindow.L0)
            self.uic2.R_1.setText(str(np.array(MainWindow.R0)))
            self.uic2.L_1.setText(str(np.array(MainWindow.temp)))
        self.uic2.But_plus2.setEnabled(False)
        self.uic2.But_MHNT_XDNCL.setEnabled(False)

    def VKT(self):
        if MainWindow.bien_dem == 15:
            r1 = []
            temp = MainWindow.r_0
            r0 = Mã_DES.HV_line(MainWindow.r_0, Mã_DES.E)
            r0 = Mã_DES.XOR(r0, MainWindow.Data[MainWindow.bien_dem])
            for i in range(int(len(r0) / 6)):
                sub_r_i = i[i * int(len(r0) / 8):i * int(len(r0) / 8) + (int(len(r0) / 8))]
                row = int(str(sub_r_i[0]) + str(sub_r_i[-1]), 2)
                col = int(str(''.join([str(i) for i in sub_r_i[1:-1]])), 2)
                sub_r_i1 = f"{Mã_DES.S_box[i][row][col]:04b}"
                for j in sub_r_i1:
                    r1.append(int(j))
            r1 = Mã_DES.HV_line(r1, Mã_DES.P)
            l1 = Mã_DES.XOR(MainWindow.l_0, r1)
            r1 = temp
        else:
            r1 = []
            l1 = MainWindow.r_0
            r0 = Mã_DES.HV_line(MainWindow.r_0, Mã_DES.E)
            r0 = Mã_DES.XOR(r0, MainWindow.Data[MainWindow.bien_dem])
            for i in range(int(len(r0) / 6)):
                sub_r_i = r0[i * int(len(r0) / 8):i * int(len(r0) / 8) + (int(len(r0) / 8))]
                row = int(str(sub_r_i[0]) + str(sub_r_i[-1]), 2)
                col = int(str(''.join([str(i) for i in sub_r_i[1:-1]])), 2)
                sub_r_i1 = f"{Mã_DES.S_box[i][row][col]:04b}"
                for j in sub_r_i1:
                    r1.append(int(j))
            r1 = Mã_DES.HV_line(r1, Mã_DES.P)
            r1 = Mã_DES.XOR(r1, MainWindow.l_0)
        MainWindow.bien_dem += 1                                                        # Bien dem day nay
        MainWindow.r_0 = r1
        MainWindow.R0 = r1
        MainWindow.l_0 = l1
        MainWindow.L0 = l1
        MainWindow.kdr = []
        MainWindow.kdr1 = []
        MainWindow.Sbox_dem = 0
        return MainWindow.open_Loop(self)

    def HVIP_1(self):
        self.HVIP_1_Window = QMainWindow()
        self.uic6 = Ui_MainWindow6()
        self.uic6.setupUi(self.HVIP_1_Window)
        self.HVIP_1_Window.show()
        self.Loop_Window.close()
        self.uic6.l_16.setText(str(np.array(MainWindow.L0)))
        self.uic6.r_16.setText(str(np.array(MainWindow.temp)))
        kq = MainWindow.L0 + MainWindow.temp
        self.uic6.l_r.setText(str(np.array(kq)))
        danh_sach = [self.uic6.IP_1,self.uic6.IP_2,self.uic6.IP_3,self.uic6.IP_4,
                     self.uic6.IP_5,self.uic6.IP_6,self.uic6.IP_7,self.uic6.IP_8]
        for i in range(len(danh_sach)):
            danh_sach[i].setText(str(Mã_DES.IP_1[i]))
        self.uic6.kqmh.setText(str(np.array(Mã_DES.HV_line(kq,Mã_DES.IP_1))))
        self.uic6.But_Save.clicked.connect(self.Save_Final_Data)

    def Save_Final_Data(self):
        file2write = open("Final Data.txt", 'w')
        file2write.write(str(np.array(Mã_DES.HV_line(MainWindow.L0 + MainWindow.temp,Mã_DES.IP_1))))
        file2write.close()


    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

