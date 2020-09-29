function dibuixaMembre(matPunts,matRectes)
[distMax,distMin] = distanciaMaximaIMinimaVertexs(matPunts);
dibuixaPuntsSolids(matPunts);
for i = 1:size(matRectes,1)
    dibuixaRecta(matRectes(1),matRectes(2),matRectes(3),distMax/2);
end
end