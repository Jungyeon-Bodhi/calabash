#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/24-UNICEF-GM-1 - Clean_Dataset.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    age_group = bd.Indicator(df, "Age Group", 0, ['Q1_age'], i_cal=None, i_type='count', description='Age Group Distribution', period='endline', target = None, visual = False)
    age_group.add_var_order(["0 - 14 years old",
                             "15 - 19 years old",
                             "20 - 24 years old",
                             "25 - 30 years old",
                             "31 - 34 years old",
                             "35 and over"])
    indicators.append(age_group)
    
    sex = bd.Indicator(df, "Sex", 0, ['Q2_sex'], i_cal=None, i_type='count', description='Gender Distribution', period='endline', target = None)
    sex.add_var_order(["Male", "Female"])
    indicators.append(sex)
    
    region = bd.Indicator(df, "Region", 0, ['Q3_region'], i_cal=None, i_type='count', description='Please select the region the survey is conducted in', period='endline', target = None, visual = False)
    region.add_var_order(["Banjul","Lower River",
                          "Central River","Upper River",
                          "Kanifing","North Bank", "West Coast"])
    indicators.append(region)
    
    knowledge_level = bd.Indicator(df, "Knowledge_level", 0, ['Q4_dis_knowledge'], i_cal=None, i_type='count', description='How would you rate your level of knowledge about disabilities?', period='endline', target = None)
    knowledge_level.add_breakdown({'Q2_sex':'Gender'})
    knowledge_level.add_var_order(["No knowledge",
                                   "Minimal knowledge",
                                   "Basic knowledge",
                                   "Adequate knowledge",
                                   "Excellent knowledge"])
    indicators.append(knowledge_level)
    
    
    aware_diss = bd.Indicator(df, "Disability_aware", 0, ['Q5_1','Q5_2','Q5_3','Q5_5','Q5_6','Q5_7','Q5_4'], i_cal=None, i_type='count', description='What types of disabilities are you aware of?', period='endline', target = None)
    aware_diss.add_breakdown({'Q2_sex':'Gender'})
    aware_diss.add_var_change({1: "Yes", 0: "No"})
    aware_diss.add_var_order([1, 0])
    aware_diss.add_label(["Cognitive impairment",
                          "Communication impairment",
                          "Hearing impairment",
                          "Physical impairment",
                          "Self-care impairment",
                          "Visual impairment",
                          "None of them"])
    indicators.append(aware_diss)
    
    knowledge_source = bd.Indicator(df, "Knowledge_source", 0, ['Q6_source'], i_cal=None, i_type='count', description='What is your main source of information on persons with disabilities?', period='endline', target = None, visual = False)
    knowledge_source.add_breakdown({'Q2_sex':'Gender'})
    knowledge_source.add_var_order(["Media (TV, Newspaper, Radio, Internet, etc.)",
                                    "Information from friends, relatives, and acquaintances",
                                    "Everyday life experiences",
                                    "Education/training",
                                    "Public institutions (health centers, hospitals, municipalities, etc.)",
                                    "I do not have any source of information",
                                    "Other"])
    indicators.append(knowledge_source)
    
    knowledge_level2 = bd.Indicator(df, "Knowledge_level2", 0, ['Q7_policy_knowledge'], i_cal=None, i_type='count', description='How would you rate your level of knowledge about\ngovernment policies or strategies such as the Persons with Disabilities Act?', period='endline', target = None)
    knowledge_level2.add_breakdown({'Q2_sex':'Gender'})
    knowledge_level2.add_var_order(["No knowledge",
                                   "Minimal knowledge",
                                   "Basic knowledge",
                                   "Adequate knowledge",
                                   "Excellent knowledge"])
    indicators.append(knowledge_level2)
    
    agree_statement = bd.Indicator(df, "Statements", 0, ['Q8_1','Q8_2','Q8_4','Q8_5','Q8_6','Q8_3'], i_cal=None, i_type='count', description='Check the box if you agree with the statements', period='endline', target = None)
    agree_statement.add_breakdown({'Q2_sex':'Gender'})
    agree_statement.add_var_change({1: "Yes", 0: "No"})
    agree_statement.add_var_order([1, 0])
    agree_statement.add_label(["Children with disabilities should attend the same schools as children without disabilities",
                               "Men with disabilities should have the right to get married",
                               "Persons with disabilities are able to participate fully in life",
                               "Persons with disabilities should have the right to vote in elections",
                               "Women with disabilities should have the right to get married",
                               "None of them"])
    indicators.append(agree_statement)
    
    excluded = bd.Indicator(df, "Excluded", 0, ['Q9_excluded'], i_cal=None, i_type='count', description='From which areas do you think persons with disabilities are being excluded the most?', period='endline', target = None)
    excluded.add_breakdown({'Q2_sex':'Gender'})
    excluded.add_var_order(["Education",
                            "Health",
                            "Social life",
                            "Career opportunities",
                            "Home",
                            "Other"])
    indicators.append(excluded)
    
    barriers = bd.Indicator(df, "Barriers", 0, ['Q10_barriers'], i_cal=None, i_type='count', description='What do you think are the obstacles/barriers that keep persons with disabilities from having a better quality of life and being socially included?', period='endline', target = None, visual = False)
    barriers.add_breakdown({'Q2_sex':'Gender'})
    barriers.add_var_order(["Lack of focused policies",
                            "Lack of financial resources",
                            "Inadequate legislative framework",
                            "Lack of government interest",
                            "Lack of public interest",
                            "Public ignorance/prejudices",
                            "Lack of informed specialists/institutions",
                            "All of the above"])
    indicators.append(barriers)
    
    return indicators
    
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
calabash = pmf.PerformanceManagementFramework('Calabash', 'Evaluation')

indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
calabash.add_indicators(indicators)

file_path1 = 'data/Calabash Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Calabash Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
calabash.PMF_generation(file_path1, file_path2, folder) # Run the PMF
