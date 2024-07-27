# File: ReadFile.py

# Description: Reads the Yale Bright Star Catalogue bsc5.dat and converts it to a comma-delimited .csv file

# Name: Andrew Harvey

# UT EID: ach4368

# Date: 4/4/23

import csv

def main():
    with open("bsc5.dat") as input_file, open("bsc5.csv", "w", newline = "") as output_file:
        writer = csv.writer(output_file)

        # create the header with the column names
        writer.writerow(["HR", "Name", "DM", "HD", "SAO", "FK5", "IRflag", "r_IRflag", "Multiple",
            "ADS", "ADSComp", "VarID", "RAh1900", "RAm1900", "RAs1900", "DE-1900", "DEd1900", "DEm1900", 
            "DEs1900", "RAh", "RAm", "RAs", "DE-", "DEd", "DEm", "DEs", "GLON", "GLAT", "Vmag", "n_Vmag", "u_Vmag", "B-V",
            "u_B-V", "U-B", "u_U-B", "R-I", "n_R-I", "SpType", "n_SpType", "pmRA", "pmDE", "n_Parallax", "Parallax",
            "RadVel", "n_RadVel", "l_RotVel", "RotVel", "u_RotVel", "Dmag", "Sep", "MultID", "MultCnt", "NoteFlag"])

        for line in input_file:
            HR = line[0:4].strip() # Split the line into columns
            Name = line[4:14].strip()
            DM = line[14:25].strip()
            HD = line[25:31].strip()
            SAO = line[31:37].strip()
            FK5 = line[37:41].strip()
            IRflag = line [41:42].strip()
            r_IRflag = line[42:43].strip()
            Multiple = line[43:44].strip()
            ADS = line[44:49].strip()
            ADSComp = line[49:51].strip()
            VarID = line[51:60].strip()
            RAh1900 = line[60:62].strip()
            RAm1900 = line[62:64].strip()
            RAs1900 = line[64:68].strip()
            DE_1900 = line[68:69].strip()
            DEd1900 = line[69:71].strip()
            DEm1900 = line[71:73].strip()
            DEs1900 = line[73:75].strip()
            RAh = line[75:77].strip()
            RAm = line[77:79].strip()
            RAs = line[79:83].strip()
            DE_ = line[83:84].strip()
            DEd = line[84:86].strip()
            DEm = line[86:88].strip()
            DEs = line[88:90].strip()
            GLON = line[90:96].strip()
            GLAT = line[96:102].strip()
            Vmag = line[102:107].strip()
            n_Vmag = line[107:108].strip()
            u_Vmag = line[108:109].strip()
            B_V = line[109:114].strip()
            u_B_V = line[114:115].strip()
            U_B = line[115:120].strip()
            u_U_B = line[120:121].strip()
            R_I = line[121:126].strip()
            n_R_I = line[126:127].strip()
            SpType = line[127:147].strip()
            n_SpType = line[147:148].strip()
            pmRA = line[148:154].strip()
            pmDE = line[154:160].strip()
            n_Parallax = line[160:161].strip()
            Parallax = line[161:166].strip()
            RadVel = line[166:170].strip()
            n_RadVel = line[170:174].strip()
            l_RotVel = line[174:176].strip()
            RotVel = line[176:179].strip()
            u_RotVel = line[179:180].strip()
            Dmag = line[180:184].strip()
            Sep = line[184:190].strip()
            MultID = line[190:194].strip()
            MultCnt = line[194:196].strip()
            NoteFlag =line[196:197].strip()

            #writes each row in the csv file
            writer.writerow([HR, Name, DM, HD, SAO, FK5, IRflag, r_IRflag, Multiple,
            ADS, ADSComp, VarID, RAh1900, RAm1900, RAs1900, DE_1900, DEd1900, DEm1900, 
            DEs1900, RAh, RAm, RAs, DE_, DEd, DEm, DEs, GLON, GLAT, Vmag, n_Vmag, u_Vmag, B_V,
            u_B_V, U_B, u_U_B, R_I, n_R_I, SpType, n_SpType, pmRA, pmDE, n_Parallax, Parallax,
            RadVel, n_RadVel, l_RotVel, RotVel, u_RotVel, Dmag, Sep, MultID, MultCnt, NoteFlag])


if __name__ == "__main__":
    main()
