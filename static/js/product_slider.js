const images = document.querySelectorAll('.image_for_slider')
const place_for_image = document.querySelector('.product__slider__place')

const product__slider__left = document.querySelector('.product__slider__left');
const product__slider__right  = document.querySelector('.product__slider__right');

const slider__points = document.querySelector('.product__slider__points')
const slider__point  = document.querySelector('.product__slider__point')


let image_number = 0

StayPoint(images, image_number)
place_for_image.src = images[image_number].src

product__slider__left.onclick = () => {
   if (image_number == 0) {
      image_number = images.length - 1
   } else {
      image_number -= 1
   }
   StayPoint(images, image_number)
   place_for_image.src = images[image_number].src
}

product__slider__right.onclick = () => {
   if (image_number == images.length - 1) {
      image_number = 0
   } else {
      image_number += 1
   }
   StayPoint(images, image_number)
   place_for_image.src = images[image_number].src
}

function StayPoint(massive, number) {
   slider__points.innerHTML = ''
   for (let i = 0; i < massive.length; i++) {
      if (i == number)  {
         slider__points.innerHTML += `
         <span class="product__slider__point point__selected"></span>
      `
      } else {
         slider__points.innerHTML += `
         <span class="product__slider__point"></span>
      `
      }
   }
}