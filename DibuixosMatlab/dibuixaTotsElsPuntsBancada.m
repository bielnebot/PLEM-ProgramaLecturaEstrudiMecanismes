function dibuixaTotsElsPuntsBancada(punts)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ample_linia_horitzontal = 6*factor
% punts = [0 0;
%         10 0;
%         0 15];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[distMax,distMin] = distanciaMaximaIMinimaVertexs(punts);
for i = 1:size(punts,1)
    dibuixaPuntBancada(punts(i,1),punts(i,2),distMin/15)
end