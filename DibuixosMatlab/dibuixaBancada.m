function dibuixaBancada(punts,rectes)
[distMax,distMin] = distanciaMaximaIMinimaVertexs(punts);
dibuixaTotsElsPuntsBancada(punts); hold on;
for i=1:size(rectes,1)
    dibuixaRecta(rectes(1),rectes(2),rectes(3),distMax/2);
end