document.querySelector('.tweetbutton').addEventListener('click',function(){
    document.querySelector('.tweetle').style.display= 'block' ;
    document.querySelector('.tweetbutton').style.visibility = 'hidden'
    document.querySelector('.anacard').style.opacity = '0.7'
    
})

document.querySelector('.kapat').addEventListener('click' , function(){
    document.querySelector('.tweetle').style.display = 'none';
    document.querySelector('.tweetbutton').style.visibility = 'visible' ;
    document.querySelector('.anacard').style.opacity = '1';
})


