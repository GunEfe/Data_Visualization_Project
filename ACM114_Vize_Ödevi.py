import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data yükleme
pop_fp = 'https://raw.githubusercontent.com/GunEfe/Data_Visualization_Project/main/Population.csv'
pop_data = pd.read_csv(pop_fp, index_col="Years", parse_dates=True)

MedianAge_fp = 'https://raw.githubusercontent.com/GunEfe/Data_Visualization_Project/main/MedianAge.csv'
MedianAge_data = pd.read_csv(MedianAge_fp, index_col="Years")

FertilityRate_fp = 'https://raw.githubusercontent.com/GunEfe/Data_Visualization_Project/main/FertilityRate.csv'
FertilityRate_data = pd.read_csv(FertilityRate_fp, index_col="Years")

ElderlyPop_fp ='https://raw.githubusercontent.com/GunEfe/Data_Visualization_Project/main/ElderlyPop.csv'
ElderlyPop_data = pd.read_csv(ElderlyPop_fp)


# Girdi
print("Bilgi almak istediğiniz ülkeyi giriniz.")
a = input("İtalya için 'I', Finlandiya için 'F', Letonya için 'L' harfini giriniz: ")

# Girdiyi Sorgulama

# İtalya
if a == "I":

	q = input("İtalya Nüfus Grafiği için 'IN' kodunu giriniz: ")

	if q == "IN":
		print("İtalya'nın Nüfus Grafiği")
		specific1 = pop_data.iloc[0:6,1:2]
		sns.set_style("ticks")
		plt.plot(specific1, marker="*",color="teal")
		plt.xlabel("Yıllar")
		plt.ylabel("Nüfus(Milyon)")
		plt.show()

	t = input("İtalya için Yaşlı Nüfus Oranını 'IYN' kodu ile görebilirsiniz: ")


	if t == "IYN":

		print("İtalya Yaşlı Nüfus Oranı")
		sns.set_theme(style="whitegrid")

		ax = sns.barplot(x="Years", y='ItalyElderlyPop(%)', data=ElderlyPop_data, palette="YlOrBr")
		plt.show()
		


# Finlandiya
elif a == "F":


	q = input("Finlandiya Nüfus Grafiği için 'FN' kodunu giriniz: ")

	if q == "FN":
		print("Finlandiya'nın Nüfus Grafiği")

		specific2 = pop_data.iloc[0:6,2:3]
		sns.set_style("ticks")
		plt.plot(specific2, "bo-")
		plt.xlabel("Yıllar")
		plt.ylabel("Nüfus(Milyon)")
		plt.show()

	t = input("Finlandiya için Yaşlı Nüfus Oranını 'FYN' kodu ile görebilirsiniz: ")



	if t == "FYN":

		print("Finlandiya Yaşlı Nüfus Oranı")
		sns.set_theme(style="whitegrid")

		ax = sns.barplot(x="Years", y='FinlandElderlyPop(%)', data=ElderlyPop_data, palette="Blues_d")
		plt.show()



# Letonya
elif a == "L":


	q = input("Letonya Nüfus Grafiği için 'LN' kodunu giriniz: " )

	if q == "LN":
		print("Letonya'nın Nüfus Grafiği")
		    
		specific3 = pop_data.iloc[0:6,3:4]
		sns.set_style("ticks")
		plt.plot(specific3, color="orange")
		plt.xlabel("Yıllar")
		plt.ylabel("Nüfus(Milyon)")
		plt.show()

	t = input("Letonya için Yaşlı Nüfus Oranını 'LYN' kodu ile görebilirsiniz: ")


	if t == "LYN": 

		print("Letonya Yaşlı Nüfus Oranı")
		sns.set_theme(style="whitegrid")

		ax = sns.barplot(x="Years", y='LatviaElderlyPop(%)', data=ElderlyPop_data, palette="dark:salmon_r")
		plt.show()



# Genel Karşılaştırmalı Medyan Yaş ve Doğurganlık Oranları

# Girdi
w = input("Karşılaştırmalı Medyan Yaşlarını 'M', Doğurganlık Oranlarını 'F' ile görebilirsiniz: ")

# Girdiyi Sorgulama
if w == "M":

	plt.figure(figsize=(22,8))

	plt.title("Median Age, by Years")

	ax = sns.heatmap(MedianAge_data, cmap="YlGnBu", annot=True )
	plt.show()



elif w == "F":
	plt.figure(figsize=(22,8))

	plt.title("Fertility Rate, by Years")
	    
	sns.heatmap(data=FertilityRate_data, annot=True)
	plt.show()