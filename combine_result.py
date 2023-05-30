import pandas as pd
import numpy as np
import os

'''
di_motif = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_di\\di_xtest"
di_tss = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_di\\di_tss_xtest.csv"
tri_motif = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_tri\\tri_xtest"
tri_tss = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_tri\\tri_tss_xtest.csv"
tetra_motif = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_tetra\\tetra_xtest"
tetra_tss = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_tetra\\tetra_tss_xtest.csv"
di_16_motif = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_16_di\\di_16_xtest"
di_16_tss = "D:\\kopal_iitd\\SEProm_training\\all_motif_data_for_16_di\\di_16_tss_xtest.csv"
'''
di_selected_motif = "F:\\Meethi Folder\\INTERNSHIPS\\IIT Delhi\\motifs_cor_sel\\motif_xtest_di_selected"
di_selected_tss = "F:\\Meethi Folder\\INTERNSHIPS\\IIT Delhi\\motifs_cor_sel\\di_selected_tss_xtest.csv"

folder_motif_lst = [di_selected_motif]
file_tss_lst = [di_selected_tss]

for f,g in zip(folder_motif_lst, file_tss_lst):

    motif_dict = {"m_0": [], "m_1": [], "m_2": [], "m_3": []}
    os.chdir(f)
    counter = 1
    for file in os.listdir():
        if counter <= 3:
            motif_dict["m_0"].append(str(file))
            counter += 1
        elif counter>=4 and counter <=7:
            motif_dict["m_1"].append(str(file))
            counter += 1
        elif counter >= 8 and counter <= 11:
            motif_dict["m_2"].append(str(file))
            counter += 1
        elif counter>=12 and counter<=15:
            motif_dict["m_3"].append(str(file))
            counter += 1

    motif_pred_dict = {"m_0":[0]*5147, "m_1":[0]*5147, "m_2":[0]*5147, "m_3":[0]*5147, "motif_final":[0]*5147}
    final = [0]*5147

    for z in motif_dict.keys():

        lst = [0] * 5147
        # iterate through all file
        for x in motif_dict[z]:

            result_motif = pd.read_csv(f +"\\"+x)
            result_motif = pd.DataFrame(result_motif)
            result_tss = pd.read_csv(g)
            result_tss = pd.DataFrame(result_tss)

            #validating the files for same index
            comparison_column = np.where(result_motif["tss"] == result_tss["tss"], True, False)
            if False not in comparison_column: print("indexes matched")

            for i in range(0,5147):
                lst[i] = lst[i]+int(result_motif.iloc[i]["new_tss"])

        if z == "m_0":
            for i in range(0,5147):
                if lst[i]>=2:
                    motif_pred_dict["m_0"][i]= 1
        elif z == "m_1":
            for i in range(0,5147):
                if lst[i]>=3:
                    motif_pred_dict["m_1"][i] = 1
        elif z == "m_2":
            for i in range(0, 5147):
                if lst[i] >= 3:
                    motif_pred_dict["m_2"][i] = 1
        elif z == "m_3":
            for i in range(0, 5147):
                if lst[i] >= 3:
                    motif_pred_dict["m_3"][i] = 1

    for i in range(0,5147):
        temp = motif_pred_dict["m_0"][i] + motif_pred_dict["m_1"][i] + motif_pred_dict["m_2"][i] + motif_pred_dict["m_3"][i]
        if temp>=1:
            motif_pred_dict["motif_final"][i] = 1


    for i in range(0,5147):
        temp = motif_pred_dict["motif_final"][i] + result_tss.iloc[i]["new_tss"]
        if temp >=1:
            final[i] = 1


    #Accuracy
    comparison_column = np.where(final == result_tss["tss"], True, False)
    comp_lst = list(comparison_column)
    print(sum(comp_lst)/len(comp_lst))












