function dibuixaPuntBancada(x,y,factor)
xOrig = x; yOrig = y;
% el triangle
vertexs = [x y;x+2*factor y-3*factor;x-2*factor y-3*factor];
cares = 1:size(vertexs,1); hold on; % matriu de connectivitat
patch('Faces',cares,'Vertices',vertexs,'FaceColor','w',"FaceAlpha",1,'EdgeColor','k','LineWidth',4);
% el cercle
vertexsCercle = generaPuntsCercleEntorn(x,y,0.9*factor);
matCon = 1:size(vertexsCercle,1);
patch('Faces',matCon,'Vertices',vertexsCercle,'FaceColor','w',"FaceAlpha",1,'EdgeColor','k','LineWidth',4);
% la línia horitzontal
line([x-3*factor x+3*factor],[y-3*factor y-3*factor],"color","k","linewidth",4,"linestyle","-");
% les diagonals
line([x-2.5*factor x-3*factor],[y-3*factor y-3.5*factor],"color","k","linewidth",2,"linestyle","-");
for i=linspace(1,5*factor,5)
    x=x+1*factor;
    line([x-2.5*factor x-3.5*factor],[y-3*factor y-4*factor],"color","k","linewidth",2,"linestyle","-");
end
line([x-2*factor x-2.5*factor],[y-3.5*factor y-4*factor],"color","k","linewidth",2,"linestyle","-");
axis equal
% xlim([x-3-5-10 x+3-5-10])
text(xOrig+0.8*factor,yOrig+0.8*factor,"\textbf{("+string(xOrig)+","+string(yOrig)+")}",'interpreter','latex',"Color",[0.1 .1 1],"FontSize",14);