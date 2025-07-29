#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:03 2024

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/25-SS-GLO-1 - Clean Dataset.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    gender = bd.Indicator(df, "Gender", 0, ['2'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    gender.add_var_order(['Female', 'Male'])
    indicators.append(gender)
    
    ls_vs3 = bd.Indicator(df, "Livelihood_Fsupport3", 0, ['28-1', '28-2', '28-3', '28-4', '28-5', '28-6'], i_cal=None, i_type='count', description='Which are these sources of income?', period='endline', target = None)
    ls_vs3.add_breakdown({'2':'Gender'})
    ls_vs3.add_label(["Retail shop",
                      "Grocery",
                      "Tailoring shop",
                      "Food kiosk/restaurant",
                      "Farming business",
                      "Other"])
    indicators.append(ls_vs3)
    
    nationality = bd.Indicator(df, "Nationality", 0, ['3'], i_cal=None, i_type='count', description="Respondent's nationality", period='endline', target = None)
    nationality.add_breakdown({'2':'Gender'})
    indicators.append(nationality)
    
    age = bd.Indicator(df, "Age Group", 0, ['Age Group'], i_cal=None, i_type='count', description='Age group distribution', period='endline', target = None, visual = False)
    age.add_breakdown({'2':'Gender', '3':'Country'})
    indicators.append(age)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability status', period='endline', target = None)
    disability.add_breakdown({'2':'Gender', '3':'Country', 'Age Group':'Age Group'})
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    project = bd.Indicator(df, "Project", 0, ['4'], i_cal=None, i_type='count', description='Project distribution', period='endline', target = None, visual = False)
    project.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    project.add_var_order(["(1) CBM - Turkana Inclusive Livelihood and Resilience Program",
                           "(2) Save the Children - Improving nutrition security and resilience of drought affected communities through disaster risk reduction and economic recovery",
                           "(3) Swissaid - Strengthening vulnerable Community Seed Banks for emergency preparedness, response and recovery",
                           "(4) VSF-Suisse - Emergency Food Security and Livelihoods Support for Vulnerable Drought Affected Pastoralists in Samburu and Isiolo Counties (EFSLS)",
                           "(5) Caritas - Immediate Recovery of Drought Affected Communities",
                           "(6) Helvetas - Emergency and Recovery for Women Pastoralists in Borana (ERWOP - Borana), Oromia Region, Ethiopia",
                           "(7) VSF-Suisse - Borana Drought Response (BDR) Project",
                           "(8) VSF-Suisse - Emergency Response for Flood-Affected Communities",
                           "(9) VSF-Suisse - Emergency Lifesaving and Livelihoods Protection Project",
                           "(10) VSF-Suisse - Emergency Lifesaving and Livelihood Support to Vulnerable IDPs and Host Communities Affected by Floods"])
    indicators.append(project)
    
    project_g = bd.Indicator(df, "Project_group", 0, ['project'], i_cal=None, i_type='count', description='Project distribution', period='endline', target = None, visual = False)
    project_g.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    project_g.add_var_order([1,2,3,4,5,6,7,8,9,10])
    indicators.append(project_g)
    
    intervention = bd.Indicator(df, "Intervention_2", 0, ['18'], i_cal=None, i_type='count', description='What type of project did you participate in?', period='endline', target = None)
    intervention.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    intervention.add_var_order(["Livelihood support (Multipurpose Cash Assistance, Agricultural, Cash for Work, Unconditional Cash Transfer, and microgrant)",
                            "WASH",
                            "Disaster risk reduction (DRR)",
                            "Veterinary support (Animal health)"])
    indicators.append(intervention)
    
    intervention2 = bd.Indicator(df, "Intervention_2", 0, ['18-2-1', '18-2-2', '18-2-3', '18-2-4'], i_cal=None, i_type='count', description='What type of project did you participate in? (Multiple)', period='endline', target = None)
    intervention2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    intervention2.add_var_change({1: "Yes", 0: "No"})
    intervention2.add_var_order([1, 0])
    intervention2.add_label(["Livelihood support",
                            "WASH",
                            "Disaster risk reduction",
                            "Veterinary support"])
    indicators.append(intervention2)
    
    
    ls_vs3 = bd.Indicator(df, "Livelihood_Fsupport3", 0, ['28-1', '28-2', '28-3', '28-4', '28-5', '28-6'], i_cal=None, i_type='count', description='Which are these sources of income?', period='endline', target = None)
    ls_vs3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vs3.add_var_change({1: "Yes", 0: "No"})
    ls_vs3.add_var_order([1, 0])
    ls_vs3.add_label(["Retail shop",
                      "Grocery",
                      "Tailoring shop",
                      "Food kiosk/restaurant",
                      "Farming business",
                      "Other"])
    indicators.append(ls_vs3)
    
    fcs_g = bd.Indicator(df, "FCS_group", 0, ['FCS_group'], i_cal=None, i_type='count', description='FCS Group', period='endline', target = None)
    fcs_g.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    fcs_g.add_var_order(["Acceptable food consumption",
                            "Borderline food consumption",
                            "Poor food consumption"])
    indicators.append(fcs_g)
    

    # Livelihood Support
    ls_vsla = bd.Indicator(df, "Livelihood_VSLA", 0, ['19'], i_cal=None, i_type='count', description='Are you aware of any VSLA (Village Savings and Loan Associations) or self-help groups such as CBOs established through the project?', period='endline', target = None, visual = False)
    ls_vsla.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vsla.add_var_order(["Yes","No"])
    indicators.append(ls_vsla)
    
    ls_vsla2 = bd.Indicator(df, "Livelihood_VSLA2", 0, ['20'], i_cal=None, i_type='count', description='To what extent are the VSLA/self-help groups still operational?', period='endline', target = None)
    ls_vsla2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vsla2.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_vsla2)
    
    ls_vsla3 = bd.Indicator(df, "Livelihood_VSLA3", 0, ['21'], i_cal=None, i_type='count', description='Has any of them managed to sell foodstuffs commercially?', period='endline', target = None, visual = False)
    ls_vsla3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vsla3.add_var_order(["Yes","No","Unsure"])
    indicators.append(ls_vsla3)
    
    ls_agropastoral = bd.Indicator(df, "Livelihood_Agro", 0, ['22'], i_cal=None, i_type='count', description='Did you receive any interventions related to agropastoral activities through the project?', period='endline', target = None, visual = False)
    ls_agropastoral.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_agropastoral.add_var_order(["Yes","No"])
    indicators.append(ls_agropastoral)
    
    ls_agropastoral2 = bd.Indicator(df, "Livelihood_Agro2", 0, ['23'], i_cal=None, i_type='count', description='To what extent have food security conditions improved because of the interventions?', period='endline', target = None)
    ls_agropastoral2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_agropastoral2.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_agropastoral2)
    
    ls_vs = bd.Indicator(df, "Livelihood_Fsupport", 0, ['24'], i_cal=None, i_type='count', description='Have you participated in Village Savings and Loan Associations (VSLAs), women’s enterprise fund, or other financial support programs?', period='endline', target = None, visual = False)
    ls_vs.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vs.add_var_order(["Yes","No"])
    indicators.append(ls_vs)
    
    ls_vs2 = bd.Indicator(df, "Livelihood_Fsupport2", 0, ['26'], i_cal=None, i_type='count', description='Since participating in VSLAs or related programs, has your source of income become more diversified compared to before?', period='endline', target = None, visual = False)
    ls_vs2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vs2.add_var_order(["Yes","No"])
    indicators.append(ls_vs2)
    
    ls_vs3 = bd.Indicator(df, "Livelihood_Fsupport3", 0, ['28-1', '28-2', '28-3', '28-4', '28-5', '28-6'], i_cal=None, i_type='count', description='Which are these sources of income?', period='endline', target = None)
    ls_vs3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_vs3.add_var_change({1: "Yes", 0: "No"})
    ls_vs3.add_var_order([1, 0])
    ls_vs3.add_label(["Retail shop",
                      "Grocery",
                      "Tailoring shop",
                      "Food kiosk/restaurant",
                      "Farming business",
                      "Other"])
    indicators.append(ls_vs3)
    
    df_2 = df[df['project'] == 2]
    ls_micro = bd.Indicator(df_2, "Livelihood_Micro", 0, ['30'], i_cal=None, i_type='count', description='To what extent has your access to micro-credit improved?', period='endline', target = None)
    ls_micro.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_micro.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_micro)
    
    ls_micro2 = bd.Indicator(df, "Livelihood_Micro2", 0, ['31'], i_cal=None, i_type='count', description='Have you taken any credit since you joined the VSLA or related project groups?', period='endline', target = None, visual = False)
    ls_micro2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_micro2.add_var_order(["Yes","No"])
    indicators.append(ls_micro2)
    
    ls_micro3 = bd.Indicator(df, "Livelihood_Micro3", 0, ['33'], i_cal=None, i_type='count', description='What was the credit used for?', period='endline', target = None)
    ls_micro3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_micro3.add_var_order(["Personal consumption",
                             "New business investment",
                             "Starting up a new income stream",
                             "Repaying other creditors",
                             "Other"])
    indicators.append(ls_micro3)
    
    ls_micro4 = bd.Indicator(df, "Livelihood_Micro4", 0, ['34'], i_cal=None, i_type='count', description='In the most recent instance you took credit, what is the status of repayment for this facility?', period='endline', target = None, visual = False)
    ls_micro4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_micro4.add_var_order(["I have not started paying",
                             "I have missed a couple of payment instalments",
                             "I have started paying and I am on course with the payment schedule and instalments",
                             "I have completed paying the credit",
                             "Other"])
    indicators.append(ls_micro4)
    
    ls_cash = bd.Indicator(df, "Livelihood_Cash", 0, ['35'], i_cal=None, i_type='count', description='Did you receive unconditional cash transfer, micro-grant, or multi-purpose cash transfer through the project?', period='endline', target = None)
    ls_cash.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash.add_var_order(["Yes","No"])
    indicators.append(ls_cash)
    
    ls_cash2 = bd.Indicator(df, "Livelihood_Cash2", 0, ['35-1-1', '35-1-2', '35-1-3'], i_cal=None, i_type='count', description='Please specify the type of financial support you received', period='endline', target = None)
    ls_cash2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash2.add_var_change({1: "Yes", 0: "No"})
    ls_cash2.add_var_order([1, 0])
    ls_cash2.add_label(["Unconditional cash transfer",
                        "Multi-purpose cash transfer",
                        "Micro-grant"])
    indicators.append(ls_cash2)
    
    ls_cash3 = bd.Indicator(df, "Livelihood_Cash3", 0, ['36'], i_cal=None, i_type='count', description='Did the financial support serve as a bridge until income from the recovery of agropastoral activities or business activities became available?', target = None, visual = False)
    ls_cash3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash3.add_var_order(["Yes","No"])
    indicators.append(ls_cash3)
    
    ls_cash4 = bd.Indicator(df, "Livelihood_Cash4", 0, ['37'], i_cal=None, i_type='count', description='To what extent did the financial support serve as a bridge to enable your household to meet its needs?', period='endline', target = None)
    ls_cash4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash4.add_var_order(["Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_cash4)
    
    df_8 = df[df['project'] == 8]
    ls_cash5 = bd.Indicator(df_8, "Livelihood_Cash5", 0, ['38'], i_cal=None, i_type='count', description='After receiving the financial support, was your household able to meet all, most, some, or none of its basic needs, as you define them?', period='endline', target = None, visual = False)
    ls_cash5.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_cash5.add_var_order(["Able to meet all basic needs",
                            "Able to meet most basic needs",
                            "Able to meet some basic needs",
                            "Able to meet no basic needs"])
    indicators.append(ls_cash5)
    
    ls_cash6 = bd.Indicator(df, "Livelihood_Cash6", 0, ['39'], i_cal=None, i_type='count', description='Was the assistance appropriate to your needs or those of members of the community?', target = None)
    ls_cash6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash6.add_var_order(["Yes","Partially","No"])
    indicators.append(ls_cash6)
    
    ls_cash7 = bd.Indicator(df, "Livelihood_Cash7", 0, ['40'], i_cal=None, i_type='count', description='Did you feel safe while receiving the assistance?', target = None, visual = False)
    ls_cash7.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash7.add_var_order(["Yes","No"])
    indicators.append(ls_cash7)
    
    ls_cash8 = bd.Indicator(df, "Livelihood_Cash8", 0, ['41'], i_cal=None, i_type='count', description='Have you received the assistance well in time to properly respond to your needs?', target = None, visual = False)
    ls_cash8.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_cash8.add_var_order(["Yes","No"])
    indicators.append(ls_cash8)
    
    ls_business = bd.Indicator(df, "Livelihood_Business", 0, ['42'], i_cal=None, i_type='count', description='Did you start your own business within the past three years?', target = None, visual = False)
    ls_business.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business.add_var_order(["Yes","No"])
    indicators.append(ls_business)
    
    ls_business2 = bd.Indicator(df, "Livelihood_Business2", 0, ['43'], i_cal=None, i_type='count', description='Do you think the project provided enough support to help you overcome the barriers you faced?', target = None)
    ls_business2.add_breakdown({'2':'Gender','3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business2.add_var_order(["Yes","No"])
    indicators.append(ls_business2)
    
    ls_business3 = bd.Indicator(df, "Livelihood_Business3", 0, ['44'], i_cal=None, i_type='count', description='What challenges did you face the most in running your business?', target = None, visual = False)
    ls_business3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    ls_business3.add_var_order(["Lack of information on business management",
                                "Disrupted social networks affecting your target market",
                                "Marketing of your business products",
                                "Accessing stock for your business",
                                "Accessing finance to expand or improve your business",
                                "Recruiting the right staff",
                                "None of them",
                                "Other"])
    indicators.append(ls_business3)
    
    ls_business4 = bd.Indicator(df, "Livelihood_Business4", 0, ['45'], i_cal=None, i_type='count', description='To what extent do you think the project provided enough support to help you overcome the barriers you faced?', period='endline', target = None)
    ls_business4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business4.add_var_order(["Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_business4)
    
    ls_business5 = bd.Indicator(df, "Livelihood_Business5", 0, ['46'], i_cal=None, i_type='count', description='Have you participated in any business skills training programs provided by the project?', target = None, visual = False)
    ls_business5.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business5.add_var_order(["Yes","No"])
    indicators.append(ls_business5)
    
    ls_business6 = bd.Indicator(df, "Livelihood_Business6", 0, ['47-1', '47-2', '47-3', '47-4', '47-5', '47-6', '47-7', '47-8', '47-9'], i_cal=None, i_type='count', description='Which types of business skills training programs have you participated in? ', period='endline', target = None)
    ls_business6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business6.add_var_change({1: "Yes", 0: "No"})
    ls_business6.add_var_order([1, 0])
    ls_business6.add_label(["Business management",
                            "Business planning",
                            "Marketing",
                            "Branding",
                            "Record keeping",
                            "Financial planning",
                            "Access to financing",
                            "Costing and pricing",
                            "Other"])
    indicators.append(ls_business6)
    
    ls_business7 = bd.Indicator(df, "Livelihood_Business7", 0, ['48'], i_cal=None, i_type='count', description='To what extent did the training programs improve your business skills?', period='endline', target = None)
    ls_business7.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business7.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_business7)
    
    ls_business8 = bd.Indicator(df, "Livelihood_Business8", 0, ['49'], i_cal=None, i_type='count', description='Has the business skills training helped you increase your income?', target = None)
    ls_business8.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_business8.add_var_order(["Yes","No"])
    indicators.append(ls_business8)
    
    ls_restore = bd.Indicator(df, "Livelihood_Restore", 0, ['51'], i_cal=None, i_type='count', description='Are you aware of any irrigation facilities restored by the project?', target = None, visual = False)
    ls_restore.add_breakdown({'2':'Gender','3':'Country', 'Disability':'Disability','project':'Project'})
    ls_restore.add_var_order(["Yes","No"])
    indicators.append(ls_restore)
    
    ls_restore2 = bd.Indicator(df, "Livelihood_Restore2", 0, ['52'], i_cal=None, i_type='count', description='To what extent are the restored irrigation facilities still operational?', period='endline', target = None)
    ls_restore2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_restore2.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_restore2)
    
    ls_restore3 = bd.Indicator(df, "Livelihood_Restore3", 0, ['53'], i_cal=None, i_type='count', description='Are you aware of any seed banks established through the project?', target = None, visual = False)
    ls_restore3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_restore3.add_var_order(["Yes","No","Unsure"])
    indicators.append(ls_restore3)
    
    ls_restore4 = bd.Indicator(df, "Livelihood_Restore4", 0, ['54'], i_cal=None, i_type='count', description='To what extent are seed banks still operational?', period='endline', target = None)
    ls_restore4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_restore4.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_restore4)
    
    ls_restore5 = bd.Indicator(df_8, "Livelihood_Restore5", 0, ['58'], i_cal=None, i_type='count', description='After the project intervention, were you able to restore crop or vegetable production?', target = None, visual = False)
    ls_restore5.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_restore5.add_var_order(["Yes","No"])
    indicators.append(ls_restore5)
    
    ls_restore6 = bd.Indicator(df_8, "Livelihood_Restore6", 0, ['59'], i_cal=None, i_type='count', description='To what extent has crop or vegetable production been restored?', target = None, visual = False)
    ls_restore6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_restore6.add_var_order(["Low",
                                "Moderate",
                                "High",
                                "Very high"])
    indicators.append(ls_restore6)
    
    df_10 = df[df['project'] == 10]
    ls_emer_agri = bd.Indicator(df_10, "Livelihood_Emer", 0, ['55'], i_cal=None, i_type='count', description='Did you receive emergency agricultural support?', target = None, visual = False)
    ls_emer_agri.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_emer_agri.add_var_order(["Yes","No"])
    indicators.append(ls_emer_agri)
    
    ls_emer_agri2 = bd.Indicator(df_10, "Livelihood_Emer2", 0, ['56'], i_cal=None, i_type='count', description='Do you think the quantity of seed distribution was sufficient?', target = None, visual = False)
    ls_emer_agri2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_emer_agri2.add_var_order(["Yes","No"])
    indicators.append(ls_emer_agri2)
    
    ls_emer_agri3 = bd.Indicator(df_10, "Livelihood_Emer3", 0, ['57'], i_cal=None, i_type='count', description='Do you think the quantity of assorted tools distribution was sufficient?', target = None, visual = False)
    ls_emer_agri3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_emer_agri3.add_var_order(["Yes","No"])
    indicators.append(ls_emer_agri3)
    
    df_3 =df[df['project'] == 3]
    ls_seed = bd.Indicator(df_3, "Livelihood_Seed", 0, ['60'], i_cal=None, i_type='count', description='To what extent has your seed security been improved?', period='endline', target = None)
    ls_seed.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability'})
    ls_seed.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_seed)
    
    ls_seed2 = bd.Indicator(df_3, "Livelihood_Seed2", 0, ['60-1'], i_cal=None, i_type='count', description='To what extent have your seed varieties been improved?', period='endline', target = None)
    ls_seed2.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability'})
    ls_seed2.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_seed2)
    
    ls_seed3 = bd.Indicator(df_3, "Livelihood_Seed3", 0, ['61'], i_cal=None, i_type='count', description='Has your seed production improved through the project?', period='endline', target = None, visual = False)
    ls_seed3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_seed3.add_var_order(["Yes", "No"])
    indicators.append(ls_seed3)
    
    ls_train = bd.Indicator(df, "Livelihood_Train", 0, ['63'], i_cal=None, i_type='count', description='Has anyone in your household received training on agricultural techniques through this project?', period='endline', target = None, visual = False)
    ls_train.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_train.add_var_order(["Yes", "No", "Unsure"])
    indicators.append(ls_train)
    
    ls_train2 = bd.Indicator(df, "Livelihood_Train2", 0, ['64'], i_cal=None, i_type='count', description='Has anyone in your household used or applied any agricultural techniques that you learned from the project?', period='endline', target = None, visual = False)
    ls_train2.add_breakdown({'2':'Gender','3':'Country', 'Disability':'Disability','project':'Project'})
    ls_train2.add_var_order(["Yes", "No"])
    indicators.append(ls_train2)
    
    ls_train3 = bd.Indicator(df, "Livelihood_Train3", 0, ['66'], i_cal=None, i_type='count', description="Have the agricultural techniques applied been successful in improving your household's farming or gardening practices?", period='endline', target = None)
    ls_train3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    ls_train3.add_var_order(["Not at all successful",
                             "A little bit successful",
                             "Somewhat successful",
                             "Very Successful"])
    indicators.append(ls_train3)
    
    
    ls_fcs = bd.Indicator(df, "Livelihood_FCS", 0, ['FCS_group'], i_cal=None, i_type='count', description="FCS", period='endline', target = None)
    ls_fcs.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_fcs.add_var_order(["Poor food consumption",
                          "Borderline food consumption",
                          "Acceptable food consumption"])
    indicators.append(ls_fcs)
    
    df_5 = df[df['project'] == 5]
    ls_consum = bd.Indicator(df_5, "Livelihood_Consump", 0, ['76'], i_cal=None, i_type='count', description='To what extent did the project help meet your food consumption needs?', period='endline', target = None)
    ls_consum.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_consum.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_consum)
    
    ls_consum2 = bd.Indicator(df_5, "Livelihood_Consump2", 0, ['77'], i_cal=None, i_type='count', description='After the project intervention, were you able to meet your basic food consumption needs?', period='endline', target = None, visual = False)
    ls_consum2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_consum2.add_var_order(["Yes","No"])
    indicators.append(ls_consum2)
    
    ls_consum3 = bd.Indicator(df_5, "Livelihood_Consump3", 0, ['78'], i_cal=None, i_type='count', description='After the project intervention, were you able to access a safe water source?', period='endline', target = None, visual = False)
    ls_consum3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability'})
    ls_consum3.add_var_order(["Yes","No"])
    indicators.append(ls_consum3)
    
    df_4 = df[df['project'] == 4]
    ls_milk = bd.Indicator(df_4, "Livelihood_Milk", 0, ['79'], i_cal=None, i_type='count', description='Are you living with children under the age of 5?', period='endline', target = None, visual = False)
    ls_milk.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_milk.add_var_order(["Yes","No"])
    indicators.append(ls_milk)
    
    df_1 = df[df['project'] == 1]
    ls_income = bd.Indicator(df_1, "Livelihood_Income", 0, ['81'], i_cal=None, i_type='count', description='Do you think the livelihood activities you participated in helped increase your income?', period='endline', target = None, visual = False)
    ls_income.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_income.add_var_order(["Yes","No"])
    indicators.append(ls_income)
    
    ls_income2 = bd.Indicator(df_1, "Livelihood_Income2", 0, ['82'], i_cal=None, i_type='count', description='To what extent did the activities contribute to increasing your income?', period='endline', target = None)
    ls_income2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    ls_income2.add_var_order(["Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_income2)
    
    ls_satis = bd.Indicator(df, "Livelihood_Satis", 0, ['83'], i_cal=None, i_type='count', description='Overall, how satisfied are you with the project in which you participated?', period='endline', target = None)
    ls_satis.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_satis.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(ls_satis)
    
    ls_satis2 = bd.Indicator(df, "Livelihood_Satis2", 0, ['84'], i_cal=None, i_type='count', description='Did you feel that the project staff treated you with respect during the implementation of the project?', period='endline', target = None)
    ls_satis2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_satis2.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(ls_satis2)
    
    ls_satis3 = bd.Indicator(df, "Livelihood_Satis3", 0, ['85'], i_cal=None, i_type='count', description='Do you think there are people deserving who were excluded from the assistance?', period='endline', target = None)
    ls_satis3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    ls_satis3.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(ls_satis3)
    
    # WASH Support
    df_10 = df[df['project'] == 10]
    wash_promotion = bd.Indicator(df_10, "WASH_Promotion", 0, ['86'], i_cal=None, i_type='count', description='Did you participate in the hygiene promotion program?', period='endline', target = None, visual = False)
    wash_promotion.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    wash_promotion.add_var_order(["Yes","No"])
    indicators.append(wash_promotion)
    
    wash_promotion1 = bd.Indicator(df_10, "WASH_Promotion2", 0, ['87-1', '87-2', '87-3', '87-4', '87-5', '87-6'], i_cal=None, i_type='count', description='At which moments do you think handwashing is necessary?', period='endline', target = None, visual = False)
    wash_promotion1.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    wash_promotion1.add_var_change({1: "Yes", 0: "No"})
    wash_promotion1.add_var_order([1, 0])
    wash_promotion1.add_label(["After defecation/using the toilet",
                               "Before eating",
                               "After changing diapers or cleaning a child’s bottom",
                               "Before preparing food",
                               "Before feeding an infant",
                               "None of them"])
    indicators.append(wash_promotion1)
    
    wash1 = bd.Indicator(df, "WASH_water", 0, ['88'], i_cal=None, i_type='count', description='Do you store your drinking water in clean containers?', period='endline', target = None, visual = False)
    wash1.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash1.add_var_order(["Yes","No"])
    indicators.append(wash1)
    
    wash2 = bd.Indicator(df, "WASH_water2", 0, ['89'], i_cal=None, i_type='count', description='Is your household using improved water sources developed or rehabilitated by the project you took part in?', period='endline', target = None, visual = False)
    wash2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash2.add_var_order(["Yes", "No", "Unsure"])
    indicators.append(wash2)
    
    wash3 = bd.Indicator(df, "WASH_water3", 0, ['90'], i_cal=None, i_type='count', description='Did you receive any hygienic kits from the project?', period='endline', target = None, visual = False)
    wash3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    wash3.add_var_order(["Yes", "No"])
    indicators.append(wash3)
    
    wash4 = bd.Indicator(df, "WASH_water4", 0, ['91-1', '91-2', '91-3', '91-4', '91-5', '91-6'], i_cal=None, i_type='count', description='If yes, what type of hygienic water containers did you receive?', period='endline', target = None, visual = False)
    wash4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash4.add_var_change({1: "Yes", 0: "No"})
    wash4.add_var_order([1, 0])
    wash4.add_label(["Clean containers",
                     "Water jerry cans",
                     "Sanitary pads",
                     "Soap",
                     "Water treatment chemicals",
                     "Other"])
    indicators.append(wash4)
    
    wash5 = bd.Indicator(df, "WASH_water5", 0, ['92'], i_cal=None, i_type='count', description='Are you still using the clean containers to store drinking water?', period='endline', target = None)
    wash5.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    wash5.add_var_order(["Yes", "No"])
    indicators.append(wash5)
    
    wash6 = bd.Indicator(df, "WASH_water6", 0, ['93'], i_cal=None, i_type='count', description='To what extent are you satisfied with the variety of hygiene items your household received in the kit?', period='endline', target = None)
    wash6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash6.add_var_order(["Not at all satisfied",
                         "A little bit satisfied",
                         "Somewhat satisfied",
                         "Very satisfied"])
    indicators.append(wash6)
    
    wash7 = bd.Indicator(df, "WASH_water7", 0, ['94'], i_cal=None, i_type='count', description='Are you able to access a safe water source?', period='endline', target = None)
    wash7.add_breakdown({'2':'Gender','3':'Country', 'Disability':'Disability','project':'Project'})
    wash7.add_var_order(["Yes", "No"])
    indicators.append(wash7)
    
    wash8 = bd.Indicator(df, "WASH_water8", 0, ['96'], i_cal=None, i_type='count', description='What is your main source of drinking water?', period='endline', target = None, visual = False)
    wash8.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash8.add_var_order(["Piped water supply",
                     "Protected well/spring",
                     "Rainwater",
                     "Unprotected well/spring",
                     "Packaged bottled water",
                     "Tanker-truck or cart",
                     "Surface water (lake, river, stream)",
                     "No drinking water source"])
    indicators.append(wash8)
    
    wash9 = bd.Indicator(df, "WASH_water9", 0, ['97'], i_cal=None, i_type='count', description='Is drinking water from the main source currently available in your home or community?', period='endline', target = None, visual = False)
    wash9.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash9.add_var_order(["Yes", "No"])
    indicators.append(wash9)
    
    wash10 = bd.Indicator(df, "WASH_water10", 0, ['98'], i_cal=None, i_type='count', description='Are you living with children under the age of 5?', period='endline', target = None, visual = False)
    wash10.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash10.add_var_order(["Yes", "No"])
    indicators.append(wash10)
    
    wash11 = bd.Indicator(df, "WASH_water11", 0, ['99'], i_cal=None, i_type='count', description='Has this child suffered from diarrhoea in the past 2 weeks (14 days)?', period='endline', target = None)
    wash11.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash11.add_var_order(["Yes", "No"])
    indicators.append(wash11)
    
    wash12 = bd.Indicator(df, "WASH_water12", 0, ['100'], i_cal=None, i_type='count', description='Where did you defecate the last time you defecated?', period='endline', target = None, visual = False)
    wash12.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash12.add_var_order(["Household Latrine/Toilet",
                          "Shared Latrine",
                          "Open Defecation (In Bushes, surroundings, refuse dumps, etc.)",
                          "Prefer not to say"])
    indicators.append(wash12)
    
    wash_satis = bd.Indicator(df, "WASH_Satis", 0, ['101'], i_cal=None, i_type='count', description='Overall, how satisfied are you with the project in which you participated?', period='endline', target = None)
    wash_satis.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    wash_satis.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(wash_satis)
    
    wash_satis2 = bd.Indicator(df, "WASH_Satis2", 0, ['102'], i_cal=None, i_type='count', description='Did you feel that the project staff treated you with respect during the implementation of the project?', period='endline', target = None)
    wash_satis2.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    wash_satis2.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(wash_satis2)

    df_2 = df[df['project'] == 2]
    wash_satis3 = bd.Indicator(df, "WASH_Satis3", 0, ['103'], i_cal=None, i_type='count', description='Do you think there are people deserving who were excluded from the assistance?', period='endline', target = None)
    wash_satis3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    wash_satis3.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(wash_satis3)
    
    # Disaster Risk Reduction
    drr = bd.Indicator(df, "DRR_faced", 0, ['104'], i_cal=None, i_type='count', description='Has your community experienced a disaster in the past three years?', period='endline', target = None)
    drr.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    drr.add_var_order(["Yes", "No"])
    indicators.append(drr)
    
    drr2 = bd.Indicator(df, "DRR_faced2", 0, ['105-1', '105-2', '105-3', '105-4', '105-5', '105-6', '105-7', '105-8'], i_cal=None, i_type='count', description='What kind of disaster did you experience?', period='endline', target = None)
    drr2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    drr2.add_var_change({1: "Yes", 0: "No"})
    drr2.add_var_order([1, 0])
    drr2.add_label(["Drought",
                    "Wildfire",
                    "Flood",
                    "Landslide",
                    "Earthquake",
                    "Tornado",
                    "None of them",
                    "Other"])
    indicators.append(drr2)
    
    drr3 = bd.Indicator(df, "DRR_faced3", 0, ['106'], i_cal=None, i_type='count', description='To what extent were you prepared to respond to the disaster in your community?', period='endline', target = None)
    drr3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    drr3.add_var_order(["Not at all",
                        "Somewhat unprepared",
                        "Moderately prepared",
                        "Well prepared",
                        "Very well prepared"])
    indicators.append(drr3)
    
    drr4 = bd.Indicator(df_2, "DRR_training", 0, ['107'], i_cal=None, i_type='count', description='Did you receive any training related to disaster risk management?', period='endline', target = None, visual = False)
    drr4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    drr4.add_var_order(["Yes", "No"])
    indicators.append(drr4)
    
    drr5 = bd.Indicator(df_2, "DRR_training2", 0, ['108'], i_cal=None, i_type='count', description='To what extent has your knowledge improved in responding to disasters?', period='endline', target = None, visual = False)
    drr5.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    drr5.add_var_order(["Not at all",
                        "Low",
                        "Moderate",
                        "High",
                        "Very high"])
    indicators.append(drr5)
    
    drr6 = bd.Indicator(df_2, "DRR_plan", 0, ['109'], i_cal=None, i_type='count', description='Does your community have any disaster risk reduction plans?', period='endline', target = None)
    drr6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    drr6.add_var_order(["Yes", "No"])
    indicators.append(drr6)
    
    drr7 = bd.Indicator(df_2, "DRR_plan2", 0, ['110'], i_cal=None, i_type='count', description='Are you aware of how to implement the existing or new community-based disaster risk reduction plans?', period='endline', target = None, visual = False)
    drr7.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability'})
    drr7.add_var_order(["Yes", "No"])
    indicators.append(drr7)
    
    drr_satis = bd.Indicator(df, "DRR_Satis", 0, ['111'], i_cal=None, i_type='count', description='Overall, how satisfied are you with the project in which you participated?', period='endline', target = None)
    drr_satis.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    drr_satis.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(drr_satis)
    
    drr_satis2 = bd.Indicator(df, "DRR_Satis2", 0, ['112'], i_cal=None, i_type='count', description='Did you feel that the project staff treated you with respect during the implementation of the project?', period='endline', target = None)
    drr_satis2.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    drr_satis2.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(drr_satis2)
    
    drr_satis3 = bd.Indicator(df, "DRR_Satis3", 0, ['113'], i_cal=None, i_type='count', description='Do you think there are people deserving who were excluded from the assistance?', period='endline', target = None)
    drr_satis3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    drr_satis3.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(drr_satis3)
    
    # Animal 
    animal = bd.Indicator(df, "Animal_treated", 0, ['114'], i_cal=None, i_type='count', description='Has your livestock been treated or dewormed through the project?', period='endline', target = None)
    animal.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal.add_var_order(["Yes", "No"])
    indicators.append(animal)
    
    animal2 = bd.Indicator(df, "Animal_treated2", 0, ['115-1', '115-2', '115-3', '115-4', '115-5', '115-6', '115-7'], i_cal=None, i_type='count', description='If yes, what type of livestock was treated?', period='endline', target = None)
    animal2.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    animal2.add_var_change({1: "Yes", 0: "No"})
    animal2.add_var_order([1, 0])
    animal2.add_label(["Cattle",
                       "Sheep",
                       "Goats",
                       "Pigs",
                       "Camels and camelids",
                       "Poultry",
                       "Other"])
    indicators.append(animal2)
    
    animal3 = bd.Indicator(df, "Animal_treated3", 0, ['116'], i_cal=None, i_type='count', description='To what extent were you satisfied with this veterinary support?', period='endline', target = None)
    animal3.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    animal3.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(animal3)
    
    animal4 = bd.Indicator(df, "Animal_treated4", 0, ['117'], i_cal=None, i_type='count', description="To what extent has the health of your livestock improved after the project's implementation?", period='endline', target = None)
    animal4.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal4.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(animal4)
    
    animal5 = bd.Indicator(df, "Animal_treated5", 0, ['118'], i_cal=None, i_type='count', description="Is the livestock's health being consistently maintained?", period='endline', target = None, visual = False)
    animal5.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    animal5.add_var_order(["Yes", "No"])
    indicators.append(animal5)
    
    animal6 = bd.Indicator(df, "Animal_milk", 0, ['119'], i_cal=None, i_type='count', description="Has your milk production increased through the intervention?", period='endline', target = None, visual = False)
    animal6.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal6.add_var_order(["Yes", "No"])
    indicators.append(animal6)
    
    animal7 = bd.Indicator(df, "Animal_milk2", 0, ['120'], i_cal=None, i_type='count', description="To what extent did milk production increase last year?", period='endline', target = None)
    animal7.add_breakdown({'2':'Gender', '3':'Country','Disability':'Disability','project':'Project'})
    animal7.add_var_order(["0 - 20%",
                           "21 - 40%",
                           "41 - 60%",
                           "61 - 80%",
                           "81 - 100%",
                           "More than 100%"])
    indicators.append(animal7)
    
    animal_satis = bd.Indicator(df, "Animal_Satis", 0, ['121'], i_cal=None, i_type='count', description='Overall, how satisfied are you with the project in which you participated?', period='endline', target = None)
    animal_satis.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal_satis.add_var_order(["Not at all",
                            "Low",
                            "Moderate",
                            "High",
                            "Very high"])
    indicators.append(animal_satis)
    
    animal_satis2 = bd.Indicator(df, "Animal_Satis2", 0, ['122'], i_cal=None, i_type='count', description='Did you feel that the project staff treated you with respect during the implementation of the project?', period='endline', target = None)
    animal_satis2.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal_satis2.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(animal_satis2)
    
    animal_satis3 = bd.Indicator(df, "Animal_Satis3", 0, ['123'], i_cal=None, i_type='count', description='Do you think there are people deserving who were excluded from the assistance?', period='endline', target = None)
    animal_satis3.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    animal_satis3.add_var_order(["Yes, completely",
                             "Yes, mostly",
                             "Not really",
                             "Not at all",
                             "Prefer not to answer"])
    indicators.append(animal_satis3)
    
    # Final
    barrier = bd.Indicator(df, "Barrier_Sustain", 0, ['125'], i_cal=None, i_type='count', description="What are the key barriers that make it difficult for you to maintain the resources obtained from the project?", period='endline', target = None, visual = False)
    barrier.add_breakdown({'2':'Gender', '3':'Country', 'Disability':'Disability','project':'Project'})
    barrier.add_var_order(["Climate hazards (drought and flooding)",
                           "Conflict and insecurity",
                           "Limited access to markets",
                           "Inflation",
                           "Disease outbreak",
                           "Lack of education/training",
                           "Cultural and social norms",
                           "Gender inequality",
                           "None of them",
                           "Other"])
    indicators.append(barrier)
    
    return indicators
    
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    
    fcs = bd.Indicator(df, "FCS", 0, ['FCS'], i_cal=None, i_type='count', description='Acceptable Food Consumption Score (FCS)', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(fcs)
    
    fcs_anova = bd.Indicator(df, "FCS_ANOVA", 0, ['FCS'], i_cal=None, i_type='count', description='Acceptable Food Consumption Score (FCS) - ANOVA', s_test = 'anova', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(fcs_anova)
    
    livelihood1 = bd.Indicator(df, "Livelihood_member", 0, ['25'], i_cal=None, i_type='count', description='How many of these financial support programs are you currently a member of?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(livelihood1)
    
    livelihood2 = bd.Indicator(df, "Livelihood_source", 0, ['27'], i_cal=None, i_type='count', description='How many sources of income have you added on since taking part in VSLA or related activities?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(livelihood2)
    
    livelihood3 = bd.Indicator(df, "Livelihood_income", 0, ['29'], i_cal=None, i_type='count', description='On an average month, how much additional income have you generated from these additional income sources you created since you took part in the project?', s_test = 'stats', s_group = {'3':'Country', '2':'Gender', 'Age Group':'Age Group', 'Disability':'Disability'})
    indicators.append(livelihood3)
    
    livelihood4 = bd.Indicator(df, "Livelihood_credit", 0, ['32'], i_cal=None, i_type='count', description='On how many occasions have you taken credit?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(livelihood4)
    
    df_3 = df[df['project'] == 3]
    livelihood6 = bd.Indicator(df_3, "Seed", 0, ['62'], i_cal=None, i_type='count', description='By what percentage has your seed production increased?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(livelihood6)
    
    livelihood6_t = bd.Indicator(df_3, "Seed_Ttest", 0, ['62'], i_cal=None, i_type='count', description='By what percentage has your seed production increased? - T test', s_test = 't-test', s_group = {'2':'Gender', 'Disability':'Disability'})
    indicators.append(livelihood6_t)
    
    df_4 = df[df['project'] == 4]
    livelihood7 = bd.Indicator(df_4, "Livelihood_milk", 0, ['80'], i_cal=None, i_type='count', description='How much goat milk did your children drink per day over the last three days?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(livelihood7)
    
    wash = bd.Indicator(df, "WASH_distance", 0, ['95'], i_cal=None, i_type='count', description='How long does it take to reach a safe water source from your house?', s_test = 'stats', s_group = {'2':'Gender', '3':'Country', 'Disability':'Disability'})
    indicators.append(wash)
    
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
fir = pmf.PerformanceManagementFramework('FIR', 'Evaluation')

indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
fir.add_indicators(indicators)

file_path1 = 'data/Fir Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/FIr Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
fir.PMF_generation(file_path1, file_path2, folder) # Run the PMF