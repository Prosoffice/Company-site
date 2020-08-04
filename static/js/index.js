$(document).ready(function(){
    
    
    


const nav = document.querySelectorAll('.nav-link')

console.log("it works")

function handleNavLinkClick(event){
  const current = document.querySelector(".activeItem")
  current.classList.remove('activeItem')
  event.target.classList.add('activeItem')
}

nav.forEach(function(link){
  link.addEventListener('click', handleNavLinkClick);
});


var typed = new Typed(".demo",{
    strings: ["You dream it, We build it." ,"We'll always be there.","Call and we answer."],
    smartBackspace:true,
    typeSpeed:100,
    backSpeed:30,
    loop:true,
    loopCount:Infinity,
    startDelay:100
    
    
});
    
    
});