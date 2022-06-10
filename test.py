import random
import numpy as np
import matplotlib.pyplot as plt

species = 200
iters = 2000

distances = np.loadtxt(open("./Distances.csv", "rb"), delimiter=",")
intervenants = np.loadtxt(open("./Intervenants.csv", "rb"), dtype=str, delimiter=",")
# print(intervenants)
# , usecols=(0, 2)
missions = np.loadtxt(open("./Missions.csv", "rb"), dtype=str, delimiter=",")
Nbr_mission = len(missions)
Nbr_inter = len(intervenants)
distances = distances[:Nbr_mission, :Nbr_mission]
# print(len(distances))  # 96
competences = []
specialities = []
for i in range(Nbr_inter):
    if intervenants[:, 1][i] not in competences:
        competences.append(intervenants[:, 1][i])
    if intervenants[:, 2][i] not in specialities:
        specialities.append(intervenants[:, 2][i])
    ''' in fact, we need to use array 'missions' to calculate, 
    but there is a coincidence that the competences and the specialities
    in 'missions' and those in 'intervenants'. Using array 'intervenants'
     can definitely reduce the calculation '''
# print(competences) # ['LSF', 'LPC']
# print(specialites) # ['Jardinage', 'Mecanique', 'Menuiserie', 'Electricite', 'Musique']
# print(Nbr_inter) # 6
# print(intervenants[:, 1]) # ['LSF' 'LPC' 'LSF' 'LSF' 'LPC' 'LPC']
print(intervenants)

def cal_dis():
    '''
    :return: a quantized value according to the distance
    '''
def cal_degree_of_satisfaction():
    '''
    :return: a quantized value according to the satisfaction
    '''
def cal_deviation():
    '''
    :return: a quantized value according to the deviation
    '''
def calfit(gene, Nbr_gene):
    '''
    :param gene: sequence of the arrangement of the 'intervenantes'
    :param Nbr_gene: lens of gene, lens of 'mission'
    :return: a quantized value according to three function:
    'cal_dis()', 'cal_degree_of_satisfaction()', 'cal_deviation()'
    '''

def detect(gene):
    '''
    :param gene: sequence of the arrangement of 'intervenantes'
    :return: gene or None
    this function is used to detect if the gene could exist because of these constraints
    '''

def crossover(father, mothor):
    '''
    :param father:
    :param mothor:
    :return: son1 and son2, but we need to detect if the two sons exist
    by using function 'detect()'
    '''
def mutate(sample):
    '''
    :param sample:
    :return:
    '''
