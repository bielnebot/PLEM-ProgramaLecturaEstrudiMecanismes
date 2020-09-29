% ELIMINA DE LA CARPETA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Elimina de la carpeta DibuixosMatlab tots els 
% fitxers .txt i .pdf dels membres del sistema.
% 
% Permet quedar-se exclusivament amb els fitxers .m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fitxerNoms = importdata("nomsMembres.txt");
nreMembres = size(fitxerNoms,1);
matNoms = [];
for i = 1:nreMembres
    matNoms = [matNoms; string(fitxerNoms{i})];
end

for i = 1:nreMembres
    delete(matNoms(i,1)+"ArxiusPerRepresentar.txt");
    delete(matNoms(i,1)+".pdf");
end
delete("nomsMembres.txt");