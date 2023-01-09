import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

qualidade.automf(number=3, 
names=['ruim', 'média', 'boa'])

servico.automf(number=3,
names=['ruim', 'aceitável', 'ótimo'])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 10])
gorjeta['média'] = fuzz.trimf(gorjeta.universe, [0, 10, 20])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [10, 20, 20])

regra1 = ctrl.Rule(qualidade['ruim'] | servico ['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['média'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['boa'], gorjeta['alta'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])

sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['qualidade'] = 8.5
sistema.input['servico'] = 6.5
sistema.compute()

print(sistema.output['gorjeta'])
gorjeta.view(sim= sistema)
input()