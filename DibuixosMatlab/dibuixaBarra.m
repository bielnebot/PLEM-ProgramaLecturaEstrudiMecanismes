function dibuixaBarra(llarg)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Dibuixa una barra horitzontal amb una
% articulació a cada extrem de llargada <llarg>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fig = figure();
hold on; axis equal;
line([0 llarg],[0 0],"color","k","linewidth",4,"linestyle","-");
plot(0,0,"o","markersize",14,'LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor',[1 1 1]);
plot(llarg,0,"o","markersize",14,'LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor',[1 1 1]);
text(0,llarg/20,"(0,0)",'interpreter','latex'); text(llarg,llarg/20,"(0,"+string(llarg)+")",'interpreter','latex');