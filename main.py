
# Import Module
import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import numpy as np

# Folder Path
path = "F:\Meethi Folder\INTERNSHIPS\IIT Delhi\motifs_cor_sel"

# Change the directory
os.chdir(path)

# Read text File

# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".csv"):
		file_path = f"{path}\{file}"

		seq_data = pd.read_csv(file_path)
		seq_data = pd.DataFrame(seq_data)

		seq_data_tss = seq_data['TSS']
		seq_data = seq_data.drop(['TSS'], axis=1)


		pca = PCA(n_components=4)
		print("pca_training")
		pca.fit(seq_data)
		seq_data_transformed = pca.transform(seq_data)
		combined_df = pd.DataFrame(seq_data_transformed)
		combined_df['TSS'] = seq_data_tss


		# Logistic Regression
		x = combined_df.drop("TSS", axis=1)
		y = combined_df["TSS"]
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
		logreg = LogisticRegression()
		logreg.fit(x_train, y_train)
		pred = logreg.predict(x_test)
		x_test_df = pd.DataFrame(x_test)
		x_test_df["tss"] = y_test
		x_test_df["new_tss"] = pred

		name = file[:-4]

		x_test_df.to_csv(name + '_xtest.csv')










