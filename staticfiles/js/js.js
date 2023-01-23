var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navigation-panel").style.top = "0";
    document.getElementById('open-btn').style.top = "0"
  } else {
    document.getElementById("navigation-panel").style.top = "-200px";
    document.getElementById('open-btn').style.top = "-200px"
  }
  prevScrollpos = currentScrollPos;
}

openBtn = document.getElementById('open-btn');
closeBtn = document.getElementById('close-btn');
openBtn.addEventListener('click', openMenu);
closeBtn.addEventListener('click', closeMenu);


function openMenu(){
  document.querySelector('.side-bar').classList.add('opened')

}




function closeMenu(){
  document.querySelector('.side-bar').classList.remove('opened')
}

topBtn = document.querySelector('.top-btn').addEventListener('click', () => { 
  document.documentElement.scrollTop = 0;
})