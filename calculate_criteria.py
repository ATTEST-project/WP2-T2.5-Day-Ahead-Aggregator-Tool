from xlrd import *
from numpy import *
from pyomo.environ import *
from math import *
import pandas as pd
from copy import *


def update_pi(m, m1_h_up, m2_h, m1_h_down, m3_h, m3_h_up, m3_h_down,
              k, h, pi, ro, load_in_bus_w, load_in_bus_g, load_in_bus_h, other_g, other_h):

    ###################################################################################################################
    # __________ Electricity __________
    ###################################################################################################################


    pi2_w_up = []
    for i in range(0, len(load_in_bus_w)):
        pi_temp_w_up = []
        for t in range(0, h):

            pi_temp_w_up.append(
                pi['w_up'][i][t] + ro['ro'] * (m.P_dso_up[k, i, t].value - m1_h_up[t].P_dso_up[k, i, 0].value))
        pi2_w_up.append(pi_temp_w_up)
    pi['w_up'] = deepcopy(pi2_w_up)

    pi2_w_down = []
    for i in range(0, len(load_in_bus_w)):
        pi_temp_w_down = []
        for t in range(0, h):
            pi_temp_w_down.append(
                pi['w_down'][i][t] + ro['ro'] * (m.P_dso_down[k, i, t].value - m1_h_down[t].P_dso_down[k, i, 0].value))
        pi2_w_down.append(pi_temp_w_down)
    pi['w_down'] = deepcopy(pi2_w_down)

    ###################################################################################################################
    # __________ Gas __________
    ###################################################################################################################


    if other_g['b_network']:
        pi2_g = []
        for i in range(0, len(load_in_bus_g)):
            pi_temp_g = []
            for t in range(0, h):
                pi_temp_g.append(
                    pi['g'][i][t] + ro['ro'] * (m.P_dso_gas[k, i, t].value - m2_h[t].P_dso_gas[i, 0].value))
            pi2_g.append(pi_temp_g)
        pi['g'] = deepcopy(pi2_g)



    ###################################################################################################################
    # __________ Heat __________
    ###################################################################################################################

    if other_h['b_network']:
        pi2_h = []
        for i in range(0, len(load_in_bus_h)):
            pi_temp_h = []
            for t in range(0, h):
                pi_temp_h.append(
                    pi['h'][i][t] + ro['ro'] * (m.P_dso_heat[k, i, t].value - m3_h[t].P_dso_heat[i, 0].value))
            pi2_h.append(pi_temp_h)
        pi['h'] = deepcopy(pi2_h)

        pi2_h_up = []
        for i in range(0, len(load_in_bus_h)):
            pi_temp_h_up = []
            for t in range(0, h):
                pi_temp_h_up.append(
                    pi['h_up'][i][t] + ro['ro'] * (m.P_dso_heat_up[k, i, t].value - m3_h_up[t].P_dso_heat_up[i, 0].value))
            pi2_h_up.append(pi_temp_h_up)
        pi['h_up'] = deepcopy(pi2_h_up)

        pi2_h_down = []
        for i in range(0, len(load_in_bus_h)):
            pi_temp_h_down = []
            for t in range(0, h):
                pi_temp_h_down.append(
                    pi['h_down'][i][t] + ro['ro'] * (
                                m.P_dso_heat_down[k, i, t].value - m3_h_down[t].P_dso_heat_down[i, 0].value))
            pi2_h_down.append(pi_temp_h_down)
        pi['h_down'] = deepcopy(pi2_h_down)


    return pi






def calculate_criteria(m, m1_h_up, m1_h_down, m2_h, m3_h, m3_h_up, m3_h_down, h, k, iter,
                       load_in_bus_w, load_in_bus_g, load_in_bus_h, ro,
                       P_dso_old_w_up, P_dso_old_w_down, P_dso_old_g, P_dso_old_h, P_dso_old_h_up, P_dso_old_h_down,
                       other_g, other_h):

    ###################################################################################################################
    criteria = 0

    criteria = criteria + sum(
        sum((m.P_dso_up[k, i, t].value - m1_h_up[t].P_dso_up[k, i, 0].value) ** 2
            for t in range(0, h)) for i in range(0, len(load_in_bus_w)))

    criteria = criteria + sum(
        sum((m.P_dso_down[k, i, t].value - m1_h_down[t].P_dso_down[k, i, 0].value) ** 2
            for t in range(0, h)) for i in range(0, len(load_in_bus_w)))

    ###################################################################################################################
    if other_g['b_network']:
        criteria = criteria + sum(
            sum((m.P_dso_gas[k, i, t].value - m2_h[t].P_dso_gas[i, 0].value) ** 2
                for t in range(0, h)) for i in range(0, len(load_in_bus_g)))

    ###################################################################################################################
    if other_h['b_network']:
        criteria = criteria + sum(
            sum((m.P_dso_heat[k, i, t].value - m3_h[t].P_dso_heat[i, 0].value) ** 2
                for t in range(0, h)) for i in range(0, len(load_in_bus_h)))

        criteria = criteria + sum(
            sum((m.P_dso_heat_up[k, i, t].value - m3_h_up[t].P_dso_heat_up[i, 0].value) ** 2
                for t in range(0, h)) for i in range(0, len(load_in_bus_h)))

        criteria = criteria + sum(
            sum((m.P_dso_heat_down[k, i, t].value - m3_h_down[t].P_dso_heat_down[i, 0].value) ** 2
                for t in range(0, h)) for i in range(0, len(load_in_bus_h)))

    ###################################################################################################################

    criteria = sqrt(criteria)


    ###################################################################################################################
    ###################################################################################################################
    ###################################################################################################################
    ###################################################################################################################

    criteria_dual = 1

    if iter >= 1:
        aux_gas = 0
        if other_g['b_network']:
            aux_gas = sum(sum((ro['ro'] * (m2_h[t].P_dso_gas[i, 0].value - P_dso_old_g[t][i])) ** 2
                              for t in range(0, h)) for i in range(0, len(load_in_bus_g)))
        aux_heat = 0
        if other_h['b_network']:
            aux_heat = sum(sum((ro['ro'] * (m3_h[t].P_dso_heat[i, 0].value - P_dso_old_h[t][i])) ** 2
                               for t in range(0, h)) for i in range(0, len(load_in_bus_h))) + \
                       sum(sum((ro['ro'] * (m3_h_up[t].P_dso_heat_up[i, 0].value - P_dso_old_h_up[t][i])) ** 2
                               for t in range(0, h)) for i in range(0, len(load_in_bus_h))) + \
                       sum(sum(
                           (ro['ro'] * (m3_h_down[t].P_dso_heat_down[i, 0].value - P_dso_old_h_down[t][i])) ** 2
                           for t in range(0, h)) for i in range(0, len(load_in_bus_h)))
        criteria_dual = sqrt(
                             sum(sum((ro['ro'] * (m1_h_up[t].P_dso_up[k, i, 0].value - P_dso_old_w_up[t][i])) ** 2
                                     for t in range(0, h)) for i in range(0, len(load_in_bus_w))) + \

                             sum(sum((ro['ro'] * (m1_h_down[t].P_dso_down[k, i, 0].value - P_dso_old_w_down[t][i])) ** 2
                                     for t in range(0, h)) for i in range(0, len(load_in_bus_w))) +
                             aux_gas +
                             aux_heat)


    return criteria, criteria_dual




















