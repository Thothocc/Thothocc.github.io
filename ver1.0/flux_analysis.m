function [flux] = flux_analysis(target,C_source)
%initCobraToolbox
load('D:\iGEM\ecmodel_batch.mat')
model = ecModel_batch
%target = 'tr_acar7p/atpNo1'
%C_source = 'rxsp0005'
txt = simulateGrowth(model,target,C_source)
flux = jsonencode(txt)
end