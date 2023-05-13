const star_place =document.querySelector('.stars')
const stars = document.querySelectorAll('.input_star')

for (let i = 0; i < stars.length; i++) {
   console.log(stars[i])
   stars[i].addEventListener('change ', (e) => {
      console.log('cahange')
     if (e.target.checked) {
      console.log(stars[i].value)
     }
   })
}