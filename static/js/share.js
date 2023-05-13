const share__panel = document.querySelector('.share__panel')

const share__panel__open = document.querySelector('.share')
const share__panel__close = document.querySelector('.share__panel__close')
const  product = document.querySelector('.product')

const share__icons = document.querySelectorAll('.share__icon')


share__panel__close.addEventListener('click', () =>  {
   share__panel.style.opacity = '0'
   document.body.style.overflowY = 'auto'
   setTimeout(() => {
      share__panel.style.display = 'none'
   }, 300)
})

product.onclick = () => {
   if (share__panel.style.display == 'flex' && share__panel.style.opacity == '1') {
      share__panel.style.opacity = '0'
      console.log('show product')
      document.body.style.overflowY = 'auto'
      setTimeout(() => {
         share__panel.style.display = 'none'
      }, 300)
   }
}

share__panel__open.onclick = () => {
   share__panel.style.display = 'flex'
   document.body.style.overflowY = 'hidden'

   setTimeout(() => {
      share__panel.style.opacity = '1'
   }, 300)
}

const copy = document.querySelector('.copy')

for (let share__icon of share__icons) {
   share__icon.onclick = () => {
      share__icon.style.scale = '1.2'
   
      setTimeout(() => {
         share__icon.style.scale = '1'
      }, 300)
   }
}

copy.onclick = () => {
   copy.style.scale = '1.2'
   navigator.clipboard.writeText(new URL(window.location.href))
   
   setTimeout(() => {
      copy.style.scale = '1'
   }, 300)
}