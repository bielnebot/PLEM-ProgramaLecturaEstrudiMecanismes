function dibuixaCorredora(centre)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Dibuixa una corredora al punt <centre>
% centre = [x y]
% 
% També es dibuixa l'eix
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hold on; axis equal;
a = 2.5; b = 1.5;
% recta/prismàtic
line([centre(1)-a centre(1)+a],[centre(2) centre(2)],"color","k","linewidth",2,"linestyle","--");
% corredora
rectangle("Position",[centre(1)-a/2 centre(2)-b/2 a b],'Curvature',[0.01,0.01],'FaceColor',[1 1 1],'EdgeColor','k','LineWidth',3)
% articulació
plot(centre(1),centre(2),"o","markersize",30,'LineWidth',3,'MarkerEdgeColor','k','MarkerFaceColor',[1 1 1]);