clc; clear all; close all;

% Define the filename and sheet name
filename = 'Student_groups_by_age_valid_2.xlsx';
sheetnames = sheetnames(filename);
col_index=72;


for i = 1:numel(sheetnames)
    % Read data from the sheet as a table
    sheet_table = readtable(filename, 'Sheet', sheetnames{i});

    % Extract the column data
    column_data = sheet_table{:, col_index};
    column_data(1) = []; %drop name of the column like TMC or whatever


    % Assign the column data to a variable with a dynamic name
    var_name = ['tmc' num2str(i)];
    eval([var_name ' = column_data;']);
end
