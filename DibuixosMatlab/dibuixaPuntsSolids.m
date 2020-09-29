function dibuixaPuntsSolids(vertexs)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Dibuixa els punts del sòlid i els uneix amb línies.
% 
% Per exemple:
% 
% vertexs = [-16 25; % vèrtexs
%             0 0;
%             22 0];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cares = 1:size(vertexs,1); % matriu de connectivitat
hold on; axis equal;
patch('Faces',cares,'Vertices',vertexs,'FaceColor','k',"FaceAlpha",0.1,'EdgeColor','k','LineWidth',4);
for i = 1:size(vertexs,1)
    plot(vertexs(i,1),vertexs(i,2),"o","markersize",14,'LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor',[1 1 1]);
    [distMax,~] = distanciaMaximaIMinimaVertexs(vertexs);
    text(vertexs(i,1)-distMax/20,vertexs(i,2)+distMax/20,"\textbf{("+string(vertexs(i,1))+", "+string(vertexs(i,2))+")}",'interpreter','latex',"Color",[0.1 .1 1],"FontSize",14);
end