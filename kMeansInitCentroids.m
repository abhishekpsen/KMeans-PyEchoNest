function centroids = kMeansInitCentroids(X, K)
%KMEANSINITCENTROIDS This function initializes K centroids that are to be 
%used in K-Means on the dataset X
%   centroids = KMEANSINITCENTROIDS(X, K) returns K initial centroids to be
%   used with the K-Means on the dataset X
%

% You should return this values correctly
centroids = zeros(K, size(X, 2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should set centroids to randomly chosen examples from
%               the dataset X
%

randidx = randperm(size(X,1));

centroids = X(randidx(1:K),:);

disp(randidx(:,1:K))


%Choosing first and last values for centroids
%centroids = [X(2,:);X(201,:);X(402,:)];
%centroids = [X(2,:);X(end,:)];

  



% =============================================================

end

