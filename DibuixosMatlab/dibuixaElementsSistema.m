% DIBUIXA ELS ELEMENTS DEL SISTEMA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% A partir del la llista de noms dels membres i dels fitxers
% de cada membre, els dibuixa i els exporta en un .pdf
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fitxerNoms = importdata("nomsMembres.txt");
nreMembres = size(fitxerNoms,1);
matNoms = [];
for i = 1:nreMembres
    matNoms = [matNoms; string(fitxerNoms{i})];
end
matNomsFitxers = matNoms+"ArxiusPerRepresentar.txt";

for i = 1:nreMembres
%     "ara el membre"+matNoms(i,1)
    dadesMembre_i = importdata(matNomsFitxers(i,1));
    filaCanvi = find(dadesMembre_i(:,1)==999);
    punts = []; rectes = [];
    for fila = 1:filaCanvi-1
        punts = [punts; dadesMembre_i(fila,[2,3])];
    end
    for fila = filaCanvi+1:size(dadesMembre_i,1)
        rectes = [rectes; dadesMembre_i(fila,[2,3,4])];
    end
    fig = figure();
    if matNoms(i,1) == "Bancada"
        dibuixaBancada(punts,rectes);
%     if rectes ~= []
%         rectes ~= [] & 
    elseif size(rectes) == [1,3] 
        if punts == [0 0] & rectes(1) == 0 & rectes(2) == 0
            dibuixaCorredora([0 0]);
        end
    else
        dibuixaMembre(punts,rectes);
    end
% títol i exportar
%     punts
%     rectes
    title(matNoms(i,1));
    axis off;
    
%     saveas(fig,matNoms(i,1),"pdf");
    set(gcf,'Units','centimeters');
    Mida_i_posicio = get(gcf,'Position');
    set(gcf,'PaperPositionMode','Auto','PaperUnits','centimeters','PaperSize',[Mida_i_posicio(3), Mida_i_posicio(4)]);
    print(gcf,matNoms(i,1),'-dpdf','-r0');
end
close all