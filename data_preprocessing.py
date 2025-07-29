#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "Perception about the rights of persons with disabilities in The Gambia"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-UNICEF-GM-1 - Raw Dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-UNICEF-GM-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

identifiers = ['Timestamp','Q1_age', 'Q2_sex', 'Q3_region']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['Timestamp', 'Consent', 'Q1_age', 'Q2_sex', 'Q3_region', 'Q4_dis_knowledge', 'Q5_type_dis',
 'Q6_source', 'Q7_policy_knowledge', 'Q8_perception', 'Q9_excluded', 'Q10_barriers','Q5_1', 'Q5_2','Q5_3', 'Q5_4', 'Q5_5','Q5_6', 'Q5_7','Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['Q5_type_dis','Q8_perception']
# Specify the columns to be excluded from the data analysis

miss_col = ['Timestamp', 'Consent', 'Q1_age', 'Q2_sex', 'Q3_region', 'Q4_dis_knowledge', 'Q6_source', 'Q7_policy_knowledge','Q9_excluded', 'Q10_barriers']
# Specify all columns that apply to all respondents for missing value detection


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

calabash = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, identifiers, cols_new,  del_type = 0, file_type=file_type)
calabash.processing()