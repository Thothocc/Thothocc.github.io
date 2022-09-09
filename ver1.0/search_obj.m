function [res] = search_obj(name)
%initCobraToolbox
load('D:\iGEM\ecmodel_batch.mat')
model = ecModel_batch
%name='ex_a'
index=find(~cellfun(@isempty,strfind(model.rxns,name)));
res=model.rxns(index)
end