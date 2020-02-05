% find the neighbours around (x, y) within the domain
function [nx, ny] = getNeighbours(x, y, stepSize)
	neighbours = [x-stepSize y; x+stepSize y; x y-stepSize; x y+stepSize; x+stepSize y+stepSize; ...
				  x+stepSize y-stepSize; x-stepSize y+stepSize; x-stepSize y-stepSize];
	nx = neighbours(:, 1);
	ny = neighbours(:, 2);
	r = 1:length(nx);
 
	% remove the out of range neighbours
	xOutI = outRangeCheck(nx(r));
	yOutI = outRangeCheck(ny(r));
	OutI = xOutI + yOutI;
 
	nx(OutI>=1) = [];
	ny(OutI>=1) = [];
end

function outRange = outRangeCheck(x)
	outRange = (x < -1e-6) + (x > 10+1e-6);
end