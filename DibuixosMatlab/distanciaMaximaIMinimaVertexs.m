function [distMax,distMin] = distanciaMaximaIMinimaVertexs(v)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Retorna la distància entre els dos punts més llunyans
% i la distància entre els dos punts més propers.
% 
% on v és:
% 
% v = [x1 y1;
%      x2 y2;
%      x3 y3;
%      ... ]
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
maxs = zeros(size(v,1),1);
mins = 1e18+zeros(size(v,1),1);
for i = 1:size(v,1)
    for j = 1:size(v,1)
        if i ~= j
            d = sqrt(((v(i,1))-(v(j,1)))^2+((v(i,2))-(v(j,2)))^2);
            if maxs(i,1) <= d
                maxs(i,1) = d;
            end
            if mins(i,1) >= d
                mins(i,1) = d;
            end
        end
    end
end
distMax = max(maxs);
distMin = min(mins);
if size(v) == [1 2]
    distMax = 1;
    distMin = 1;
end