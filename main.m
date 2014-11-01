%load('Songs.dat');

load('ClassicalSongs.dat');
load('RapSongs.dat');
load('MetalSongs.dat');
load('AcousticSongs.dat');


%randrocksongidx = randperm(882);
%randRockSongs = Songs(randrocksongidx(1:425),:);
%countrySongs = Songs(883:end,:);

accuracies = [];
minerrors = [];
binsizes = 100:50:400;

for binsize = binsizes
 
   %binsize = 50;

  Songs = [ClassicalSongs(1:binsize,:);RapSongs(1:binsize,:);MetalSongs(1:binsize,:);AcousticSongs(1:binsize,:)];

  time_signature = Songs(:,1);
  energy = Songs(:,2);
  liveness = Songs(:,3);
  tempo = Songs(:,4);
  speechiness = Songs(:,5);
  acousticness = Songs(:,6);
  danceability = Songs(:,7);
  instrumentalness = Songs(:,8);
  key = Songs(:,9);
  duration = Songs(:,10);
  loudness = Songs(:,11);

  %Choose your own features
  %X = [energy liveness tempo speechiness acousticness danceability instrumentalness duration loudness];

  %Or pass the entire thing
  X = Songs;

  %Normalize X
  [X_norm, mu, sigma] = featureNormalize(X);
  X = X_norm;

  % Run your K-Means algorithm on this data
  % You should try different values of K and max_iters here
  K = 4;
  max_iters = 20;

  minerror = 1000000000000000;

  for cnt=1:20
    % When using K-Means, it is important the initialize the centroids
    % randomly. 
    % You should complete the code in kMeansInitCentroids.m before proceeding
    initial_centroids = kMeansInitCentroids(X, K);
    %disp(initial_centroids);

    % Run K-Means
    [tempcentroids, tempidx] = runkMeans(X, initial_centroids, max_iters);
    %fprintf('Tempcentroids\n');
    %disp(tempcentroids);
    error = 0;
    for icnt=1:size(X,1)
      error = error + sum((X(icnt,:) - tempcentroids(tempidx(icnt),:)).^2);
    endfor
    fprintf('Error');
    disp(error);
    if(error<minerror)
      fprintf('Found better error %d',cnt);
      minerror = error;
      centroids = tempcentroids;
      idx = tempidx;
    endif
  endfor

  %Output indices, that is idx

  idx1 = idx(1:binsize,:);
  idx2 = idx(binsize+1:binsize*2,:);
  idx3= idx(binsize*2+1:binsize*3,:);
  idx4 = idx(binsize*3+1:binsize*4,:);
  %idx5 = idx(801:end,:);

  subplot(1,4,1);
  n1 = hist(idx1,K);
  hist(idx1);
  title('Classical');
  subplot(1,4,2);
  n2 = hist(idx2,K);
  hist(idx2);
  title('Rap');
  subplot(1,4,3);
  n3 = hist(idx3,K);
  hist(idx3);
  title('Metal');
  subplot(1,4,4);
  n4 = hist(idx4,K);
  hist(idx4);
  title('Acoustic');
  %subplot(1,5,5);
  %hist(idxReggae);
  
  imgname = sprintf('SongClustering%d.png',binsize);
  
  print -dpng imgname;

  accuracy = ((max(n1) + max(n2) + max(n3) + max(n4))/(4*binsize))*100;
  fprintf('Accuracy Percent\n');
  disp(accuracy);
  accuracies(:,end+1) = accuracy;
  minerrors(:,end+1) = minerror;

endfor

%plot(binsizes,accuracies);
%print -dpng 'Accuracies.png';