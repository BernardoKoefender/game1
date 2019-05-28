###STEP 0: load image.
imageURL  = "step0.jpg";
imageRGB  = imread( imageURL );

###STEP 1: extract information and convert to grayscale.
imageGray = rgb2gray( imageRGB );
imgsize   = size( imageGray );
imgheight = imgsize(1,1);
imgwidth  = imgsize(1,2);
imwrite( imageGray , gray( 256 ), "step1.jpg" );

###STEP 2: create new matrix with the size of the zoomed image and initialize it with 0.
imgwidthzeroes  = imgwidth  * 2 - 1;
imgheightzeroes = imgheight * 2 - 1;
for( i = 1 : imgheightzeroes )
  for( j = 1 : imgwidthzeroes )
    imagegrayzeroes( i, j ) = 0;
  end;
end;
imwrite( imagegrayzeroes, gray( 256 ), "step2.jpg" );

###STEP 3: merge the zeroes matrix with the original image(grayscale).
auxi = auxj = 1;
for( i = 1 : imgheightzeroes )
  if( mod( ( i ), 2 ) == 1 )
    for( j = 1 : imgwidthzeroes )
      if( mod( ( j ), 2 ) == 1 )
        imagegrayzeroes( i, j ) = imageGray( auxi, auxj );
        auxj = auxj + 1;
      end;
    end;
    auxj = 1;
    auxi = auxi + 1;
  end;
end;
imwrite( imagegrayzeroes, gray( 256 ), "step3.jpg" );

###STEP 4: Interpoalate horizontaly
for( i = 1 : ( imgheightzeroes ) )
  for( j = 1 : ( imgwidthzeroes ) )
    if( mod( i, 2 ) == 0 )
      if( mod( j, 2 ) == 1 )
        imagegrayzeroes( i, j ) = int32( ( imagegrayzeroes( i + 1, j ) + imagegrayzeroes( i - 1, j ) ) / 2 );
      end;
    end;
  end;
end;
imwrite( imagegrayzeroes, gray( 256 ), "step4.jpg" );

###STEP 5: Interpoalate verticaly
for( i = 1 : ( imgheightzeroes ) )
  for( j = 1 : ( imgwidthzeroes ) )
      if( mod( j, 2 ) == 0 )
        imagegrayzeroes( i, j ) = int32( ( imagegrayzeroes( i, j + 1 ) + imagegrayzeroes( i, j - 1 ) ) / 2 );
      end;
  end;
end;
imwrite( imagegrayzeroes, gray( 256 ), "step5.jpg" );