const star_place =document.querySelector('.stars')
const stars = document.querySelectorAll('.input_star')
let comment_stay_stars = document.querySelectorAll('.comment__stay__stars')

for (let i = 0; i < stars.length; i++) {
   console.log(stars[i])
   stars[i].addEventListener('change ', (e) => {
      console.log('cahange')
     if (e.target.checked) {
      console.log(stars[i].value)
     }
   })
}

for (let stars of comment_stay_stars) {
   stars_count = parseInt(stars.innerHTML)
   stars.innerHTML = ""

   for (let i = 0; i < stars_count; i++) {
      stars.innerHTML += "<i class='fa-solid fa-star'></i>"
   }
}