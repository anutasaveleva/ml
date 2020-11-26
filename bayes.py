import numpy as np
import pandas as pd


def read_data(file):
    data = pd.read_csv(file, delimiter=';')
    return data


diseases = read_data('disease.csv')
symptoms = read_data('symptom.csv')

# считаем вероятности болезней
disease_probs = []
pat_count = diseases["количество пациентов"].values
all_pats = pat_count[-1]
for item in pat_count[:-1]:
    disease_probs.append(item / all_pats)

# Задаем массив симптомов больного
our_symptoms = [np.random.randint(0, 2) for i in range(len(symptoms) - 1)]
print(our_symptoms)

our_probs = [1] * (len(diseases["Болезнь"]) - 1)
for i in range(len(diseases["Болезнь"]) - 1):
    our_probs[i] *= disease_probs[i]
    for j in range(len(symptoms)-1):
        if our_symptoms[j]==1:
            our_probs[i] *= float(symptoms.iloc[j][i+1].replace(',', '.'))
print(our_probs.index(max(our_probs)))
print("Вероятный диагноз пациента: " + diseases["Болезнь"][our_probs.index(max(our_probs))])