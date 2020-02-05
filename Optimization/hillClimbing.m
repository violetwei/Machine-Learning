function [result, timeToConverge] = hillClimbing(f, x0, y0, stepSize)
	timeToConverge = 0;
	while true
		timeToConverge = timeToConverge + 1; 
		fValue = f(x0, y0);
		[n_x, n_y] = getNeighbours(x0, y0, stepSize);

		% if there is no neighbour within domain, break from the loop
		if(length(n_x) == 0 || length(n_y) == 0)
			break
		end
  
		[xi, yi, fi] = findMaxValue(f, n_x, n_y);
  
		if(fi > fValue)
			x0 = xi;
			y0 = yi;
		else
			% local maximum found, return
			break;
		end 
	end 
 
	result = [x0 y0 f(x0, y0)];
end

% find the maximum function value among the (x, y) pairs
function [max_X, max_Y, maxValue] = findMaxValue(f, x, y)
	fValues = f(x, y);
	[maxValue, maxIndex] = max(fValues);
	max_X = x(maxIndex);
	max_Y = y(maxIndex);
end
